import random
from colorama import Fore, Style, init
import os
import time

# Initialize colorama
init()

# More detailed ASCII art for hangman stages (circle faces for all)
HANGMAN_ART = [
    '''
      +---+
      |   |
          |    
          |    
          |    
     _____|_____''',
    '''
      +---+
      |   |
      🙂  |    
          |    
          |    
     _____|_____''',
    '''
      +---+
      |   |
      😐  |    
      |   |    
          |    
     _____|_____''',
    '''
      +---+
      |   |
      😟  |    
     /|   |    
          |    
     _____|_____''',
    '''
      +---+
      |   |
      😰  |    
     /|\  |    
          |    
     _____|_____''',
    '''
      +---+
      |   |
      😰  |    
     /|\  |    
     /    |    
     _____|_____''',
    '''
      +---+
      |   |
      😵  |    
     /|\  |    
     / \  |    
     _____|_____'''
]

# Use the same art for both boy and girl
BOY_HANGMAN = HANGMAN_ART
GIRL_HANGMAN = HANGMAN_ART

# Words organized by increasing difficulty
WORDS = [
    # Beginner words (Level 1-2)
    {
        'animals': ['LION', 'BEAR', 'WOLF', 'SEAL', 'HAWK'],
        'space': ['STAR', 'MOON', 'MARS', 'RING', 'DUST'],
        'mythology': ['ZEUS', 'THOR', 'LOKI', 'ARES'],
        'science': ['ATOM', 'CELL', 'HEAT', 'WAVE']
    },
    # Medium words (Level 3-4)
    {
        'animals': ['DOLPHIN', 'PENGUIN', 'CHEETAH', 'OCTOPUS'],
        'space': ['METEOR', 'SATURN', 'COMET', 'NEBULA'],
        'mythology': ['DRAGON', 'PHOENIX', 'HYDRA', 'SPHINX'],
        'science': ['PLASMA', 'PROTON', 'MAGNET', 'ENERGY']
    },
    # Hard words (Level 5-6)
    {
        'animals': ['PLATYPUS', 'PANGOLIN', 'AXOLOTL', 'CHAMELEON'],
        'space': ['QUASAR', 'PULSAR', 'NEUTRON', 'ASTEROID'],
        'mythology': ['MINOTAUR', 'BASILISK', 'CHIMERA', 'KRAKEN'],
        'science': ['QUANTUM', 'ISOTOPE', 'POLYMER', 'CATALYST']
    },
    # Expert words (Level 7+)
    {
        'animals': ['RHINOCEROS', 'HIPPOPOTAMUS', 'ORANGUTAN', 'PTERODACTYL'],
        'space': ['CONSTELLATION', 'SUPERNOVA', 'MAGNETOSPHERE', 'HELIOSPHERE'],
        'mythology': ['AMPHISBAENA', 'HIPPOCAMPUS', 'LEVIATHAN', 'WENDIGO'],
        'science': ['ELECTROMAGNETIC', 'THERMODYNAMICS', 'PHOTOSYNTHESIS', 'MITOCHONDRIA']
    }
]

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color):
    """Print text in specified color."""
    print(f"{color}{text}{Style.RESET_ALL}")

def choose_character():
    """Let player choose boy or girl character."""
    while True:
        clear_screen()
        print_colored("\n👤 Choose your character:", Fore.CYAN)
        print_colored("1. Boy 👦", Fore.BLUE)
        print_colored("2. Girl 👧", Fore.MAGENTA)
        choice = input("\nEnter 1 or 2: ")
        
        if choice == '1':
            return BOY_HANGMAN, "Boy"
        elif choice == '2':
            return GIRL_HANGMAN, "Girl"
        print_colored("\n❌ Please enter 1 or 2!", Fore.RED)
        time.sleep(1)

def get_category(available_categories):
    """Let player choose category."""
    while True:
        clear_screen()
        print_colored("\n🎯 Choose your category:", Fore.CYAN)
        for i, category in enumerate(available_categories, 1):
            print_colored(f"{i}. {category.title()}", Fore.GREEN)
        choice = input(f"\nEnter a number (1-{len(available_categories)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_categories):
            return available_categories[int(choice) - 1]
        print_colored("\n❌ Please enter a valid number!", Fore.RED)
        time.sleep(1)

def get_word(games_won):
    """Get a word based on number of games won."""
    # Calculate difficulty level (0-3) based on games won
    difficulty = min(games_won // 2, 3)  # Increase difficulty every 2 wins, max at level 3
    current_words = WORDS[difficulty]
    category = random.choice(list(current_words.keys()))
    word = random.choice(current_words[category])
    return word, category, difficulty

def display_game(word, guessed_letters, tries_left, category, difficulty, hangman_art, character, message=""):
    """Display the current game state."""
    clear_screen()
    difficulty_names = ["Beginner", "Medium", "Hard", "Expert"]
    print_colored(f"\n📊 Category: {category.title()}", Fore.BLUE)
    print_colored(f"💪 Difficulty: {difficulty_names[difficulty]}", Fore.BLUE)
    print_colored(f"👤 Character: {character}", Fore.CYAN)
    print_colored(hangman_art[6 - tries_left], Fore.CYAN)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print_colored("\nWord: " + display_word, Fore.GREEN)
    print_colored("\nGuessed letters: " + ", ".join(sorted(guessed_letters)), Fore.YELLOW)
    print_colored(f"Tries left: {tries_left}", Fore.RED)
    if message:
        print_colored("\n" + message, Fore.MAGENTA)

def play_game():
    """Main game function."""
    print_colored("\n🎮 Welcome to HANGMAN! 🎮", Fore.CYAN)
    print_colored("Words get harder as you win more games in each category!", Fore.GREEN)
    time.sleep(1)
    # Track difficulty for each category
    all_categories = list(WORDS[0].keys())
    category_levels = {cat: 0 for cat in all_categories}  # 0=Beginner, 1=Medium, 2=Hard, 3=Expert
    category_wins = {cat: 0 for cat in all_categories}
    while True:
        hangman_art, character = choose_character()
        category = get_category(all_categories)
        difficulty = category_levels[category]
        current_words = WORDS[difficulty]
        word = random.choice(current_words[category])
        guessed_letters = set()
        tries_left = 6
        message = f"Category: {category.upper()}"
        won = False
        while tries_left > 0:
            display_game(word, guessed_letters, tries_left, category, difficulty, hangman_art, character, message)
            guess = input("\nGuess a letter: ").upper()
            if len(guess) != 1:
                message = "Please enter a single letter!"
                continue
            if not guess.isalpha():
                message = "Please enter a letter!"
                continue
            if guess in guessed_letters:
                message = "You already guessed that letter!"
                continue
            guessed_letters.add(guess)
            if guess in word:
                message = "Good guess! 🎉"
                if all(letter in guessed_letters for letter in word):
                    display_game(word, guessed_letters, tries_left, category, difficulty, hangman_art, character)
                    print_colored("\n🎊 Congratulations! You won! 🎊", Fore.GREEN)
                    category_wins[category] += 1
                    won = True
                    break
            else:
                tries_left -= 1
                message = "Wrong guess! 😕"
                if tries_left == 0:
                    display_game(word, guessed_letters, tries_left, category, difficulty, hangman_art, character)
                    print_colored(f"\n💔 Game Over! The word was: {word}", Fore.RED)
        if category_wins[category] > 0:
            print_colored(f"\n🏆 {category.title()} games won: {category_wins[category]}", Fore.YELLOW)
        # Only increase difficulty for this category if you won and not already at Expert
        if won and category_levels[category] < 3:
            category_levels[category] += 1
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again == 'yes':
            continue
        else:
            print_colored("\nThanks for playing! Goodbye! 👋", Fore.CYAN)
            break

if __name__ == "__main__":
    play_game() 