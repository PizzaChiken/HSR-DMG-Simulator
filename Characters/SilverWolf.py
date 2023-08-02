from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class SilverWolf(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '은랑'
        self.Element = '양자'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적지정'} 

        # 기본
        self.BaseStat['기초HP'] += 1048
        self.BaseStat['기초공격력'] += 640
        self.BaseStat['기초방어력'] += 461
        self.BaseStat['기초속도'] += 107
        self.BaseStat['에너지최대치'] += 110  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.06 + 0.06 + 0.04
        self.BaseStat['양자속성피해증가'] += 0.032 + 0.048
        self.BaseStat['효과명중'] += 0.04 + 0.06 + 0.08

        if self.Eidolons >= 3:
            self.SkillLevel[1] += 2
            self.SkillLevel[2] += 2
        if self.Eidolons >= 5:
            self.SkillLevel[3] += 2
            self.SkillLevel[0] += 1

        
        self.NADMG = np.array([[0, 0.5, 0],
                                [0, 0.6, 0],
                                [0, 0.7, 0],
                                [0, 0.8, 0],
                                [0, 0.9, 0],
                                [0, 1.0, 0],
                                [0, 1.1, 0],
                                [0, 1.2, 0],
                                [0, 1.3, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillProb = np.array([0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.8125, 0.825, 0.8375, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9])[self.SkillLevel[1]-1]
        self.BSkillMainDMG =  np.array([[0, 0.98, 0],
                                        [0, 1.078, 0],
                                        [0, 1.176, 0],
                                        [0, 1.274, 0],
                                        [0, 1.372, 0],
                                        [0, 1.47, 0],
                                        [0, 1.5925, 0],
                                        [0, 1.715, 0],
                                        [0, 1.8375, 0],
                                        [0, 1.96, 0],
                                        [0, 2.058, 0],
                                        [0, 2.156, 0],
                                        [0, 2.254, 0],
                                        [0, 2.352, 0],
                                        [0, 2.45, 0],])[self.SkillLevel[1]-1]
        self.BSkillResDecrease = np.array([-0.075, -0.0775, -0.08, -0.0825, -0.085, -0.0875, -0.090625, -0.09375, -0.096875, -0.1, -0.1025, -0.105, -0.1075, -0.11, -0.1125])[self.SkillLevel[1]-1]
        
        self.TalentProb = np.array([0.6, 0.612, 0.624, 0.636, 0.648, 0.66, 0.675, 0.69, 0.705, 0.72, 0.732, 0.744, 0.756, 0.768, 0.78])[self.SkillLevel[2]-1]
        self.TalentAtkDecrease = np.array([-0.005, -0.055, -0.06, -0.065, -0.07, -0.075, -0.08125, -0.0875, -0.09375, -0.1, -0.105, -0.11, -0.115, -0.12, -0.125])[self.SkillLevel[2]-1]
        self.TalentDefDecrease = np.array([0.04, 0.044, 0.048, 0.052, 0.056, 0.06, 0.065, 0.07, 0.075, 0.08, 0.084, 0.088, 0.092, 0.096, 0.1])[self.SkillLevel[2]-1]
        self.TalentSpeedDecrease = np.array([-0.03, -0.033, -0.036, -0.039, -0.042, -0.045, -0.04875, -0.0525, -0.05625, -0.06, -0.063, -0.066, -0.069, -0.072, -0.075])[self.SkillLevel[2]-1]

        self.UltimateProb = np.array([0.85, 0.865, 0.88, 0.895, 0.91, 0.925, 0.94375, 0.9625, 0.98125, 1, 1.015, 1.03, 1.045, 1.06, 1.075])[self.SkillLevel[3]-1]
        self.UltimateDefDecrease = np.array([0.36, 0.369, 0.378, 0.387, 0.396, 0.405, 0.41625, 0.4275, 0.43875, 0.45, 0.459, 0.468, 0.477, 0.486, 0.495])[self.SkillLevel[3]-1]
        self.UltimateDMG = np.array([[0, 2.28, 0],
                                    [0, 2.432, 0],
                                    [0, 2.584, 0],
                                    [0, 2.736, 0],
                                    [0, 2.888, 0],
                                    [0, 3.04, 0],
                                    [0, 3.23, 0],
                                    [0, 3.42, 0],
                                    [0, 3.61, 0],
                                    [0, 3.8, 0],
                                    [0, 3.952, 0],
                                    [0, 4.104, 0],
                                    [0, 4.256, 0],
                                    [0, 4.408, 0],
                                    [0, 4.56, 0],])[self.SkillLevel[3]-1]

       
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(SilverWolfGenerate(self))
        if self.Eidolons >= 2:
            self.Game.TriggerList.append(SilverWolfEidolon2(self))
        if self.Eidolons >= 6:
            self.Game.TriggerList.append(SilverWolfEidolon6(self))

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')

        # 특성
        BugList = ['은랑결함1호', '은랑결함2호', '은랑결함3호']
        for debuff in target[0].DebuffList:
            if debuff['설명'] in BugList:
                BugList.remove(debuff['설명'])
        if len(BugList) > 0 :
            DebuffName = random.choice(BugList)
        else:
            DebuffName = random.choice(['은랑결함1호', '은랑결함2호', '은랑결함3호'])
        if DebuffName == '은랑결함1호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함1호', '남은턴' : 4, '효과' : [(f'공격력%증가', self.TalentAtkDecrease)]})
        elif DebuffName == '은랑결함2호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함2호', '남은턴' : 4, '효과' : [(f'방어력감소', self.TalentDefDecrease)]})
        elif DebuffName == '은랑결함3호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함3호', '남은턴' : 4, '효과' : [(f'속도%증가', self.TalentSpeedDecrease)]})
        else:
            raise ValueError
      
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)


    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)
        self.Game.ChangeSkillPoint(-1)


        self.EnergyGenerate(30, Flat=False)
        weakList  = []
        if len(target[0].DebuffList) >= 3:
            self.check = True
        else:
            self.check = False

        for char in self.Game.Characters:
            if char.Element not in weakList and char.Element not in target[0].WeakList:
                weakList.append(char.Element)
        if len(weakList) > 0:
            weak = random.choice(weakList)
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.BSkillProb, Debuff = {'디버프형태' : '약점부여', '설명' : '은랑약점부여', '남은턴' : 3, '속성' : weak, '효과' : [(f'{weak}속성저항증가', -0.2)]})

        if self.check == True:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '은랑전투스킬저항감소', '남은턴' : 2, '효과' : [(f'모든속성저항증가', self.BSkillResDecrease-0.03)]})
        elif self.check == False:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '은랑전투스킬저항감소', '남은턴' : 2, '효과' : [(f'모든속성저항증가', self.BSkillResDecrease)]})

        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillMainDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬공격')
      
        # 특성
        BugList = ['은랑결함1호', '은랑결함2호', '은랑결함3호']
        for debuff in target[0].DebuffList:
            if debuff['설명'] in BugList:
                BugList.remove(debuff['설명'])
        if len(BugList) > 0 :
            DebuffName = random.choice(BugList)
        else:
            DebuffName = random.choice(['은랑결함1호', '은랑결함2호', '은랑결함3호'])
        if DebuffName == '은랑결함1호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함1호', '남은턴' : 4, '효과' : [(f'공격력%증가', self.TalentAtkDecrease)]})
        elif DebuffName == '은랑결함2호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함2호', '남은턴' : 4, '효과' : [(f'방어력감소', self.TalentDefDecrease)]})
        elif DebuffName == '은랑결함3호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함3호', '남은턴' : 4, '효과' : [(f'속도%증가', self.TalentSpeedDecrease)]})
        else:
            raise ValueError
        
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)



    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, , 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.UltimateProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑필살기방감', '남은턴' : 3, '효과' : [(f'방어력감소', self.UltimateDefDecrease)]})
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 90, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기공격')

        if self.Eidolons >= 1: 
            stack = len(target[0].DebuffList)
            if stack > 5:
                stack = 5
            self.EnergyGenerate(stack * 7, False)
            if self.Eidolons >= 4:
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '추가피해', Toughness = 0, Multiplier = [0, 0.2, 0], FlatDMG = 0, DamageName = f'{self.Name}4돌추가피해', Multiple = max(1, stack))


        # 특성
        BugList = ['은랑결함1호', '은랑결함2호', '은랑결함3호']
        for debuff in target[0].DebuffList:
            if debuff['설명'] in BugList:
                BugList.remove(debuff['설명'])
        if len(BugList) > 0 :
            DebuffName = random.choice(BugList)
        else:
            DebuffName = random.choice(['은랑결함1호', '은랑결함2호', '은랑결함3호'])
        if DebuffName == '은랑결함1호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함1호', '남은턴' : 4, '효과' : [(f'공격력%증가', self.TalentAtkDecrease)]})
        elif DebuffName == '은랑결함2호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함2호', '남은턴' : 4, '효과' : [(f'방어력감소', self.TalentDefDecrease)]})
        elif DebuffName == '은랑결함3호':
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.TalentProb, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함3호', '남은턴' : 4, '효과' : [(f'속도%증가', self.TalentSpeedDecrease)]})
        else:
            raise ValueError
        
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError


class SilverWolfGenerate:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '적격파됨':
            # 특성
            BugList = ['은랑결함1호', '은랑결함2호', '은랑결함3호']
            for debuff in Target[0].DebuffList:
                if debuff['설명'] in BugList:
                    BugList.remove(debuff['설명'])
            if len(BugList) > 0 :
                DebuffName = random.choice(BugList)
            else:
                DebuffName = random.choice(['은랑결함1호', '은랑결함2호', '은랑결함3호'])
            if DebuffName == '은랑결함1호':
                self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함1호', '남은턴' : 4, '효과' : [(f'공격력%증가', self.Object.TalentAtkDecrease)]}, Except = self)
            elif DebuffName == '은랑결함2호':
                self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함2호', '남은턴' : 4, '효과' : [(f'방어력감소', self.Object.TalentDefDecrease)]}, Except = self)
            elif DebuffName == '은랑결함3호':
                self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '스탯', '설명' : '은랑결함3호', '남은턴' : 4, '효과' : [(f'속도%증가', self.Object.TalentSpeedDecrease)]}, Except = self)
            else:
                raise ValueError
            
class SilverWolfEidolon2:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('게임시작', '적리젠'):
            for Enemy in self.Object.Game.Enemys:
                self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Enemy, BaseProbability = 10, Debuff = {'디버프형태' : '스탯', '설명' : '은랑2돌', '남은턴' : 1000, '효과' : [(f'효과저항', -0.2)]}, Except = self)
                      
class SilverWolfEidolon6:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    stack = len(Target[0].DebuffList)
                    if stack > 5:
                        stack = 5
                    self.Object.TempBuffList.append(('모든피해증가', 0.2 * stack))