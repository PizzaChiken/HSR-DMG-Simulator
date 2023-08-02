

from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Pela(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '페라'
        self.Element = '얼음'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 988
        self.BaseStat['기초공격력'] += 547
        self.BaseStat['기초방어력'] += 463
        self.BaseStat['기초속도'] += 105
        self.BaseStat['에너지최대치'] += 110  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['효과명중'] += 0.04 + 0.06
        self.BaseStat['얼음속성피해증가'] += 0.032 + 0.048 + 0.048 + 0.032 + 0.064
        self.BaseStat['공격력%증가'] += 0.064 + 0.04 + 0.08
        
        if self.Eidolons >= 3:
            self.SkillLevel[1] += 2
            self.SkillLevel[0] += 1
        if self.Eidolons >= 5:
            self.SkillLevel[2] += 2
            self.SkillLevel[3] += 2

        
        self.NADMG = np.array([[0, 0.5, 0],
                                [0, 0.6, 0],
                                [0, 0.7, 0],
                                [0, 0.8, 0],
                                [0, 0.9, 0],
                                [0, 1.0, 0],
                                [0, 1.1, 0],
                                [0, 1.2, 0],
                                [0, 1.3, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillDMG = np.array([[0, 1.05, 0],
                                    [0, 1.155, 0],
                                    [0, 1.26, 0],
                                    [0, 1.365, 0],
                                    [0, 1.47, 0],
                                    [0, 1.575, 0],
                                    [0, 1.70625, 0],
                                    [0, 1.8375, 0],
                                    [0, 1.96875, 0],
                                    [0, 2.1, 0],
                                    [0, 2.205, 0],
                                    [0, 2.31, 0],
                                    [0, 2.415, 0],
                                    [0, 2.52, 0],
                                    [0, 2.625, 0],])[self.SkillLevel[1]-1]
        
        

        self.TalentEnergy = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8.125, 8.75, 9.375, 10, 10.5, 11, 11.5, 12, 12.5])[self.SkillLevel[2]-1]


        self.UltimateDefDecrease = np.array([0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.3625, 0.375, 0.3875, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45])[self.SkillLevel[3]-1]
        self.UltimateDMG = np.array([[0, 0.6, 0],
                                    [0, 0.64, 0],
                                    [0, 0.68, 0],
                                    [0, 0.72, 0],
                                    [0, 0.76, 0],
                                    [0, 0.8, 0],
                                    [0, 0.85, 0],
                                    [0, 0.9, 0],
                                    [0, 0.95, 0],
                                    [0, 1.0, 0],
                                    [0, 1.04, 0],
                                    [0, 1.08, 0],
                                    [0, 1.12, 0],
                                    [0, 1.16, 0],
                                    [0, 1.2, 0],])[self.SkillLevel[3]-1]
        self.TalentPossible = True
        self.Trace1Possible = False

    def StartTurn(self):
        super().StartTurn()
        self.TalentPossible = True


    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(PelaTrace(self))
        self.Game.TriggerList.append(PelaEidolons(self))

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)
        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat=False)

        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 

        if self.TalentPossible == True:
            if len(target[0].DebuffList) > 0 :
                self.TalentPossible = False
                self.EnergyGenerate(self.TalentEnergy, False)
       
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False) 

        if len(target[0].BuffList) > 0:
            target[0].DeleteBuff(random.choice(target[0].BuffList))
            self.Trace1Possible = True
            if self.Eidolons >= 2:
                self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff = {'버프형태' : '스탯', '설명': '페라2돌가속', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('속도%증가', 0.1)]})

        if self.Eidolons >= 4:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '페라4돌얼깍', '남은턴' : 2, '효과' : [(f'얼음속성저항증가', -0.2)]})

        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')

        if self.TalentPossible == True:
            if len(target[0].DebuffList) > 0 :
                self.TalentPossible = False
                self.EnergyGenerate(self.TalentEnergy, False)

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        for Enemy in self.Game.Enemys.copy():
            self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '페라분석', '남은턴' : 2, '효과' : [(f'방어력감소', self.UltimateDefDecrease)]})
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기공격')
            if self.TalentPossible == True:
                if len(Enemy.DebuffList) > 0 :
                    self.TalentPossible = False
                    self.EnergyGenerate(self.TalentEnergy, False)
            
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    
    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    
        

class PelaTrace:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                if self.Object.Trace1Possible == True:
                    self.Start = True
                    self.Object.Trace1Possible = False

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if len(Target[0].DebuffList) > 0:
                        self.Object.TempBuffList.append(('모든피해증가', 0.2))
                    if self.Start == True:
                        self.Object.TempBuffList.append(('모든피해증가', 0.2))

        if Trigger == '디버프발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Object in self.Object.Game.Characters:
                    Attacker.TempBuffList.append(('효과명중', 0.1))

        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            self.Start = False

class PelaEidolons:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Attack = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '적사망' or Trigger == '적전원사망':
            if self.Object.Eidolons >= 1:
                self.Object.EnergyGenerate(5, False)

        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                self.Start = True

            if Trigger == '데미지발동시작':
                if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                    if Attacker == self.Object:
                        if self.Start == True:
                            self.Attack = True
            
            if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
                if self.Start == True:
                    if self.Attack == True:
                        if self.Object.Eidolons >= 6:
                            for target in Target:
                                if len(target.DebuffList) > 0:
                                    self.Object.Game.ApplyDamage(Attacker = self.Object, Target = target, Element = self.Object.Element, DamageType = '추가피해', Toughness = 0, Multiplier = [0.0, 0.4, 0.0], FlatDMG = 0, DamageName = '페라6돌추가피해', Except = self)
                                    break
                self.Start = False
                self.Attack = False
        




            

            

        
