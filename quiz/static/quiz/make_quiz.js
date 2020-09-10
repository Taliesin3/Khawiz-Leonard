"use strict";

document.addEventListener("DOMContentLoaded", function() {
    // Count which question is displayed
    var counter = 1;
    console.log(counter)

    // Display the first question
    document.getElementById(`question${counter}`).style.display = "block";
    
    // When next is clicked, display next question and 
    // enable/disable relevant buttons
    document.getElementById("next").onclick = function() {
        counter++;
        document.querySelectorAll(".quiz-question").forEach(function(div) {
            div.style.display = "none";
        })
        document.getElementById(`question${counter}`).style.display = "block";
        document.getElementById("previous").disabled = false;

        // enable/disable relevant buttons when at the last question
        // NB: qListLength is defined in a <script> tag in quiz.html
        if (counter === qListLength) {
            document.getElementById("next").disabled = true;
            document.getElementById("submit").disabled = false;
        }
    }

    // When previous is clicked, display previous question and 
    // enable/disable relevant buttons
    document.getElementById("previous").onclick = function() {
        counter--;
        document.querySelectorAll(".quiz-question").forEach(function(div) {
            div.style.display = "none";
        })
        document.getElementById(`question${counter}`).style.display = "block";
        document.getElementById("submit").disabled = true;
        document.getElementById("next").disabled = false;

        if (counter === 1) {
            document.getElementById("previous").disabled = true;
        }
    }
        
});