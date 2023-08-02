from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Serval(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '서벌'
        self.Element = '번개'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 917
        self.BaseStat['기초공격력'] += 653
        self.BaseStat['기초방어력'] += 375
        self.BaseStat['기초속도'] += 104
        self.BaseStat['에너지최대치'] += 100  
        self.BaseStat['기초도발'] += 75
        # 추가
        self.BaseStat['치명타확률'] += 0.053 + 0.027 + 0.027 + 0.04 + 0.04
        self.BaseStat['효과명중'] += 0.06 + 0.04 + 0.08
        self.BaseStat['효과저항'] += 0.04 + 0.06
        
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
                    
        self.BSkillMainDMG = np.array([[0, 0.7, 0],
                                        [0, 0.77, 0],
                                        [0, 0.94, 0],
                                        [0, 0.91, 0],
                                        [0, 0.98, 0],
                                        [0, 1.05, 0],
                                        [0, 1.1375, 0],
                                        [0, 1.225, 0],
                                        [0, 1.3125, 0],
                                        [0, 1.4, 0],
                                        [0, 1.47, 0],
                                        [0, 1.54, 0],
                                        [0, 1.61, 0],
                                        [0, 1.68, 0],
                                        [0, 1.75, 0],])[self.SkillLevel[1]-1]
        
        self.BSkillSubDMG = np.array([[0, 0.3, 0],
                                        [0, 0.33, 0],
                                        [0, 0.36, 0],
                                        [0, 0.39, 0],
                                        [0, 0.42, 0],
                                        [0, 0.45, 0],
                                        [0, 0.4875, 0],
                                        [0, 0.525, 0],
                                        [0, 0.5625, 0],
                                        [0, 0.6, 0],
                                        [0, 0.63, 0],
                                        [0, 0.66, 0],
                                        [0, 0.69, 0],
                                        [0, 0.72, 0],
                                        [0, 0.75, 0],])[self.SkillLevel[1]-1]
        
        self.BSkillShockDMG = np.array([[0, 0.4, 0],
                                        [0, 0.44, 0],
                                        [0, 0.48, 0],
                                        [0, 0.52, 0],
                                        [0, 0.56, 0],
                                        [0, 0.62, 0],
                                        [0, 0.7, 0],
                                        [0, 0.8, 0],
                                        [0, 0.92, 0],
                                        [0, 1.04, 0],
                                        [0, 1.092, 0],
                                        [0, 1.144, 0],
                                        [0, 1.196, 0],
                                        [0, 1.248, 0],
                                        [0, 1.3, 0],])[self.SkillLevel[1]-1]

        self.TalentDMG = np.array([[0, 0.36, 0],
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
                                    [0, 0.9, 0],])[self.SkillLevel[2]-1]
        
        self.UltimateDMG = np.array([[0, 1.08, 0],
                                    [0, 1.152, 0],
                                    [0, 1.224, 0],
                                    [0, 1.296, 0],
                                    [0, 1.368, 0],
                                    [0, 1.44, 0],
                                    [0, 1.53, 0],
                                    [0, 1.62, 0],
                                    [0, 1.71, 0],
                                    [0, 1.8, 0],
                                    [0, 1.872, 0],
                                    [0, 1.944, 0],
                                    [0, 2.016, 0],
                                    [0, 2.088, 0],
                                    [0, 2.16, 0],])[self.SkillLevel[3]-1]
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(ServalManiaPlusEidolon6(self))

    def Init(self):
        super().Init()
        self.EnergyGenerate(15, True)
    

    def NormalAttack(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)
        self.EnergyGenerate(20, Flat = False)
        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
        
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격') 
        
        if self.Eidolons >= 1:
            for NeighboringTarget in NeighboringTargets:
                self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}1돌확산공격', Multiple = 0.6)
        
        check = False
        for Enemy in self.Game.Enemys.copy():
            if any([debuff['디버프형태'] == '감전' for debuff in Enemy.DebuffList]):
                self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '추가피해', Toughness = 0, Multiplier = self.TalentDMG, FlatDMG = 0, DamageName = f'{self.Name}특성추가피해') 
                check = True
        if check == True:
            if self.Eidolons >= 2:
                self.EnergyGenerate(4, False)

        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)



    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False)

        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillMainDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬메인공격')
        self.Game.ApplyDebuff(Attacker = self, Target = target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Name}스킬감전'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 2, '계수' : self.BSkillShockDMG})
        
        for NeighboringTarget in NeighboringTargets:
            self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillSubDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬확산공격')
            self.Game.ApplyDebuff(Attacker = self, Target = NeighboringTarget, BaseProbability = 1.0, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Name}스킬감전'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 2, '계수' : self.BSkillShockDMG})
        
        check = False
        for Enemy in self.Game.Enemys.copy():
            if any([debuff['디버프형태'] == '감전' for debuff in Enemy.DebuffList]):
                self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '추가피해', Toughness = 0, Multiplier = self.TalentDMG, FlatDMG = 0, DamageName = f'{self.Name}특성추가피해') 
                check = True
        if check == True:
            if self.Eidolons >= 2:
                self.EnergyGenerate(4, False)

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        for Enemy in self.Game.Enemys.copy(): # 중간에 적이 사망하면 for loop에 오류생김
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기')
            shocked = False
            for debuff in Enemy.DebuffList:
                if debuff['디버프형태'] == '감전':
                    debuff['남은턴'] += 2
                    shocked = True
            if shocked == False:
                if self.Eidolons >= 4:
                    self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Name}스킬감전'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 2, '계수' : self.BSkillShockDMG})
        
        
        check = False
        for Enemy in self.Game.Enemys.copy():
            if any([debuff['디버프형태'] == '감전' for debuff in Enemy.DebuffList]):
                self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '추가피해', Toughness = 0, Multiplier = self.TalentDMG, FlatDMG = 0, DamageName = f'{self.Name}특성추가피해') 
                check = True
        if check == True:
            if self.Eidolons >= 2:
                self.EnergyGenerate(4, False)

        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError

class ServalManiaPlusEidolon6:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('적사망', '적전원사망'):
             self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '서벌열광공증', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('공격력%증가', 0.2)]}, Except = self)

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Object.Eidolons >= 6:
                    if Attacker == self.Object:
                        if any([debuff['디버프형태']=='감전' for debuff in Target[0].DebuffList]):
                            self.Object.TempBuffList.append(('모든피해증가', 0.3))