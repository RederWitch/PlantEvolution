from generate_first_gen import generate_first_generation
from choose_parents import choose_parents
from draw_all import draw_generation
from reproducing import create_next_generation

import sys
import vpython as vp
from time import sleep

GEN_MEMBERS_COUNT = 20
HOW_MANNY_GENERATION = 10


def show_generation(generation, name, scene=None):
    if scene:
        scene.delete()
    scene = vp.canvas(background=vp.color.gray(luminance=0.7), width=1000, height=1000)
    print(f"Showing generation: {name}")
    draw_generation(generation)
    return scene


def choice_maker():
    while True:
        sleep(1)
        print("\tPress 1. to see Parents\n\tPress 2. to go to next generation")
        try:
            choice = int(sys.stdin.read(2).strip())
            if choice == 1 or choice == 2:
                print(f"\t\tPicked: {choice}\n")
                return choice
        except:
            print("There is no such option, Try again!\n")


def next_step():
    print("\tPress ENTER to continue to next Generation")
    sys.stdin.read(1).strip()


def main():
    generation = generate_first_generation(GEN_MEMBERS_COUNT)
    scene = show_generation(generation, "Generation 0")

    for i in range(HOW_MANNY_GENERATION):

        parent_table = choose_parents(generation)

        choice = choice_maker()

        if choice == 1:
            scene = show_generation(parent_table, f"Generation: {i} parents", scene)
            next_step()
        generation = create_next_generation(parent_table)
        scene = show_generation(generation, f"Generation: {i + 1}", scene)
        if i == HOW_MANNY_GENERATION - 1:
            break
        next_step()

    print("Koniec generacji")


if __name__ == '__main__':
    main()
