from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime, timedelta
import requests

# Initialize ChatterBot
bot = ChatBot("MyBot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Replace with your actual OpenWeatherMap API key
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
WEATHER_CITY = "Kathmandu"

print("Type 'exit' to stop the chatbot.")

while True:
    user_input = input("You: ")
    user_input_lower = user_input.lower()

    # Exit condition
    if user_input_lower == 'exit':
        break

    # Time in Nepal
    elif "time" in user_input_lower or "current time in nepal" in user_input_lower:
        nepal_time = datetime.utcnow() + timedelta(hours=5, minutes=45)
        print("Bot: The current time in Nepal is:", nepal_time.strftime("%I:%M %p, %A"))

    # Live weather in Kathmandu (or another chosen city)
    elif "weather" in user_input_lower or "weather today" in user_input_lower:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={WEATHER_CITY}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            print(f"Bot: The current weather in {WEATHER_CITY} is {temp}°C and {desc}.")
        else:
            print("Bot: Sorry, I couldn't fetch the latest weather right now.")
    
    # NLP definition
    elif "nlp" in user_input_lower or "natural language processing" in user_input_lower:
        print("Bot: Natural Language Processing (NLP) helps computers understand, interpret, and respond to human language.")

    # Ambiguity definition
    elif "ambiguity" in user_input_lower:
        print("Bot: Ambiguity means a word, phrase, or sentence can be understood in more than one way, making its meaning unclear.")
    
    # Core banking definition
    elif "core banking" in user_input_lower:
        print("Bot: Core banking is a centralized system for managing bank transactions, accounts, and customer services in real time.")

    # Exam tips
    elif "exam tips" in user_input_lower or "how to prepare for exam" in user_input_lower:
        print("Bot: Revise all key topics, practice sample questions, time yourself, and focus on your weak areas.")

    # Greetings
    elif user_input_lower in ["hello", "hi", "hey"]:
        print("Bot: Hi! How can I help you today?")
    elif "good morning" in user_input_lower:
        print("Bot: Good morning! Hope you have a productive day!")
    elif "good night" in user_input_lower:
        print("Bot: Good night! Sleep well!")

    # Default ChatterBot conversation
    else:
        response = bot.get_response(user_input)
        print("Bot:", response)
