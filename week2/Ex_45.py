import random


def intro():
    print("*****ESCAPE THE MAZE*****")


class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n- - - - - - - - ")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "You died. Game over.",
        "Oops! You failed to escape.",
        "Better luck next time.",
        "Looks like this is the end for you.",
    ]

    def enter(self):
        print(random.choice(Death.quips))
        exit(1)


class Start(Scene):
    def enter(self):
        print("You find yourself trapped in a maze.")
        print("You must find your way out to escape.")
        print("Which direction do you choose?")
        action = input("(left/right): ").lower()

        if action == "left":
            print("You head left and encounter a dead end.")
            return "death"
        elif action == "right":
            print("You head right and find a path leading deeper into the maze.")
            return "corridor"
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")
            return "start"


class LongCorridor(Scene):
    def enter(self):
        print("You enter a long corridor with multiple twists and turns.")
        print("There's an eerie silence, and you feel like you're being watched.")
        print("What do you do?")
        action = input("(advance/retreat): ").lower()
        if action == "uzumymw":
            print("Cheat Activated!...Invincibility Enabled..")
            return "treasure"
        elif action == "advance":
            print("You continue forward, cautiously navigating the twists and turns.")
            print("Suddenly, you stumble upon a door.")
            return "treasure"
        elif action == "relocate":
            print("You decide to retreat and try another path.")
            print("As you turn around, you come face to face with a menacing figure.")
            return "death"
        else:
            print("Invalid choice. Please enter 'advance' or 'retreat'.")
            return "corridor"


class Treasure(Scene):
    def enter(self):
        print("You've reached the end of the maze and found the treasure!")
        print("Congratulations! You successfully escaped!")
        exit(0)


class Map(object):
    scenes = {
        "start": Start(),
        "corridor": LongCorridor(),
        "treasure": Treasure(),
        "death": Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


if __name__ == "__main__":

    intro()
    a_map = Map("start")
    a_game = Engine(a_map)
    a_game.play()
