from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Sampo(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '삼포'
        self.Element = '바람'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 1023
        self.BaseStat['기초공격력'] += 617
        self.BaseStat['기초방어력'] += 397
        self.BaseStat['기초속도'] += 102
        self.BaseStat['에너지최대치'] += 120  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.06 + 0.06 + 0.04
        self.BaseStat['효과저항'] += 0.04 + 0.06
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
 
        self.BSkillDMG =  np.array([[0, 0.28, 0],
                                    [0, 0.308, 0],
                                    [0, 0.336, 0],
                                    [0, 0.364, 0],
                                    [0, 0.392, 0],
                                    [0, 0.42, 0],
                                    [0, 0.455, 0],
                                    [0, 0.49, 0],
                                    [0, 0.525, 0],
                                    [0, 0.56, 0],
                                    [0, 0.588, 0],
                                    [0, 0.616, 0],
                                    [0, 0.644, 0],
                                    [0, 0.672, 0],
                                    [0, 0.7, 0],])[self.SkillLevel[1]-1]
        
        self.TalentDMG =  np.array([[0, 0.2, 0],
                                    [0, 0.22, 0],
                                    [0, 0.24, 0],
                                    [0, 0.26, 0],
                                    [0, 0.28, 0],
                                    [0, 0.31, 0],
                                    [0, 0.35, 0],
                                    [0, 0.4, 0],
                                    [0, 0.46, 0],
                                    [0, 0.52, 0],
                                    [0, 0.546, 0],
                                    [0, 0.572, 0],
                                    [0, 0.598, 0],
                                    [0, 0.624, 0],
                                    [0, 0.65, 0],])[self.SkillLevel[2]-1]
        
        self.TalentDMGEidolon6 =  np.array([[0, 0.2+0.15, 0],
                                            [0, 0.22+0.15, 0],
                                            [0, 0.24+0.15, 0],
                                            [0, 0.26+0.15, 0],
                                            [0, 0.28+0.15, 0],
                                            [0, 0.31+0.15, 0],
                                            [0, 0.35+0.15, 0],
                                            [0, 0.4+0.15, 0],
                                            [0, 0.46+0.15, 0],
                                            [0, 0.52+0.15, 0],
                                            [0, 0.546+0.15, 0],
                                            [0, 0.572+0.15, 0],
                                            [0, 0.598+0.15, 0],
                                            [0, 0.624+0.15, 0],
                                            [0, 0.65+0.15, 0],])[self.SkillLevel[2]-1]
        
        self.UltimateDebuff = np.array([0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.2625, 0.275, 0.2825, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35])[self.SkillLevel[3]-1]
        self.UltimateDMG = np.array([[0, 0.96, 0],
                                    [0, 1.024, 0],
                                    [0, 1.088, 0],
                                    [0, 1.152, 0],
                                    [0, 1.216, 0],
                                    [0, 1.28, 0],
                                    [0, 1.36, 0],
                                    [0, 1.44, 0],
                                    [0, 1.52, 0],
                                    [0, 1.6, 0],
                                    [0, 1.664, 0],
                                    [0, 1.728, 0],
                                    [0, 1.792, 0],
                                    [0, 1.856, 0],
                                    [0, 1.92, 0],])[self.SkillLevel[3]-1]

       
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(SampoSpiceUP(self))
        if self.Eidolons >= 2:
            self.Game.TriggerList.append(SampoEidolon2(self))

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        for i in range(3):
            self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 10, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격', Multiple = 1/3)

            # 특성
            if self.Eidolons >= 6:
                self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMGEidolon6})
            else:
                self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMG})
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)


    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)
        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(6, Flat=False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')

        if self.Eidolons >= 4:
            check = False
            for Debuff in target[0].DebuffList:
                if Debuff['디버프형태'] == '풍화':
                    if Debuff['중첩'] >= 5:
                        check = True
            if check == True:
                for debuff in target[0].DebuffList:
                    if debuff['디버프형태'] == '풍화':
                        self.Game.ApplyDoTDamage(target[0], debuff, Multiple = 0.08)

        if self.Eidolons >= 6:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMGEidolon6})
        else:
            self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMG})

        cnt = 4
        if self.Eidolons >= 1:
            cnt = 5
        for _ in range(cnt):
            if len(self.Game.Enemys) != 0: 
                rndtarget = random.choice(self.Game.Enemys)
                self.EnergyGenerate(6, Flat=False)
                self.Game.ApplyDamage(Attacker = self, Target = rndtarget, Element = self.Element, DamageType = '전투스킬', Toughness = 15, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬')

                if self.Eidolons >= 4:
                    check = False
                    for Debuff in rndtarget.DebuffList:
                        if Debuff['디버프형태'] == '풍화':
                            if Debuff['중첩'] >= 5:
                                check = True
                    if check == True:
                        for debuff in rndtarget.DebuffList:
                            if debuff['디버프형태'] == '풍화':
                                self.Game.ApplyDoTDamage(rndtarget, debuff, Multiple = 0.08)

                if self.Eidolons >= 6:
                    self.Game.ApplyDebuff(Attacker = self, Target = rndtarget, BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMGEidolon6})
                else:
                    self.Game.ApplyDebuff(Attacker = self, Target = rndtarget, BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMG})
                
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, , 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        self.EnergyGenerate(10, Flat = False)

        for Enemy in self.Game.Enemys.copy():
            for i in range(4):
                self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 15, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기', Multiple=1/4)
                if self.Eidolons >= 6:
                    self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMGEidolon6})
                else:
                    self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 0.65, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.TalentDMG})
            self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '삼포궁받지피증', '남은턴' : 2, '효과': [('받는지속피해증가', self.UltimateDebuff)]})
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError


class SampoSpiceUP:
    def __init__(self, Object):
        self.Object = Object
        self.start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Object in Target:
                    if any([Debuff['디버프형태']=='풍화' for Debuff in Attacker.DebuffList]):
                        self.Object.TempBuffList.append(('받는피해증가', -0.15))

class SampoEidolon2:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '적사망' or Trigger == '적전원사망':
            if any([debuff['디버프형태']=='풍화' for debuff in Target[0].DebuffList]):
                for Enemy in self.Object.Game.Enemys:
                    if self.Object.Eidolons >= 6:
                        self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self.Object, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.Object.TalentDMGEidolon6}, Except = self)
                    else:
                        self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '풍화', '설명' : '삼포스킬풍화', '공격자' : self.Object, '발동타입' : '스킬', '남은턴' : 4, '중첩' : 1, '계수' : self.Object.TalentDMG}, Except = self)
