

from Characters.BaseCharacter import BaseCharacter
import numpy as np

class DanHengImbibitorLunae(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        print('\n\n주의 : 단항음월은 테섭 기준으로 작성되었음 (V2) \n\n')
        self.Name = '단항음월'
        self.Element = '허수'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '자신지정', '필살기' : '적지정'} 

        # 기본
        self.BaseStat['기초HP'] += 1242
        self.BaseStat['기초공격력'] += 699
        self.BaseStat['기초방어력'] += 364
        self.BaseStat['기초속도'] += 102
        self.BaseStat['에너지최대치'] += 140  
        self.BaseStat['기초도발'] += 125
        # 추가
        self.BaseStat['치명타확률'] += 0.04 + 0.027 + 0.053
        self.BaseStat['허수속성피해증가'] += 0.032 + 0.048 + 0.048 + 0.032 + 0.064
        self.BaseStat['HP%증가'] += 0.04 + 0.06

        # 추가능력2
        self.BaseStat['속박저항'] += 0.35
        self.BaseStat['얽힘저항'] += 0.35
        self.BaseStat['빙결저항'] += 0.35
        self.BaseStat['도발저항'] += 0.35
        
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
                    
        self.NAEnhanced1DMG = np.array([[0, 1.3, 0],
                                        [0, 1.56, 0],
                                        [0, 1.82, 0],
                                        [0, 2.08, 0],
                                        [0, 2.34, 0],
                                        [0, 2.6, 0],
                                        [0, 2.86, 0],
                                        [0, 3.12, 0],
                                        [0, 3.38, 0]])[self.SkillLevel[0]-1]
                
        self.NAEnhanced2MainDMG = np.array([[0, 1.9, 0],
                                            [0, 2.28, 0],
                                            [0, 2.66, 0],
                                            [0, 3.04, 0],
                                            [0, 3.42, 0],
                                            [0, 3.8, 0],
                                            [0, 4.18, 0],
                                            [0, 4.56, 0],
                                            [0, 4.94, 0]])[self.SkillLevel[0]-1]
                
        self.NAEnhanced2SubDMG = np.array([[0, 0.3, 0],
                                            [0, 0.36, 0],
                                            [0, 0.42, 0],
                                            [0, 0.48, 0],
                                            [0, 0.54, 0],
                                            [0, 0.6, 0],
                                            [0, 0.66, 0],
                                            [0, 0.72, 0],
                                            [0, 0.78, 0]])[self.SkillLevel[0]-1]
        
        self.NAEnhanced3MainDMG = np.array([[0, 2.5, 0],
                                            [0, 3.0, 0],
                                            [0, 3.5, 0],
                                            [0, 4.0, 0],
                                            [0, 4.5, 0],
                                            [0, 5.0, 0],
                                            [0, 5.5, 0],
                                            [0, 6.0, 0],
                                            [0, 6.5, 0]])[self.SkillLevel[0]-1]
        
        self.NAEnhanced3SubDMG = np.array([[0, 0.9, 0],
                                            [0, 1.08, 0],
                                            [0, 1.26, 0],
                                            [0, 1.44, 0],
                                            [0, 1.62, 0],
                                            [0, 1.8, 0],
                                            [0, 1.98, 0],
                                            [0, 2.16, 0],
                                            [0, 2.34, 0]])[self.SkillLevel[0]-1]
                    
        
        self.BSkillCritBuff = np.array([0.06, 0.066, 0.072, 0.078, 0.084, 0.09, 0.0975, 0.105, 0.1125, 0.12, 0.126, 0.132, 0.138, 0.144, 0.15])[self.SkillLevel[1]-1]

        self.TalentDMGBuff = np.array([0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08125, 0.0875, 0.09375, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125])[self.SkillLevel[2]-1]
        
        self.UltimateMainDMG = np.array([[0, 1.8, 0],
                                        [0, 1.92, 0],
                                        [0, 2.04, 0],
                                        [0, 2.16, 0],
                                        [0, 2.28, 0],
                                        [0, 2.4, 0],
                                        [0, 2.55, 0],
                                        [0, 2.7, 0],
                                        [0, 2.85, 0],
                                        [0, 3.0, 0],
                                        [0, 3.12, 0],
                                        [0, 3.24, 0],
                                        [0, 3.36, 0],
                                        [0, 3.48, 0],
                                        [0, 3.6, 0],])[self.SkillLevel[3]-1]

        self.UltimateSubDMG = np.array([[0, 0.84, 0],
                                        [0, 0.896, 0],
                                        [0, 0.952, 0],
                                        [0, 1.008, 0],
                                        [0, 1.064, 0],
                                        [0, 1.12, 0],
                                        [0, 1.19, 0],
                                        [0, 1.26, 0],
                                        [0, 1.33, 0],
                                        [0, 1.4, 0],
                                        [0, 1.456, 0],
                                        [0, 1.512, 0],
                                        [0, 1.568, 0],
                                        [0, 1.624, 0],
                                        [0, 1.68, 0],])[self.SkillLevel[3]-1]
                
        self.NAEnhance = 0
        self.EnhanceStack = 0
        self.TalentStack = 0
        self.Eidolon6Stack = 0

    def Init(self):
        super().Init()
        self.EnergyGenerate(15, True)

    def ChangeEnhanceStack(self, stack):
        beforeStack = self.EnhanceStack
        self.EnhanceStack += stack
        if self.EnhanceStack > 3:
            self.EnhanceStack = 3
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 단항 역린 {stack} 변화, 이전 : {beforeStack}, 현재 : {self.EnhanceStack}")

    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(DanHengIMTrace1(self))
        if self.Eidolons >= 6:
            self.Game.TriggerList.append(DanHengIMEidolon6(self))

    def NormalAttack(self, target):
        if self.NAEnhance == 0:
            self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 0단 일반공격 발동, 타겟 : {target[0].Name}")
            self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)
            self.Game.ChangeSkillPoint(1)
            self.EnergyGenerate(20, Flat=False)
            for i in range(2):
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30/2, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}0단일반공격', Multiple = 1/2) 
                if self.Eidolons >= 1:
                    self.TalentStack = min(10, self.TalentStack+2)
                else:
                    self.TalentStack = min(6, self.TalentStack+1)
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항긍지', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.TalentDMGBuff * self.TalentStack)]})
        
        elif self.NAEnhance == 1:
            self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 1단 일반공격 발동, 타겟 : {target[0].Name}")
            self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)
            self.EnergyGenerate(30, Flat=False)
            for i in range(3):
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 60/3, Multiplier = self.NAEnhanced1DMG, FlatDMG = 0, DamageName = f'{self.Name}1단일반공격', Multiple = 1/3)
                if self.Eidolons >= 1:
                    self.TalentStack = min(10, self.TalentStack+2)
                else:
                    self.TalentStack = min(6, self.TalentStack+1)
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항긍지', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.TalentDMGBuff * self.TalentStack)]})
        
        elif self.NAEnhance == 2:
            self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 2단 일반공격 발동, 타겟 : {target[0].Name}")
            self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)
            self.EnergyGenerate(35, Flat=False)
            NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
            for i in range(5):
                if i >= 3 :
                    stack = 1
                    for Buff in self.BuffList:
                        if Buff['설명'] == '단항질타':
                            stack = min(Buff['스택']+ 1, 4)
                    duration = 2 if self.Eidolons>=4 else 1
                    self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항질타', '시간타입' : 'B', '체크' : False, '남은턴' : duration, '스택' : stack, '효과' : [('치명타피해', self.BSkillCritBuff * stack)]})
                    for NeighboringTarget in NeighboringTargets:
                        self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '일반공격', Toughness = 30/2, Multiplier = self.NAEnhanced2SubDMG, FlatDMG = 0, DamageName = f'{self.Name}2단일반확산공격', Multiple = 1/2)
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 90/5, Multiplier = self.NAEnhanced2MainDMG, FlatDMG = 0, DamageName = f'{self.Name}2단일반메인공격', Multiple = 1/5)
                if self.Eidolons >= 1:
                    self.TalentStack = min(10, self.TalentStack+2)
                else:
                    self.TalentStack = min(6, self.TalentStack+1)
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항긍지', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.TalentDMGBuff * self.TalentStack)]})
        
        elif self.NAEnhance == 3:
            self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 3단 일반공격 발동, 타겟 : {target[0].Name}")
            self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)
            self.EnergyGenerate(40, Flat=False)
            NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
            if self.Eidolons >= 6:
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항6돌허수관통', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('허수속성저항관통', 0.2 * self.Eidolon6Stack)]})
                self.Eidolon6Stack = 0
            for i in range(7):
                if i >= 3 :
                    stack = 1
                    for Buff in self.BuffList:
                        if Buff['설명'] == '단항질타':
                            stack = min(Buff['스택']+ 1, 4)
                    duration = 2 if self.Eidolons>=4 else 1
                    self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항질타', '시간타입' : 'B', '체크' : False, '남은턴' : duration, '스택' : stack, '효과' : [('치명타피해', self.BSkillCritBuff * stack)]})
                    for NeighboringTarget in NeighboringTargets:
                        self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '일반공격', Toughness = 60/4, Multiplier = self.NAEnhanced3SubDMG, FlatDMG = 0, DamageName = f'{self.Name}3단일반확산공격', Multiple = 1/4)
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 120/7, Multiplier = self.NAEnhanced3MainDMG, FlatDMG = 0, DamageName = f'{self.Name}3단일반메인공격', Multiple = 1/7)
                if self.Eidolons >= 1:
                    self.TalentStack = min(10, self.TalentStack+2)
                else:
                    self.TalentStack = min(6, self.TalentStack+1)
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항긍지', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.TalentDMGBuff * self.TalentStack)]})
            if self.Eidolons >= 6:
                for Buff in self.BuffList:
                    if Buff['설명'] == '단항6돌허수관통':
                        self.DeleteBuff(Buff)
        else:
            raise ValueError
        
        self.NAEnhance = 0
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동")

        if self.EnhanceStack > 0:
            self.ChangeEnhanceStack(-1)
        else:
            self.Game.ChangeSkillPoint(-1)
        save = self.NAEnhance
        self.NAEnhance += 1
        if self.NAEnhance < 0 or self.NAEnhance > 3:
            raise ValueError
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 단항음월  평타강화 시전, 이전 : {save}, 현재 : {self.NAEnhance}")
        
        self.Game.TurnStep = '행동선택'
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
        for i in range(3):
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 60/3, Multiplier = self.UltimateMainDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기메인공격', Multiple = 1/3)
            for NeighboringTarget in NeighboringTargets:
                    self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '필살기', Toughness = 60/3, Multiplier = self.UltimateSubDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기확산공격', Multiple = 1/3)
            if self.Eidolons >= 1:
                self.TalentStack = min(10, self.TalentStack+2)
            else:
                self.TalentStack = min(6, self.TalentStack+1)
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '단항긍지', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.TalentDMGBuff * self.TalentStack)]})
        
        if self.Eidolons >= 2:
            self.ChangeEnhanceStack(3)
            self.ChangeActionGauge(10000)
        else:
            self.ChangeEnhanceStack(2)
            
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    
    def BattleSkillIsPossible(self):
        if self.NAEnhance == 3:
            return False
        
        elif self.EnhanceStack > 0 :
            return True
        
        elif self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    
    def EndTurn(self):
        super().EndTurn()
        if any([Buff['설명'] in ('단항긍지') for Buff in self.BuffList]):
            raise ValueError
        else:
            self.TalentStack = 0
        

class DanHengIMTrace1:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    WeakList = Target[0].WeakList.copy()
                    for Debuff in Target[0].DebuffList:
                        if Debuff['디버프형태'] == '약점부여':
                            WeakList += Debuff['속성']
                    if '허수' in WeakList:
                        self.Object.TempBuffList.append(('치명타확률', 0.12))

class DanHengIMEidolon6:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터필살기발동시작':
            if Attacker in self.Object.Game.Characters and Attacker != self.Object:
                self.Object.Eidolon6Stack = min(3, self.Object.Eidolon6Stack+1)




            

            

        
