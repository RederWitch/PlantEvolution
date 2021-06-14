import random
from Genotyp import root_genes, stalk_genes, leaves_genes, stalk_creations_genes, leaves_color_genes


def generate_first_generation(GEN_MEMBERS_COUNT: int = 10) -> list:
    GENERATION = []

    random.seed(a=None)

    for i in range(GEN_MEMBERS_COUNT):
        DNA = []
        # root 0
        y = random.randint(0, 1)
        DNA.append(root_genes[y])
        # stalk 1
        x = random.randint(0, 1)
        DNA.append(stalk_genes[x])
        # leaves 2
        x = random.randint(0, 3)
        DNA.append(leaves_genes[x])
        # stalk creation 3
        x = random.randint(0, 3)
        DNA.append(stalk_creations_genes[x])
        # leaves color 4
        x = random.randint(0, 3)
        DNA.append(leaves_color_genes[x])
        # root length 5
        leng = random.randint(1, 20)
        DNA.append(leng)
        # stalk height 6
        DNA.append(random.randint(2, 50))

        GENERATION.append(DNA)
    return GENERATION
