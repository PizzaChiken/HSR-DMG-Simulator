

from Characters.BaseCharacter import BaseCharacter
import numpy as np

class Seele(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '제레'
        self.Element = '양자'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적지정'} 
        self.ActiveNormalAttack = False

        # 기본
        self.BaseStat['기초HP'] += 931
        self.BaseStat['기초공격력'] += 640.33
        self.BaseStat['기초방어력'] += 363.83
        self.BaseStat['기초속도'] += 115
        self.BaseStat['에너지최대치'] += 120  
        self.BaseStat['기초도발'] += 75
        # 추가
        self.BaseStat['치명타피해'] += 0.053 + 0.08 + 0.107
        self.BaseStat['공격력%증가'] += 0.04 + 0.06 + 0.08 + 0.04 + 0.06
        self.BaseStat['방어력%증가'] += 0.075 + 0.05
        
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
        
        self.BSkillDMG = np.array([[0, 1.1, 0],
                                    [0, 1.21, 0],
                                    [0, 1.32, 0],
                                    [0, 1.43, 0],
                                    [0, 1.54, 0],
                                    [0, 1.65, 0],
                                    [0, 1.7875, 0],
                                    [0, 1.925, 0],
                                    [0, 2.0625, 0],
                                    [0, 2.2, 0],
                                    [0, 2.31, 0],
                                    [0, 2.42, 0],
                                    [0, 2.53, 0],
                                    [0, 2.64, 0],
                                    [0, 2.75, 0],])[self.SkillLevel[1]-1]

        self.TalentDMGBuff = np.array([0.4, 0.44, 0.48, 0.52, 0.56, 0.60, 0.65, 0.70, 0.75, 0.80, 0.84, 0.88, 0.92, 0.96, 1.0])[self.SkillLevel[2]-1]
        
        self.UltimateDMG = np.array([[0, 2.55, 0],
                                    [0, 2.72, 0],
                                    [0, 2.89, 0],
                                    [0, 3.06, 0],
                                    [0, 3.23, 0],
                                    [0, 3.4, 0],
                                    [0, 3.6125, 0],
                                    [0, 3.825, 0],
                                    [0, 4.0375, 0],
                                    [0, 4.25, 0],
                                    [0, 4.42, 0],
                                    [0, 4.59, 0],
                                    [0, 4.76, 0],
                                    [0, 4.93, 0],
                                    [0, 5.1, 0],])[self.SkillLevel[3]-1]
            
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(SeeleTalent(self))
        self.Game.TriggerList.append(SeeleNightShade(self))
        if self.Eidolons >=1:
            self.Game.TriggerList.append(SeeleEidolons1(self))
        if self.Eidolons >=6:
            self.Game.TriggerList.append(SeeleEidolons6(self))

    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 0, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격', Multiple = 0.5) # Multiplier[0] : HP계수, Multiplier[1] : 공격력계수, Multiplier[2] : 방어력계수
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격', Multiple = 0.5)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)
        self.ActiveNormalAttack = True

    def BattleSkill(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)

        stack = False
        if self.Eidolons >= 2:
            for Buff in self.BuffList:
                if Buff['설명'] == '제레전투스킬가속':
                    stack = True
            if stack == True:
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '제레전투스킬가속', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('속도%증가', 0.5)]})
            else:
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '제레전투스킬가속', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('속도%증가', 0.25)]})    
        else:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '제레전투스킬가속', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('속도%증가', 0.25)]})
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 0, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬', Multiple = 1/6)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 0, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬', Multiple = 1/6)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 0, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬', Multiple = 1/6)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬', Multiple = 3/6)

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '제레특성증폭', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('양자속성피해증가', self.TalentDMGBuff), ('양자속성저항관통', 0.2)]})
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 90, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기')
            
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

        if self.Eidolons >= 6:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 10, Debuff = {'디버프형태' : '스탯', '설명' : '제레6돌혼란의나비', '남은턴' : 1, '효과' : []})

    
    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    
    def EndTurn(self):
        super().EndTurn()
        if self.ActiveNormalAttack == True:
            self.ActiveNormalAttack = False
            self.ChangeActionGauge(2000)
        

class SeeleTalent:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.check =  False
        self.SaveTurnStep = None
        self.SaveTurnObject = None
        self.Resurgence = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터일반공격발동시작' or Trigger == '캐릭터전투스킬발동시작' or Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                self.Start = True

        elif Trigger == '적사망':
            if self.Start == True:
                if self.Object.Eidolons >= 4:
                    self.Object.EnergyGenerate(15, False)
                if self.Resurgence == False:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '제레특성증폭', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('양자속성피해증가', self.Object.TalentDMGBuff), ('양자속성저항관통', 0.2)]}, Except = self)
                    self.SaveTurnStep = self.Object.Game.TurnStep
                    self.SaveTurnObject = self.Object.Game.TurnObject
                    self.Object.Game.TurnStep = '행동선택'
                    self.Object.Game.TurnObject = self.Object
                    self.Resurgence = True
                    self.check = True # 재현을 발동시킨 공격이 종료되는것을 검사
                    self.Object.Game.AppendBattleHistory(f'\n시간 : {self.Object.Game.CurrentTime}, 적처치로 인한 제레 추가턴')

        elif Trigger == '캐릭터필살기발동종료':
            self.Start = False
            if self.check == True:
                self.check = False

        elif Trigger == '캐릭터일반공격발동종료' or Trigger == '캐릭터전투스킬발동종료':
            self.Start = False
            if self.check == True:
                self.check = False
            elif self.check == False:
                if Trigger == '캐릭터일반공격발동종료' or Trigger == '캐릭터전투스킬발동종료':
                    if self.Resurgence == True:
                        if self.Object.Game.TurnObject == self.Object and self.SaveTurnObject != None and self.SaveTurnStep != None:
                            self.Object.Game.TurnObject = self.SaveTurnObject
                            self.Object.Game.TurnStep = self.SaveTurnStep
                            self.SaveTurnObject = None
                            self.SaveTurnStep = None
                            self.Resurgence = False

                        else:
                            print(self.Object.Game.TurnObject)
                            print(self.Object.Game.TurnObject == self.Object)
                            print(self.SaveTurnObject != None)
                            print(self.SaveTurnStep != None)
                            raise ValueError
            else:
                raise ValueError

class SeeleNightShade:
    def __init__(self, Object):
        self.Object = Object
        self.start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '적턴시작':
            if Attacker in self.Object.Game.Enemys:
                CurrentHP = self.Object.CurrentHP
                MaxHP = self.Object.CurrentStat['기초HP'] * (1 + self.Object.CurrentStat['HP%증가']) + self.Object.CurrentStat['고정HP증가']
                if CurrentHP < 0.5 * MaxHP:
                    self.start = True
                    self.Object.BaseStat['기초도발'] = 75 * 0.5
                    self.Object.CalcCurrentStat()
        
        if Trigger == '적턴종료':
            if self.start == True:
                self.start = False
                self.Object.BaseStat['기초도발'] = 75
                self.Object.CalcCurrentStat()

class SeeleEidolons1:
    def __init__(self, Object):
        self.Object = Object
        self.start =  False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    CurrentHP = Target[0].CurrentHP
                    MaxHP = Target[0].CurrentStat['기초HP'] * (1 + Target[0].CurrentStat['HP%증가']) + Target[0].CurrentStat['고정HP증가']
                    if CurrentHP <= 0.8 * MaxHP:
                        self.Object.TempBuffList.append(('치명타확률', 0.15))

class SeeleEidolons6:
    def __init__(self,Object):
        self.Object = Object
        self.Targets = []
        self.Start = False
        self.Target = None
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터일반공격발동시작' or Trigger =='캐릭터전투스킬발동시작' or Trigger == '캐릭터필살기발동시작' or Trigger =='캐릭터추가공격발동시작':
            self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if any([Debuff['설명'] == '제레6돌혼란의나비' for Debuff in Target[0].DebuffList]):
                        if Target[0] not in self.Targets:
                            self.Targets.append(Target[0])
        
        if Trigger == '캐릭터일반공격발동종료' or Trigger =='캐릭터전투스킬발동종료' or Trigger == '캐릭터필살기발동종료' or Trigger == '캐릭터추가공격발동종료':
            if self.Start == True:
                for target in self.Targets:
                    self.Object.Game.ApplyDamage(Attacker = self.Object, Target = target, Element = '양자', DamageType = '추가피해', Toughness = 0, Multiplier = self.Object.UltimateDMG, FlatDMG = 0, DamageName = f'제레6돌추가피해', Multiple = 0.15, Except = self)
            self.Start = False
            self.Targets = []



            

            

        
