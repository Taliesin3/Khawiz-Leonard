import random, json

from django.shortcuts import render
from django.http import HttpResponse

from .utils import lookup
from .models import Team



# Create your views here.
def index(request):
    teams = Team.objects.order_by("fullName")
    return render(request, "index.html", {
        "teams": teams
    })

def teamQuiz(request):   
    # Get team information
    divisions = ["Atlantic", "Pacific", "Central"]
    divName = "division"
    team = "Hawks"

    # Contact API for quiz data
    quiz_type = "team"
    teamId = 1  # TODO: use teamId provided by form, hardcoded for testing purposes
    # dataset = lookup(quiz_type, teamId)
    dataset = {     # TODO: re-implement lookup function in the line above, hardcoded dataset for testing purposes
        'api': {'status': 200, 'message': 'GET players/teamId/1', 'results': 45, 'filters': ['playerId', 'teamId', 'league', 'country', 'lastName', 'firstName'], 'players': [
            {'firstName': "DeAndre'", 'lastName': 'Bembry', 'teamId': '1', 'yearsPro': '3', 'collegeName': "St. Joseph's (PA)", 'country': 'USA', 'playerId': '49', 'dateOfBirth': '1994-07-04', 'affiliation': "St. Joseph's (PA)/USA", 'startNba': '2016', 'heightInMeters': '1.96', 'weightInKilograms': '95.3', 'leagues': {'standard': {'jersey': '95', 'active': '1', 'pos': 'G-F'}}}, 
            {'firstName': 'Clint', 'lastName': 'Capela', 'teamId': '1', 'yearsPro': '5', 'collegeName': 'Switzerland', 'country': 'Switzerland', 'playerId': '92', 'dateOfBirth': '1994-05-18', 'affiliation': 'Elan Chalon (France)/Switzerland', 'startNba': '2014', 'heightInMeters': '2.08', 'weightInKilograms': '108.9', 'leagues': {'standard': {'jersey': '15', 'active': '1', 'pos': 'C'}}}, 
            {'firstName': 'Vince', 'lastName': 'Carter', 'teamId': '1', 'yearsPro': '21', 'collegeName': 'North Carolina', 'country': 'USA', 'playerId': '94', 'dateOfBirth': '1977-01-26', 'affiliation': 'North Carolina/USA', 'startNba': '1998', 'heightInMeters': '1.98', 'weightInKilograms': '99.8', 'leagues': {'standard': {'jersey': '15', 'active': '1', 'pos': 'G-F'}}}, 
            {'firstName': 'Dewayne', 'lastName': 'Dedmon', 'teamId': '1', 'yearsPro': '6', 'collegeName': 'USC', 'country': 'USA', 'playerId': '131', 'dateOfBirth': '1989-08-12', 'affiliation': 'USC/USA', 'startNba': '2013', 'heightInMeters': '2.13', 'weightInKilograms': '111.1', 'leagues': {'standard': {'jersey': '14', 'active': '1', 'pos': 'C'}}}, 
            {'firstName': 'Malcolm', 'lastName': 'Delaney', 'teamId': '1', 'yearsPro': '2', 'collegeName': 'Virginia Tech', 'country': 'USA', 'playerId': '133', 'dateOfBirth': '1989-03-11', 'affiliation': 'Virginia Tech/USA', 'startNba': '2016', 'heightInMeters': '1.9', 'weightInKilograms': '86.2', 'leagues': {'standard': {'jersey': '5', 'active': '1', 'pos': 'G'}}}, 
            {'firstName': 'Jeremy', 'lastName': 'Evans', 'teamId': '1', 'yearsPro': '7', 'collegeName': 'Western Kentucky', 'country': 'USA', 'playerId': '162', 'dateOfBirth': '1987-10-24', 'affiliation': 'Western Kentucky/USA', 'startNba': '2010', 'heightInMeters': '2.06', 'weightInKilograms': '90.7', 'leagues': {'standard': {'jersey': '6', 'active': '1', 'pos': 'F'}}}, 
            {'firstName': 'Treveon', 'lastName': 'Graham', 'teamId': '1', 'yearsPro': '3', 'collegeName': 'Va Commonwealth', 'country': 'USA', 'playerId': '199', 'dateOfBirth': '1993-10-28', 'affiliation': 'Virginia Commonwealth/USA', 'startNba': '2016', 'heightInMeters': '1.96', 'weightInKilograms': '99.3', 'leagues': {'standard': {'jersey': '2', 'active': '1', 'pos': 'G-F'}}}, 
            {'firstName': 'Kirk', 'lastName': 'Hinrich', 'teamId': '1', 'yearsPro': '12', 'collegeName': 'Kansas', 'country': 'USA', 'playerId': '241', 'dateOfBirth': '1981-01-02', 'affiliation': '', 'startNba': '2003', 'heightInMeters': '1.93', 'weightInKilograms': '86.2', 'leagues': {'standard': {'jersey': '12', 'active': '', 'pos': 'G'}}}, {'firstName': 'Matt', 'lastName': 'Mooney', 'teamId': '1', 'yearsPro': '0', 'collegeName': 'Texas Tech', 'country': '', 'playerId': '2337', 'dateOfBirth': '1997-02-07', 'affiliation': 'Texas Tech', 'startNba': '0', 'heightInMeters': '1.9', 'weightInKilograms': '90.7', 'leagues': {'vegas': {'jersey': '13', 'active': '1', 'pos': 'G'}}}, 
            {'firstName': 'Reid', 'lastName': 'Travis', 'teamId': '1', 'yearsPro': '0', 'collegeName': 'Kentucky', 'country': '', 'playerId': '2338', 'dateOfBirth': '1995-11-25', 'affiliation': 'Kentucky', 'startNba': '0', 'heightInMeters': '2.03', 'weightInKilograms': '108.0', 'leagues': {'vegas': {'jersey': '32', 'active': '1', 'pos': 'F'}}}, 
            {'firstName': 'Sedrick', 'lastName': 'Barefield', 'teamId': '1', 'yearsPro': '0', 'collegeName': 'Utah', 'country': 'USA', 'playerId': '2374', 'dateOfBirth': '1996-11-18', 'affiliation': 'University of Utah/USA', 'startNba': '0', 'heightInMeters': '1.88', 'weightInKilograms': '86.2', 'leagues': {'vegas': {'jersey': '63', 'active': '1', 'pos': 'G'}}}
        ]}
    }

    # check that lookup returned data
    if not dataset:
        return render(request, "apology.html")    
    

    # remove players that only played in summer leagues etc. and randomise players
    players = dataset["api"]["players"]
    players = [
        player for player in players if
        "standard" in player["leagues"] and player["affiliation"] != ""
    ]
    players = random.sample(players, len(players))

    # define questions
    # TODO: add code to incorrect answers to exclude them picking the same value as the correct answer by chance
    questions = [
    {
        "question": f"What division do the {team} play in?",
        "answers": {
        "a": f"{divisions[2]}",
        "b": f"{divisions[0]}",
        "c": f"{divisions[1]}"
        },
        "correctAnswer": "b"
    }, 
    {
        "question": f"What jersey number does {players[0]['firstName']} {players[0]['lastName']} wear?",
        "answers": {
        "a": f"{players[0]['leagues']['standard']['jersey']}",
        "b": f"{players[1]['leagues']['standard']['jersey']}",
        "c": f"{players[2]['leagues']['standard']['jersey']}"
        },
        "correctAnswer": "a"
    },
    {
        "question": f"How many years has {players[1]['firstName']} {players[1]['lastName']} been in the league?",
        "answers": {
        "a": f"{random.randint(0,7)}", # TODO: decent chance of being same number as correct answer
        "b": f"{players[1]['yearsPro']}",
        "c": f"{random.randint(8,16)}"  # TODO: decent chance of being the same as a/b, add in code to exclude options
        },
        "correctAnswer": "b"
    },
    {
        "question": f"Where did {players[2]['firstName']} {players[2]['lastName']} play before he entered the NBA?",
        "answers": {
        "a": f"{players[3]['affiliation'].rpartition('/')[0]}",
        "b": f"{players[1]['affiliation'].rpartition('/')[0]}",
        "c": f"{players[2]['affiliation'].rpartition('/')[0]}",
        },
        "correctAnswer": "c"
    },
    {
        "question": f"What year was {players[3]['firstName']} {players[3]['lastName']} born?",
        "answers": {
        "a": f"{players[3]['dateOfBirth'][0:4]}",
        "b": f"{players[4]['dateOfBirth'][0:4]}",
        "c": f"{players[2]['dateOfBirth'][0:4]}"
        },
        "correctAnswer": "a"
    },
    {
        "question": f"How tall is {players[4]['firstName']} {players[4]['lastName']}?",
        "answers": {
        "a": f"{players[5]['heightInMeters']} m",
        "b": f"{players[3]['heightInMeters']} m",
        "c": f"{players[4]['heightInMeters']} m"
        },
        "correctAnswer": "c"
    },
    {
        "question": f"How much does {players[5]['firstName']} {players[5]['lastName']} weigh?",
        "answers": {
        "a": f"{players[5]['weightInKilograms']} kg",
        "b": f"{players[6]['weightInKilograms']} kg",
        "c": f"{players[4]['weightInKilograms']} kg"
        },
        "correctAnswer": "a"
    }
    ]
    # randomise questions
    questionList = random.sample(questions, len(questions))
    
    
    return render(request, "quiz.html", {
        "questionList": questionList,
        "team": team
    })

