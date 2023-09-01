from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Jingliu(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        print('\n\n주의 : 경류는 테섭 기준으로 작성되었음 (V1) \n\n')
        self.Name = '경류'
        self.Element = '얼음'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적지정'} 

        # 기본
        self.BaseStat['기초HP'] += 1358
        self.BaseStat['기초공격력'] += 679
        self.BaseStat['기초방어력'] += 388
        self.BaseStat['기초속도'] += 100
        self.BaseStat['에너지최대치'] += 140  
        self.BaseStat['기초도발'] += 125
        # 추가
        self.BaseStat['HP%증가'] += 0.04 + 0.06
        self.BaseStat['치명타확률'] += 0.04 + 0.027 + 0.053
        self.BaseStat['얼음속성피해증가'] += 0.032 + 0.048 + 0.048 + 0.032 + 0.064

        if self.Eidolons >= 2:
            self.BaseStat['필살기피해증가'] += 0.3

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
        

        
        self.BSkillDMG = np.array([[0, 1.0, 0],
                                   [0, 1.1, 0],
                                   [0, 1.2, 0],
                                   [0, 1.3, 0],
                                   [0, 1.4, 0],
                                   [0, 1.5, 0],
                                   [0, 1.625, 0],
                                   [0, 1.75, 0],
                                   [0, 1.875, 0],
                                   [0, 2.0, 0],
                                   [0, 2.1, 0],
                                   [0, 2.2, 0],
                                   [0, 2.3, 0],
                                   [0, 2.4, 0],
                                   [0, 2.5, 0],])[self.SkillLevel[1]-1]
        
        self.BSkillEnhanceMainDMG = np.array([[0, 1.2, 0],
                                            [0, 1.32, 0],
                                            [0, 1.44, 0],
                                            [0, 1.56, 0],
                                            [0, 1.68, 0],
                                            [0, 1.8, 0],
                                            [0, 1.95, 0],
                                            [0, 2.1, 0],
                                            [0, 2.25, 0],
                                            [0, 2.4, 0],
                                            [0, 2.52, 0],
                                            [0, 2.64, 0],
                                            [0, 2.76, 0],
                                            [0, 2.88, 0],
                                            [0, 3.0, 0],])[self.SkillLevel[1]-1]
        
        self.BSkillEnhanceSubDMG = np.array([[0, 0.6, 0],
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
                    
        
        self.TalentMaxATK =  np.array([0.6, 0.66, 0.72, 0.78, 0.84, 0.9, 0.975, 1.05, 1.125, 1.2, 1.26, 1.32, 1.38, 1.44, 1.5])[self.SkillLevel[2]-1]
        
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
        
        self.UltimateSubDMG = np.array([[0, 0.9, 0],
                                        [0, 0.96, 0],
                                        [0, 1.02, 0],
                                        [0, 1.08, 0],
                                        [0, 1.14, 0],
                                        [0, 1.2, 0],
                                        [0, 1.275, 0],
                                        [0, 1.35, 0],
                                        [0, 1.425, 0],
                                        [0, 1.5, 0],
                                        [0, 1.56, 0],
                                        [0, 1.62, 0],
                                        [0, 1.68, 0],
                                        [0, 1.74, 0],
                                        [0, 1.8, 0],])[self.SkillLevel[3]-1]
        
        self.TalentStack = 0
        self.Enhance = False
        self.ExtraTurn = False
        self.SaveTurnStep = None
        self.SaveTurnObject = None
    
    def ChangeTalentStack(self, stack):
        beforeStack = self.TalentStack
        self.TalentStack += stack
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 경류 삭망 스택 {stack} 변화, 이전 : {beforeStack}, 현재 : {self.TalentStack}")
        if self.Enhance == False and self.TalentStack == 2:
            self.Enhance = True
            self.ExtraTurn = True
            self.SaveTurnStep = self.Game.TurnStep
            self.SaveTurnObject = self.Game.TurnObject
            self.Game.TurnStep = '행동선택' 
            self.Game.TurnObject = self
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, \n경류 전백 상태 돌입, 추가턴")
            if self.Eidolons >= 6:
                self.ChangeTalentStack(1)
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '경류전백', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('효과저항', 0.35), ('속도%증가', 0.1)]})
        if self.TalentStack == 0:
            self.Enhance = False
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, \n경류 전백 상태 종료")
            for Buff in self.BuffList.copy():
                if Buff['설명'] == '경류전백':
                    self.DeleteBuff(Buff)
    
    def ConsumeCharacterHP(self):
        TotalConsumedHP = 0
        for Character in self.Game.Characters:
            if Character != self:
                if self.Eidolons >= 4:
                    ConsumedHP = Character.ConsumesHP(self, 0.1, 0)
                else:
                    ConsumedHP = Character.ConsumesHP(self, 0.06, 0)
                TotalConsumedHP += ConsumedHP

        if self.Eidolons >= 4:
            ATKIncrease = min(TotalConsumedHP * 2.5, self.CurrentStat['기초공격력'] * (self.TalentMaxATK+0.4))
        else:
            ATKIncrease = min(TotalConsumedHP * 2.5, self.CurrentStat['기초공격력'] * self.TalentMaxATK)

        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, 경류 공격력 {ATKIncrease} 증가")
        return ATKIncrease


    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)
        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')

        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)


    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        if self.Enhance == False:
            self.Game.ChangeSkillPoint(-1)
            self.EnergyGenerate(30, Flat = False)
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}일반전투스킬')
            
            self.ChangeTalentStack(1)

            self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
            self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

        elif self.Enhance == True:
            self.EnergyGenerate(20, Flat = False)
            NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])

            if self.Eidolons >= 1:
                self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '경류1돌', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('치명타확률', 0.12)]})

            ATKIncrease = self.ConsumeCharacterHP()

            TempBuff = [('고정공격력증가', ATKIncrease), ('모든피해증가', 0.1)]
            if self.Eidolons >= 6:
                TempBuff = [('고정공격력증가', ATKIncrease), ('모든피해증가', 0.1), ('치명타피해', 0.5)]

            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillEnhanceMainDMG, FlatDMG = 0, DamageName = f'{self.Name}강화전투스킬메인', AttackerTempBuff = TempBuff)
            for NeighboringTarget in NeighboringTargets:
                self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillEnhanceSubDMG, FlatDMG = 0, DamageName = f'{self.Name}강화전투스킬확산', AttackerTempBuff = TempBuff)

            if self.Eidolons >= 1 and len(NeighboringTargets) == 0:
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillEnhanceSubDMG, FlatDMG = 0, DamageName = f'{self.Name}1돌강화전투스킬확산', AttackerTempBuff = TempBuff, Multiple=0.6)
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillEnhanceSubDMG, FlatDMG = 0, DamageName = f'{self.Name}1돌강화전투스킬확산', AttackerTempBuff = TempBuff, Multiple=0.6)

            if self.ExtraTurn == True:
                self.Game.TurnStep = self.SaveTurnStep
                self.Game.TurnObject = self.SaveTurnObject
                self.ExtraTurn = False
                self.SaveTurnStep = None
                self.SaveTurnObject = None

            self.ChangeTalentStack(-1)

            self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
            self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

        else:
            raise ValueError


    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, , 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])

        if self.Eidolons >= 1:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명' : '경류1돌', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [('치명타확률', 0.12)]})

        ATKIncrease = self.ConsumeCharacterHP()

        TempBuff = [('고정공격력증가', ATKIncrease), ('모든피해증가', 0.1)]
        if self.Eidolons >= 6:
            TempBuff = [('고정공격력증가', ATKIncrease), ('모든피해증가', 0.1), ('치명타피해', 0.5)]

        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateMainDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기메인공격', AttackerTempBuff = TempBuff)
        for NeighboringTarget in NeighboringTargets:
            self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateSubDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기확산공격', AttackerTempBuff = TempBuff)

        if self.Eidolons >= 1 and len(NeighboringTargets) == 0:
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateSubDMG, FlatDMG = 0, DamageName = f'{self.Name}1돌필살기확산공격', AttackerTempBuff = TempBuff, Multiple = 0.6)
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateSubDMG, FlatDMG = 0, DamageName = f'{self.Name}1돌필살기확산공격', AttackerTempBuff = TempBuff, Multiple = 0.6)
            
        self.ChangeTalentStack(1)
        
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            if self.Enhance == True:
                return True
            else:
                return False
        else:
            raise ValueError
    
    def NAIsPossible(self):
        if self.Enhance == True:
            return False
        else:
            return True

    def EndTurn2(self):
        super().EndTurn2()
        self.ExtraTurn = False
        self.SaveTurnStep = None
        self.SaveTurnObject = None

