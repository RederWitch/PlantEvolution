from typing import List
from draw import *


def draw_fenotyp(DNA: List, i: int = 0, offset: int = 0):
    x = 15 * (i % 5) - 30 + offset
    y = int(i / 5) * 30 - 40

    ground = vp.box(pos=vp.vector(x, y, 0), length=5, height=0.1, width=5)
    draw_root(DNA[0].get_id(), DNA[5], x, y)
    draw_stalk(DNA[1].get_id(), DNA[3].get_id(), DNA[6], x, y)
    draw_leaves(DNA[2].get_id(), DNA[4].get_id(), DNA[1].get_id(), DNA[6], x, y)


def draw_generation(generation: List):
    offset = 0
    j = 0

    for i in range(len(generation)):
        draw_fenotyp(generation[i], i, offset)
        offset += 6
        if i % 10 == 9:
            offset = -offset
