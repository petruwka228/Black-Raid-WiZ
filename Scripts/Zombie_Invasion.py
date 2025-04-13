f = open('Events_Story.ini', 'a', encoding='utf-8-sig')
for i in range(1, 120):
    for j in range(1, 10):
        f.write(f'[Event-Zombie-Invasion-{i}-{j}-0]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
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
        f.write('NotWorkFractions=Mutants,airdrop,camp\n')
        f.write('InvasionOwner=Mutants\n')
        f.write('InvasionUnit1 = 1\n')
        f.write('InvasionUnit2 = 0\n')
        f.write('InvasionUnit3 = 0\n')
        f.write('InvasionUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(10, 19):
        f.write(f'[Event-Zombie-Invasion-{i}-{j}-1]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
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
        f.write('NotWorkFractions=Mutants,airdrop,camp\n')
        f.write('InvasionOwner=Mutants\n')
        f.write('InvasionUnit1 = 0\n')
        f.write('InvasionUnit2 = 1\n')
        f.write('InvasionUnit3 = 0\n')
        f.write('InvasionUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(19, 28):
        f.write(f'[Event-Zombie-Invasion-{i}-{j}-2]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
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
        f.write('NotWorkFractions=Mutants,airdrop,camp\n')
        f.write('InvasionOwner=Mutants\n')
        f.write('InvasionUnit1 = 0\n')
        f.write('InvasionUnit2 = 0\n')
        f.write('InvasionUnit3 = 1\n')
        f.write('InvasionUnit4 = 0\n')
        f.write('\n')

for i in range(1, 120):
    for j in range(28, 36):
        f.write(f'[Event-Zombie-Invasion-{i}-{j}-3]\n')  # ---
        f.write(f'Step={j}\n')
        f.write(f'Zona={i}\n')  # -----
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
        f.write('NotWorkFractions=Mutants,airdrop,camp\n')
        f.write('InvasionOwner=Mutants\n')
        f.write('InvasionUnit1 = 0\n')
        f.write('InvasionUnit2 = 0\n')
        f.write('InvasionUnit3 = 0\n')
        f.write('InvasionUnit4 = 1\n')
        f.write('\n')
f.close()