from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Lesson, LessonProgress, Exercise, ExerciseProgress
from .forms import CustomUserCreationForm, ProfileForm
from django.views.decorators.csrf import csrf_exempt
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return render(request, 'learning/register.html')


def main_view(request):
    user = request.user
    lessons = Lesson.objects.order_by('order')

    if request.user.is_authenticated:
        progress = LessonProgress.objects.filter(user=user)

        if not progress.exists() and lessons.exists():
            first_lesson = lessons.first()
            LessonProgress.objects.create(user=user, lesson=first_lesson, unlocked=True)

        unlocked_ids = LessonProgress.objects.filter(user=user, unlocked=True).values_list('lesson_id', flat=True)
        lessons = Lesson.objects.filter(id__in=unlocked_ids).order_by('order')

    return render(request, 'learning/main.html', {
        'lessons': lessons,
    })


@login_required
@csrf_exempt
def lesson_detail(request, lesson_id): 
    user = request.user
    lessons = Lesson.objects.order_by('order')
    selected_lesson = get_object_or_404(Lesson, pk=lesson_id)

    # Проверка доступа к уроку
    progress, _ = LessonProgress.objects.get_or_create(user=user, lesson=selected_lesson)
        

    # Получаем все упражнения урока
    exercises = Exercise.objects.filter(lesson=selected_lesson).order_by('order')
    exercise_completed = False

    if request.method == "POST":
        exercise_id = request.POST.get("exercise_id")

        if exercise_id:
            answer = request.POST.get(f"answer_{exercise_id}", "").strip()

            # Найти упражнение, связанное с уроком
            current_exercise = get_object_or_404(Exercise, id=exercise_id, lesson=selected_lesson)

            # Получить или создать прогресс по упражнению
            ep, _ = ExerciseProgress.objects.get_or_create(user=user, exercise=current_exercise)

            if answer.lower() == current_exercise.correct_answer.lower():
                ep.is_completed = True
                ep.save()

                # Открыть следующее упражнение
                next_ex = exercises.filter(order__gt=current_exercise.order).first()
                if next_ex:
                    next_ep, _ = ExerciseProgress.objects.get_or_create(user=user, exercise=next_ex)
                    next_ep.unlocked = True
                    next_ep.save()

                exercise_completed = True

                # Если все упражнения завершены — открыть следующий урок
                all_completed = all(
                    ExerciseProgress.objects.filter(user=user, exercise=ex).first() and 
                    ExerciseProgress.objects.get(user=user, exercise=ex).completed
                    for ex in exercises
                )
                if all_completed:
                    next_lesson = lessons.filter(order__gt=selected_lesson.order).first()
                    if next_lesson:
                        LessonProgress.objects.get_or_create(
                            user=user, lesson=next_lesson, defaults={'unlocked': True}
                        )
        else:
            # Безопасная обработка случая, если не передан exercise_id
            print("Ошибка: не передан ID упражнения")

    # Проверка, пройдены ли все упражнения текущего урока
    all_completed = all(
    ExerciseProgress.objects.filter(user=user, exercise=ex, is_completed=True).exists()
    for ex in exercises
)

    next_lesson = lessons.filter(order__gt=selected_lesson.order).first()

    exercise_completion_status = {
    ex.id: ExerciseProgress.objects.filter(user=user, exercise=ex, is_completed=True).exists()
    for ex in exercises
    }

    return render(request, 'learning/lesson_detail.html', {
        'lesson': selected_lesson,
        'lessons': lessons,
        'next_lesson': next_lesson,
        'exercise_completed': all_completed,
        'exercise_completion_status': exercise_completion_status,
    })


def complete_lesson(request, lesson_id):
    user = request.user
    current_lesson = get_object_or_404(Lesson, id=lesson_id)

    progress, _ = LessonProgress.objects.get_or_create(user=user, lesson=current_lesson)
    progress.unlocked = True
    progress.save()

    next_lesson = Lesson.objects.filter(order__gt=current_lesson.order).order_by('order').first()
    if next_lesson:
        LessonProgress.objects.get_or_create(user=user, lesson=next_lesson, defaults={'unlocked': True})

    return redirect('main')


def about_page(request):
    return render(request, 'learning/about.html')


def support(request):
    return render(request, 'learning/support.html')

def sub(request):
    return render(request, 'learning/sub.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_premium = form.cleaned_data.get('is_premium', False)
            user.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'learning/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'learning/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('register')


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'learning/profile.html', {'form': form})


# Обработка ошибок
def custom_404(request, exception):
    return render(request, 'learning/404.html', status=404)

def error404(request):
    return render(request, 'learning/404.html')

