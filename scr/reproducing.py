import random
from Genotyp import root_genes, stalk_genes, leaves_genes, stalk_creations_genes, leaves_color_genes


def mutate(plant: list) -> list:
    gen_to_mutate = random.randint(0, 6)
    tmp = plant[gen_to_mutate]

    if gen_to_mutate == 0:
        index = root_genes.index(plant[0])
        plant[0] = root_genes[(index + 1) % 2]

    if gen_to_mutate == 1:
        index = stalk_genes.index(plant[1])
        plant[1] = stalk_genes[(index + 1) % 2]

    if gen_to_mutate == 2:
        index = leaves_genes.index(plant[2])
        plant[2] = leaves_genes[(index + 1) % 4]

    if gen_to_mutate == 3:
        index = stalk_creations_genes.index(plant[3])
        plant[3] = stalk_creations_genes[(index + 1) % 4]

    if gen_to_mutate == 4:
        index = leaves_color_genes.index(plant[4])
        plant[4] = leaves_color_genes[(index + 1) % 4]

    if gen_to_mutate in [5, 6]:
        wsp = random.randint(5, 20) / 10
        plant[gen_to_mutate] = round(plant[gen_to_mutate] * wsp, 2)

    print(f"mutacja genu: {gen_to_mutate} z {tmp} na {plant[gen_to_mutate]}")

    return plant


def breeding(parent_1: list, parent_2: list) -> list:
    new_plant_1 = []
    new_plant_2 = []

    for i in range(3):
        new_plant_1.append(parent_1[i])
        new_plant_2.append(parent_2[i])
    for j in range(2):
        new_plant_1.append(parent_2[j + 3])
        new_plant_2.append(parent_1[j + 3])

    rot1 = random.randint(0, 9)
    # Root Length i=5
    tmp = (rot1 * parent_2[5] + (10 - rot1) * parent_1[5]) / 10
    new_plant_1.append(round(tmp, 2))
    rot2 = random.randint(0, 9)
    tmp = (rot2 * parent_1[5] + (10 - rot2) * parent_2[5]) / 10
    new_plant_2.append(round(tmp, 2))

    # Stalk height i=6
    hei1 = random.randint(0, 9)
    tmp = (hei1 * parent_1[6] + (10 - hei1) * parent_2[6]) / 10
    new_plant_1.append(round(tmp, 2))
    hei2 = random.randint(0, 9)
    tmp = (hei2 * parent_2[6] + (10 - hei2) * parent_1[6]) / 10
    new_plant_2.append(round(tmp, 2))

    tmp = [new_plant_1, new_plant_2]

    mutagen = random.randint(0, 99)
    if mutagen % 10 == 0:
        plant = tmp.pop(random.randint(0, 1))
        tmp.append(mutate(plant))

    return tmp


def create_next_generation(parent_table: list) -> list:
    next_generation = list()

    for i in range(int(len(parent_table) / 2)):
        p1 = random.randint(0, len(parent_table) - 1)
        parent1 = parent_table.pop(p1)
        p2 = random.randint(0, len(parent_table) - 1)
        parent2 = parent_table.pop(p2)
        for plant in breeding(parent1, parent2):
            next_generation.append(plant)

    return next_generation
