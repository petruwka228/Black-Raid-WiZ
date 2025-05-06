from dir import *
import random
q = [11, 16, 21]
b = -1
f = open('Events_Story.ini', 'a', encoding='utf-8-sig')
for i in q:
    b+=1
    a = random.choice(zones_airdrop)
    d = random.randint(0, len(goods_airdrop_icon)-1)
    f.write(f'[Event-airdrop-info-{b}-0]\n')  # ---
    f.write(f'Step={i}\n')
    f.write(f'Zona={a}\n')  # -----
    f.write('Type=Info\n')
    f.write('Img=gfx\icons\Events\\airdrop.jpg\n')  # ----
    f.write(f'TargetResourceImg=gfx\old\\NoData_100x100.png\n')  # ----
    f.write('Name=Аирдроп на подходе\n')
    f.write(f'Desc-Owner=Следующий аирдроп будет на помеченной точке на {i+4} ходу\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на помеченной точке на {i+4} ходу\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=True\n')
    f.write('AddToGameLog=True\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=\n')
    f.write('\n')
    f.write(f'[Event-airdrop-ChangeZonaOwner-{b}]\n')  # ---
    f.write(f'Step={i}\n')
    f.write(f'Zona={a}\n')  # -----
    f.write('Type=ChangeZonaOwner\n')
    f.write('Img=gfx\icons\Events\\airdrop.jpg\n')  # ----
    f.write(f'TargetResourceImg=gfx\old\\NoData_100x100.png\n')  # ----
    f.write('Name=Аирдроп на подходе\n')
    f.write(f'Desc-Owner=Следующий аирдроп будет на помеченной точке на {i+4} ходу\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на помеченной точке на {i+4} ходу\n')
    f.write('ShowForOwner=False\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky\n')
    f.write('NewOwner=Airdrop\n')
    f.write('\n')
    f.write(f'[Event-airdrop-info-{b}-1]\n')  # ---
    f.write(f'Step={i+4}\n')
    f.write(f'Zona={a}\n')  # -----
    f.write('Type=Info\n')
    f.write('Img=gfx\icons\Events\\airdrop.jpg\n')  # ----
    f.write(f'TargetResourceImg=gfx\old\\NoData_100x100.png\n')  # ----
    f.write('Name=Аирдроп на подходе\n')
    f.write(f'Desc-Owner=Аирдроп приземлился. Поторопитесь, чтобы его забрать\n')  # -----
    f.write(f'Desc-NonOwner=Аирдроп приземлился. Поторопитесь, чтобы его забрать\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=True\n')
    f.write('AddToGameLog=True\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=\n')
    f.write('\n')
    for j in range(i+4, 31):
        f.write(f'[Event-airdrop-AddResources-{b}-{j}]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={a}\n')  # -----
        f.write('Type=AddResources\n')
        f.write('Img=gfx\icons\events\\5.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\{goods_airdrop_icon[d]}.png\n')  # ----
        f.write('Name=Найден предмет\n')
        f.write(f'Desc-Owner=Ваш боец получил из аирдропа предмет: {goods_airdrop_name[d]}\n')  # -----
        f.write('Desc-NonOwner=Кто-то забрал лут из аирдропа\n')
        f.write('ShowForOwner=True\n')
        f.write('ShowForNonOwner=True\n')
        f.write('AddToGameLog=False\n')
        f.write(f'NameResources={goods_airdrop_ID[d]}\n')  # ----
        f.write('CountResources=1\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write('NotWorkFractions=Mutants,Shopot,Airdrop\n')
        f.write(f'EventFlag=Flag-airdrop-{b}\n')  # ----
        f.write(f'EventFlagResult=Flag-airdrop-{b}\n')  # ----
        f.write('EventFlagStatusNeed=False\n')
        f.write('EventFlagStatusSet=True\n')
        f.write('\n')
f.close()