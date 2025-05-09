import random
from dir import *
f = open('settings.ini', 'w', encoding='utf-8-sig')
s = groups[:]
random.shuffle(s)
q = [33, 47, 49, 55, 73, 82]
a = random.choice(q)
f.write(f'''[Main]
;; Описание
ScenarioName=Чёрный рейд
ScenarioDescription=Здесь вы управляете только 3 бойцами и главная задача эвакуироваться с острова. Мод исключительно для мультиплеера и рассчитан на минимум 4 игрока.
ScenarioLogo-Standart=gfx\Logo.png
ScenarioLogo-Active=gfx\Logo-Active.png
Map=map

;; Настройки
Achievements=False
AchievementsCount=0
EventsRandomDefault=False
EventsRandomCanChange=False
EventsStoryDefault=True
EventsStoryCanChange=False
BurstDefault=False
BurstCanChange=False
MoveAndAtackArmyThroughAllyDefault=1
MoveAndAtackArmyThroughAllyCanChange=1
EndRoundChangeResources=True
ActiveMutantsEveryRound=True
BrainPsy=True
BrainMixer=True
BrainPsy-PlayerCanChangeStatus=False
BrainMixer-PlayerCanChangeStatus=False
BrainPsyBasedZona=0
BrainPsyAffectedZones={','.join([str(i) for i in range(1, 120)])}
BrainMixerBasedZona=0
BrainMixerAffectedZones={a}

BurstNumEvent=Burst
NoFoodNumEvent=NoFood
BrainPsyWorkNumEvent=BrainPsy
BrainMixerWorkNumEvent=BrainMixer
BrainPsyAlarmNumEvent=BrainPsyStatus
BrainMixerAlarmNumEvent=BrainMixerStatus
MoveMoneyNumEvent=MoneySend
IdeologyLeaveUnitsNumEvent=IdeologyUnitsLeave
AutoSearchMaxArtsNumEvent=MaxAutoSearchArts
AutoSearchPartArtsNumEvent=PartAutoSearchArts

;; Настройки базового баланса
ActiveMutantAddEveryPercent=1
ActiveMutantScaleForMutantUnit1=1
ActiveMutantScaleForMutantUnit2=25
ActiveMutantScaleForMutantUnit3=50
ActiveMutantScaleForMutantUnit4=75
BasedChanceForSearchArts=1000
BasedChanceOfDethForSearchArts=0
ExcludedUpgrades=Upgrade-8, Upgrade-9, Upgrade-10, Upgrade-11, Upgrade-12, Upgrade-13, Upgrade-14, Upgrade-15, Upgrade-16, Upgrade-17, Upgrade-18, Upgrade-19, Upgrade-20, Upgrade-21, Upgrade-22, Upgrade-23, Upgrade-24
ExcludedBuildings=building1, building2, building3, building4, building5, building6, building7, building8, building9, building10, building11, building12
BasedCostArmyMove=10
BasedCostAtackType1=10
BasedCostAtackType2=10
BasedCostKillMutants=0
UnitCostModificator=0
SpyCostCRModificator=1
SpyBasedChanceCountForReconnaissance=1
SpyBasedCostMoneyForReconnaissance=10000
BasedCashBooty=30
BasedCostNewAdvisor=10
BasedCostNewRule=150
DiplomacyActionCost=5
MaxAutoArtsNameRule=6
PartAutoArtsNameRule=7
BrainControlChangeBasedCost=25
BasedCostDestroyBuildComands=1
BasedCostForUpgradeAmmo-Money=0
BasedCostForUpgardeAmmo-Comands=0
BasedImprovementProductivityWorkshop=1
BasedCostForLeaveZone=0
OwnerFractionOfAbandonedZone=Mutants
BasedCostChangeMainZone=100
BasedPercentLostResources=0
NoBaseNeeded=Mutants,Stalkers,Bandits,Soldiers,Duty,Freedom,Monolith,Mercenaries,Scientists,Shopot,Zombie,Clearsky,Camp,base,boss

;; Условия победы и поражения
End-Standart-Victory=False
End-Standart-Lose=True
End-Step-Victory=False
End-Step-Lose=True
End-EventFlag-Victory=True
End-EventFlag-Lose=True
End-EventFlag-Victory-Number=EndVictory
End-EventFlag-Lose-Number=EndLose
EndStep=35

;; Настройки звукового сопровождения
AmbientSoundTimer=30000
MusicCheckTimer=2000
GroupsForPlayer={','.join(s)}

[Music]
;;;;;;;;;;;;
;; Музыка ;;
;;;;;;;;;;;;
music\Black-Raid.mp3

[AmbientSounds]
;;;;;;;;;;;;;;;;;;;
;; Фоновые звуки ;;
;;;;;;;;;;;;;;;;;;;
sfx\\ambient\Fon1.mp3
sfx\\ambient\Fon2.mp3
sfx\\ambient\Fon3.mp3
sfx\\ambient\Fon4.mp3
sfx\\ambient\Fon5.mp3
sfx\\ambient\Fon6.mp3
sfx\\ambient\Fon7.mp3
sfx\\ambient\Fon8.mp3
sfx\\ambient\Fon9.mp3
sfx\\ambient\Fon10.mp3
sfx\\ambient\Fon11.mp3
sfx\\ambient\Fon12.mp3
sfx\\ambient\Fon13.mp3
sfx\\ambient\Fon14.mp3
sfx\\ambient\Fon15.mp3
sfx\\ambient\Fon16.mp3
sfx\\ambient\Fon17.mp3
sfx\\ambient\Fon18.mp3
sfx\\ambient\Fon19.mp3
sfx\\ambient\Fon20.mp3
sfx\\ambient\Fon21.mp3
sfx\\ambient\Fon22.mp3
sfx\\ambient\Fon23.mp3
sfx\\ambient\Fon24.mp3
sfx\\ambient\Fon25.mp3
sfx\\ambient\Fon26.mp3
sfx\\ambient\Fon27.mp3
sfx\\ambient\Fon28.mp3
sfx\\ambient\Fon29.mp3
sfx\\ambient\Fon30.mp3
sfx\\ambient\Fon31.mp3
sfx\\ambient\Fon32.mp3
sfx\\ambient\Fon33.mp3
sfx\\ambient\Fon34.mp3
sfx\\ambient\Fon35.mp3
sfx\\ambient\Fon36.mp3
sfx\\ambient\Fon37.mp3
sfx\\ambient\Fon38.mp3
sfx\\ambient\Fon39.mp3
sfx\\ambient\Fon40.mp3
sfx\\ambient\Fon41.mp3
sfx\\ambient\Fon42.mp3
sfx\\ambient\Fon43.mp3
sfx\\ambient\Fon44.mp3
sfx\\ambient\Fon45.mp3
sfx\\ambient\Fon46.mp3
sfx\\ambient\Fon47.mp3
sfx\\ambient\Fon48.mp3
sfx\\ambient\Fon49.mp3
sfx\\ambient\Fon50.mp3
sfx\\ambient\Fon51.mp3
sfx\\ambient\Fon52.mp3
sfx\\ambient\Fon53.mp3
sfx\\ambient\Fon54.mp3
sfx\\ambient\Fon55.mp3


''')
f.close()
