from dir import *
import random

f = open('Events_Story.ini', 'a', encoding='utf-8-sig')

for i in range(8):
    a = random.choice(camp)
    b = random.randint(0, len(goods_skilled)-1)
    c = random.randint(1, 5)
    f.write(f'[Event-Camp-Invasion-{i}-0]\n')  # ---
    f.write(f'Step={i}\n')
    f.write(f'Zona={a}\n')  # -----
    f.write('Type=Invasion\n')
    f.write('Img=gfx\icons\events\9.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
    f.write('Name=Найден предмет\n')
    f.write(f'Desc-Owner=Ваш боец нашел предмет:\n')  # -----
    f.write('Desc-NonOwner=\n')
    f.write('ShowForOwner=False\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky\n')
    f.write('InvasionOwner=Zombie\n')
    f.write('InvasionUnit1 = 5\n')
    f.write('InvasionUnit2 = 5\n')
    f.write('InvasionUnit3 = 0\n')
    f.write('InvasionUnit4 = 0\n')
    f.write('\n')
    for j in range(2, 40):
        f.write(f'[Event-Camp-AddResources-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\{goods_skilled_icon[b]}.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили территорию и получили предметы:\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write(f'NameResources={goods_skilled[b]}\n')  # ----
        f.write('CountResources=1\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Zombie, Mutants, Shopot\n')
        f.write(f'EventFlag=Flag-Camp-AddResources-{i}-0\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-AddResources-{i}-{j}-0\n')  # -----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
        f.write(f'[Event-Camp-AddResources-{i}-{j}-1]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\medic.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили территорию и получили предметы:\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write(f'NameResources=medic\n')  # ----
        f.write(f'CountResources={c}\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Zombie, Mutants, Shopot\n')
        f.write(f'EventFlag=Flag-Camp-AddResources-{i}-1\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-AddResources-{i}-{j}-1\n')  # -----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
        f.write(f'[Event-Camp-AddResources-{i}-{j}-2]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили территорию и получили предметы:\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write(f'NameResources=money\n')  # ----
        f.write(f'CountResources=1000\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Zombie, Mutants, Shopot\n')
        f.write(f'EventFlag=Flag-Camp-AddResources-{i}-2\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-AddResources-{i}-{j}-2\n')  # -----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
        f.write(f'[Event-Camp-info-{i}-{j}]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a}\n')  # -----
        f.write('Type=Info\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили территорию и получили предметы:\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=False\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Zombie, Mutants, Shopot\n')
        f.write(f'EventFlag=Flag-Camp-AddResources-{i}\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-Info-{i}-{j}\n')  # -----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
        for k in range(j+5, 40):
            f.write(f'[Event-Camp-Invasion-{i}-0]\n')  # ---
            f.write(f'Step={k}\n')
            f.write(f'Zona={a}\n')  # -----
            f.write('Type=Invasion\n')
            f.write('Img=gfx\icons\events\9.png\n')  # ----
            f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
            f.write('Name=Найден предмет\n')
            f.write(f'Desc-Owner=Ваш боец нашел предмет:\n')  # -----
            f.write('Desc-NonOwner=\n')
            f.write('ShowForOwner=False\n')
            f.write('ShowForNonOwner=False\n')
            f.write('AddToGameLog=False\n')
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
            f.write(
                'NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky\n')
            f.write('InvasionOwner=Zombie\n')
            f.write('InvasionUnit1 = 5\n')
            f.write('InvasionUnit2 = 5\n')
            f.write('InvasionUnit3 = 0\n')
            f.write('InvasionUnit4 = 0\n')
            f.write(f'EventFlag=Flag-Camp-AddResources-{i}-{k-5}\n')  # ----
            f.write(f'EventFlagResult=Flag-Camp-Info-{i}-{k-5}\n')  # -----
            f.write('EventFlagStatusNeed=True\n')
            f.write('EventFlagStatusSet=False\n')
            f.write('\n')

f.close()