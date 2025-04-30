from dir import *
import random
random.shuffle(camp)
a = camp[:8]
f = open('Events_Story.ini', 'a', encoding='utf-8-sig')

for i in range(8):
    f.write(f'[Event-Camp-Invasion-{a[i]}-1-0]\n')  # ---
    f.write(f'Step=1\n')
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
    f.write(f'EventFlag=Flag-Camp-{a[i]}-1\n')  # ----
    f.write(f'EventFlagResult=Flag-Camp-{a[i]}-1\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('InvasionOwner=Camp\n')
    f.write('InvasionUnit1 = 1\n')
    f.write('InvasionUnit2 = 1\n')
    f.write('InvasionUnit3 = 0\n')
    f.write('InvasionUnit4 = 0\n')
    f.write('\n')
    for j in range(2, 31):
        b = random.randint(0, len(goods_skilled)-1)
        f.write(f'[Event-Camp-AddResources-{a[i]}-{j}]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a[i]}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\{goods_skilled_icon[b]}.png\n')  # ----
        f.write('Name=Лагерь зачищен\n')
        f.write(f'Desc-Owner=Вы зачистили лагерь зомбированных и получили предмет: {goods_skilled_name[b]}\n')  # -----
        f.write('Desc-NonOwner=\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write(f'NameResources={goods_skilled[b]}\n')  # ----
        f.write('CountResources=1\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Mutants,Airdrop,Shopot,Zombie\n')
        f.write(f'EventFlag=Flag-Camp-{a[i]}-{j-1}\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=True\n')
        f.write('EventFlagStatusSet=False\n')
        f.write('\n')
    for j in range(6, 31):
        f.write(f'[Event-Camp-Invasion-{a[i]}-{j}]\n')  # ---
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
        f.write(f'EventFlag=Flag-Camp-{a[i]}-{j-5}\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('InvasionOwner=Camp\n')
        f.write('InvasionUnit1 = 1\n')
        f.write('InvasionUnit2 = 1\n')
        f.write('InvasionUnit3 = 0\n')
        f.write('InvasionUnit4 = 0\n')
        f.write('\n')
        for k in range(j, 0, -1):
            f.write(f'[Event-Camp-EventFlag-{a[i]}-{j}-{k}]\n')  # ---
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
            f.write(f'EventFlag=Flag-Camp-{a[i]}-{k}\n')  # ----
            f.write(f'EventFlagResult=Flag-Camp-{a[i]}-{k - 1}\n')  # ----
            f.write('EventFlagStatusNeed=True\n')
            f.write('EventFlagStatusSet=True\n')
            f.write('\n')
    for j in range(2, 31):
        f.write(f'[Event-Camp-Info-{a[i]}-{j}-1]\n')  # ---
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
        f.write(f'EventFlag=Flag-Camp-{a[i]}-{j - 1}\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=True\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
    for j in range(2, 31):
        f.write(f'[Event-Camp-Info-{a[i]}-{j}-0]\n')  # ---
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
        f.write('NotWorkFractions=Camp\n')
        f.write(f'EventFlag=Flag-Camp-{a[i]}-{j - 1}\n')  # ----
        f.write(f'EventFlagResult=Flag-Camp-{a[i]}-{j}\n')  # ----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=False\n')
        f.write('\n')
f.close()