from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Bailu(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '백로'
        self.Element = '번개'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '아군지정', '필살기' : '아군전체'} 

        # 기본
        self.BaseStat['기초HP'] += 1319
        self.BaseStat['기초공격력'] += 567.72
        self.BaseStat['기초방어력'] += 485.1
        self.BaseStat['기초속도'] += 98
        self.BaseStat['에너지최대치'] += 100  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['효과저항'] += 0.04 + 0.06
        self.BaseStat['HP%증가'] += 0.04 + 0.08 + 0.04 + 0.06 + 0.06
        self.BaseStat['방어력%증가'] += 0.05 + 0.075 + 0.1
        
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
        
        self.BSkillHeal = np.array([[0.078, 0, 0],
                                    [0.082875, 0, 0],
                                    [0.08775, 0, 0],
                                    [0.092626, 0, 0],
                                    [0.09575, 0, 0],
                                    [0.1014, 0, 0],
                                    [0.1053, 0, 0],
                                    [0.1092, 0, 0],
                                    [0.1131, 0, 0],
                                    [0.117, 0, 0],
                                    [0.1209, 0, 0],
                                    [0.1248, 0, 0],
                                    [0.1287, 0, 0],
                                    [0.1326, 0, 0],
                                    [0.1365, 0, 0],])[self.SkillLevel[1]-1]
        self.BSkillFlatHeal = np.array([78, 124.8, 159.9, 195, 218.4, 241.8, 259.35, 276.9, 294.45, 312, 329.55, 347.1, 364.65, 382.2, 399.75])[self.SkillLevel[1]-1]

        self.TalentHeal = np.array([[0.036, 0, 0],
                                    [0.03825, 0, 0],
                                    [0.0405, 0, 0],
                                    [0.04275, 0, 0],
                                    [0.045, 0, 0],
                                    [0.0468, 0, 0],
                                    [0.0486, 0, 0],
                                    [0.0504, 0, 0],
                                    [0.0522, 0, 0],
                                    [0.054, 0, 0],
                                    [0.0558, 0, 0],
                                    [0.0576, 0, 0],
                                    [0.0594, 0, 0],
                                    [0.0612, 0, 0],
                                    [0.063, 0, 0],])[self.SkillLevel[2]-1]
        self.TalentFlatHeal = np.array([36, 57.6, 73.8, 90, 100.8, 111.6, 119.7, 127.8, 135.9, 144, 152.1, 160.2, 168.3, 176.4, 184.5])[self.SkillLevel[2]-1]

        self.TalentRevive = np.array([[0.12, 0, 0],
                                    [0.1275, 0, 0],
                                    [0.135, 0, 0],
                                    [0.1425, 0, 0],
                                    [0.15, 0, 0],
                                    [0.156, 0, 0],
                                    [0.162, 0, 0],
                                    [0.168, 0, 0],
                                    [0.174, 0, 0],
                                    [0.18, 0, 0],
                                    [0.186, 0, 0],
                                    [0.192, 0, 0],
                                    [0.198, 0, 0],
                                    [0.204, 0, 0],
                                    [0.21, 0, 0],])[self.SkillLevel[2]-1]
        self.TalentFlatRevive = np.array([120, 192, 246, 300, 336, 372, 399, 426, 453, 480, 507, 534, 561, 588, 615])[self.SkillLevel[2]-1]

        self.UltimateHeal = np.array([[0.09, 0, 0],
                                    [0.095625, 0, 0],
                                    [0.10125, 0, 0],
                                    [0.106875, 0, 0],
                                    [0.1125, 0, 0],
                                    [0.117, 0, 0],
                                    [0.1215, 0, 0],
                                    [0.126, 0, 0],
                                    [0.1305, 0, 0],
                                    [0.135, 0, 0],
                                    [0.1395, 0, 0],
                                    [0.144, 0, 0],
                                    [0.1485, 0, 0],
                                    [0.153, 0, 0],
                                    [0.1575, 0, 0],])[self.SkillLevel[3]-1]
        self.UltimateFlatHeal = np.array([90, 144, 184.5, 225, 252, 279, 299.25, 319.5, 339.75, 360, 380.25, 400.5, 420.75, 441, 461.25])[self.SkillLevel[3]-1]
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(BailuTalentHeal(self))
        self.Game.TriggerList.append(BailuTalentRevive(self))
        self.Game.TriggerList.append(BailuQihuangAnalects(self))

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
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)

        self.Game.ChangeSkillPoint(-1)

        self.EnergyGenerate(30, Flat=False)

        self.Game.ApplyHeal(Attacker = self, Target = target[0], Multiplier = self.BSkillHeal, FlatHeal = self.BSkillFlatHeal, HealName = f'{self.Name}전투스킬')
        if self.Eidolons >= 4:
            cnt = 1
            for Buff in target[0].BuffList:
                if Buff['설명'] == '백로4돌피증':
                    cnt += Buff['효과'][0][1]//0.1
                    if cnt > 3:
                        cnt = 3
            self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff ={'버프형태' : '스탯', '설명' : '백로4돌피증', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과': [(f'{target[0].Element}속성피해증가', cnt * 0.1)]})

        for i in range(2):
            rndCharacter = random.choice(self.Game.Characters)
            self.Game.ApplyHeal(Attacker = self, Target = rndCharacter, Multiplier = self.BSkillHeal, FlatHeal = self.BSkillFlatHeal, HealName = f'{self.Name}전투스킬', Multiple = 1 - 0.15*(i+1))
            if self.Eidolons >= 4:
                cnt = 1
                for Buff in rndCharacter.BuffList:
                    if Buff['설명'] == '백로4돌피증':
                        cnt += Buff['효과'][0][1]//0.1
                        if cnt > 3:
                            cnt = 3
                self.Game.ApplyBuff(Attacker = self, Target = rndCharacter, Buff ={'버프형태' : '스탯', '설명' : '백로4돌피증', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과': [(f'{rndCharacter.Element}속성피해증가', cnt * 0.1)]})

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        for Character in self.Game.Characters:
            self.Game.ApplyHeal(Attacker = self, Target = Character, Multiplier = self.UltimateHeal, FlatHeal = self.UltimateFlatHeal, HealName = f'{self.Name}전투스킬')
            Nolife = True
            for Buff in Character.BuffList:
                if Buff['설명'] == '백로생명':
                    Buff['남은턴'] += 1
                    Nolife = False
            if Nolife == True:
                self.Game.ApplyBuff(Attacker = self, Target = Character, Buff ={'버프형태' : '기타', '설명' : '백로생명', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '남은횟수' : 3})
        if self.Eidolons >= 2:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '스탯', '설명' : '백로2돌치유량', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '효과': [('치유량보너스', 0.15)]})


        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    
    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError
    
    def DeleteBuff(self, Buff):
        super().DeleteBuff(Buff)
        if self.Eidolons >= 1:
            if Buff['설명'] == '백로생명':
                MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
                if self.CurrentHP == MaxHP:
                    self.EnergyGenerate(8, False)


class BailuTalentHeal:
    def __init__(self,Object):
        self.Object = Object
        self.Targets = []
        self.Start = False
        self.Target = None
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '적일반공격발동시작' or Trigger =='적전투스킬발동시작' or Trigger == '적필살기발동시작' or Trigger =='적추가공격발동시작':
            self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Start == True:
                    if any([Buff['설명'] == '백로생명' for Buff in Target[0].BuffList]):
                        if Target[0] not in self.Targets:
                            self.Targets.append(Target[0])
                            Target[0].TempBuffList.append(('받는피해증가', -0.1))
        
        if Trigger == '적일반공격발동종료' or Trigger =='적전투스킬발동종료' or Trigger == '적필살기발동종료' or Trigger == '적추가공격발동종료':
            if self.Start == True:
                for target in self.Targets:
                    self.Object.Game.ApplyHeal(Attacker = self.Object, Target = target, Multiplier = self.Object.TalentHeal, FlatHeal = self.Object.TalentFlatHeal, HealName = f'{self.Object.Name}생명', Except = self)
                    for buff in target.BuffList:
                        if buff['설명'] == '백로생명':
                            buff['남은횟수'] -= 1
                            if buff['남은횟수'] == 0:
                                target.DeleteBuff(buff)
            self.Start = False
            self.Targets = []

class BailuTalentRevive:
    def __init__(self,Object):
        self.Object = Object
        self.RevivePossible = 1
        if self.Object.Eidolons >= 6:
            self.RevivePossible = 2
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '아군사망':
            if self.RevivePossible > 0:
                if Target[0] != self.Object:
                    self.RevivePossible -=1
                    Target[0].IsDead = False
                    Target[0].CurrentHP = 0
                    self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Target[0], Multiplier = self.Object.TalentRevive, FlatHeal = self.Object.TalentFlatRevive, HealName = f'{self.Object.Name}부활', Except = self)

class BailuQihuangAnalects:
    def __init__(self, Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '힐발동종료':
            if Attacker == self.Object:
                if Value[1] ==  True: # OverHeal = True
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Target[0], Buff ={'버프형태' : '스탯', '설명' : '백로초과힐', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('HP%증가', 0.1)]}, Except = self)
                    MaxHP = Target[0].CurrentStat['기초HP'] * (1 + Target[0].CurrentStat['HP%증가']) + Target[0].CurrentStat['고정HP증가']
                    if Target[0].CurrentHP <= MaxHP+1:
                        Target[0].CurrentHP = MaxHP
                    else:
                        print(MaxHP)
                        print(Target[0].CurrentHP)
                        raise ValueError

