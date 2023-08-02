from Characters.BaseCharacter import BaseCharacter
import numpy as np

class Kafka(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '카프카'
        self.Element = '번개'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '적지정', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 1087
        self.BaseStat['기초공격력'] += 679
        self.BaseStat['기초방어력'] += 485
        self.BaseStat['기초속도'] += 100
        self.BaseStat['에너지최대치'] += 120  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.06 + 0.06 + 0.04
        self.BaseStat['효과명중'] += 0.06 + 0.04 + 0.08
        self.BaseStat['HP%증가'] += 0.04 + 0.06

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
        
        self.BSkillMultiple = np.array([0.6, 0.615, 0.63, 0.645, 0.66, 0.675, 0.69375, 0.7125, 0.73125, 0.75, 0.765, 0.78, 0.795, 0.81, 0.825])[self.SkillLevel[1]-1]
        self.BSkillMainDMG =  np.array([[0, 0.8, 0],
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
                                        [0, 2.0, 0],])[self.SkillLevel[1]-1]
        self.BSkillSubDMG =  np.array([[0, 0.3, 0],
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
                
        self.TalentDMG = np.array([[0, 0.42, 0],
                                    [0, 0.518, 0],
                                    [0, 0.616, 0],
                                    [0, 0.714, 0],
                                    [0, 0.812, 0],
                                    [0, 0.91, 0],
                                    [0, 1.0325, 0],
                                    [0, 1.155, 0],
                                    [0, 1.2775, 0],
                                    [0, 1.4, 0],
                                    [0, 1.498, 0],
                                    [0, 1.596, 0],
                                    [0, 1.694, 0],
                                    [0, 1.792, 0],
                                    [0, 1.89, 0],])[self.SkillLevel[2]-1]

        self.UltimateDMG = np.array([[0, 0.48, 0],
                                    [0, 0.512, 0],
                                    [0, 0.544, 0],
                                    [0, 0.576, 0],
                                    [0, 0.608, 0],
                                    [0, 0.64, 0],
                                    [0, 0.68, 0],
                                    [0, 0.72, 0],
                                    [0, 0.76, 0],
                                    [0, 0.8, 0],
                                    [0, 0.832, 0],
                                    [0, 0.864, 0],
                                    [0, 0.896, 0],
                                    [0, 0.928, 0],
                                    [0, 0.96, 0],])[self.SkillLevel[3]-1]
        self.UltimateMultiple = np.array([0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.925, 0.95, 0.875, 1, 1.02, 1.04, 1.06, 1.08, 1.1])[self.SkillLevel[3]-1]
        self.UltimateShock = np.array([[0, 1.16, 0],
                                        [0, 1.26875, 0],
                                        [0, 1.3775, 0],
                                        [0, 1.48625, 0],
                                        [0, 1.595, 0],
                                        [0, 1.758125, 0],
                                        [0, 1.975625, 0],
                                        [0, 2.2475, 0],
                                        [0, 2.57375, 0],
                                        [0, 2.9, 0],
                                        [0, 3.041375, 0],
                                        [0, 3.18275, 0],
                                        [0, 3.324125, 0],
                                        [0, 3.4655, 0],
                                        [0, 3.606875, 0],])[self.SkillLevel[3]-1]
        self.UltimateShockEidolon6 = np.array([[0, 1.16 + 1.56, 0],
                                                [0, 1.26875 + 1.56, 0],
                                                [0, 1.3775 + 1.56, 0],
                                                [0, 1.48625 + 1.56, 0],
                                                [0, 1.595 + 1.56, 0],
                                                [0, 1.758125 + 1.56, 0],
                                                [0, 1.975625 + 1.56, 0],
                                                [0, 2.2475 + 1.56, 0],
                                                [0, 2.57375 + 1.56, 0],
                                                [0, 2.9 + 1.56, 0],
                                                [0, 3.041375 + 1.56, 0],
                                                [0, 3.18275 + 1.56, 0],
                                                [0, 3.324125 + 1.56, 0],
                                                [0, 3.4655 + 1.56, 0],
                                                [0, 3.606875 + 1.56, 0],])[self.SkillLevel[3]-1]
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(KafakaTalent(self))
        self.Game.TriggerList.append(KafkaPlunderPlusEidolon24(self))

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
        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False)

        NeighboringTargets = self.Game.GetNeighboringEnemy(target[0])
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '전투스킬', Toughness = 60, Multiplier = self.BSkillMainDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬메인공격')
        for debuff in target[0].DebuffList:
            if debuff['디버프형태'] == '열상' or debuff['디버프형태'] == '풍화' or debuff['디버프형태'] == '감전' or debuff['디버프형태'] == '연소' :
                self.Game.ApplyDoTDamage(target[0], debuff, Multiple = self.BSkillMultiple)
        
        for NeighboringTarget in NeighboringTargets:
            self.Game.ApplyDamage(Attacker = self, Target = NeighboringTarget, Element = self.Element, DamageType = '전투스킬', Toughness = 30, Multiplier = self.BSkillSubDMG, FlatDMG = 0, DamageName = f'{self.Name}전투스킬확산공격')
       
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)

        for Enemy in self.Game.Enemys.copy():
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기공격')
            if self.Eidolons >= 6:
                self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.3, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Name}스킬감전'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 3, '계수' : self.UltimateShockEidolon6} )
            else:
                self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.3, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Name}스킬감전'  , '공격자' : self, '발동타입' : '스킬', '남은턴' : 2, '계수' : self.UltimateShock} )
            for debuff in Enemy.DebuffList:
                if debuff['디버프형태'] == '열상' or debuff['디버프형태'] == '풍화' or debuff['디버프형태'] == '감전' or debuff['디버프형태'] == '연소' :
                    self.Game.ApplyDoTDamage(Enemy, debuff, Multiple = self.UltimateMultiple)
        
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError

class KafakaTalent:
    def __init__(self, Object):
        self.Object = Object
        self.Possible = True
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object:
                self.Possible = True
        
        if Trigger == '캐릭터일반공격발동종료2':
            if Attacker in self.Object.Game.Characters and Attacker != self.Object:
                if self.Possible == True:
                    self.Possible = False
                    self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, 카프카 추가공격 시작")
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동시작', self.Object, Target, None, Except = self)
                    self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Target[0], Element = self.Object.Element, DamageType = '추가공격', Toughness = 30, Multiplier = self.Object.TalentDMG, FlatDMG = 0, DamageName = f'{self.Object.Name}특성추가공격', Except = self)
                    if self.Object.Eidolons >=1 :
                        self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' :  f'{self.Object.Name}1돌지속피해받피증', '남은턴' : 2, '효과' : [('받는지속피해증가', 0.3)]}, Except = self)         
                    if self.Object.Eidolons >= 6:
                        self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 1.3, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Object.Name}스킬감전'  , '공격자' : self.Object, '발동타입' : '스킬', '남은턴' : 3, '계수' : self.Object.UltimateShockEidolon6}, Except = self)
                    else:
                        self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 1.3, Debuff = {'디버프형태' : '감전', '설명' :  f'{self.Object.Name}스킬감전'  , '공격자' : self.Object, '발동타입' : '스킬', '남은턴' : 2, '계수' : self.Object.UltimateShock}, Except = self)
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료', self.Object, Target, None, Except = self)
                    self.Object.Game.ActiveTrigger('캐릭터추가공격발동종료2', self.Object, Target, None, Except = self)

class KafkaPlunderPlusEidolon24:
    def __init__(self, Object):
        self.Object = Object
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '도트데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Object.Eidolons >= 2:
                    if Attacker in self.Object.Game.Characters:
                        Attacker.TempBuffList.append(('지속피해피해증가', 0.25))
                if Value[0] == '감전':
                    if self.Object.Eidolons >= 4:
                        if Attacker == self.Object:
                            self.Object.EnergyGenerate(2, False)
        
        if Trigger in('적사망', '적전원사망'):
            if any([Debuff['디버프형태'] == '감전' for Debuff in Target[0].DebuffList]):
                self.Object.EnergyGenerate(5, False)