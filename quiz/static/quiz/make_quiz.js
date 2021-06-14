"use strict";
document.addEventListener("DOMContentLoaded", function () {
    // Initiate vars for question displayed, number qs correct and
    // the array of answers
    var questionNumber = 1;
    var numCorrect = 0;
    var answerArr = [];
    // add placeholder 'x' for each possible answer
    for (var i = 0; i < qListLength; i++) {
        answerArr.push(undefined);
    }
    // Display the first question
    // TODO: change all style.display to classList.add/remove
    $("#question" + questionNumber).show();
    // Get next, previous and submit buttons
    var nextButton = document.getElementById("next");
    var prevButton = document.getElementById("previous");
    var submitButton = document.getElementById("submit");
    // When next is clicked
    nextButton.onclick = function () {
        // record the answer in the answer array
        var userAnswer = $("input[name=question" + questionNumber + "]:checked").val();
        answerArr["" + questionNumber - 1] = userAnswer;
        console.log(answerArr);
        // display next question and enable/disable relevant buttons
        questionNumber++;
        document.querySelectorAll(".quiz-question").forEach(function (div) {
            div.style.display = "none";
        });
        $("#question" + questionNumber).show();
        prevButton.disabled = false;
        // enable/disable relevant buttons when at the last question
        // NB: qListLength is defined in a <script> tag in quiz.html
        if (questionNumber === qListLength) {
            nextButton.disabled = true;
            submitButton.disabled = false;
        }
    };
    // When previous is clicked
    prevButton.onclick = function () {
        // display previous question and enable/disable relevant buttons
        questionNumber--;
        document.querySelectorAll(".quiz-question").forEach(function (div) {
            div.style.display = "none";
        });
        $("#question" + questionNumber).show();
        submitButton.disabled = true;
        nextButton.disabled = false;
        if (questionNumber === 1) {
            prevButton.disabled = true;
        }
    };
    // When submit is clicked, show results
    submitButton.onclick = function () {
        // disable previous button
        prevButton.disabled = true;
        submitButton.disabled = true;
        // fill out final answer in answer array
        var userAnswer = $("input[name=question" + questionNumber + "]:checked").val();
        answerArr["" + questionNumber - 1] = userAnswer;
        // hide all questions
        document.querySelectorAll(".quiz-question").forEach(function (div) {
            div.style.display = "none";
        });
        // compare user answers against correct answers, tally number correct
        for (i = 0; i < answerArr.length; i++) {
            if (answerArr[i] === correctAnswers[i]) {
                numCorrect++;
            }
        }
        // generate scores page
        $("#quiz-container").append("<div id=\"results\"><h3>You got " + numCorrect + " out of " + qListLength + " correct!</h3></div>");
        // create try again button
        $("#tryAgain").show();
    };
});
