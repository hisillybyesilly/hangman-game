import random
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

def clear_screen():
    # Clear screen command for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
clear_screen()
print(f"\n{Fore.BLUE}✨ Welcome to the Mythical Creature Quiz! ✨{Style.RESET_ALL}")
print(f"{Fore.CYAN}Answer these questions to discover which mythical creature matches your personality!{Style.RESET_ALL}\n")

# Questions for the quiz
questions = [
    {
        "question": "How do you handle challenges?",
        "options": [
            "Face them head-on with courage",
            "Use wisdom and strategy",
            "Rely on your instincts",
            "Seek help from others",
            "Transform the situation"
        ]
    },
    {
        "question": "What's your ideal environment?",
        "options": [
            "High mountains and open skies",
            "Deep forests and ancient trees",
            "Mystical lakes and rivers",
            "Hidden caves and treasures",
            "Magical gardens and flowers"
        ]
    },
    {
        "question": "What's your greatest strength?",
        "options": [
            "Raw power and strength",
            "Wisdom and knowledge",
            "Speed and agility",
            "Magic and transformation",
            "Protection and loyalty"
        ]
    }
]

# Mythical creatures and their descriptions
creatures = {
    "Dragon": {
        "description": "Powerful and wise, you're a natural leader with immense strength and knowledge.",
        "traits": ["Strong", "Wise", "Protective", "Majestic"],
        "color": Fore.RED
    },
    "Unicorn": {
        "description": "Pure of heart and magical in nature, you bring light and hope wherever you go.",
        "traits": ["Pure", "Magical", "Graceful", "Healing"],
        "color": Fore.WHITE
    },
    "Phoenix": {
        "description": "You have the amazing ability to rise from challenges stronger than before.",
        "traits": ["Renewal", "Strength", "Transformation", "Hope"],
        "color": Fore.YELLOW
    },
    "Mermaid": {
        "description": "Mysterious and free-spirited, you navigate life's waters with grace and intuition.",
        "traits": ["Mysterious", "Free", "Intuitive", "Adaptable"],
        "color": Fore.BLUE
    },
    "Loch Ness Monster": {
        "description": "Mysterious and playful, you love exploring and discovering new things.",
        "traits": ["Mysterious", "Playful", "Curious", "Friendly"],
        "color": Fore.CYAN
    },
    "Pegasus": {
        "description": "Free-spirited and graceful, you soar through life with elegance and determination.",
        "traits": ["Free", "Graceful", "Determined", "Elegant"],
        "color": Fore.MAGENTA
    },
    "Kraken": {
        "description": "Mysterious and powerful, you command respect and have deep emotional strength.",
        "traits": ["Mysterious", "Powerful", "Deep", "Commanding"],
        "color": Fore.BLUE
    },
    "Yeti": {
        "description": "Strong and gentle, you're a protector who loves the mountains and snow.",
        "traits": ["Strong", "Gentle", "Protective", "Mysterious"],
        "color": Fore.WHITE
    },
    "Siren": {
        "description": "You have a powerful voice and can influence others with your words and charm.",
        "traits": ["Charming", "Powerful", "Mysterious", "Influential"],
        "color": Fore.RED
    },
    "Bigfoot": {
        "description": "Mysterious and kind, you love exploring nature and helping others while staying hidden.",
        "traits": ["Mysterious", "Kind", "Helpful", "Adventurous"],
        "color": Fore.GREEN
    }
}

def get_user_choice(question, options):
    clear_screen()
    print(f"\n{Fore.CYAN}{question}{Style.RESET_ALL}")
    for i, option in enumerate(options, 1):
        print(f"{Fore.BLUE}{i}. {option}{Style.RESET_ALL}")
    
    while True:
        try:
            choice = input(f"\n{Fore.GREEN}Enter your choice (1-5) or 'n' to skip: {Style.RESET_ALL}")
            if choice.lower() == 'n':
                return random.randint(1, 5)
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            print(f"{Fore.RED}Please enter a number between 1 and 5.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

def calculate_result(answers):
    scores = {creature: 0 for creature in creatures}
    
    for answer in answers:
        if answer == 1:  # Dragon-like answers
            scores["Dragon"] += 2
        elif answer == 2:  # Unicorn-like answers
            scores["Unicorn"] += 2
        elif answer == 3:  # Phoenix-like answers
            scores["Phoenix"] += 2
        elif answer == 4:  # Mermaid-like answers
            scores["Mermaid"] += 2
        else:  # Loch Ness Monster-like answers
            scores["Loch Ness Monster"] += 2
    
    return max(scores.items(), key=lambda x: x[1])[0]

def main():
    answers = []
    
    for q in questions:
        choice = get_user_choice(q["question"], q["options"])
        answers.append(choice)
    
    clear_screen()
    result = calculate_result(answers)
    creature_info = creatures[result]
    
    print(f"\n{Fore.MAGENTA}✨ Your Mythical Creature Match ✨{Style.RESET_ALL}")
    print(f"\n{creature_info['color']}{result}{Style.RESET_ALL}")
    print(f"\n{creature_info['description']}")
    print(f"\n{Fore.CYAN}Your Traits:{Style.RESET_ALL}")
    for trait in creature_info["traits"]:
        print(f"{creature_info['color']}• {trait}{Style.RESET_ALL}")
    
    print(f"\n{Fore.MAGENTA}Thanks for taking the quiz! ✨{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 