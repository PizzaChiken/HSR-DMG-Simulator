from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Clara(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '클라라'
        self.Element = '물리'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적전체', '필살기' : '자신지정'} 

        # 기본
        self.BaseStat['기초HP'] += 1242
        self.BaseStat['기초공격력'] += 737
        self.BaseStat['기초방어력'] += 485.1
        self.BaseStat['기초속도'] += 90
        self.BaseStat['에너지최대치'] += 110  
        self.BaseStat['기초도발'] += 125
        # 추가
        self.BaseStat['HP%증가'] += 0.04 + 0.06
        self.BaseStat['공격력%증가'] += 0.04 + 0.04 + 0.06 + 0.06 + 0.08
        self.BaseStat['물리속성피해증가'] += 0.032 + 0.048 + 0.064
        self.BaseStat['받는피해증가'] += -0.1      #특성 받피감 구현

        # 추가능력1
        self.BaseStat['속박저항'] += 0.35
        self.BaseStat['얽힘저항'] += 0.35
        self.BaseStat['빙결저항'] += 0.35
        self.BaseStat['도발저항'] += 0.35
        
        if self.Eidolons >= 3:
            self.SkillLevel[1] += 2
            self.SkillLevel[0] += 1
        if self.Eidolons >= 5:
            self.SkillLevel[3] += 2
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
        
        self.BSkillDMG = np.array([[0, 0.6, 0],
                                    [0, 0.66, 0],
                                    [0, 0.72, 0],
                                    [0, 0.78, 0],
                                    [0, 0.84, 0],
                                    [0, 0.9, 0],
                                    [0, 0.975, 0],
                                    [0, 1.05, 0],
                                    [0, 1.125, 0],
                                    [0, 1.2, 0],
                                    [0, 1.26, 0],
                                    [0, 1.32, 0],
                                    [0, 1.38, 0],
                                    [0, 1.44, 0],
                                    [0, 1.5, 0],])[self.SkillLevel[1]-1]

        self.TalentDMG = np.array([[0, 0.8, 0],
                                    [0, 0.88, 0],
                                    [0, 0.96, 0],
                                    [0, 1.04, 0],
                                    [0, 1.12, 0],
                                    [0, 1.2, 0],
                                    [0, 1.3, 0],
                                    [0, 1.4, 0],
                                    [0, 1.5, 0],
                                    [0, 1.6, 0],
                                    [0, 1.68, 0],
                                    [0, 1.76, 0],
                                    [0, 1.84, 0],
                                    [0, 1.92, 0],
                                    [0, 2, 0],])[self.SkillLevel[2]-1]
                
        self.UltimateMultiplier = np.array([0.96, 1.024, 1.088, 1.152, 1.216, 1.28, 1.36, 1.44, 1.52, 1.6, 1.664, 1.728, 1.792, 1.856, 1.92])[self.SkillLevel[3]-1]
        self.UltDamageReduce = np.array([-0.15, -0.16, -0.17, -0.18, -0.19, -0.2, -0.2125, -0.225, -0.2475, -0.25, -0.26, -0.27, -0.28, -0.29, -0.3])[self.SkillLevel[3]-1]    #-가 받는피해감소, +는 받는피해증가
        self.Mark = []
    
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(ClaraCounterAttack(self))
        self.Game.TriggerList.append(ClaraTrace(self))

    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)
        for Enemy in self.Game.Enemys.copy():
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')
            if Enemy in self.Mark:
                self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}표식전투스킬')
                if not self.Eidolons >= 1:
                    self.Mark.remove(Enemy)
            
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        if self.Eidolons >= 2:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '클라라궁버프', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('도발%증가', 5), ('받는피해증가', self.UltDamageReduce), ('공격력%증가', 0.3)]})
        else:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '클라라궁버프', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('도발%증가', 5), ('받는피해증가', self.UltDamageReduce)]})
        if self.Eidolons >= 6:
            cnt = 3
        else:
            cnt = 2
        self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '기타', '설명' : '클라라반격강화', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '남은횟수' : cnt})
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    

    def ChangeUltStack(self, stack):
        for buff in self.BuffList.copy():
            if buff['설명'] == '클라라반격강화':
                beforeStack = buff['남은횟수']
                buff['남은횟수'] += stack
                self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 클라라 궁극기 스택 {stack} 변화, 이전 : {beforeStack}, 현재 : {buff['남은횟수']}")
                if buff['남은횟수'] == 0:
                    self.DeleteBuff(buff)

    def checkUltStackExist(self):
        for buff in self.BuffList:
            if buff['설명'] == '클라라반격강화':
                if buff['남은횟수'] > 0 :
                   return True
        return False
    
    def GetDamage(self, Attacker, Damage, Element, ToughnessDMG, Type):
        super().GetDamage(Attacker, Damage, Element, ToughnessDMG, Type)
        if self.Eidolons >= 4:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '클라라4돌피해감소', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('받는피해증가', -0.3)]})   #클라라 4돌 받피감


class ClaraCounterAttack: 
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Attacked = False
        

    def Active(self, trigger, Attacker, Target, Value):
        if trigger in ('적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
            self.Start = True

        if trigger == '데미지발동시작':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Start == True:
                    if self.Object.checkUltStackExist() == True:
                        if Target[0] in self.Object.Game.Characters:
                            self.Attacked = 'ult'
                    else:
                        if self.Object.Eidolons >= 6:
                            if random.random() < 0.5 :
                                if Target[0] in self.Object.Game.Characters:
                                    self.Attacked = 'normal'
                                    self.Object.Mark.append(Attacker)
                        if Target[0] == self.Object:
                            self.Attacked = 'normal'

                    if Target[0] == self.Object:
                        self.Object.Mark.append(Attacker)
                    
        
        if trigger in ('적일반공격발동종료2', '적전투스킬발동종료2', '적필살기발동종료2', '적추가공격발동종료2'):
            if self.Start == True:
                if self.Attacked != False:
                    if self.Object.CheckFrozen() != True and self.Object.TurnSkip == False:
                        if self.Attacked == 'ult':
                            self.Attacked = False
                            self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 클라라 반격")
                            if Attacker in self.Object.Game.Enemys:
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, Attacker, None, Except = self)
                                neighboringTargets = self.Object.Game.GetNeighboringEnemy(Attacker)
                                self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Attacker, Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName = f'{self.Object.Name}특성강화공격', Multiple = ( 1 + self.Object.UltimateMultiplier), Except = self)
                                for neighboringTarget in neighboringTargets:
                                        self.Object.Game.ApplyDamage(Attacker = self.Object, Target = neighboringTarget, Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMG , FlatDMG = 0, DamageName = f'{self.Object.Name}특성확산공격', Multiple = ( 1 + self.Object.UltimateMultiplier) / 2 , Except = self)
                                self.Object.EnergyGenerate(5, False)
                                self.Object.ChangeUltStack(-1) # 궁스택 감소 코드
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, Attacker, None, Except = self)
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, Attacker, None)

                        elif self.Attacked=='normal':
                            self.Attacked = False
                            self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 클라라 반격")
                            if Attacker in self.Object.Game.Enemys:
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, Attacker, None, Except = self)
                                self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Attacker, Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMG , FlatDMG = 0, DamageName = f'{self.Object.Name}특성추가공격', Except = self)
                                self.Object.EnergyGenerate(5, False)
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, Attacker, None, Except = self)
                                self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, Attacker, None, Except = self)
                        else:
                            raise ValueError # 오류체크용
                    if random.random() <= 0.35:
                        if len(self.Object.DebuffList) > 0:
                            self.Object.DeleteDebuff(random.choice(self.Object.DebuffList))
            self.Start = False
            self.Attacked = False

class ClaraTrace: 
    def __init__(self, Object):
        self.Object = Object     

    def Active(self, trigger, Attacker, Target, Value):
        if trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object and Value[0] == '추가공격':
                    Attacker.TempBuffList.append(('추가공격피해증가', 0.3))