import sys
import copy
import numpy as np
from Game import HSRBattle
from ClassList import ClassList
import MCTS
import random
import time


Simulation_iteration = 50
MCTS_search_iteration = 300
GameTime = 650
PrintTempBuff = False
UseMultiprocessing = True
ProcessNum = 10
SimulateName = f'보스1일반2 제브은나 {Simulation_iteration}게임 {MCTS_search_iteration}회 {GameTime}초'

if __name__ == '__main__':
    Control = input('직접 컨트롤 하시겠습니까? (y/n): ')
    if Control == 'y':
        Control = True
    elif Control == 'n':
        Control = False
    else:
        raise ValueError('y/n으로 입력해주세요')
        
    classlist = ClassList()
    # 캐릭터
    character1 = classlist.GetCharacter('제레')([6,10,10,10], Eidolons=0) # 치피/공%/양피/공%, 속도1, 공%1, 치확12, 치피10
    character1.AddLightCone(classlist.GetLightCone('야경속에서'), SuperImpose=1)
    character1.AddRelic([['별처럼빛나는천재', [('고정속도증가', 6.9), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['별처럼빛나는천재', [('HP%증가', 0.07776), ('공격력%증가', 0.98064), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['별처럼빛나는천재', [('효과명중', 0.07776), ('효과저항', 0.07776), ('치명타확률', 0.40824), ('치명타피해', 1.34784)]],
                        ['별처럼빛나는천재', [('에너지회복효율', 0), ('치유량보너스', 0), ('양자속성피해증가', 0.388)]],
                        ['뭇별경기장', []],
                        ['뭇별경기장', []]])
    
    character2 = classlist.GetCharacter('브로냐')([6,10,10,10], Eidolons=0) # 치피/속도/HP%/에충, 속도2, HP%10, 방%2, 치피10
    character2.AddLightCone(classlist.GetLightCone('아직전투는끝나지않았다'), SuperImpose=1)
    character2.AddRelic([['가상공간을누비는메신저', [('고정속도증가', 34.2), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['가상공간을누비는메신저', [('HP%증가', 0.89856), ('공격력%증가', 0.07776), ('방어력%증가', 0.1944), ('격파특수효과', 0.11664)]],
                        ['장수를원하는제자', [('효과명중', 0.07776), ('효과저항', 0.07776), ('치명타확률', 0.05832), ('치명타피해', 1.34784)]],
                        ['장수를원하는제자', [('에너지회복효율', 0.194), ('치유량보너스', 0), ('바람속성피해증가', 0)]],
                        ['불로인의선주', []],
                        ['불로인의선주', []]])

    character3 = classlist.GetCharacter('은랑')([6,10,10,10], Eidolons=0) # 효명/속도/양피/에충 속도10 치확12 치피2
    character3.AddLightCone(classlist.GetLightCone('계속내리는비'), SuperImpose=1)
    character3.AddRelic([['별처럼빛나는천재', [('고정속도증가', 52.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['별처럼빛나는천재', [('HP%증가', 0.07776), ('공격력%증가', 0.07776), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['별처럼빛나는천재', [('효과명중', 0.50976), ('효과저항', 0.07776), ('치명타확률', 0.40824), ('치명타피해', 0.23328)]],
                        ['별처럼빛나는천재', [('에너지회복효율', 0.194), ('치유량보너스', 0), ('양자속성피해증가', 0.388)]],
                        ['범은하상사', []],
                        ['범은하상사', []]])

    character4 = classlist.GetCharacter('나찰')([6,10,10,10], Eidolons=0) # 치유/속도/공%/에충, 속도10, 공%10, 효저4
    character4.AddLightCone(classlist.GetLightCone('관의울림'), SuperImpose=1)
    character4.AddRelic([['흔적없는손님', [('고정속도증가', 52.6), ('고정HP증가', 781.20751), ('고정공격력증가', 390.103754), ('고정방어력증가', 38.103754)]],
                        ['흔적없는손님', [('HP%증가', 0.07776), ('공격력%증가', 0.89856), ('방어력%증가', 0.0972), ('격파특수효과', 0.11664)]],
                        ['흔적없는손님', [('효과명중', 0.07776), ('효과저항', 0.23328), ('치명타확률', 0.05832), ('치명타피해', 0.11664)]],
                        ['흔적없는손님', [('에너지회복효율', 0.194), ('치유량보너스', 0.345), ('허수속성피해증가', 0)]],
                        ['부러진용골', []],
                        ['부러진용골', []]])
    
    Game = HSRBattle(GameTime, Control, PrintTempBuff)
    Game.AddCharacter([character1, character2, character3, character4])

    # 적, ['물리', '화염', '번개', '얼음', '바람', '허수', '양자']
    Game.AddEnemy([
                (classlist.GetEnemy('허수아비일반'), '허수아비일반-1', ['양자', '허수']),
                (classlist.GetEnemy('허수아비보스'), '허수아비보스', ['양자', '허수']),
                (classlist.GetEnemy('허수아비일반'), '허수아비일반-2', ['양자', '허수']),
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
