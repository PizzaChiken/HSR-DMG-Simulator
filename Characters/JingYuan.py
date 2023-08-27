from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class JingYuan(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '경원'
        self.Element = '번개'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적전체', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 1164
        self.BaseStat['기초공격력'] += 698.54
        self.BaseStat['기초방어력'] += 485.1
        self.BaseStat['기초속도'] += 99
        self.BaseStat['에너지최대치'] += 130  
        self.BaseStat['기초도발'] += 75
        # 추가
        self.BaseStat['치명타확률'] += 0.027 + 0.04 + 0.053
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.04 + 0.06 + 0.06
        self.BaseStat['방어력%증가'] += 0.05 + 0.075
        
        if self.Eidolons >= 3:
            self.SkillLevel[3] += 2
            self.SkillLevel[0] += 1
        if self.Eidolons >= 5:
            self.SkillLevel[1] += 2
            self.SkillLevel[2] += 2

        
        self.NADMG = np.array([[0, 0.5, 0],
                                [0, 0.6, 0],
                                [0, 0.7, 0],
                                [0, 0.8, 0],
                                [0, 0.9, 0],
                                [0, 1.0, 0],
                                [0, 1.1, 0],
                                [0, 1.2, 0],
                                [0, 1.3, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillDMG = np.array([[0, 0.5, 0],
                                    [0, 0.55, 0],
                                    [0, 0.6, 0],
                                    [0, 0.65, 0],
                                    [0, 0.7, 0],
                                    [0, 0.75, 0],
                                    [0, 0.8125, 0],
                                    [0, 0.875, 0],
                                    [0, 0.9375, 0],
                                    [0, 1.0, 0],
                                    [0, 1.05, 0],
                                    [0, 1.1, 0],
                                    [0, 1.15, 0],
                                    [0, 1.2, 0],
                                    [0, 1.25, 0],])[self.SkillLevel[1]-1]

        self.TalentDMG = np.array([[0, 0.33, 0],
                                    [0, 0.363, 0],
                                    [0, 0.396, 0],
                                    [0, 0.429, 0],
                                    [0, 0.462, 0],
                                    [0, 0.495, 0],
                                    [0, 0.53625, 0],
                                    [0, 0.5775, 0],
                                    [0, 0.61875, 0],
                                    [0, 0.66, 0],
                                    [0, 0.693, 0],
                                    [0, 0.726, 0],
                                    [0, 0.759, 0],
                                    [0, 0.792, 0],
                                    [0, 0.825, 0],])[self.SkillLevel[2]-1]
                
        self.UltimateDMG = np.array([[0, 1.2, 0],
                                    [0, 1.28, 0],
                                    [0, 1.36, 0],
                                    [0, 1.44, 0],
                                    [0, 1.52, 0],
                                    [0, 1.6, 0],
                                    [0, 1.7, 0],
                                    [0, 1.8, 0],
                                    [0, 1.9, 0],
                                    [0, 2.0, 0],
                                    [0, 2.08, 0],
                                    [0, 2.16, 0],
                                    [0, 2.24, 0],
                                    [0, 2.32, 0],
                                    [0, 2.4, 0],])[self.SkillLevel[3]-1]
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(JingYuanBattaliaCrush(self))
        if self.Eidolons >=6 :
            self.Game.TriggerList.append(JingYuanEidolons6(self))
    
    def Init(self):
        super().Init()
        self.Summons = LightningLord(self)
        self.Game.Summons.append(self.Summons)
        self.EnergyGenerate(15, True)

    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)
        for Enemy in self.Game.Enemys.copy():
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')
        self.Summons.AddStack(2)
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 신군 2스택 추가, 현재 신군 스택 : {self.Summons.Stack}")
        self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '경원전투스킬치확', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('치명타확률', 0.1)]})
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        for Enemy in self.Game.Enemys.copy(): # 중간에 적이 사망하면 for loop에 오류생김
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기')
        self.Summons.AddStack(3)
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 신군 3스택 추가, 현재 신군 스택 : {self.Summons.Stack}")
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    
    def GetDamage(self, Attacker, Damage, Element, ToughnessDMG, Type):
        super().GetDamage(Attacker, Damage, Element, ToughnessDMG, Type)
        if self.IsDead == True:
            self.Game.Summons.remove(self.Summons)

class LightningLord:
    def __init__(self, Object):
        self.Object = Object
        self.Type = '소환수'
        self.Name = '신군'
        self.ActionGauge = 0
        self.Speed = 60
        self.Stack = 3

    def Action(self): # 나중에 뜯어고쳐야함 현재 빙결시에만 스킵되는데 얽힘,속박시에도 스킵되어야함
        if self.Object.CheckFrozen() != True and self.Object.TurnSkip == False:
            self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 신군 공격 시작, 스택 : {self.Stack}")
            self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, self.Object.Game.Enemys, None, Except = self)
            for i in range(self.Stack):
                if len(self.Object.Game.Enemys) != 0:
                    RndTarget = random.choice(self.Object.Game.Enemys)
                    NeighboringTargets = self.Object.Game.GetNeighboringEnemy(RndTarget)
                    self.Object.Game.ApplyDamage(Attacker = self.Object, Target = RndTarget, Element = self.Object.Element, DamageType = '추가공격', Toughness = 15, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName = f'{self.Object.Name}신군메인공격', Except = self)
                    if self.Object.Eidolons >= 4:
                        self.Object.EnergyGenerate(2, False)
                    for NeighboringTarget in NeighboringTargets:
                        if self.Object.Eidolons >= 1:
                            multiple = 0.5
                        else:
                            multiple = 0.25
                        self.Object.Game.ApplyDamage(Attacker = self.Object, Target = NeighboringTarget, Element = self.Object.Element, DamageType = '추가공격', Toughness = 0, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName = f'{self.Object.Name}신군확산공격', Multiple = multiple, Except = self)
                    
            self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, self.Object.Game.Enemys, None, Except = self)
            self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, self.Object.Game.Enemys, None, Except = self)
            if self.Object.Eidolons >=2:
                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '경원2돌피증', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '효과' : [('일반공격피해증가', 0.2), ('전투스킬피해증가', 0.2), ('필살기피해증가', 0.2)]}, Except = self)
            self.ActionGauge = 0 
            self.Stack = 3

            self.Object.Game.AppendBattleHistory(f"시간 : {self.Object.Game.CurrentTime}, 신군 공격 종료")
            self.Object.Game.AppendBattleHistory(f"객체별 현재 속도       : {[char.Name + ' : ' + str(char.CalcSpeed()) for char in self.Object.Game.Characters] + [Enemy.Name + ' : ' + str(Enemy.CalcSpeed()) for Enemy in self.Object.Game.Enemys] + [Summons.Name + ' : ' + str(Summons.CalcSpeed()) for Summons in self.Object.Game.Summons]}")
            self.Object.Game.AppendBattleHistory(f"객체별 현재 행동게이지 : {[char.Name + ' : ' + str(char.ActionGauge) for char in self.Object.Game.Characters] + [Enemy.Name + ' : ' + str(Enemy.ActionGauge) for Enemy in self.Object.Game.Enemys] + [Summons.Name + ' : ' + str(Summons.ActionGauge) for Summons in self.Object.Game.Summons]} \n")

        else:
            self.ActionGauge = 0
    
    def AddStack(self, cnt):
        self.Stack += cnt
        if self.Stack > 10:
            self.Stack = 10

    def CalcSpeed(self):
        return self.Speed + 10 * (self.Stack-3)

 
class JingYuanBattaliaCrush:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object and Value[0] == '추가공격':
                    if Value[1]=='경원신군메인공격' or Value[1]=='경원신군확산공격':
                        if self.Object.Summons.Stack >= 6:
                            self.Object.TempBuffList.append(('치명타피해', 0.25))
                    else:
                        raise ValueError

class JingYuanEidolons6:
    def __init__(self, Object):
        self.Object = Object
        self.StackList = {}
        self.Start = False
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터추가공격발동시작':
            if Attacker == self.Object:
                self.Start = True
                self.StackList = {Enemy : 0 for Enemy in self.Object.Game.Enemys}
            
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object and Value[0] == '추가공격':
                    if self.Start == True:
                        Target[0].TempBuffList.append(('받는피해증가', 0.12 * self.StackList[Target[0]]))
                        if Value[1]=='경원신군메인공격':
                            self.StackList[Target[0]] = min(3, self.StackList[Target[0]] + 1)
                    else: 
                        raise ValueError
            
        if Trigger == '캐릭터추가공격발동종료':
            if Attacker == self.Object:
                if self.Start == True:
                    self.Start = False
                    self.StackList = {}
                else:
                    raise ValueError
            

