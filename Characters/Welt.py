import random
from Characters.BaseCharacter import BaseCharacter
import numpy as np

class Welt(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '웰트'
        self.Element = '허수'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적전체'}       

        # 기본
        self.BaseStat['기초HP'] += 1125
        self.BaseStat['기초공격력'] += 620.93
        self.BaseStat['기초방어력'] += 509.36
        self.BaseStat['기초속도'] += 102
        self.BaseStat['에너지최대치'] += 120  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['효과저항'] += 0.04 + 0.06
        self.BaseStat['공격력%증가'] += 0.06 + 0.06 + 0.04 + 0.08 + 0.04       
        self.BaseStat['허수속성피해증가'] += 0.048 + 0.032 + 0.064
        
        if self.Eidolons >= 3:
            self.SkillLevel[1] += 2
            self.SkillLevel[2] += 2
        if self.Eidolons >= 5:
            self.SkillLevel[3] += 2
            self.SkillLevel[0] += 1
        
        if self.Eidolons >= 1:
            self.Eidolons1Chance = 0

        
        self.NADMG = np.array([[0, 0.5, 0],
                                [0, 0.6, 0],
                                [0, 0.7, 0],
                                [0, 0.8, 0],
                                [0, 0.9, 0],
                                [0, 1.0, 0],
                                [0, 1.1, 0],
                                [0, 1.2, 0],
                                [0, 1.3, 0]])[self.SkillLevel[0]-1]
        
        self.BSkillDMG = np.array([[0, 0.36, 0],
                                    [0, 0.396, 0],
                                    [0, 0.432, 0],
                                    [0, 0.468, 0],
                                    [0, 0.504, 0],
                                    [0, 0.54, 0],
                                    [0, 0.585, 0],
                                    [0, 0.63, 0],
                                    [0, 0.675, 0],
                                    [0, 0.72, 0],
                                    [0, 0.756, 0],
                                    [0, 0.792, 0],
                                    [0, 0.828, 0],
                                    [0, 0.864, 0],
                                    [0, 0.9, 0],])[self.SkillLevel[1]-1]
        
        self.BSkillProb = np.array([0.65, 0.66, 0.67, 0.68, 0.68, 0.70, 0.7125, 0.725, 0.7375, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8])[self.SkillLevel[1]-1]
        if self.Eidolons >= 4: # 4돌
            self.BSkillProb += 0.35

        self.TalentDMG =  np.array([[0, 0.30, 0],
                                    [0, 0.33, 0],
                                    [0, 0.36, 0],
                                    [0, 0.39, 0],
                                    [0, 0.42, 0],
                                    [0, 0.45, 0],
                                    [0, 0.4875, 0],
                                    [0, 0.525, 0],
                                    [0, 0.5625, 0],
                                    [0, 0.60, 0],
                                    [0, 0.63, 0],
                                    [0, 0.66, 0],
                                    [0, 0.69, 0],
                                    [0, 0.72, 0],
                                    [0, 0.75, 0],])[self.SkillLevel[2]-1]
        
        self.UltimateDMG = np.array([[0, 0.90, 0],
                                    [0, 0.96, 0],
                                    [0, 1.02, 0],
                                    [0, 1.08, 0],
                                    [0, 1.14, 0],
                                    [0, 1.20, 0],
                                    [0, 1.275, 0],
                                    [0, 1.35, 0],
                                    [0, 1.425, 0],
                                    [0, 1.50, 0],
                                    [0, 1.56, 0],
                                    [0, 1.62, 0],
                                    [0, 1.68, 0],
                                    [0, 1.74, 0],
                                    [0, 1.80, 0],])[self.SkillLevel[3]-1]
        
        self.UltimateDecreaseAG  = np.array([-3200, -3280, 3360, -3440, -3520, -3600, -3700, -3800, -3900, -4000, -4080, -4160, -4240, -4320, -4400])[self.SkillLevel[3]-1]
    
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(WeltTalent(self))
        self.Game.TriggerList.append(WeltPunishment(self))

    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, 웰트 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = '웰트일반공격') # Multiplier[0] : HP계수, Multiplier[1] : 공격력계수, Multiplier[2] : 방어력계수
        if self.Eidolons >=1:
            if self.Eidolons1Chance >= 1:
                self.Eidolons1Chance -=1
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '추가피해', Toughness = 0, Multiplier = [multiplier * 0.5 for multiplier in self.NADMG], FlatDMG = 0, DamageName = '웰트1돌')
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)

    def BattleSkill(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, 웰트 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = '웰트전투스킬')
        self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = self.BSkillProb, Debuff = {'디버프형태' : '스탯', '설명' : '웰트전투스킬감속', '남은턴' : 2, '효과' : [('속도%증가', -0.1)]})
        if self.Eidolons >=1:
            if self.Eidolons1Chance >= 1:
                self.Eidolons1Chance -=1
                self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = '허수', DamageType = '추가피해', Toughness = 0, Multiplier = [multiplier * 0.5 for multiplier in self.BSkillDMG], FlatDMG = 0, DamageName = '웰트1돌')

        cnt = 2
        if self.Eidolons >= 6:
            cnt = 3
        for _ in range(cnt):
            if len(self.Game.Enemys) != 0: 
                rndtarget = random.choice(self.Game.Enemys)
                self.Game.ApplyDamage(Attacker = self, Target = rndtarget, Element = '허수', DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillDMG, FlatDMG = 0, DamageName = '웰트전투스킬')
                self.Game.ApplyDebuff(Attacker = self, Target = rndtarget, BaseProbability = self.BSkillProb, Debuff = {'디버프형태' : '스탯', '설명' : '웰트전투스킬감속', '남은턴' : 2, '효과' : [('속도%증가', -0.1)]})

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        self.CurrentEnergy = 0
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, 웰트 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)
        if self.Eidolons >= 1:
            self.Eidolons1Chance = 2
        self.EnergyGenerate(5, Flat = False)
        self.EnergyGenerate(10, Flat = False) # 심판
        for Enemy in self.Game.Enemys.copy():
            self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '웰트필살기취약', '남은턴' : 2, '효과': [('받는피해증가', 0.12)]}) # 징벌
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = '허수', DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = '웰트필살기')
            self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '속박', '설명' : '웰트스킬속박', '남은턴' : 1, '행동게이지증감' : self.UltimateDecreaseAG, '효과': [('속도%증가', -0.1)]})
            
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    
    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False
        else:
            raise ValueError

class WeltTalent:
    def __init__(self, Object):
        self.Object = Object
        self.Damage = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    for targetDebuff in Target[0].DebuffList:
                        if '감속' in targetDebuff['설명'] or '속박' in targetDebuff['설명']:
                            if Value[1] == '웰트일반공격' or Value[1] == '웰트전투스킬' or Value[1] == '웰트필살기':
                                self.Damage = True
        
        if Trigger == '데미지발동종료':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if self.Damage == True:
                        self.Damage = False
                        self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Target[0], Element = '허수', DamageType = '추가피해', Toughness = 0, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName='웰트특성', Except = self)
                        if self.Object.Eidolons >= 2: # 2돌
                            self.Object.EnergyGenerate(3, False)

class WeltPunishment: #판결
    def __init__(self, Object):
        self.Object = Object
        self.Buff = ('허수속성피해증가', 0.2)

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if Target[0].IsBroken == True:
                        self.Object.TempBuffList.append(self.Buff)
            
            

            

        
