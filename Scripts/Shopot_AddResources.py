from dir import *

f = open('Events_Story.ini', 'a', encoding='utf-8-sig')
for i in zones:
    f.write(f'[Event-Shopot-AddResources-{i}-0-0]\n')  # ---
    f.write(f'Step=10\n')
    f.write(f'Zona={i}\n')  # -----
    f.write('Type=AddResources\n')
    f.write('Img=gfx\icons\story_SHOC\MonolithUnits.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\SGI.png\n')  # ----
    f.write('Name=Новое снаряжение\n')
    f.write(f'Desc-Owner=Вы получили новое снаряжение\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на локации:на {i + 4} ходу\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write(f'NameResources=M4A1\n')  # ----
    f.write('CountResources=3\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Mutants,'
            'Clearsky\n')
    f.write(f'EventFlag=Flag-airdrop-{i}-0\n')  # ----
    f.write(f'EventFlagResult=Flag-Shopot-{i}-0-0\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('\n')
    f.write(f'[Event-Shopot-AddResources-{i}-1-0]\n')  # ---
    f.write(f'Step=10\n')
    f.write(f'Zona={i}\n')  # -----
    f.write('Type=AddResources\n')
    f.write('Img=gfx\icons\story_SHOC\MonolithUnits.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\Monolith-3A.png\n')  # ----
    f.write('Name=Новое снаряжение\n')
    f.write(f'Desc-Owner=Вы получили новое снаряжение\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на локации:на {i + 4} ходу\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write(f'NameResources=S-altyn\n')  # ----
    f.write('CountResources=3\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Mutants,'
            ' Clearsky\n')
    f.write(f'EventFlag=Flag-airdrop-{i}-0\n')  # ----
    f.write(f'EventFlagResult=Flag-Shopot-{i}-1-0\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('\n')
for i in zones:
    f.write(f'[Event-Shopot-AddResources-{i}-0-1]\n')  # ---
    f.write(f'Step=20\n')
    f.write(f'Zona={i}\n')  # -----
    f.write('Type=AddResources\n')
    f.write('Img=gfx\icons\story_SHOC\MonolithUnits.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\Gauss.png\n')  # ----
    f.write('Name=Новое снаряжение\n')
    f.write(f'Desc-Owner=Вы получили новое снаряжение\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на локации:на {i + 4} ходу\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write(f'NameResources=OC-14M\n')  # ----
    f.write('CountResources=3\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Mutants, '
            'Clearsky\n')
    f.write(f'EventFlag=Flag-airdrop-{i}-0\n')  # ----
    f.write(f'EventFlagResult=Flag-Shopot-{i}-0-1\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('\n')
    f.write(f'[Event-Shopot-AddResources-{i}-1-1]\n')  # ---
    f.write(f'Step=20\n')
    f.write(f'Zona={i}\n')  # -----
    f.write('Type=AddResources\n')
    f.write('Img=gfx\icons\story_SHOC\MonolithUnits.png\n')  # ----
    f.write(f'TargetResourceImg=gfx\icons\goods\Stalkers-4.png\n')  # ----
    f.write('Name=Аирдроп на подходе\n')
    f.write(f'Desc-Owner=Новое снаряжение\n')  # -----
    f.write(f'Desc-NonOwner=Следующий аирдроп будет на локации:на {i + 4} ходу\n')
    f.write('ShowForOwner=True\n')
    f.write('ShowForNonOwner=False\n')
    f.write('AddToGameLog=False\n')
    f.write(f'NameResources=M-ace\n')  # ----
    f.write('CountResources=3\n')
    f.write('SoundFXForOwner=True\n')
    f.write('SoundFXForOwnerFile=sfx\events\message.mp3\n')
    f.write('SoundFXForNonOwner=True\n')
    f.write('SoundFXForNonOwnerFile=sfx\events\message.mp3\n')
    f.write('NotWorkFractions=Stalkers,Bandits,Soldiers,Duty,Freedom,Mercenaries,Monolith,Scientists,Mutants, '
            'Clearsky\n')
    f.write(f'EventFlag=Flag-airdrop-{i}-0\n')  # ----
    f.write(f'EventFlagResult=Flag-Shopot-{i}-1-1\n')  # ----
    f.write('EventFlagStatusNeed=False\n')
    f.write('EventFlagStatusSet=True\n')
    f.write('\n')
f.close()