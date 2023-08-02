import random
import math
from Enemys.BaseEnemy import BaseEnemy

class TestEnemyNormal(BaseEnemy):
    def __init__(self, Name, WeakList):
        super().__init__()
        self.Name = Name
        self.MaxToughness = 60 
        self.WeakList = WeakList
        for Weak in self.WeakList:
            self.BaseStat[f'{Weak}속성저항증가'] = 0.0
        self.WindStack = 1
        self.EnemyType = '일반'

        # 혼돈 10층 방랑자 기준
        self.BaseStat['기초HP'] += 32997
        self.BaseStat['기초공격력'] += 663
        self.BaseStat['기초방어력'] += 1100
        self.BaseStat['기초속도'] += 132

        self.BaseStat['효과명중'] += 0.32
        self.BaseStat['효과저항'] += 0.2

    def Skill_1(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 단일공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('적일반공격발동시작', self, target, None)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '일반공격', Toughness = 0, Multiplier = [0.0, 3.0, 0.0], FlatDMG = 0, DamageName = f'{self.Name} 단일공격') # Multiplier[0] : HP계수, Multiplier[1] : 공격력계수, Multiplier[2] : 방어력계수
        #self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 0.6, Debuff = {'디버프형태' : '빙결', '설명' : f'{self.Name}스킬빙결'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 1, '계수' : [0.0, 0.0, 0.0]})
        target[0].EnergyGenerate(10, False)
        self.Game.ActiveTrigger('적일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('적일반공격발동종료2', self, target, None)

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
            
            self.Skill_1([target])
                        
                    