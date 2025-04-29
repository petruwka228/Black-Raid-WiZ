from dir import *
import random
q = zones_traders[:]
random.shuffle(q)
f = open('Traders.ini', 'w', encoding='utf-8-sig')
for i in range(len(q)):
    f.write(f"""[Trader{i+1}]
Name= Торговец
Img=gfx\icons\\traders\\{random.choice(viv)}.png
Need= {q[i]}
Cost = 0
Chance = 100
StartStep=0
EndStep=0
NeedText=
Coef-Sell-Food=1,00
Coef-Sell-Medic=50,00
Coef-Sell-Supplies=10,00
Coef-Sell-Parts=False
Coef-Sell-Arts=False
Coef-Sell-Weapon=1,00
Coef-Sell-Armor=1,00
Coef-Sell-BuildingMaterials=1,00
Coef-Sell-AmmoComponents=1,00
Coef-Buy-Food=0,00
Coef-Buy-Medic=0,00
Coef-Buy-Supplies=0,00
Coef-Buy-Parts=0,00
Coef-Buy-Arts=1,00
Coef-Buy-Armor=0,00
Coef-Buy-Weapon=0,00
Coef-Buy-BuildingMaterials=0,00
Coef-Buy-AmmoComponents=0,00

""")
f.close()