import numpy as np
import copy
import random
import sys
import time
import multiprocessing
from functools import partial

class Node:
    def __init__(self, state, parent):
        self.parent = parent
        self.state = state

        self.visits = 0
        self.Damage = 0
        self.children = []

    def expand(self):
        for ActionIdx in range(len(self.state.PossibleAction)):
            new_state = copy.deepcopy(self.state)
            new_state.ApplyCharacterAction(new_state.PossibleAction[ActionIdx])
            new_state.GetPossibleAction()
            child_node = Node(new_state, self)
            self.children.append(child_node)

    def select_child(self):
        total_visits = sum(child.visits for child in self.children)
        log_total_visits = np.log(total_visits) 
        mean = np.mean([child.Damage for child in self.children]) 
        std = np.std([child.Damage for child in self.children]) 
        if std == 0:
            std = 1
 
        scores = [
            self.DamageToProb(child.Damage, mean, std) + np.sqrt(2) * np.sqrt(log_total_visits / child.visits)
            for child in self.children
        ]
        max_score_index = np.argmax(scores)
        return self.children[max_score_index]

    def select_best_child(self):
        scores = [child.Damage for child in self.children]
        max_score_index = np.argmax(scores)
        return self.children[max_score_index]

    def update(self, result):
        self.Damage = (self.Damage * self.visits + result)/(self.visits+1)
        self.visits += 1
    
    def DamageToProb(self, Damage, mean, std):
        Standardization = (Damage - mean)/std
        return 1/(1 + np.exp(-Standardization))

class MonteCarloTreeSearch:
    def __init__(self, state):
        self.root = Node(state, None)
        self.root.expand()

    def run(self, num_simulations):
        for i in range(num_simulations):
            node = self.selection()
            if node.state.Terminal == False:
                if node.visits >= num_simulations/100 :
                    node.expand()
                    node = random.choice(node.children)
            result = self.simulation(node)
            self.backpropagation(node, result)

        if self.root.state.Terminal == False:
            best_child = self.root.select_best_child()
            self.root.children = []
            self.root = best_child
            self.root.parent = None
        return self.root.state.Terminal

    def selection(self):
        node = self.root
        while True:
            if node.children != []:
                for child in node.children:
                    if child.visits == 0:
                        return child
                node = node.select_child()
            else:
                break
        return node

    def simulation(self, node):
        if node.state.Terminal == False:
            state = copy.deepcopy(node.state)
        else:
            state = node.state
        while state.Terminal == False:
            if state.PossibleAction == []:
                print(state.TurnStep)
                print(state.TurnObject)
                print(state.Enemys)
                for history in state.BattleHistory:
                    print(history)
            action = random.choice(state.PossibleAction)
            state.ApplyCharacterAction(action)
            state.GetPossibleAction()
        result = sum(state.Damage.values())
        return result

    def backpropagation(self, node, result):
        while True:
            node.update(result)
            if node == self.root: 
                break
            else:
                node = node.parent

def update_progress(progress, remainTime, progressTime):
    bar_length = 50
    filled_length = int(round(bar_length * progress))
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {int(progress * 100)}%, {progressTime} 경과, 남은 시간 예상 : {remainTime}')
    sys.stdout.flush()

def RunOneSimulation(Game, MCTS_search_iteration):
    Simulator = MonteCarloTreeSearch(Game)
    Terminal = False
    while Terminal == False:
        Terminal = Simulator.run(MCTS_search_iteration)

    return sum(Simulator.root.state.Damage.values()), Simulator.root.state.Damage.copy(), Simulator.root.state.TypeDamage.copy(), Simulator.root.state.BattleHistory.copy()

def RunOneProcess(Dic, Game, MCTS_search_iteration, startTotal, Simulation_iteration):
    TotalDamage, Damage, TypeDamage, BattleHistory = RunOneSimulation(copy.deepcopy(Game), MCTS_search_iteration)
    Dic['count'] += 1
    count = Dic['count']
    end = time.time()
    progressTime = f'{(end-startTotal)//60}분'
    averageTime = (end-startTotal)/(count)
    remainTime = f'{(averageTime * (Simulation_iteration - (count)))//60}분'
    progress = (count) / Simulation_iteration
    update_progress(progress, remainTime, progressTime)
    return TotalDamage, Damage, TypeDamage, BattleHistory


def RunSimulation(Game, Simulation_iteration, MCTS_search_iteration, Multiprocessing, ProcessNum, SimulationName):
    print(f'사용가능 프로세서 개수 : {multiprocessing.cpu_count()}, 사용하는 프로세서 개수 : {ProcessNum}')
    print(f'\n{SimulationName} 시뮬레이션')
    startTotal = time.time()
    SimulationTotalDamageHistory = []
    SimulationDamageHistory = []
    SimulationTypeDamageHistory = []
    SimulationBattleHistory = []
    update_progress(0, '?', 0)

    if Multiprocessing == True:
        Manager = multiprocessing.Manager()
        Dic = Manager.dict()
        Dic['count'] = 0
        Pool = multiprocessing.Pool(processes=ProcessNum)
        func = partial(RunOneProcess, Game = Game, MCTS_search_iteration = MCTS_search_iteration, startTotal=startTotal, Simulation_iteration=Simulation_iteration)
        try:
            results = Pool.map(func, [Dic for i in range(Simulation_iteration)])
        except:
            Pool.terminate()
            raise ValueError
        
        for result in results:
            TotalDamage, Damage, TypeDamage, BattleHistory = result
            SimulationTotalDamageHistory.append(TotalDamage)
            SimulationDamageHistory.append(Damage)
            SimulationTypeDamageHistory.append(TypeDamage)
            SimulationBattleHistory.append(BattleHistory)
        
        Pool.close()
        Pool.join()
    else:
        for _ in range(Simulation_iteration):
            Dic = {}
            Dic['count']=0
            TotalDamage, Damage, TypeDamage, BattleHistory = RunOneProcess(Dic, Game, MCTS_search_iteration, startTotal, Simulation_iteration)
            SimulationTotalDamageHistory.append(TotalDamage)
            SimulationDamageHistory.append(Damage)
            SimulationTypeDamageHistory.append(TypeDamage)
            SimulationBattleHistory.append(BattleHistory)

    endTotal = time.time()
    print(f'\n시뮬레이션 완료, 수행시간 : {(endTotal-startTotal)//60}분\n')

    MaxIndex = np.argmax(SimulationTotalDamageHistory)
    MinIndex = np.argmin(SimulationTotalDamageHistory)
    average = np.average(SimulationTotalDamageHistory)
    StandardDeviation = np.std(SimulationTotalDamageHistory)

    averageDamage = SimulationDamageHistory[0].copy()
    averageTypeDamage = SimulationTypeDamageHistory[0].copy()
    for i in range(1, len(SimulationDamageHistory)):
        for char in SimulationDamageHistory[i]:
            averageDamage[char] += SimulationDamageHistory[i][char]
        for char in SimulationTypeDamageHistory[i]:
            for DamageType in ['일반공격', '전투스킬', '필살기', '추가공격', '추가피해', '지속피해', '격파피해']:
                averageTypeDamage[char][DamageType] += SimulationTypeDamageHistory[i][char][DamageType]
    for char in averageDamage:
        averageDamage[char] = averageDamage[char] / Simulation_iteration
    for char in averageTypeDamage:
        for DamageType in ['일반공격', '전투스킬', '필살기', '추가공격', '추가피해', '지속피해', '격파피해']:
            averageTypeDamage[char][DamageType] = averageTypeDamage[char][DamageType]/Simulation_iteration
    

    print(f'{len(SimulationTotalDamageHistory)}번의 시뮬레이션, 평균 데미지 : {average}, 표준편차 : {StandardDeviation}')
    print('캐릭터별 평균 데미지 : ', averageDamage)
    print('\n캐릭터별 데미지 종류별 : ')
    for Char in averageTypeDamage:
        print(f'{Char} : {averageTypeDamage[Char]}')
    print(f'\n최대 데미지 : {SimulationTotalDamageHistory[MaxIndex]}, 캐릭터별 딜량 : {SimulationDamageHistory[MaxIndex]}, {MaxIndex+1}번째 시뮬레이션')
    print(f'최소 데미지 : {SimulationTotalDamageHistory[MinIndex]}, 캐릭터별 딜량 : {SimulationDamageHistory[MinIndex]}, {MinIndex+1}번째 시뮬레이션')

    with open(f'{SimulationName}.txt', 'w') as file:
        file.write(f'{len(SimulationTotalDamageHistory)}번의 시뮬레이션, 평균 데미지 : {average}, 표준편차 : {StandardDeviation}\n')
        file.write('캐릭터별 평균 데미지 : '+ str(averageDamage)+'\n')
        file.write('\n캐릭터별 데미지 종류별 : \n')
        for Char in averageTypeDamage:
            file.write(f'{Char} : {averageTypeDamage[Char]}'+'\n')
        file.write(f'\n최대 데미지 : {SimulationTotalDamageHistory[MaxIndex]}, 캐릭터별 딜량 : {SimulationDamageHistory[MaxIndex]}, {MaxIndex+1}번째 시뮬레이션\n')
        file.write(f'최소 데미지 : {SimulationTotalDamageHistory[MinIndex]}, 캐릭터별 딜량 : {SimulationDamageHistory[MinIndex]}, {MinIndex+1}번째 시뮬레이션\n\n')
        file.write(f'\n최대 데미지 시뮬레이션기록\n\n')
        for item in SimulationBattleHistory[MaxIndex]:
            file.write(item + '\n')
            
    while True:
        answer = input('\n시뮬레이션 기록을 보시겠습니까 (y/n) : ')
        if answer == 'y':
            idx = int(input(f'\n몇번째 시뮬레이션 기록을 보시겠습니까? (총 {Simulation_iteration}회, 최대 : {MaxIndex+1}, 최소 : {MinIndex+1}) : '))
            print(f'\n{SimulationName} 시뮬레이션')
            for history in SimulationBattleHistory[idx-1]:
                print(history)
        elif answer == 'n':
            break