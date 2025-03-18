document.addEventListener("DOMContentLoaded", function () {
    const lessonButtons = document.querySelectorAll(".lesson-button");
    const lessonBox = document.querySelector(".lesson-box");
    const lessonTitle = document.querySelector(".lesson-title");
    
    lessonButtons.forEach(button => {
        button.addEventListener("click", function () {
            let lessonId = this.getAttribute("data-lesson");
            
            if (!lessonId || lessonId === "null") {
                lessonId = this.getAttribute("data-practice");
            }

            if (!lessonId) {
                console.error("Ошибка: lessonId и practiceId не заданы.");
                return;
            }

            fetch(`/lesson/${lessonId}/`)
                .then(response => response.text())
                .then(data => {
                    lessonTitle.textContent = this.textContent;
                    lessonBox.innerHTML = data;
                })
                .catch(error => console.error("Ошибка загрузки урока:", error));
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const checkBtn = document.getElementById("check-btn");
    const nextTaskBtn = document.getElementById("next-task-btn");
    const questionForm = document.getElementById("question-form");
    
    if (checkBtn && nextTaskBtn && questionForm) {
        checkBtn.addEventListener("click", function () {
            const selectedAnswer = document.querySelector('input[name="answer"]:checked');
            const correctAnswer = questionForm.getAttribute("data-correct-answer");

            if (selectedAnswer) {
                if (selectedAnswer.value === correctAnswer) {
                    nextTaskBtn.style.display = "inline-block";
                    checkBtn.disabled = true;
                } else {
                    alert("Неправильный ответ. Попробуйте еще раз.");
                }
            } else {
                alert("Пожалуйста, выберите вариант ответа.");
            }
        });
    }
});
