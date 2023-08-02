from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Blade(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '블레이드'
        self.Element = '바람'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '자신지정', '필살기' : '적지정'} 

        # 기본
        self.BaseStat['기초HP'] += 1358
        self.BaseStat['기초공격력'] += 543
        self.BaseStat['기초방어력'] += 485
        self.BaseStat['기초속도'] += 97
        self.BaseStat['에너지최대치'] += 130  
        self.BaseStat['기초도발'] += 125
        # 추가
        self.BaseStat['HP%증가'] += 0.04 + 0.06 + 0.06 + 0.04 +0.08
        self.BaseStat['치명타확률'] += 0.04 + 0.027 + 0.053
        self.BaseStat['효과저항'] += 0.04 + 0.06 

        self.BaseStat['추가공격피해증가'] += 0.2

        if self.Eidolons >= 3:
            self.SkillLevel[3] += 2
            self.SkillLevel[2] += 2
        if self.Eidolons >= 5:
            self.SkillLevel[1] += 2
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
        
        self.NAEnhancedMainDMG = np.array([[0.5, 0.2, 0],
                                            [0.6, 0.24, 0],
                                            [0.7, 0.28, 0],
                                            [0.8, 0.32, 0],
                                            [0.9, 0.36, 0],
                                            [1.0, 0.4, 0],
                                            [1.1, 0.44, 0],
                                            [1.2, 0.48, 0],
                                            [1.3, 0.52, 0]])[self.SkillLevel[0]-1]
        
        self.NAEnhancedSubDMG = np.array([[0.2, 0.08, 0],
                                        [0.24, 0.096, 0],
                                        [0.28, 0.112, 0],
                                        [0.32, 0.128, 0],
                                        [0.36, 0.144, 0],
                                        [0.4, 0.16, 0],
                                        [0.44, 0.176, 0],
                                        [0.48, 0.192, 0],
                                        [0.52, 0.208, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillDMGBuff =  np.array([0.12, 0.148, 0.176, 0.204, 0.232, 0.26, 0.295, 0.33, 0.365, 0.4, 0.428, 0.456, 0.484, 0.512, 0.54])[self.SkillLevel[1]-1]
        
        self.TalentDMG =  np.array([[0.55, 0.22, 0],
                                    [0.605, 0.242, 0],
                                    [0.66, 0.264, 0],
                                    [0.715, 0.286, 0],
                                    [0.77, 0.308, 0],
                                    [0.825, 0.33, 0],
                                    [0.89375, 0.3575, 0],
                                    [0.9625, 0.385, 0],
                                    [1.03125, 0.4125, 0],
                                    [1.1, 0.44, 0],
                                    [1.155, 0.462, 0],
                                    [1.21, 0.484, 0],
                                    [1.265, 0.506, 0],
                                    [1.32, 0.528, 0],
                                    [1.375, 0.55, 0],])[self.SkillLevel[2]-1]
        self.TalentDMGEidolon6 =  np.array([[0.55 + 0.5, 0.22, 0],
                                            [0.605 + 0.5, 0.242, 0],
                                            [0.66 + 0.5, 0.264, 0],
                                            [0.715 + 0.5, 0.286, 0],
                                            [0.77 + 0.5, 0.308, 0],
                                            [0.825 + 0.5, 0.33, 0],
                                            [0.89375 + 0.5, 0.3575, 0],
                                            [0.9625 + 0.5, 0.385, 0],
                                            [1.03125 + 0.5, 0.4125, 0],
                                            [1.1 + 0.5, 0.44, 0],
                                            [1.155 + 0.5, 0.462, 0],
                                            [1.21 + 0.5, 0.484, 0],
                                            [1.265 + 0.5, 0.506, 0],
                                            [1.32 + 0.5, 0.528, 0],
                                            [1.375 + 0.5, 0.55, 0],])[self.SkillLevel[2]-1]
        
        self.UltimateMainHPMultiplier = np.array([0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.85, 0.9, 0.95, 1.0, 1.04, 1.08, 1.12, 1.16, 1.2])[self.SkillLevel[3]-1]
        if self.Eidolons >= 1:
            self.UltimateMainHPMultiplier += 1.5
        self.UltimateMainDMG = np.array([[0.6, 0.24, 0],
                                        [0.64, 0.256, 0],
                                        [0.68, 0.272, 0],
                                        [0.72, 0.288, 0],
                                        [0.76, 0.304, 0],
                                        [0.8, 0.32, 0],
                                        [0.85, 0.34, 0],
                                        [0.9, 0.36, 0],
                                        [0.95, 0.38, 0],
                                        [1.0, 0.4, 0],
                                        [1.04, 0.416, 0],
                                        [1.08, 0.432, 0],
                                        [1.12, 0.448, 0],
                                        [1.16, 0.464, 0],
                                        [1.2, 0.48, 0],])[self.SkillLevel[3]-1]
        
        self.UltimateSubHPMultiplier = np.array([0.24, 0.256, 0.272, 0.288, 0.304, 0.32, 0.34, 0.36, 0.38, 0.4, 0.416, 0.432, 0.448, 0.464, 0.48])[self.SkillLevel[3]-1]
        self.UltimateSubDMG = np.array([[0.24, 0.096, 0],
                                        [0.256, 0.1024, 0],
                                        [0.272, 0.1088, 0],
                                        [0.288, 0.1152, 0],
                                        [0.304, 0.1216, 0],
                                        [0.32, 0.128, 0],
                                        [0.34, 0.136, 0],
                                        [0.36, 0.144, 0],
                                        [0.38, 0.152, 0],
                                        [0.4, 0.16, 0],
                                        [0.416, 0.1664, 0],
                                        [0.432, 0.1728, 0],
                                        [0.448, 0.1792, 0],
                                        [0.464, 0.1856, 0],
                                        [0.48, 0.192, 0],])[self.SkillLevel[3]-1]

        self.LostHP = 0
        self.TalentStack = 0
        if self.Eidolons >= 4:
            self.Eidolon4Stack = 0
    
    def ChangeTalentStack(self, stack):
        beforeStack = self.TalentStack
        self.TalentStack += stack
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 블레이드 특성스탯 {stack} 변화, 이전 : {beforeStack}, 현재 : {self.TalentStack}")

    def AddLostHP(self, damage):
        MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
        self.LostHP += damage
        if self.LostHP > 0.9 * MaxHP:
            self.LostHP = 0.9 * MaxHP
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 블레이드 누적 손실 HP {damage} 변화, 현재 누적 손실 HP : {self.LostHP}")

    def ConsumesHP(self, Attacker, Multiplier, Flat):
        MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
        saveCurrentHP = self.CurrentHP
        ConsumedHP = MaxHP * Multiplier + Flat
        if 0<self.CurrentHP <=1:
            self.CurrentHP = 1
        ConsumedHP = min(self.CurrentHP-1, ConsumedHP)
        self.CurrentHP -= ConsumedHP
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {ConsumedHP} 소모, 현재 HP : {self.CurrentHP}, 최대 HP : {MaxHP}") 
        self.AddLostHP(ConsumedHP)
        self.Game.ActiveTrigger('캐릭터체력소모', Attacker, [self], ConsumedHP)
        if self.Eidolons >= 4:
            if (saveCurrentHP > 0.5 * MaxHP) and (self.CurrentHP <= 0.5 * MaxHP):
                self.Eidolon4Stack = min(2, self.Eidolon4Stack + 1)
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '블레이드4돌체퍼', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('HP%증가', self.Eidolon4Stack * 0.2)]})



    def GetDamage(self, Attacker, Damage, Element, ToughnessDMG, Type):
        if self.IsDead == False:
            ShieldList = []
            for  Buff in self.BuffList:
                if Buff['버프형태'] == '실드':
                    ShieldList.append(Buff)

            MiNRemainDamage = Damage
            for Shield in ShieldList:
                RemainDamage = Damage - Shield['수치']
                if RemainDamage > 0:
                    self.DeleteBuff(Shield)
                else:
                    Shield['수치'] -= Damage
                    RemainDamage = 0
                if RemainDamage < MiNRemainDamage:
                    MiNRemainDamage = RemainDamage
            
            MaxHP = self.TempStat['기초HP'] * (1 + self.TempStat['HP%증가']) + self.TempStat['고정HP증가']
            if self.CurrentHP > MaxHP:
                self.CurrentHP = MaxHP # 만약 디버프로 인해 최대 HP값이 현재 HP보다 줄어들었다면 현재 HP는 최대 HP값으로 조정된다
            saveCurrentHP = self.CurrentHP
            self.CurrentHP -= MiNRemainDamage
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {MiNRemainDamage} 감소, 현재 HP : {self.CurrentHP}, 최대 HP : {MaxHP}")
            self.AddLostHP(MiNRemainDamage)

            if self.CurrentHP <= 0:
                self.CurrentHP = 0
                self.IsDead = True
                self.Game.IsDead(Attacker, self, Type)
            if self.Eidolons >= 4:
                if (saveCurrentHP > 0.5 * MaxHP) and (self.CurrentHP <= 0.5 * MaxHP):
                    self.Eidolon4Stack = min(2, self.Eidolon4Stack + 1)
                    self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '블레이드4돌체퍼', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('HP%증가', self.Eidolon4Stack * 0.2)]})

            return MiNRemainDamage
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(BladeTalent(self))
        self.Game.TriggerList.append(BladeTrace3(self))

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        if any([buff['설명'] == '블레이드지옥의변화' for buff in self.BuffList]):
            self.EnergyGenerate(30, False)
            self.ConsumesHP(self, 0.1, 0)
            NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 60, Multiplier = self.NAEnhancedMainDMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')
            for NeighboringTarget in NeighboringTargets:
                self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NAEnhancedSubDMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격확산공격')
            if any([target[0].IsBroken == True] + [NTarget.IsBroken==True for NTarget in NeighboringTargets]):
                self.Game.ApplyHeal(self, self, [0.05, 0, 0], 100, '블레이드추가능력')

        else:
            self.Game.ChangeSkillPoint(1)
            self.EnergyGenerate(20, Flat = False)
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')

        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)


    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)
        self.ConsumesHP(self, 0.3, 0)
        if self.Eidolons >= 2:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '블레이드지옥의변화', '시간타입' : 'A', '체크' : False, '남은턴' : 3, '효과' : [('모든피해증가', self.BSkillDMGBuff), ('치명타확률', 0.15)]})
        else: 
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '블레이드지옥의변화', '시간타입' : 'A', '체크' : False, '남은턴' : 3, '효과' : [('모든피해증가', self.BSkillDMGBuff)]})
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
        self.Game.TurnStep = '행동선택'


    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, , 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
        if self.CurrentHP < 0.5 * MaxHP:
            self.CurrentHP = 0.5 * MaxHP
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {self.CurrentHP}로 조정, 최대 HP : {MaxHP}")
        else:
            self.ConsumesHP(self, 0, self.CurrentHP - 0.5 * MaxHP)

        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateMainDMG, FlatDMG = self.LostHP*self.UltimateMainHPMultiplier, DamageName = f'{self.Name}필살기메인공격')
        for NeighboringTarget in NeighboringTargets:
            self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateSubDMG, FlatDMG = self.LostHP*self.UltimateSubHPMultiplier, DamageName = f'{self.Name}필살기확산공격')
        self.AddLostHP(-self.LostHP)
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            if any([buff['설명'] == '블레이드지옥의변화' for buff in self.BuffList]):
                return False
            else:
                return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError


class BladeTalent:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Attacked = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
            self.Start = True

        if Trigger == '데미지발동종료':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Start == True:
                    if  (self.Object in Target):
                        self.Attacked = True

        if Trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료'):
            if self.Start == True:
                if self.Attacked == True:
                    self.Object.ChangeTalentStack(1)
            self.Start = False
            self.Attacked = False

        if Trigger == '도트데미지발동종료':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Object in Target:
                    self.Object.ChangeTalentStack(1)

        if Trigger == '캐릭터체력소모':
            if self.Object in Target:
                if Value >= 0:
                    self.Object.ChangeTalentStack(1)
        
        if Trigger in ('적일반공격발동종료2', '적전투스킬발동종료2', '적필살기발동종료2', '적추가공격발동종료2','캐릭터일반공격발동종료2', '캐릭터전투스킬발동종료2', '캐릭터필살기발동종료2', '캐릭터추가공격발동종료2', '캐릭터턴시작결산'):
                if self.Object.Eidolons >= 6:
                    if self.Object.TalentStack >= 4:
                        self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 블레이드 추가공격 시작")
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, self.Object.Game.Enemys, None, Except = self)
                        self.Object.EnergyGenerate(10, False)
                        for Enemy in self.Object.Game.Enemys.copy():
                            self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Enemy, Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMGEidolon6, FlatDMG = 0, DamageName = f'{self.Object.Name}특성추가공격', Except = self)      
                        self.Object.Game.ApplyHeal(self.Object, self.Object, [0.25, 0, 0], 0, '블레이드특성추가공격힐', Except = self)
                        self.Object.ChangeTalentStack(-self.Object.TalentStack)
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, self.Object.Game.Enemys, None, Except = self)
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, self.Object.Game.Enemys, None, Except = self)
                else:
                    if self.Object.TalentStack >= 5:
                        self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 블레이드 추가공격 시작")
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, self.Object.Game.Enemys, None, Except = self)
                        self.Object.EnergyGenerate(10, False)
                        for Enemy in self.Object.Game.Enemys.copy():
                            self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Enemy, Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName = f'{self.Object.Name}특성추가공격', Except = self)      
                        self.Object.Game.ApplyHeal(self.Object, self.Object, [0.25, 0, 0], 0, '블레이드특성추가공격힐', Except = self)
                        self.Object.ChangeTalentStack(-self.Object.TalentStack)
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, self.Object.Game.Enemys, None, Except = self)
                        self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, self.Object.Game.Enemys, None, Except = self)


class BladeTrace3:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '힐발동시작':
            if self.Object in Target:
                MaxHP = self.Object.CurrentStat['기초HP'] * (1 + self.Object.CurrentStat['HP%증가']) + self.Object.CurrentStat['고정HP증가']
                if self.Object.CurrentHP < 0.5 * MaxHP:
                    Attacker.TempBuffList.append(('치유량보너스', 0.2))
                
        