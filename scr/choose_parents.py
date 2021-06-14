from mark_genotyp import mark_genotyp
import random


def choose_parents(generation: list) -> list:
    marks_sum = 0
    mark_table = []
    parent_table = []

    random.seed()

    for plant in generation:
        plant_mark = mark_genotyp(plant)
        marks_sum += plant_mark
        mark_table.append(marks_sum)

    for i in range(len(generation)):
        n = random.randint(0, marks_sum)
        for j in range(len(generation)):
            if n <= mark_table[j]:
                n = j
                break
        parent_table.append(generation[n])

    return parent_table
