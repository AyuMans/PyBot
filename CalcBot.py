print("CalcBot: Hey! I am CalcBot! 🤖")
print("Type 'Calculator' to start calculating!")
print("If you are done, type 'exit' to stop calculating!")
print("Type 'Bye' to end program.")
print("If you need further instructions, just ask! :D")

greetings = [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "howdy",
    "greetings",
    "welcome",
    "what's up",
    "what’s going on",
    "how are you",
    "how's it going",
    "how do you do",
    "nice to meet you",
    "pleased to meet you",
    "yo",
    "sup",
    "whassup",
    "wassup",
    "‘sup",
    "hey there",
    "heyyy",
    "hiya",
    "hiiii",
    "holla",
    "yo yo",
    "what’s good",
    "what's poppin",
    "what’s cookin",
    "howzit",
    "hey buddy",
    "how you doin’",
    "long time no see",
    "hola",
    "bonjour",
    "ciao",
    "namaste",
    "salam",
    "konnichiwa",
    "annyeong",
    "ola",
    "sawasdee",
    "hallo"
]

how_are_you_phrases = [
    "how are you",
    "how are you doing",
    "how’s it going",
    "how are things",
    "how have you been",
    "how do you do",
    "you good",
    "what’s up",
    "what up",
    "sup",
    "how you doing",
    "how r u",
    "how are u",
    "how u doing",
    "you okay",
    "are you okay",
    "everything good",
    "you doing fine",
    "what’s going on",
    "are you alright",
    "im fine how are you",
    "i'm fine how are you",
    "i am fine how are you",
    "i’m doing good how about you",
    "i’m okay how are you",
    "i’m great how are you",
    "all good how about you",
    "doing fine what about you"
]

who_are_you_phrases = [
    "who are you",
    "who r u",
    "what is your name",
    "what’s your name",
    "tell me your name",
    "identify yourself",
    "can you tell me your name",
    "who is this",
    "who am i talking to",
    "who am i speaking to",
    "what do i call you",
    "are you a bot",
    "are you human",
    "are you real",
    "you real",
    "are you alive",
    "what are you",
    "what even are you",
    "what kind of bot are you",
    "you ai",
    "are you ai"
]

bye_phrases = [
    "bye",
    "goodbye",
    "see you",
    "see ya",
    "later",
    "catch you later",
    "talk to you later",
    "see you later",
    "ciao",
    "peace",
    "farewell",
    "take care",
    "gotta go",
    "i'm out",
    "i have to go",
    "bye bye",
    "see ya later",
    "gtg",
    "ttyl",
    "adios",
    "ok bye",
    "ok goodnight",
    "good night",
    "night",
    "buh bye",
    "have a good day",
    "have a nice day",
    "until next time",
    "cya"
]

help_phrases = [
    "help",
    "i need help",
    "can you help me",
    "please help",
    "could you help me",
    "i want help",
    "how does this work",
    "how to use this",
    "what can you do",
    "what are your features",
    "show me what you can do",
    "what commands can i use",
    "tell me your functions",
    "help me out",
    "assist me",
    "give me help",
    "how does it work",
    "explain yourself",
    "what are you for",
    "what do i type",
    "i’m confused",
    "i dont understand",
    "i do not understand",
    "can you explain",
    "commands list",
    "usage",
    "instructions",
    "support",
    "show help",
    "how do i start",
    "how to begin",
    "how to start"
]

memory_phrases = [
    "what was the result",
    "last result",
    "previous result",
    "last answer",
    "previous answer",
    "what did i get",
    "tell me the last result"
]

last_result = None


def Calc():
    global last_result
    
    while True:
            op = input("Operation: ").strip().lower()
            if op == "exit":
                print("Exiting...")
                return
    
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second Number: "))
            except ValueError:
                print("CalcBot: Numbers Only!")
                continue
            
            if op == "+":
                last_result = num1 + num2
                print(f"Result: {last_result}")
                
            elif op == "-":
                last_result = num1 - num2
                print(f"Result: {last_result}")
            elif op == "*" or op == "x":
                last_result = num1 * num2
                print(f"Result: {last_result}")
            elif op == "/":
                last_result = num1 / num2
                if num2 == 0:
                    print("ERROR: Division by Zero!")
                else:
                    print(f"Result: {last_result}")
            elif op == "%":
                last_result = num1 % num2
                print(f"Result: {last_result}")
            elif op == "^" or "**":
                last_result = num1 ** num2
                print(f"Result: {last_result}")

            else:
                print(f"Syntax Error --> Operation Error --> '{op}'")
                
while True:
    

    user = input("You: ").strip().lower()
    if user.strip() == "calculator":
        Calc()
    elif any(phrase in user for phrase in how_are_you_phrases):
        print("CalcBot: I am fine 🎉 ! How about you?")
    elif any(phrase in user for phrase in who_are_you_phrases):
        print("CalcBot: I am CalcBot! 🤖 I can Calculate numbers!")
    elif any(greet in user for greet in greetings):
        print("CalcBot: Hello! How are you?")
    elif any(phrase in user for phrase in help_phrases):
        print("""CalcBot: 🤖 Here's how you can use me!
- Type 'calculator' to start math mode
- Use +, -, *, or / and input your numbers
- Type 'Last Result' to view your last result
- Type 'exit' to quit
Happy Calculating! 🎉""")
    elif any(phrase in user for phrase in memory_phrases):
        if last_result is not None:
            print(f"CalcBot: Your Last result was {last_result}")
        else:
            print("CalcBot: No calculation done yet!")
    elif any(phrase in user for phrase in bye_phrases):
        print("CalcBot: Bye! 🤖")
        break
    else:
        print("CalcBot: Sorry, I do not understand that yet! :(")
                    
        
            
        