
def quiz(questions):
    score = 0
    
    while True:
        
        import random
        items = random.sample(list(questions.items()), 10)
        random.shuffle(items)
        for q, a in items:
            op = input(q + " ").strip().lower()
            if op == "exit":
                print("Quiting Quiz...")
                print(f"Your score is {score}/10")
                if score == 0:
                    print("MultiBot: Bro you kinda suck...")
                return False
            elif op == a.strip().lower():
                print("Correct!")
                score += 1
            else:
                print("Wrong. The answer is", a)
                continue
        print(f"Your score is {score}/10")
        if score == 10:
            print("MultiBot: WOW! A PERFECT SCORE!")
        elif score == 0:
            print("MultiBot: Bro you kinda suck...")
        return True
    
last_result = None  
def calc():
    
    global last_result
    
    while True:
        op = input("Operation: ").strip().lower()
        if op == "exit":
            print("Exiting Calculator...")
            return last_result
        try:
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
        except ValueError:
            print("MultiBot: Numbers Only!")
            continue
        if op == "+":
            last_result = num1 + num2
        elif op == "-":
            last_result = num1 - num2
        elif op == "*" or op == "x":
            last_result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("ERROR: Division by Zero!")
                continue
            else:
                last_result = num1 / num2
        print(f"Result: {last_result}")
        
import variables
def chat(user):
# 📌 Handling response outside the function (in a different file)?
# ✅ Always use return instead of print!
# 📂 Main file → Presentation layer
# 📄 Function files (like myfunc.py) → Logic layer
# 📄 Func file: What will the function DO?
# 📂 Main file: How will the function be PRESENTED?
#     (printed, logged, stored, sent to a website, etc.)
    
    if any(phrase in user for phrase in variables.how_are_you_phrases):
        return "I am fine! You good?"
    elif any(phrase in user for phrase in variables.who_are_you_phrases):
        return "I am !"
    elif any(greet in user for greet in variables.greetings):
        return "Helloo!"
    elif any(phrase in user for phrase in variables.bye_phrases):
        return "Bah-Bai! Type 'end' to close program..."
    elif any(phrase in user for phrase in variables.help_phrases):
        return (
            "Instructions to Use Bot:\n"
            "- Calculator Mode: Type 'calc' to activate. Choose any of the operations (+, - , *, /) and select your numbers!\n"
            "- Quiz Mode: Type 'quiz' to activate. Answer all the questions and try to get a perfect score!\n"
            "- Type 'exit' to quit modes or 'end' to close program"
        )
    else:
        return None

        