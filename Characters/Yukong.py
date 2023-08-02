from Characters.BaseCharacter import BaseCharacter
import numpy as np

class Yukong(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '어공'
        self.Element = '허수'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '아군전체', '필살기' : '적지정'}
         

        # 기본
        self.BaseStat['기초HP'] += 917
        self.BaseStat['기초공격력'] += 600
        self.BaseStat['기초방어력'] += 385
        self.BaseStat['기초속도'] += 107
        self.BaseStat['에너지최대치'] += 130  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.06  
        self.BaseStat['허수속성피해증가'] += 0.032 + 0.048 + 0.048 + 0.032 + 0.064
        self.BaseStat['HP%증가'] += 0.04 +0.06 + 0.08
        
        if self.Eidolons >= 3:
            self.SkillLevel[0] += 1
            self.SkillLevel[1] += 2
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
        
        self.BSkillAtkBuff = np.array([0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.65, 0.7, 0.75, 0.8, 0.84, 0.88, 0.92, 0.96, 1.0])[self.SkillLevel[1]-1]

        self.TalentDMG = np.array([[0, 0.4, 0],
                                    [0, 0.44, 0],
                                    [0, 0.48, 0],
                                    [0, 0.52, 0],
                                    [0, 0.56, 0],
                                    [0, 0.6, 0],
                                    [0, 0.65, 0],
                                    [0, 0.7, 0],
                                    [0, 0.75, 0],
                                    [0, 0.8, 0],
                                    [0, 0.84, 0],
                                    [0, 0.88, 0],
                                    [0, 0.92, 0],
                                    [0, 0.96, 0],
                                    [0, 1.0, 0],])[self.SkillLevel[2]-1]

        self.UltimateCRBuff = np.array([0.21, 0.217, 0.224, 0.231, 0.238, 0.245, 0.25375, 0.2625, 0.27125, 0.28, 0.287, 0.294, 0.301, 0.308, 0.315])[self.SkillLevel[3]-1]

        self.UltimateCDBuff = np.array([0.39, 0.416, 0.442, 0.468, 0.494, 0.52, 0.5525, 0.585, 0.6175, 0.65, 0.676, 0.702, 0.728, 0.754, 0.78])[self.SkillLevel[3]-1]

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
        self.TalentPossible = True
        self.BStack = 0
        self.BExcept = False
        self.Trace3Possible = 0
        self.Eidolon2List = []

        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(YukongManageBStack(self))
        self.Game.TriggerList.append(YukongTrace(self))
        self.Game.TriggerList.append(YukongEidolon(self))
    
    def StartTurn(self):
        super().StartTurn()
        if self.TalentPossible == False:
            self.TalentPossible = 'CoolDown'
        elif self.TalentPossible == 'CoolDown':
            self.TalentPossible = True
        self.Trace3Possible = max(0, self.Trace3Possible -1)
            
    def ChangeBStack(self, stack):
        beforeStack = self.BStack
        self.BStack += stack
        if self.BStack > 2:
            self.BStack = 2
        if self.BStack < 0:
            raise ValueError
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 어공활시위호령 {stack} 변화, 이전 : {beforeStack}, 현재 : {self.BStack}")

        if beforeStack == 0 and self.BStack > 0:
            for Character in self.Game.Characters:
             self.Game.ApplyBuff(Attacker = self, Target = Character, Buff = {'버프형태' : '스탯', '설명' : '어공활시위호령', '시간타입' : 'B', '체크' : False, '남은턴' : 1000, '효과' : [(f'공격력%증가', self.BSkillAtkBuff)]})
       
        if self.BStack == 0:
            for Character in self.Game.Characters:
                for Buff in Character.BuffList:
                    if Buff['설명'] == '어공활시위호령':
                        Character.DeleteBuff(Buff)

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 
        if self.TalentPossible == True:
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.TalentDMG, FlatDMG = 0, DamageName = f'{self.Name}특성공격') 
            self.TalentPossible = False
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False)

        self.ChangeBStack(2)
        self.BExcept = True

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        if self.Eidolons >= 6:
            self.ChangeBStack(1)

        for Character in self.Game.Characters:
            if any([Buff['설명'] == '어공활시위호령' for Buff in Character.BuffList]):
                self.Game.ApplyBuff(Attacker = self, Target = Character, Buff = {'버프형태' : '스탯', '설명' : '어공활시위호령', '시간타입' : 'B', '체크' : False, '남은턴' : 1000, '효과' : [(f'공격력%증가', self.BSkillAtkBuff), ('치명타확률', self.UltimateCRBuff), ('치명타피해', self.UltimateCDBuff)]})
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 90, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기') 
        self.Eidolon2List = []

        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
        

class YukongManageBStack:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴종료':
            if Attacker in self.Object.Game.Characters:
                if self.Object.BExcept == True:
                    self.Object.BExcept = False
                else:
                    if self.Object.BStack > 0:
                        self.Object.ChangeBStack(-1)

class YukongTrace: 
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Object in self.Object.Game.Characters:
                    Attacker.TempBuffList.append(('허수속성피해증가', 0.12))
        
        if Trigger== '디버프적중종료':
            if self.Object in Target:
                if self.Object.Trace3Possible == 0:
                    self.Object.DeleteBuff(Value[0])
                    self.Object.Trace3Possible == 2

        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작','캐릭터필살기발동시작'):
            if Attacker.Type == '캐릭터':
                if self.Object.BStack > 0:
                    self.Object.EnergyGenerate(2, False)
            else:
                raise ValueError

class YukongEidolon:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '게임시작':
            if self.Object.Eidolons >= 1:
                for Character in self.Object.Game.Characters:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Character, Buff = {'버프형태' : '스탯', '설명' : '어공1돌가속', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '효과' : [('속도%증가', 0.1)]}, Except = self)

        if Trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료','캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Object.Eidolons >= 2:
                for Character in self.Object.Game.Characters:
                    if Character.CurrentEnergy >= Character.BaseStat['에너지최대치'] and Character not in self.Object.Eidolon2List:
                        self.Object.Eidolon2List.append(Character)
                        self.Object.EnergyGenerate(5, False)

        if Trigger == '데미지발동시작':
            if self.Object.Eidolons >= 4:
                if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                    if Attacker == self.Object:
                        if self.Object.BStack > 0:
                            self.Object.TempBuffList.append(('모든피해증가', 0.3))