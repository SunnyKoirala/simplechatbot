from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("MyBot")
trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

print("Type 'exit' to stop the chatbot.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = bot.get_response(user_input)
    print("Bot:", response)
