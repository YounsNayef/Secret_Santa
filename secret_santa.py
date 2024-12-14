import random
from time import sleep

def print_with_delay(message, delay=1):
    print(message)
    sleep(delay)

def assign_secret_santa(participants):
    # Make a copy of participants list for receivers
    receivers = participants.copy()
    assignments = {}
    
    for giver in participants:
        possible_receivers = [r for r in receivers if r != giver]
        
        if not possible_receivers:
            return assign_secret_santa(participants)
        
        chosen_receiver = random.choice(possible_receivers)
        assignments[giver] = chosen_receiver
        receivers.remove(chosen_receiver)
    
    return assignments

def main():
    print_with_delay("🎄 Secret Santa Generator 🎄")
    print_with_delay("\nLet's set up your Secret Santa exchange!", 1.5)
    
    # Get participants
    participants = []
    while True:
        name = input("\nEnter participant's name (or press Enter when done): ").strip()
        if not name:
            if len(participants) < 3:
                print("Come on, we need at least 3 people for this to be fun! 😊")
                continue
            break
        
        if name in participants:
            print("Oops! This person is already on the list! 😅")
            continue
            
        participants.append(name)
        print(f"Added {name} to the list! 🎁")

    print_with_delay("\nAlright, mixing things up...", 1.5)
    print_with_delay("Checking it twice...", 1.5)
    print_with_delay("Making sure it's nice...", 1.5)

    # Make assignments
    assignments = assign_secret_santa(participants)

    # Display results
    print("\n🎉 Here are your Secret Santa assignments! 🎉")
    print("\nMake sure each person only sees their own assignment!")
    print("-" * 50)

    for giver, receiver in assignments.items():
        input(f"\nPress Enter to see who {giver} is buying for...")
        print(f"🎁 {giver}, you're getting a gift for... {receiver}!")
        print("\n" + "-" * 50)

    print("\nAll done! Happy gifting! 🎄✨")
    print("Remember to keep it a secret! 🤫")

if __name__ == "__main__":
    main() 