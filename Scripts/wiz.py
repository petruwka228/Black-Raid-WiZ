import random
from dir import *
f = open('Events_Story.ini', 'a', encoding='utf-8-sig')
for j in zones: # менять значения сначала zones_a, потом zones_b, из-за того что консоль PyCharm не вмещает все территории
    fl = random.randint(1,2)
    if fl == 1:
        c = random.randint(0, len(goods_armor_name)-1)
        d = random.randint(1, 5)
        for i in range(1, 30):
            f.write(f'[Event-AddResources-{j}-{i}-0]\n')  # ---
            f.write(f'Step={i}\n')
            f.write(f'Zona={j}\n')  # -----
            f.write('Type=AddResources\n')
            f.write('Img=gfx\icons\events\9.png\n')  # ----
            f.write(f'TargetResourceImg=gfx\icons\goods\{goods_armor_icon[c]}.png\n')  # ----
            f.write('Name=Найден предмет\n')
            f.write(f'Desc-Owner=Ваш боец нашел предмет: {goods_armor_name[c]}\n')  # -----
            f.write('Desc-NonOwner=\n')
            f.write('ShowForOwner=True\n')
            f.write('ShowForNonOwner=False\n')
            f.write('AddToGameLog=False\n')
            f.write(f'NameResources={goods_armor_ID[c]}\n')  # ----
            f.write('CountResources=1\n')
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
            f.write('NotWorkFractions=Mutants,Airdrop,Shopot,Zombie\n')
            f.write(f'EventFlag=Flag-{j}-0\n')  # ----
            f.write(f'EventFlagResult=Flag-{j}-0\n')  # ----
            f.write('EventFlagStatusNeed=False\n')
            f.write('EventFlagStatusSet=True\n')
            f.write('\n')
            f.write(f'[Event-AddResources-{j}-{i}-1]\n')  # ----
            f.write(f'Step={i}\n')
            f.write(f'Zona={j}\n')  # -----
            f.write('Type=AddResources\n')
            f.write('Img=gfx\icons\events\\6.png\n')  # ----
            f.write('TargetResourceImg=gfx\icons\goods\Medic.png\n')  # ---
            f.write('Name=Найден предмет\n')
            f.write('Desc-Owner = Ваш боец нашел предмет: Медикаменты\n')  # -----
            f.write('Desc-NonOwner=\n')
            f.write('ShowForOwner=True\n')
            f.write('ShowForNonOwner=False\n')
            f.write('AddToGameLog=False\n')
            f.write('NameResources=Medic\n')  # -----
            f.write(f'CountResources={d}\n')  # ----
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
            f.write('NotWorkFractions=Mutants,Airdrop,Shopot,Zombie\n')
            f.write(f'EventFlag=Flag-{j}-1\n')  # ----
            f.write(f'EventFlagResult=Flag-{j}-1\n')  # -----
            f.write('EventFlagStatusNeed=False\n')
            f.write('EventFlagStatusSet=True\n')
            f.write('\n')
    else:
        c = random.randint(0, len(goods_weapon_name) - 1)
        for i in range(1, 30):
            f.write(f'[Event-AddResources-{j}-{i}-0]\n')  # ---
            f.write(f'Step={i}\n')
            f.write(f'Zona={j}\n')  # -----
            f.write('Type=AddResources\n')
            f.write('Img=gfx\icons\events\8.png\n')  # ----
            f.write(f'TargetResourceImg=gfx\icons\goods\{goods_weapon_ID[c]}.png\n')  # ----
            f.write('Name=Найден предмет\n')
            f.write(f'Desc-Owner=Ваш боец нашел предмет: {goods_weapon_name[c]}\n')  # -----
            f.write('Desc-NonOwner=\n')
            f.write('ShowForOwner=True\n')
            f.write('ShowForNonOwner=False\n')
            f.write('AddToGameLog=False\n')
            f.write(f'NameResources={goods_weapon_ID[c]}\n')  # ----
            f.write('CountResources=1\n')
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
            f.write('NotWorkFractions=Mutants,Airdrop,Shopot,Zombie\n')
            f.write(f'EventFlag=Flag-{j}-0\n')  # ----
            f.write(f'EventFlagResult=Flag-{j}-0\n')  # ----
            f.write('EventFlagStatusNeed=False\n')
            f.write('EventFlagStatusSet=True\n')
            f.write('\n')
f.close()