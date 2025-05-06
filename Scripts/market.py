from dir import *
f = open('Events_Story.ini', 'a', encoding='utf-8-sig')

for i in range(1, 35):
    for j in zones_traders:
        f.write(f'[Event-airdrop-ChangeZonaOwner-{j}-{i}]\n')  # ---
        f.write(f'Step={i}\n')
        f.write(f'Zona={j}\n')
        f.write('Type=ChangeZonaOwner\n')
        f.write('Img=gfx\icons\Events\\airdrop.jpg\n')  # ----
        f.write(f'TargetResourceImg=gfx\old\\NoData_100x100.png\n')  # ----
        f.write('Name=Аирдроп на подходе\n')
        f.write(f'Desc-Owner=Следующий аирдроп будет на помеченной точке на {i + 4} ходу\n')  # -----
        f.write(f'Desc-NonOwner=Следующий аирдроп будет на помеченной точке на {i + 4} ходу\n')
        f.write('ShowForOwner=False\n')
        f.write('ShowForNonOwner=False\n')
        f.write('AddToGameLog=False\n')
        f.write('SoundFXForOwner=True\n')
        f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
        f.write('SoundFXForNonOwner=True\n')
        f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
        f.write(
            'NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Shopot,Clearsky,'
            'shop\n')
        f.write('NewOwner=shop\n')
        f.write('\n')

f.close()