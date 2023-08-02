from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Bronya(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '브로냐'
        self.Element = '바람'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '아군지정', '필살기' : '아군전체'}
        self.ActiveNormalAttack = False
         

        # 기본
        self.BaseStat['기초HP'] += 1242
        self.BaseStat['기초공격력'] += 582.12
        self.BaseStat['기초방어력'] += 533.61
        self.BaseStat['기초속도'] += 99
        self.BaseStat['에너지최대치'] += 120  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['효과저항'] += 0.04 + 0.06 
        self.BaseStat['바람속성피해증가'] += 0.032 + 0.048 + 0.048 + 0.032 + 0.064
        self.BaseStat['치명타피해'] += 0.08 + 0.053 + 0.107
        
        if self.Eidolons >= 3:
            self.SkillLevel[3] += 2
            self.SkillLevel[2] += 2
        if self.Eidolons >= 5:
            self.SkillLevel[1] += 2
            self.SkillLevel[0] += 1

        self.Eidolons1Possible = True

        
        self.NADMG = np.array([[0, 0.5, 0],
                                [0, 0.6, 0],
                                [0, 0.7, 0],
                                [0, 0.8, 0],
                                [0, 0.9, 0],
                                [0, 1.0, 0],
                                [0, 1.1, 0],
                                [0, 1.2, 0],
                                [0, 1.3, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillDMGBuff = np.array([0.33, 0.363, 0.396, 0.429, 0.462, 0.495, 0.53625, 0.5775, 0.61875, 0.66, 0.693, 0.726, 0.759, 0.792, 0.825])[self.SkillLevel[1]-1]

        self.TalentAG = np.array([1500, 1650, 1800, 1950, 2100, 2250, 2437.5, 2625, 2812.5, 3000, 3150, 3300, 3450, 3600, 3750])[self.SkillLevel[2]-1]

        self.UltimateATKBuff = np.array([0.33, 0.352, 0.374, 0.396, 0.418, 0.44, 0.4675, 0.495, 0.5225, 0.55, 0.572, 0.594, 0.616, 0.638, 0.66])[self.SkillLevel[3]-1]

        self.UltimateCritMultipleBuff = np.array([0.12, 0.124, 0.128, 0.132, 0.136, 0.14, 0.145, 0.15, 0.155, 0.16, 0.164, 0.168, 0.172, 0.176, 0.18])[self.SkillLevel[3]-1]

        self.UltimateCritFlatBuff = np.array([0.12, 0.128, 0.136, 0.144, 0.152, 0.16, 0.17, 0.18, 0.19, 0.2, 0.208, 0.216, 0.224, 0.232, 0.24])[self.SkillLevel[3]-1]
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(BronyaTraces(self))
        if self.Eidolons >= 4:
            self.Game.TriggerList.append(BronyaEidolons4(self))
    
    def StartTurn(self):
        super().StartTurn()
        if self.Eidolons >= 1:
            if self.Eidolons1Possible == False:
                self.Eidolons1Possible = 'CoolDown'
            elif self.Eidolons1Possible == 'CoolDown':
                self.Eidolons1Possible = True

    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 
        self.ActiveNormalAttack = True
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)
        if len(target[0].DebuffList) > 0:
            RndDebuff = random.choice(target[0].DebuffList)
            if RndDebuff['디버프형태'] == '빙결':
                target[0].TurnSkip = False
            target[0].DeleteDebuff(RndDebuff)

        duration = 1
        if self.Eidolons >= 6:
            duration = 2
        self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff = {'버프형태' : '스탯', '설명' : '브로냐전투스킬피증', '시간타입' : 'B', '체크' : False, '남은턴' : duration, '효과' : [(f'모든피해증가', self.BSkillDMGBuff)]})
        
        if self.Eidolons >= 1:
            if self.Eidolons1Possible == True:
                if random.random() <  0.5:
                    self.Eidolons1Possible == False
                    self.Game.ChangeSkillPoint(1)
        
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

        if target[0] != self:
            for Character in self.Game.Characters:
                Character.UltimateActiveCheck = False
            self.EndTurn()
            target[0].ActionGauge = 10000
            self.Game.TurnObject = target[0]
            self.Game.TurnObject.StartTurn()
            self.Game.TurnStep = self.TurnStep = '행동전필살기선택'
            if self.Eidolons >= 2:
                self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff = {'버프형태' : '스탯', '설명' : '브로냐2돌가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [(f'속도%증가', 0.3)]})
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        for Character in self.Game.Characters:
            self.Game.ApplyBuff(Attacker = self, Target = Character, Buff ={'버프형태' : '스탯', '설명' : '브로냐궁', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '효과' : [('공격력%증가', self.UltimateATKBuff), ('치명타피해', self.CurrentStat['치명타피해'] * self.UltimateCritMultipleBuff + self.UltimateCritFlatBuff)]})
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

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
            self.ChangeActionGauge(self.TalentAG)

class BronyaTraces:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '게임시작':
            for Character in self.Object.Game.Characters:
                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Character, Buff = {'버프형태' : '스탯', '설명' : '브로냐진영', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('방어력%증가', 0.2)]}, Except = self)

        if Trigger == '데미지발동시작' or Trigger == '도트데미지발동시작' or Trigger == '격파데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Object in self.Object.Game.Characters:
                    Attacker.TempBuffList.append(('모든피해증가', 0.1))

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object and Value[0] == '일반공격':
                    self.Object.TempBuffList.append(('치명타확률', 1.0))

class BronyaEidolons4:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Possible = True
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object:
                self.Possible = True
        
        if Trigger == '캐릭터일반공격발동종료2':
            if Attacker in self.Object.Game.Characters and Attacker != self.Object:
                if self.Possible == True:
                    self.Possible = False
                    self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 브로냐 4돌추가공격 시작")
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, Target, None, Except = self)
                    self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Target[0], Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.NADMG, FlatDMG = 0, DamageName = f'{self.Object.Name}4돌추가공격', Multiple = 0.8, Except = self) 
                    self.Object.EnergyGenerate(5, False)
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, Target, None, Except = self)
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, Target, None, Except = self)