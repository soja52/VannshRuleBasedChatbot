import re
import random 
from colorama import Fore, init
init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
     "cities": ["Tokyo", "Paris", "New York"]
}


jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def greet_user():
    print(Fore.CYAN + "Hello I am your travel bot, your virtual travel assistant ")
    name = input(Fore.GREEN + "What is your name?")
    print(Fore.BLUE + f"Nice to meet you {name}, How can i help you?")
    return name 

def help():
    print(Fore.LIGHTMAGENTA_EX + "I can assist you with the following")
    print(Fore.LIGHTYELLOW_EX + "Provide travel recommendations ")
    print(Fore.LIGHTWHITE_EX + "Offer packing tips")
    print(Fore.LIGHTGREEN_EX + "Tell travel jokes")
    print(Fore.LIGHTBLACK_EX + "Ask question or press exit to leave")

def process_input(user_input):
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+', ' ',user_input)
    return user_input

def provide_recommendations():
    print(Fore.LIGHTCYAN_EX + "Are you interested in beaches, mountains, or cities")
    preference = input(Fore.LIGHTYELLOW_EX + "You: ")
    preference = process_input(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.MAGENTA + f"How about visiting {suggestion}")
        print(Fore.YELLOW + "Do you like this suggestion Yes/No?")
        response = input(Fore.RED + "You: ").strip().lower()

        if response == "yes":
            print(Fore.CYAN + f"Have an amazing time in {suggestion}")
        elif response == "no":
            print(Fore.BLUE + "No worries, let's find another place")
            provide_recommendations()
        else:
             print(Fore.GREEN + "Lets start over again")
             provide_recommendations()
    else:
        print(Fore.LIGHTWHITE_EX + "Sorry I don't have any recommendations for that preference")
    help()

def packing_tips():
    print(Fore.LIGHTGREEN_EX + "Where are you travelling to?")
    destination = input(Fore.CYAN + "You: ")
    destination = process_input(destination)
    print(Fore.LIGHTMAGENTA_EX + "How many days will u stay?")
    days = input(Fore.WHITE + "You: ")
    print(Fore.LIGHTBLUE_EX + f"packing tips for {days} days in {destination}")
    print(Fore.CYAN + "pack clothing items")
    print(Fore.GREEN + "Don't forget travel adapters and chargers")
    print(Fore.YELLOW + f"Check Weather forecast before packing")

def joke():
    joke = random.choice(jokes)
    print(Fore.LIGHTCYAN_EX + F"travelbot: {joke}")
    
def chat():
    name = greet_user() 
    help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        processed_input = process_input(user_input)
        if "recommendation" in processed_input or "suggest" in processed_input:
          provide_recommendations()
        elif "pack" in processed_input or "packing" in processed_input:
          packing_tips()
        elif "joke" in processed_input or "funny" in processed_input:
          joke()
        elif "help" in processed_input:
          help()
        elif "exit" in processed_input or "bye" in processed_input:
          print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
          break
        else:
          print(Fore.RED + "TravelBot: I'm sorry, I didn't quite catch that. Could you please rephrase")

if __name__ == "__main__":

    chat()