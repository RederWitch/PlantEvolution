from typing import List


# Funkcja sumowuje wagi wodym fotosyntezy i co2 allelli
# i mnoży razy 10 ?
# następnie jeżeli sprawdza stosunek korzenia do łodygi
# jeżeli łodyga jest 3 krotnie większa niż korzeń palowy lub 2 krotnie korzeń wiazkowy
# nakłada dodatkowe kary w ocenie -> roślina mogła by się przewrócić

def check_length_danger(Plant_DNA: List) -> int:
    penalties = 0
    if Plant_DNA[0].get_id() == "0":
        threshold = 3
    else:
        threshold = 2
    if Plant_DNA[6] / Plant_DNA[5] > threshold: penalties += 1
    if Plant_DNA[5] / Plant_DNA[6] > 1.5: penalties += 1
    return penalties


def mark_genotyp(Plant_DNA: List):
    water = 0
    foto = 0
    co2 = 0
    penalty = 30

    for gen in range(len(Plant_DNA) - 2):
        water += Plant_DNA[gen].get_water()
        foto += Plant_DNA[gen].get_foto()
        co2 += Plant_DNA[gen].get_co2()

    mark = (water + foto + co2) * 10 - check_length_danger(Plant_DNA) * penalty
    if mark < 0: mark = 0
    return int(mark)
