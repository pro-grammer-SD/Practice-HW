import random
import re
import time
from datetime import datetime, timezone
from colorama import Fore, Style, init

init(autoreset=True)

# Data
cities = ["Paris", "Tokyo", "New York", "Barcelona", "Rome", "Dubai"]
packing_tips = [
    "Roll your clothes to save space.",
    "Pack versatile outfits you can mix and match.",
    "Don't forget a universal charger.",
    "Pack travel-size toiletries."
]
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I asked the librarian if the library had books on paranoia. She whispered, 'They're right behind you.'",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]
news_samples = [
    "New airline routes open between Europe and Asia.",
    "Travel restrictions eased for vaccinated travelers.",
    "Eco-tourism is booming in 2025!"
]
weather_samples = [
    "Sunny and warm with a slight breeze.",
    "Cloudy with chances of rain later in the day.",
    "Clear skies and perfect for sightseeing!",
    "Chilly morning, but warming up by noon."
]

# State
state = None
last_city = None
history_file = "chat_history.txt"

# Functions
def respond(msg, color=Fore.CYAN):
    print(f"{color}TravelBot: {msg}")

def get_random_city():
    return random.choice(cities)

def get_weather(city):
    return f"The weather in {city} is: {random.choice(weather_samples)}"

def get_time(city):
    timezone_offsets = {
        "Paris": 2, "Tokyo": 9, "New York": -4,
        "Barcelona": 2, "Rome": 2, "Dubai": 4
    }
    now_utc = datetime.now(timezone.utc)
    offset = timezone_offsets.get(city, 0)
    local_time = now_utc.hour + offset
    return f"The local time in {city} is {local_time % 24:02d}:{now_utc.minute:02d}"

def save_history(user_input):
    with open(history_file, "a") as f:
        f.write(user_input + "\n")

def handle_input(user_input):
    global state, last_city

    save_history(user_input)

    if user_input in ["exit", "bye"]:
        respond("Safe travels! 👋")
        return False

    if state == "confirm_city":
        if re.search(r"\byes\b", user_input):
            respond(f"Awesome! Enjoy {last_city}!")
        elif re.search(r"\bno\b", user_input):
            new_city = get_random_city()
            last_city = new_city
            respond(f"No worries. Maybe try {new_city}?")
        else:
            respond("Just say 'yes' or 'no'.")
        state = None
        return True

    # If a known city name is in the input, set it as last_city
    for city in cities + ["kolkata"]:  # Add extra cities here
        if re.search(rf"\b{re.escape(city.lower())}\b", user_input):
            last_city = city
            respond(f"Got it! {city} is saved as your current city.")
            return True

    if re.search(r"\b(recommend|city|travel|trip)\b", user_input):
        last_city = get_random_city()
        respond(f"How about {last_city}?")
        respond("Do you like it? (yes/no)")
        state = "confirm_city"
    elif re.search(r"\bpack|packing\b", user_input):
        respond(random.choice(packing_tips))
    elif re.search(r"\bjoke\b", user_input):
        respond(random.choice(jokes), color=Fore.MAGENTA)
    elif re.search(r"\bnews\b", user_input):
        respond(f"Latest travel update: {random.choice(news_samples)}", color=Fore.BLUE)
    elif re.search(r"\bweather\b", user_input):
        if last_city:
            respond(get_weather(last_city))
        else:
            respond("Please tell me a city first so I know where to check weather.")
    elif re.search(r"\btime\b", user_input):
        if last_city:
            respond(get_time(last_city))
        else:
            respond("Please tell me a city first so I know where to check time.")
    else:
        respond("Try asking for a 'recommendation', 'packing' tip, 'joke', 'news', 'weather', or 'time'.")
    return True

# Startup
respond("Hey! I'm your travel buddy ✈️", Fore.CYAN)
print(f"{Fore.CYAN}I can:\n- Suggest travel spots\n- Offer packing tips\n- Tell a joke\n- Give news/weather/time updates\nType 'exit' or 'bye' to end.\n")

# Main loop
while True:
    user = input(Fore.YELLOW + "You: " + Style.RESET_ALL).strip().lower()
    if not handle_input(user):
        break
