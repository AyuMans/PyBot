last_result = None

def Calc():
    while True:
        global last_result
        op = input("Operation: ").strip().lower()
        
        if op == "exit":
            print("Exiting...")
            return last_result
        
        try:
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
        except ValueError:
            print("CalcBot: Numbers Only!")
            continue
        
        if op == "+":
            last_result = num1 + num2
        elif op == "-":
            last_result = num1 - num2
        elif op == "*" or op == "x":
            last_result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("ERROR --> Division by Zero!")
                continue
            else:
                last_result = num1 / num2
        elif op == "%":
            last_result = num1 % num2
        elif op == "^" or op == "**":
            last_result = num1 ** num2
        else:
            print(f"Syntax Error ---> Operation Invalid --> {op}")
            continue
            
        print(f"Result: {last_result}")
        
        
        
        


def quiz(questions):
    score = 0
    import random
    while True:
        items = list(questions.items())
        random.shuffle(items)
        for q, a in items:
            user = input(q + " ").strip().lower()
            if user == "quit":
                print("Quiz Mode Off")
                print(f"QuizBot: Your score is {score}/{len(questions)}")
                return score
            if user == a.strip().lower():
                print("QuizBot: Correct!")
                score += 1
            else:
                print("QuizBot: Wrong Answer! The answer is", a)
        print(f"QuizBot: Your score is {score}/{len(questions)}")
        if score == len(questions):
            print("QuizBot: WOW! A Perfect Score!")
            
        if score == 0:
            print("QuizBot: Im sorry, but you suck!")
        return score
        
                    









            
        
        
        