import sys
import copy
import numpy as np
from Game import HSRBattle
from ClassList import ClassList
import MCTS
import random
import time


Simulation_iteration = 30
MCTS_search_iteration = 300
GameTime = 650
MaximumWave = 3 # 최대 웨이브(리젠 횟수) 이후 게임 종료됨
PrintTempBuff = False
UseMultiprocessing = True
ProcessNum = 10
SimulateName = f'정예2 담정페나 에이언즈5재 {Simulation_iteration}게임 {MCTS_search_iteration}회 {GameTime}초'

if __name__ == '__main__':
    Control = input('직접 컨트롤 하시겠습니까? (y/n): ')
    if Control == 'y':
        Control = True
    elif Control == 'n':
        Control = False
    else:
        raise ValueError('y/n으로 입력해주세요')
        
    classlist = ClassList()
    # 캐릭터것
    character1 = classlist.GetCharacter('단항음월')([6,10,10,10], Eidolons=2) # 치피/속도/허피/공%, 공%8, 치확6, 치피10
    character1.AddLightCone(classlist.GetLightCone('태양보다밝게빛나는것'), SuperImpose=1)
    character1.AddRelic([['들이삭과동행하는거너', [('고정속도증가', 29.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['들이삭과동행하는거너', [('HP%증가', 0.07776), ('공격력%증가', 0.8208), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['들이삭과동행하는거너', [('효과명중', 0.07776), ('효과저항', 0.07776), ('치명타확률', 0.23328), ('치명타피해', 1.34784)]],
                        ['들이삭과동행하는거너', [('에너지회복효율', 0), ('치유량보너스', 0), ('허수속성피해증가', 0.388)]],
                        ['우주봉인정거장', []],
                        ['우주봉인정거장', []]])
    
    character2 = classlist.GetCharacter('정운')([6,10,10,10], Eidolons=6) # 공%/속도/공%/에충, 속도10, 공%10, HP% 6
    character2.AddLightCone(classlist.GetLightCone('행성과의만남'), SuperImpose=5)
    character2.AddRelic([['들이삭과동행하는거너', [('고정속도증가', 52.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['들이삭과동행하는거너', [('HP%증가', 0.31104), ('공격력%증가', 1.2528), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['들이삭과동행하는거너', [('효과명중', 0.07776), ('효과저항', 0.07776), ('치명타확률', 0.05832), ('치명타피해', 0.11664)]],
                        ['들이삭과동행하는거너', [('에너지회복효율', 0.194), ('치유량보너스', 0), ('번개속성피해증가', 0)]],
                        ['불로인의선주', []],
                        ['불로인의선주', []]])

    character3 = classlist.GetCharacter('페라')([6,10,10,10], Eidolons=6) # 효명/속도/얼피/에충 속도10 치확12 치피2
    character3.AddLightCone(classlist.GetLightCone('땀방울처럼빛나는결심'), SuperImpose=5)
    character3.AddRelic([['가상공간을누비는메신저', [('고정속도증가', 52.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['가상공간을누비는메신저', [('HP%증가', 0.07776), ('공격력%증가', 0.07776), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['장수를원하는제자', [('효과명중', 0.50976), ('효과저항', 0.07776), ('치명타확률', 0.40824), ('치명타피해', 0.23328)]],
                        ['장수를원하는제자', [('에너지회복효율', 0.194), ('치유량보너스', 0), ('얼음속성피해증가', 0.388)]],
                        ['생명의바커공', []],
                        ['생명의바커공', []]])

    character4 = classlist.GetCharacter('나찰')([6,10,10,10], Eidolons=0) # 치유/속도/공%/에충, 속도10, 공%10, 효저4
    character4.AddLightCone(classlist.GetLightCone('관의울림'), SuperImpose=1)
    character4.AddRelic([['흔적없는손님', [('고정속도증가', 52.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['흔적없는손님', [('HP%증가', 0.07776), ('공격력%증가', 0.89856), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['흔적없는손님', [('효과명중', 0.07776), ('효과저항', 0.23328), ('치명타확률', 0.05832), ('치명타피해', 0.11664)]],
                        ['흔적없는손님', [('에너지회복효율', 0.194), ('치유량보너스', 0.345), ('허수속성피해증가', 0)]],
                        ['부러진용골', []],
                        ['부러진용골', []]])
    
    Game = HSRBattle(GameTime, MaximumWave, Control, PrintTempBuff)
    Game.AddCharacter([character1, character2, character3, character4])

    # 적, ['물리', '화염', '번개', '얼음', '바람', '허수', '양자']
    Game.AddEnemy([
                (classlist.GetEnemy('허수아비정예'), '허수아비정예-1', ['물리', '화염', '번개', '얼음', '바람', '허수', '양자']),
                (classlist.GetEnemy('허수아비정예'), '허수아비정예-2', ['물리', '화염', '번개', '얼음', '바람', '허수', '양자']), 
                ])
    Game.Init()
    Game.GetPossibleAction()


    if Control == False:
        MCTS.RunSimulation(Game, Simulation_iteration, MCTS_search_iteration, UseMultiprocessing, ProcessNum, SimulateName)

    elif Control == True:
        while Game.Terminal == False:
            for idx in range(len(Game.PossibleAction)):
                print(idx, Game.PossibleAction[idx])
            action = int(input('몇번째 행동을 선택하시겠습니까? : '))
            Game.ApplyCharacterAction(Game.PossibleAction[action])
            Game.GetPossibleAction()
