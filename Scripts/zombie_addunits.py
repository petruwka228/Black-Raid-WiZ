f = open('Events_Story.ini', 'a', encoding='utf-8-sig')
for i in range(1, 120):
    for j in range(1, 10):
        f.write(f'[Event-Zombie-AddUnits-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
        f.write('Type=AddUnits\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
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
        f.write('NotWorkFractions=Stalkers, Bandits, Soldiers, Duty, Freedom, Monolith, Mercenaries, Scientists,'
                ' Shopot, Clearsky\n')
        f.write('CountUnit1 = 1\n')
        f.write('CountUnit2 = 0\n')
        f.write('CountUnit3 = 0\n')
        f.write('CountUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(10, 19):
        f.write(f'[Event-Zombie-AddUnits-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
        f.write('Type=AddUnits\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
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
        f.write('NotWorkFractions=Stalkers, Bandits, Soldiers, Duty, Freedom, Monolith, Mercenaries, Scientists,'
                ' Shopot, Clearsky\n')
        f.write('CountUnit1 = 0\n')
        f.write('CountUnit2 = 1\n')
        f.write('CountUnit3 = 0\n')
        f.write('CountUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(19, 28):
        f.write(f'[Event-Zombie-AddUnits-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
        f.write('Type=AddUnits\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
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
        f.write('NotWorkFractions=Stalkers, Bandits, Soldiers, Duty, Freedom, Monolith, Mercenaries, Scientists,'
                ' Shopot, Clearsky\n')
        f.write('CountUnit1 = 0\n')
        f.write('CountUnit2 = 0\n')
        f.write('CountUnit3 = 1\n')
        f.write('CountUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(28, 36):
        f.write(f'[Event-Zombie-AddUnits-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
        f.write('Type=AddUnits\n')
        f.write('Img=gfx\icons\events\9.png\n')  # ----
        f.write(f'TargetResourceImg=gfx\icons\goods\Abakan.png\n')  # ----
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
        f.write('NotWorkFractions=Stalkers, Bandits, Soldiers, Duty, Freedom, Monolith, Mercenaries, Scientists,'
                ' Shopot, Clearsky,boss\n')
        f.write('CountUnit1 = 0\n')
        f.write('CountUnit2 = 0\n')
        f.write('CountUnit3 = 0\n')
        f.write('CountUnit4 = 1\n')
        f.write('\n')
f.close()