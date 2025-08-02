print("MultiBot: Hey there! I am MultiBot! I can do Many things!")
print("Type 'features' to see what I can do!")
print("Type 'End' to close program.")


questions = {
    "What is the capital of Japan?": "Tokyo",
    "Who discovered gravity when an apple fell on his head?": "Isaac Newton",
    "What is the smallest prime number?": "2",
    "Which language is primarily spoken in Brazil?": "Portuguese",
    "What does HTTP stand for?": "HyperText Transfer Protocol",
    "How many legs does a spider have?": "8",
    "What gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "What is the longest river in the world?": "Nile",
    "Who is the author of 'Harry Potter'?": "J.K. Rowling",
    "What planet do we live on?": "Earth",
    "What is the capital of France?": "Paris",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the boiling point of water in Celsius?": "100",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "In which year did India gain independence?": "1947",
    "What is the chemical symbol for Gold?": "Au",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the square root of 64?": "8",
    "Who is known as the father of computers?": "Charles Babbage"
}


import multibotfunc
import variables
while True:
    
    user = input("You: ").strip().lower()
    
    if user == "end":
        break
    elif user == "exit":
        print("MultiBot: If you're trying to close program, type 'End'.")
        continue
    if user == "quiz":
        while True:
            
            finished = multibotfunc.quiz(questions)
            if not finished:
                break
            _ = input("Try Again? (yes/no): ").strip().lower()
            if _ != "yes":
                print("Exiting Quiz Mode...")
                break
                
    elif user == "calc":
        multibotfunc.calc()
    elif any(phrase in user for phrase in variables.memory_phrases):
        if multibotfunc.last_result is not None:
            print(f"Your last result was {multibotfunc.last_result}")
        else:
            print("MultiBot: No Calculations done yet!")
    elif any(phrase in user for phrase in variables.how_are_you_phrases):
        print("MultiBot: I am fine!! you good?")
    elif any(phrase in user for phrase in variables.who_are_you_phrases):
        print("MultiBot: I am MultiBot! I can do MANY things!")
    elif any(greet in user for greet in variables.greetings):
        print("MultiBot: Hellooo!")
    elif any(phrase in user for phrase in variables.bye_phrases):
        print("MultiBot: Bah-bye!! Type 'End' to close program...")
    elif any(phrase in user for phrase in variables.help_phrases):
        print("""Intructions to Use MultiBot:
-Calculator Mode: Type 'Calc' to activate. Choose any of the operations (+, - , *, /) and select your numbers!
-Quiz Mode: Type 'Quiz' to activate. Answer all the questions and try to get a perfect score!
-Type 'exit' to quit modes or 'end' to close program""")
        
    elif user == "features":
        print("""MultiBot: These are my Features:
-Caclculator ( Type 'Calc' to activate)
-Quiz (Type 'Quiz' to activate)
If you need further instructions type 'help'""")
        continue
        
    else:
        print("Sorry, I do not understand that yet.")    