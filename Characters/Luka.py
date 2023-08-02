from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Luka(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '루카'
        self.Element = '물리'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적지정'} 

        # 기본
        self.BaseStat['기초HP'] += 917
        self.BaseStat['기초공격력'] += 582
        self.BaseStat['기초방어력'] += 485
        self.BaseStat['기초속도'] += 103
        self.BaseStat['에너지최대치'] += 130  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.06 + 0.06 + 0.04
        self.BaseStat['방어력%증가'] += 0.05 + 0.075
        self.BaseStat['효과명중'] += 0.04 + 0.06 + 0.08

        self.FightingWill = 1

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
        
        self.EnhancedNASubDMG = np.array([[0, 0.1, 0],
                                            [0, 0.12, 0],
                                            [0, 0.14, 0],
                                            [0, 0.16, 0],
                                            [0, 0.18, 0],
                                            [0, 0.2, 0],
                                            [0, 0.22, 0],
                                            [0, 0.24, 0],
                                            [0, 0.26, 0]])[self.SkillLevel[0]-1]
        
        self.EnhancedNAMainDMG = np.array([[0, 0.4, 0],
                                            [0, 0.48, 0],
                                            [0, 0.56, 0],
                                            [0, 0.64, 0],
                                            [0, 0.72, 0],
                                            [0, 0.8, 0],
                                            [0, 0.88, 0],
                                            [0, 0.96, 0],
                                            [0, 1.04, 0]])[self.SkillLevel[0]-1]
 
        self.BSkillDMG =  np.array([[0, 0.6, 0],
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
        
        self.BSkillMaxDebuffDMG = np.array([[0, 1.3, 0],
                                            [0, 1.43, 0],
                                            [0, 1.56, 0],
                                            [0, 1.69, 0],
                                            [0, 1.82, 0],
                                            [0, 2.015, 0],
                                            [0, 2.275, 0],
                                            [0, 2.6, 0],
                                            [0, 2.99, 0],
                                            [0, 3.38, 0],
                                            [0, 3.549, 0],
                                            [0, 3.718, 0],
                                            [0, 3.887, 0],
                                            [0, 4.056, 0],
                                            [0, 4.225, 0]])[self.SkillLevel[1]-1]
        
        self.TalentMultiple =  np.array([0.68, 0.697, 0.714, 0.731, 0.748, 0.765, 0.78625, 0.8075, 0.82875, 0.85, 0.867, 0.884, 0.901, 0.918, 0.935])[self.SkillLevel[2]-1]
        
        self.UltimateDebuff = np.array([0.12, 0.128, 0.136, 0.144, 0.152, 0.16, 0.17, 0.18, 0.19, 0.2, 0.208, 0.216, 0.224, 0.232, 0.24])[self.SkillLevel[3]-1]
        self.UltimateDMG = np.array([[0, 1.98, 0],
                                    [0, 2.112, 0],
                                    [0, 2.244, 0],
                                    [0, 2.376, 0],
                                    [0, 2.508, 0],
                                    [0, 2.64, 0],
                                    [0, 2.805, 0],
                                    [0, 2.97, 0],
                                    [0, 3.135, 0],
                                    [0, 3.3, 0],
                                    [0, 3.342, 0],
                                    [0, 3.564, 0],
                                    [0, 3.696, 0],
                                    [0, 3.828, 0],
                                    [0, 3.96, 0],])[self.SkillLevel[3]-1]

    def ChangeFightingWill(self, stack):
        self.FightingWill += stack
        if self.FightingWill > 4:
            self.FightingWill = 4
        if stack > 0:
            self.EnergyGenerate(3, False)
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 루카 투지 {stack} 변화, 현재 투지 : {self.FightingWill}")
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        if self.Eidolons >= 1:
            self.Game.TriggerList.append(LukaEidolon1(self))
        if self.Eidolons >= 4:
            self.Game.TriggerList.append(LukaEidolon4(self))

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)

        if self.FightingWill < 2:
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')
            self.ChangeFightingWill(1)
        else:
            self.ChangeFightingWill(-2)
            for i in range(3):
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 0, Multiplier = self.EnhancedNASubDMG, FlatDMG = 0, DamageName = f'{self.Name}강화일반공격')
                if self.Eidolons >= 6:
                    for debuff in target[0].DebuffList:
                        if debuff['디버프형태'] == '열상':
                            self.Game.ApplyDoTDamage(target[0], debuff, Multiple = 0.08)

                if random.random() < 0.5:
                    self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 0, Multiplier = self.EnhancedNASubDMG, FlatDMG = 0, DamageName = f'{self.Name}강화일반공격')
                    if self.Eidolons >= 6:
                        for debuff in target[0].DebuffList:
                            if debuff['디버프형태'] == '열상':
                                self.Game.ApplyDoTDamage(target[0], debuff, Multiple = 0.08)
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 60, Multiplier = self.EnhancedNAMainDMG, FlatDMG = 0, DamageName = f'{self.Name}강화일반공격')
            
            for debuff in target[0].DebuffList:
                if debuff['디버프형태'] == '열상':
                    self.Game.ApplyDoTDamage(target[0], debuff, Multiple = self.TalentMultiple)

        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)


    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False)

        self.ChangeFightingWill(1)
        if len(target[0].BuffList) > 0:
            target[0].BuffList.remove(random.choice(target[0].BuffList))
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')
        self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '열상', '설명' : '루카스킬열상'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 3, '계수' : 0.24, '최대치계수' : self.BSkillMaxDebuffDMG})

        if self.Eidolons >= 2:
            WeakList = target[0].WeakList.copy()
            for Debuff in target[0].DebuffList:
                if Debuff['디버프형태'] == '약점부여':
                    WeakList += Debuff['속성']
            if '물리' in WeakList:
                self.ChangeFightingWill(1)       
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, , 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        self.ChangeFightingWill(2)
        self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '루카궁받피증', '남은턴' : 3, '효과' : [('받는피해증가', self.UltimateDebuff)]})
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '필살기', Toughness = 90, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기')

        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError


class LukaEidolon1:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if any([debuff['디버프형태']=='열상' for debuff in Target[0].DebuffList]):
                        self.Object.TempBuffList.append(('모든피해증가', 0.15))

class LukaEidolon4:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작', '힐발동시작' , '버프발동시작', '디버프발동시작'):
            if Attacker == self.Object:
                self.Object.TempBuffList.append(('공격력%증가', self.Object.FightingWill * 0.05))