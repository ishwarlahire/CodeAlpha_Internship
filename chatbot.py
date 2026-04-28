# TASK 4: Basic Chatbot Goal: Build a simple rule-based chatbot. Scope: ● Input from user like: "hello", "how are you", "bye". ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!". Key Concepts Used: if-elif, functions, loops, input/output.
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