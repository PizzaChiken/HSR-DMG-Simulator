import random
import math
from Enemys.BaseEnemy import BaseEnemy

class TestEnemyBoss(BaseEnemy):
    def __init__(self, Name, WeakList):
        super().__init__()
        self.Name = Name
        self.MaxToughness = 480
        self.WeakList = WeakList
        for Weak in self.WeakList:
            self.BaseStat[f'{Weak}속성저항증가'] = 0.0
        self.WindStack = 3
        self.EnemyType = '정예'

        # 혼돈 10층 연경 기준
        self.BaseStat['기초HP'] += 439954
        self.BaseStat['기초공격력'] += 663
        self.BaseStat['기초방어력'] += 1100
        self.BaseStat['기초속도'] += 158

        self.BaseStat['효과명중'] += 0.32
        self.BaseStat['효과저항'] += 0.4

    def Skill_1(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 단일공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('적일반공격발동시작', self, target, None)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '일반공격', Toughness = 0, Multiplier = [0.0, 3.0, 0.0], FlatDMG = 0, DamageName = f'{self.Name} 단일공격') # Multiplier[0] : HP계수, Multiplier[1] : 공격력계수, Multiplier[2] : 방어력계수
        target[0].EnergyGenerate(10, False)
        self.Game.ActiveTrigger('적일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('적일반공격발동종료2', self, target, None)


    def Skill_2(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전체공격 발동")
        self.Game.ActiveTrigger('적필살기발동시작', self, target, None)
        for Character in self.Game.Characters.copy():
            self.Game.ApplyDamage(Attacker = self, Target = Character, Element = '허수', DamageType = '필살기', Toughness = 0, Multiplier = [0.0, 3.0, 0.0], FlatDMG = 0, DamageName = f'{self.Name} 전체공격')
            Character.EnergyGenerate(5, False)
        self.Game.ActiveTrigger('적필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('적필살기발동종료2', self, target, None)

    def Action(self):
        if self.TurnSkip == True:
            self.Game.AppendBattleHistory(f'시간 : {self.Game.CurrentTime}, {self.Name} 빙결로 인한 턴 스킵')
        else:
            if self.TargetCharacter == None:
                AggroList = self.Game.GetAggro()
                target = random.choices(self.Game.Characters, AggroList)[0]
            elif self.TargetCharacter in self.Game.Characters:
                target = self.TargetCharacter
            else:
                raise ValueError
            action = random.choices(['skill_1', 'skill_2'], [2, 1])[0]
            if action == 'skill_1':
                self.Skill_1([target])
            elif action == 'skill_2':
                self.Skill_2([target])
            else:
                raise ValueError
                        
                    