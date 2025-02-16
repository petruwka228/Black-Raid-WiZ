from dir import *
import random
q = zones_traders[:]
random.shuffle(q)
a = q[:12]
f = open('Traders.ini', 'w', encoding='utf-8-sig')
f.write("""[Main]
World=False
YourGroup=False
OtherGroup=False
BlackMarket=False
Trader1=True
Trader2=True
Trader3=True
Trader4=True
Trader5=True
Trader6=True
Trader7=True
Trader8=True
Trader9=True
Trader10=True
Trader11=True
Trader12=True

[World]
Name= Внешний мир
Img=gfx\icons\\traders\World.gif
Chance = 50
Cost = 10
Need= 0
StartStep=0
EndStep=0
NeedText=Связь с внешним миром не всегда удается установить. Шанс 50%. Цена попытки установить связь:
Coef-Sell-Food=False
Coef-Sell-Medic=1,75
Coef-Sell-Supplies=1,75
Coef-Sell-Parts=False
Coef-Sell-Arts=False
Coef-Sell-Weapon=1,75
Coef-Sell-Armor=1,75
Coef-Sell-BuildingMaterials=2
Coef-Sell-AmmoComponents=3
Coef-Buy-Food=0,25
Coef-Buy-Medic=0,25
Coef-Buy-Supplies=0,25
Coef-Buy-Parts=1,75
Coef-Buy-Arts=1,75
Coef-Buy-Armor=0,25
Coef-Buy-Weapon=0,25
Coef-Buy-BuildingMaterials=0,25
Coef-Buy-AmmoComponents=0,25

[YourGroup]
Name= Торговец вашей группировки
Img=gfx\icons\\traders\Other.gif
Cost = 10
NeedText=Вы всегда можете поторговать со своим торговцем. Цена:
Coef-Sell-Food=1,25
Coef-Sell-Medic=1,25
Coef-Sell-Supplies=1,25
Coef-Sell-Parts=False
Coef-Sell-Arts=False
Coef-Sell-Weapon=1,25
Coef-Sell-Armor=1,25
Coef-Sell-BuildingMaterials=1
Coef-Sell-AmmoComponents=1
Coef-Buy-Food=0,50
Coef-Buy-Medic=0,50
Coef-Buy-Supplies=0,75
Coef-Buy-Parts=0,75
Coef-Buy-Arts=0,75
Coef-Buy-Armor=0,75
Coef-Buy-Weapon=0,75
Coef-Buy-BuildingMaterials=1
Coef-Buy-AmmoComponents=1

[OtherGroup]
Name= Торговец чужой группировки
Img=gfx\icons\\traders\Other.gif
Cost = 1
NeedText=Чтобы торговать с чужими группировками сначала выберите на карте чужую территорию
Coef-Sell-Food=1,50
Coef-Sell-Medic=1,50
Coef-Sell-Supplies=1,50
Coef-Sell-Parts=False
Coef-Sell-Arts=False
Coef-Sell-Weapon=1,50
Coef-Sell-Armor=1,50
Coef-Sell-BuildingMaterials=1,25
Coef-Sell-AmmoComponents=1,50
Coef-Buy-Food=0,50
Coef-Buy-Medic=0,50
Coef-Buy-Supplies=0,50
Coef-Buy-Parts=0,50
Coef-Buy-Arts=0,50
Coef-Buy-Armor=0,50
Coef-Buy-Weapon=0,50
Coef-Buy-BuildingMaterials=0,75
Coef-Buy-AmmoComponents=0,75

[BlackMarket]
Name= Черный рынок
Img=gfx\icons\\traders\BlackMarket.png
Need= Multiplayer
NeedText=Только мультиплеер
StartStep=0
EndStep=0
Coef=

""")
for i in range(12):
    f.write(f"""[Trader{i+1}]
Name= Торговец
Img=gfx\icons\\traders\\{random.choice(viv)}.png
Need= {a[i]}
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