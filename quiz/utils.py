import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_counter = 0     # TODO: currently resets when server restarts. Maybe store in session or browser cache?
API_KEY = os.getenv("API_KEY")

# API call for team/player info
def lookup(quiz_type, *args):       # Optional arguments specify which team/player etc.

    global api_counter
    print(api_counter)
    if api_counter > 50:
        return False        # TODO: returning False might not be the best way to signal a problem

    # TODO: separate API info into .env file
    else:
        url = f"https://api-nba-v1.p.rapidapi.com/players/teamId/{args[0]}"
        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
        }
        response = requests.request("GET", url, headers=headers)
        api_counter += 1
        return response.json()
