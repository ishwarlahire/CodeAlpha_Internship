print("Welcome to Basic Chatbot")
print("Type 'bye' to exit\n")

while True:
    msg = input("You: ").lower()

    if msg == "hello" or msg == "hi":
        print("Bot: Hi!")
    
    elif msg == "how are you":
        print("Bot: I'm fine, thanks!")
    
    elif msg == "what is your name":
        print("Bot: My name is ChatBot, Made by Ishwar Lahire")
    
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")