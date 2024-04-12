# Survival ISland
import random

player_inventory = ["knife"]
locations_visited = set()


def welcome():
    print("******Welcome to the Survival Island******")


def choose_action(location):
    print("You're at ", location)
    print("What would you like to do?\n")
    print("1. Explore the area..")
    print("2. Gather Resources..")
    print("3. Craft tools..")
    print("4. Deploy to another location..")

    action = input(">")
    if action == "1":
        explore_area(location)
    elif action == "2":
        gather_resources()
    elif action == "3":
        craft_tools()
    elif action == "4":
        deploy_to_another_location()
    else:
        print("Invalid Action! Try Again.\n")


def explore_area(location):
    print("You are exploring the area....")
    print("You find a coconut tree....\nYou hear Strange Noises...")


def gather_resources():
    resources = random.choices(["wood", "stone", "fire", "boat"])
    for resource in resources:
        print("You gather..", resource)
        player_inventory.append(resource)


def craft_tools():
    print("You craft tools...")

    if "wood" and "stone" in player_inventory:
        print("You craft a spear...")
        player_inventory.append("spear")
    else:
        print("You don't have enough resources to craft tools..")


def deploy_to_another_location():
    print("Where would you like to go?")
    print("1. Beach")
    print("2. Cave")

    choice = input("> ")
    if choice == "1":

        print("You head towards beach...")
        print("You died!...You should stay where you are...")
    elif choice == "2":
        print("You moron....You died!! Stay where you are..")


def main():
    welcome()
    current_location = "Beach"
    locations_visited.add(current_location)
    while True:
        choose_action(current_location)

        # Randomly generate an event based on location
        if random.random() < 0.3 and current_location not in locations_visited:
            print("You encounter a wild animal!")

            print("You must defend yourself or flee.")

            print("You narrowly escape the encounter.")
            locations_visited.add(current_location)


if __name__ == "__main__":
    main()
