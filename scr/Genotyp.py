# Krotki zaweirające allele danych genów
from Allel import Allel

r0 = Allel('0', "Palowy", "root", water=1)
r1 = Allel('1', "Wiązkowy", "root", water=2)
root_genes = (r0, r1)

s0 = Allel('0', "zielona", "stalk", foto=1, co2=1)
s1 = Allel('1', "magazynująca", "stalk", water=1, foto=1)
stalk_genes = (s0, s1)

l0 = Allel('00', "małe liście", "leaves", foto=1, co2=1)
l1 = Allel('01', "duże liście", "leaves", foto=2, co2=2, water=-1)
l2 = Allel('10', "mięsiste", "leaves", water=1, foto=-1, co2=1)
l3 = Allel('11', "kolce", "leaves", water=1)
leaves_genes = (l0, l1, l2, l3)

sc0 = Allel('00', "skórka", "stalk creations", co2=-1, water=1)
sc1 = Allel('01', "wosk", "stalk creations", water=2, foto=-1)
sc2 = Allel('10', "kora", "stalk creations", water=1, foto=-1, co2=-1)
sc3 = Allel('11', "brak", "stalk creations")
stalk_creations_genes = (sc0, sc1, sc2, sc3)

lc0 = Allel('00', "zieleń", "leaves color", foto=1)
lc1 = Allel('01', "pomarańcz", "leaves color")
lc2 = Allel('10', "czerwień", "leaves color", foto=-1, co2=1)
lc3 = Allel('11', "fiolet", "leaves color", foto=-1)
leaves_color_genes = (lc0, lc1, lc2, lc3)
