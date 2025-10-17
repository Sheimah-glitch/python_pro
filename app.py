# --- 1. DISPLAY FUNCTIONS ---
def show_intro():
    print("💰 Welcome to SmartMoney - Your Financial Literacy App 💰")
    print("Learn how to manage your money, save smart, and avoid debt")

def show_menu():
    print("--- Choose a topic to learn: ---")
    print("1. Budgeting Basics")
    print("2. Saving and Investing") 
    print("3. Understanding Debt")
    print("4. Exit")

# --- 2. QUIZ FUNCTION (Defined First) ---
def quiz(topic):
    questions = {
        "budgeting": [
            {
                "q": "What percentage of income should ideally go to savings in the 50/30/20 rule?",
                "a": "20"
            }
        ],
        "saving": [
            {"q": "True or False: Saving small amount regularly is better than saving large amounts rarely.", "a": "true"}
        ],
        "debt" :[
            {"q": "Is all debt bad? (yes/no)", "a": "no"}
        ]
    }
    
    score = 0 
    
    if topic not in questions:
        print(f"Error: Quiz topic '{topic}' not found.")
        return

    print(f"--- Starting Quiz for: {topic.capitalize()} ---")
    
    for q in questions[topic]:
        
        answer = input(q["q"] + " ").lower().strip() 
        if answer == q["a"].lower().strip(): 
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Oops! The correct answer was {q['a']}")  

    print(f"Your score for this lesson: {score}/{len(questions[topic])}")


# --- 3. LESSON FUNCTIONS ---
def budgeting_lesson():
    print("📘 Budgeting Basics 📘")
    print("A budget helps you track how much money you earn and spend.")
    print("Tip: Try the 50/30/20 rule - 50% needs, 30% wants, 20% savings.")
    quiz("budgeting")

def saving_lesson():
    print("🏦 Saving and Investing 🏦")  
    print("Saving helps you handle emergencies and reach goals.")
    print("Tip: Start small, but stay consistent - even 100 bob a week add up!")
    quiz("saving")

def debt_lesson():
    print("💳 Understanding Debt 💳")  
    print("Debt isn't always bad, but high-interest loans can trap you.")
    print("Tip: Borrow only what you can repay and compare interest rates.")
    quiz("debt")

# --- 4. MAIN PROGRAM EXECUTION ---

def main():
    show_intro()
    while True:
        show_menu()
        # Added space after colon for better input prompt
        choice = input("Enter your choice (1-4): ").strip() 
        if choice == "1":
            budgeting_lesson()
        elif choice == "2":
            saving_lesson()
        elif choice == "3":
            debt_lesson()
        elif choice == "4":
            print("Goodbye! Keep learning and managing your money wisely")  
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()