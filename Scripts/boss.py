from dir import *
import random
a = boss
random.shuffle(a)
f = open('Events_Story.ini', 'a', encoding='utf-8-sig')

for i in range(2):
    f.write(f'[Event-boss-Invasion-{a[i]}-1-0]\n')  # ---
    f.write(f'Step=20\n')
    f.write(f'Zona={a[i]}\n')  # -----
    f.write('Type=Invasion\n')
    f.write('Img=gfx\icons\events\9.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
    f.write('Name=Найден предмет\n')
    f.write(f'Desc-Owner=Ваш боец нашел предмет:\n')  # -----
    f.write('Desc-NonOwner=\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky,'
            'airdrop\n')
    f.write(f'EventFlag=Flag-boss-{a[i]}-20\n')  # ----
    f.write(f'EventFlagResult=Flag-boss-{a[i]}-20\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('InvasionOwner=boss\n')
    f.write('InvasionUnit1 = 5\n')
    f.write('InvasionUnit2 = 5\n')
    f.write('InvasionUnit3 = 5\n')
    f.write('InvasionUnit4 = 1\n')
    f.write('\n')
    for j in range(21, 31):
        b = random.randint(0, len(goods_master)-1)
        f.write(f'[Event-boss-AddResources-{a[i]}-{j}]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a[i]}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\{goods_master_icon[b]}.png\n')  # ----
        f.write('Name=Лагерь зачищен\n')
        f.write(f'Desc-Owner=Вы зачистили базу зомбированных и получили предмет: {goods_master_name[b]}\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write(f'NameResources={goods_master[b]}\n')  # ----
        f.write('CountResources=1\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Mutants,Airdrop,Shopot,Zombie\n')
        f.write(f'EventFlag=Flag-boss-{a[i]}-{j-1}\n')  # ----
        f.write(f'EventFlagResult=Flag-boss-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=True\n')
        f.write('EventFlagStatusSet=False\n')
        f.write('\n')
    for j in range(25, 31):
        f.write(f'[Event-boss-Invasion-{a[i]}-{j}]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a[i]}\n')  # -----
        f.write('Type=Invasion\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Ваш боец нашел предмет:\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write(
            'NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky,'
            'airdrop\n')
        f.write(f'EventFlag=Flag-boss-{a[i]}-{j-5}\n')  # ----
        f.write(f'EventFlagResult=Flag-boss-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('InvasionOwner=boss\n')
        f.write('InvasionUnit1 = 5\n')
        f.write('InvasionUnit2 = 5\n')
        f.write('InvasionUnit3 = 5\n')
        f.write('InvasionUnit4 = 1\n')
        f.write('\n')
        for k in range(j, 19, -1):
            f.write(f'[Event-boss-EventFlag-{a[i]}-{j}-{k}]\n')  # ---
            f.write(f'Step={j}\n')
            f.write(f'Zona={a[i]}\n')  # -----
            f.write('Type=Info\n')
            f.write('Img=gfx\icons\events\9.png\n')  # ----
            f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
            f.write('Name=Найден предмет\n')
            f.write(f'Desc-Owner=Вы зачистили лагерь зомбированных и получили пред\n')  # -----
            f.write('Desc-NonOwner=\n')
            f.write('ShowForOwner=False\n')
            f.write('ShowForNonOwner=False\n')
            f.write('AddToGameLog=False\n')
            f.write(f'NameResources=\n')  # ----
            f.write('CountResources=1\n')
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
            f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,'
                    'Clearsky\n')
            f.write(f'EventFlag=Flag-boss-{a[i]}-{k}\n')  # ----
            f.write(f'EventFlagResult=Flag-boss-{a[i]}-{k - 1}\n')  # ----
            f.write('EventFlagStatusNeed=True\n')
            f.write('EventFlagStatusSet=True\n')
            f.write('\n')
    for j in range(21, 31):
        f.write(f'[Event-boss-Info-{a[i]}-{j}-1]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a[i]}\n')  # -----
        f.write('Type=Info\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили лагерь зомбированных и получили пред\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=False\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write(f'NameResources=\n')  # ----
        f.write('CountResources=1\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,'
                'Clearsky\n')
        f.write(f'EventFlag=Flag-boss-{a[i]}-{j - 1}\n')  # ----
        f.write(f'EventFlagResult=Flag-boss-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=True\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
    for j in range(21, 31):
        f.write(f'[Event-boss-Info-{a[i]}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a[i]}\n')  # -----
        f.write('Type=Info\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\money.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Вы зачистили лагерь зомбированных и получили пред\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=False\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write(f'NameResources=\n')  # ----
        f.write('CountResources=1\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=boss\n')
        f.write(f'EventFlag=Flag-boss-{a[i]}-{j - 1}\n')  # ----
        f.write(f'EventFlagResult=Flag-boss-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=False\n')
        f.write('\n')
f.close()