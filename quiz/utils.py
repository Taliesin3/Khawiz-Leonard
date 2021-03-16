import requests
import os
from datetime import date
from dotenv import load_dotenv
load_dotenv()

TODAY = date.today().strftime("%d")

# API call for team/player info
# Optional args specify which team/player etc.
def lookup(quiz_type, *args):       
    get_date = date.today().strftime("%d")
    
    if get_date != TODAY:
        TODAY = get_date
        os.environ["API_COUNT"] = 0

    API_COUNT = os.environ.get("API_COUNT")
    
    # 100 API calls per day on free plan
    if API_COUNT > 75:
        print("Error: Daily API call limit exceeded, please try again tomorrow.")
        return False
    else:
        API_KEY = os.environ.get("API_KEY")

    if quiz_type == "team":
        url = f"https://api-nba-v1.p.rapidapi.com/players/teamId/{args[0]}"
        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
        }
        response = requests.request("GET", url, headers=headers)
        os.environ["API_COUNT"] = API_COUNT + 1
        return response.json()
    
    if quiz_type == "player":
        url = f"https://api-nba-v1.p.rapidapi.com/players/playerId/{args[0]}"
        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        os.environ["API_COUNT"] = API_COUNT + 1
        return response.json()
