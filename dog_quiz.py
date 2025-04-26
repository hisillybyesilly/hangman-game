import random
from colorama import init, Fore, Style, Back
import time
import os

# Initialize colorama for colored output
init()

# Dog breeds and their personality traits
DOG_BREEDS = {
    "Golden Retriever": {
        "traits": ["friendly", "patient", "intelligent", "loyal", "energetic"],
        "description": "You're like a Golden Retriever! 🌟 You're friendly, patient, and always ready to help others. Your positive attitude and loyalty make you a great friend to everyone around you. You bring sunshine wherever you go! ☀️",
        "emoji": "🐕"
    },
    "German Shepherd": {
        "traits": ["protective", "intelligent", "loyal", "confident", "courageous"],
        "description": "You're like a German Shepherd! 🦮 You're protective of your loved ones, highly intelligent, and always ready to take charge. Your confidence and courage make you a natural leader. You're the one everyone looks up to! 👑",
        "emoji": "🦮"
    },
    "Pug": {
        "traits": ["playful", "charming", "stubborn", "loving", "sociable"],
        "description": "You're like a Pug! 🐾 You're playful, charming, and love being the center of attention. Your stubborn streak and loving nature make you an unforgettable character. You're the life of the party! 🎉",
        "emoji": "🐾"
    },
    "Border Collie": {
        "traits": ["intelligent", "energetic", "focused", "hardworking", "loyal"],
        "description": "You're like a Border Collie! 🐕‍🦺 You're highly intelligent, always on the go, and incredibly focused on your goals. Your work ethic and loyalty are unmatched. You're the one who gets things done! ⚡",
        "emoji": "🐕‍🦺"
    },
    "Labrador": {
        "traits": ["friendly", "outgoing", "active", "patient", "loving"],
        "description": "You're like a Labrador! 🐕 You're outgoing, friendly, and always up for an adventure. Your patience and loving nature make you a joy to be around. You're everyone's best friend! 💖",
        "emoji": "🐕"
    }
}

# Quiz questions
QUESTIONS = [
    "How do you prefer to spend your free time?",
    "How would your friends describe your personality?",
    "What's your ideal weekend activity?",
    "How do you handle stressful situations?",
    "What's your communication style?"
]

# Answer options for each question
ANSWERS = [
    ["Relaxing at home", "Playing sports", "Socializing with friends", "Learning new things", "Going on adventures"],
    ["Friendly and outgoing", "Protective and loyal", "Playful and charming", "Focused and determined", "Patient and kind"],
    ["Movie night with friends", "Training or learning something new", "Party or social gathering", "Outdoor adventure", "Quiet time with loved ones"],
    ["Stay calm and think logically", "Take charge and solve the problem", "Try to make light of the situation", "Focus on finding a solution", "Seek support from others"],
    ["Warm and approachable", "Direct and clear", "Playful and humorous", "Professional and precise", "Empathetic and understanding"]
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    clear_screen()
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{'='*15} 🐕 DOG QUIZ 🐕 {'='*15}")
    print(f"{'='*50}{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Welcome to the most pawsome personality quiz ever! 🐾")
    print(f"Answer these questions to discover which dog breed matches your personality!{Style.RESET_ALL}\n")
    time.sleep(1)

def print_question(question, options, current_question, total_questions):
    clear_screen()
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{'='*15} Q{current_question}/{total_questions} {'='*15}")
    print(f"{'='*50}{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}{'─'*50}")
    print(f"🤔 {question}")
    print(f"{'─'*50}{Style.RESET_ALL}\n")
    
    for i, option in enumerate(options, 1):
        print(f"{Fore.WHITE}{i}. {option}{Style.RESET_ALL}")
    print()

def get_user_answer():
    while True:
        try:
            print(f"\n{Fore.CYAN}Type your choice (1-5) and press Enter")
            print(f"Or type 'n' and press Enter for next{Style.RESET_ALL}")
            choice = input("Your choice: ")
            if choice.lower() == 'n':
                return None
            if choice.isdigit() and 1 <= int(choice) <= 5:
                return int(choice) - 1
            print(f"{Fore.RED}❌ Please type 1-5 or 'n' and press Enter{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Please type a valid number{Style.RESET_ALL}")

def calculate_result(answers):
    breed_scores = {breed: 0 for breed in DOG_BREEDS}
    
    for i, answer in enumerate(answers):
        for breed, info in DOG_BREEDS.items():
            if info["traits"][i] in ANSWERS[i][answer].lower():
                breed_scores[breed] += 1
    
    max_score = max(breed_scores.values())
    matching_breeds = [breed for breed, score in breed_scores.items() if score == max_score]
    return random.choice(matching_breeds)

def print_result(breed):
    clear_screen()
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{'='*15} 🎉 RESULTS 🎉 {'='*15}")
    print(f"{'='*50}{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}You are most like a...{Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}{DOG_BREEDS[breed]['emoji']} {breed}! {DOG_BREEDS[breed]['emoji']}{Style.RESET_ALL}")
    print(f"\n{Fore.WHITE}{DOG_BREEDS[breed]['description']}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

def main():
    print_welcome()
    
    answers = []
    total_questions = len(QUESTIONS)
    
    for i, (question, options) in enumerate(zip(QUESTIONS, ANSWERS), 1):
        while True:
            print_question(question, options, i, total_questions)
            answer = get_user_answer()
            
            if answer is not None:
                answers.append(answer)
                if i < total_questions:
                    print(f"\n{Fore.YELLOW}Moving to next question...{Style.RESET_ALL}")
                    time.sleep(1)
                break
            elif i < total_questions:
                print(f"\n{Fore.YELLOW}Moving to next question...{Style.RESET_ALL}")
                time.sleep(1)
                break
            else:
                print(f"\n{Fore.RED}This is the last question! Please make a choice.{Style.RESET_ALL}")
                time.sleep(2)
    
    if len(answers) > 0:
        print(f"\n{Fore.YELLOW}Calculating your results...{Style.RESET_ALL}")
        time.sleep(2)
        
        result = calculate_result(answers)
        print_result(result)
    else:
        print(f"\n{Fore.RED}You didn't answer any questions! Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 