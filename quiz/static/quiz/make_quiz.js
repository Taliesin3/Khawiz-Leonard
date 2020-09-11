"use strict";

document.addEventListener("DOMContentLoaded", function() {
    // Initiate vars for question displayed, number qs correct and
    // the array of answers
    var questionNumber = 1;
    var numCorrect = 0;
    var answerArr = [];

    // add placeholder 'x' for each possible answer
    for (var i = 0; i < qListLength; i++) {
        answerArr.push(undefined)
    }

    // Display the first question
    // TODO: change all style.display to classList.add/remove
    $(`#question${questionNumber}`).show();
    
    // When next is clicked
    document.getElementById("next").onclick = function() {
        
        // record the answer in the answer array
        var userAnswer = $(`input[name=question${questionNumber}]:checked`).val();
        answerArr[`${questionNumber}` - 1] = userAnswer;
        console.log(answerArr)

        // display next question and enable/disable relevant buttons
        questionNumber++;
        document.querySelectorAll(".quiz-question").forEach(function(div) {
            div.style.display = "none";
        })
        $(`#question${questionNumber}`).show();
        document.getElementById("previous").disabled = false;

        // enable/disable relevant buttons when at the last question
        // NB: qListLength is defined in a <script> tag in quiz.html
        if (questionNumber === qListLength) {
            document.getElementById("next").disabled = true;
            document.getElementById("submit").disabled = false;
        }
    }

    // When previous is clicked
    document.getElementById("previous").onclick = function() {
        
        // display previous question and enable/disable relevant buttons
        questionNumber--;
        document.querySelectorAll(".quiz-question").forEach(function(div) {
            div.style.display = "none";
        })
        $(`#question${questionNumber}`).show();
        document.getElementById("submit").disabled = true;
        document.getElementById("next").disabled = false;

        if (questionNumber === 1) {
            document.getElementById("previous").disabled = true;
        }
    }


    // When submit is clicked, show results
    document.getElementById("submit").onclick = function() {
        
        // disable previous button
        document.getElementById("previous").disabled = true;
        document.getElementById("submit").disabled = true;

        // fill out final answer in answer array
        var userAnswer = $(`input[name=question${questionNumber}]:checked`).val();
        answerArr[`${questionNumber}` - 1] = userAnswer;

        // hide all questions
        document.querySelectorAll(".quiz-question").forEach(function(div) {
            div.style.display = "none";
        })

        // compare user answers against correct answers, tally number correct
        for(i = 0; i < answerArr.length; i++) {
            if(answerArr[i] === correctAnswers[i]) {
                numCorrect++;
            }
        }
        console.log(numCorrect);

        // generate scores page
        $("#quiz-container").append( 
            `<div id="results"><h3>You got ${numCorrect} out of ${qListLength} correct!</h3></div>`
        );

        // create try again button
        $("#tryAgain").show();
    }
});