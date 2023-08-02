from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np

class Tingyun(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '정운'
        self.Element = '번개'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '아군지정', '필살기' : '아군지정'} 
        self.Benediction = None

        # 기본
        self.BaseStat['기초HP'] += 847
        self.BaseStat['기초공격력'] += 529.2
        self.BaseStat['기초방어력'] += 396.9
        self.BaseStat['기초속도'] += 112
        self.BaseStat['에너지최대치'] += 130  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.06 + 0.04 + 0.06 + 0.04 + 0.08
        self.BaseStat['번개속성피해증가'] += 0.032 + 0.048
        self.BaseStat['방어력%증가'] += 0.075 + 0.05 + 0.1
        self.BaseStat['일반공격피해증가'] += 0.4    
        
        if self.Eidolons >= 3:
            self.SkillLevel[3] += 2
            self.SkillLevel[0] += 1
        if self.Eidolons >= 5:
            self.SkillLevel[1] += 2
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
                    
        self.BSkillAtkBuff = np.array([0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.40625, 0.4375, 0.46875, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625])[self.SkillLevel[1]-1]
        self.BSkillAtkLimit = np.array([0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.2125, 0.225, 0.2375, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])[self.SkillLevel[1]-1]
        self.BSkillDMG =  np.array([[0, 0.2, 0],
                                    [0, 0.22, 0],
                                    [0, 0.24, 0],
                                    [0, 0.26, 0],
                                    [0, 0.28, 0],
                                    [0, 0.3, 0],
                                    [0, 0.325, 0],
                                    [0, 0.35, 0],
                                    [0, 0.375, 0],
                                    [0, 0.4, 0],
                                    [0, 0.42, 0],
                                    [0, 0.44, 0],
                                    [0, 0.46, 0],
                                    [0, 0.48, 0],
                                    [0, 0.5, 0],])[self.SkillLevel[1]-1]
        
        self.TalentDMG = np.array([[0, 0.33, 0],
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
                                    [0, 0.75, 0],])[self.SkillLevel[2]-1]

        self.UltimateBuff = np.array([0.2, 0.23, 0.26, 0.29, 0.32, 0.35, 0.3875, 0.425, 0.4625, 0.5, 0.53, 0.56, 0.59, 0.62, 0.65])[self.SkillLevel[3]-1]

    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(TingyunBenediction(self))
        if self.Eidolons >= 2:
            self.Game.TriggerList.append(TingyunEidolons2(self))

    def StartTurn(self):
        super().StartTurn()
        self.EnergyGenerate(5, False)
    
    def NormalAttack(self, target):
        if len(target) != 1:
            raise ValueError # target : [타겟1] - 리스트형태임
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 일반공격 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터일반공격발동시작', self, target, None)

        self.Game.ChangeSkillPoint(1)

        self.EnergyGenerate(20, Flat = False)
        self.Game.ApplyDamage(Attacker = self, Target = target[0], Element = self.Element, DamageType = '일반공격', Toughness = 30, Multiplier = self.NADMG, FlatDMG = 0, DamageName = f'{self.Name}일반공격')
        if self.Benediction != None:
            self.Game.ApplyDamage(Attacker = self.Benediction, Target = target[0], Element = self.Element, DamageType ='추가피해', Toughness = 0, Multiplier = self.TalentDMG, FlatDMG = 0, DamageName = '정운특성')
        self.Game.ActiveTrigger('캐릭터일반공격발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터일반공격발동종료2', self, target, None)



    def BattleSkill(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 전투스킬 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터전투스킬발동시작', self, target, None)
        self.Game.ChangeSkillPoint(-1)
        self.EnergyGenerate(30, Flat=False)

        if self.Benediction != None:
            for Buff in self.Benediction.BuffList.copy():
                if Buff['설명'] == '정운축복':
                    self.Benediction.DeleteBuff(Buff)
        TargetCurrentATK = target[0].CurrentStat['기초공격력']
        TingyunCurrentATK = self.CurrentStat['기초공격력'] * (1 + self.CurrentStat['공격력%증가']) + self.CurrentStat['고정공격력증가']
        BuffATK = min(TargetCurrentATK * self.BSkillAtkBuff, TingyunCurrentATK * self.BSkillAtkLimit)
        self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff = {'버프형태' : '스탯', '설명': '정운축복', '시간타입' : 'B', '체크' : False, '남은턴' : 3, '효과' : [('고정공격력증가', BuffATK)]})
        self.Benediction = target[0]
        self.Game.ApplyBuff(Attacker = self, Target = self, Buff = {'버프형태' : '스탯', '설명': '정운전투스킬가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('속도%증가', 0.2)]})
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)

    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동, 타겟 : {target[0].Name}")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        if self.Eidolons >= 6 :
            energy = 60
        else:
            energy = 50
        target[0].EnergyGenerate(energy, True)
        self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff ={'버프형태' : '스탯', '설명' : '정운궁', '시간타입' : 'B', '체크' : False, '남은턴' : 2, '효과' : [(f'모든피해증가', self.UltimateBuff)]})
        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)

    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError

class TingyunBenediction:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Attack = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object.Benediction:
                self.Start = True
                if self.Object.Eidolons >= 1:
                    if Trigger == '캐릭터필살기발동시작':
                        self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object.Benediction, Buff = {'버프형태' : '스탯', '설명': '정운1돌가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('속도%증가', 0.2)]}, Except = self)


        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker == self.Object.Benediction:
                        self.Attack = True
        
        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                if self.Attack == True:
                    if self.Object.Eidolons >= 4:
                        multiple = 1.2
                    else:
                        multiple = 1
                    if len(self.Object.Game.Enemys) > 0: #신군은 타겟이 없어서 적 전체를 타겟으로하는데 신군의 공격으로 적이 전부 사망하면 적이 없어서 에러가 발생
                        self.Object.Game.ApplyDamage(Attacker = self.Object.Benediction, Target = Target[-1], Element = self.Object.Element, DamageType ='추가피해', Toughness = 0, Multiplier = self.Object.BSkillDMG, FlatDMG = 0, DamageName = '정운축복', Multiple = multiple, Except = self)
            self.Start = False
            self.Attack = False
        
        if Trigger == '캐릭터턴종료':
            if Attacker == self.Object.Benediction:
                BenedictionEnd = True
                for Buff in self.Object.Benediction.BuffList:
                    if Buff['설명'] == '정운축복':
                        BenedictionEnd = False
                if BenedictionEnd == True:
                    self.Benediction = None

class TingyunEidolons2:
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Possible = True
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object.Benediction:
                self.Possible = True

        if Trigger in ('적사망', '적전원사망'):
            if Attacker == self.Object.Benediction:
                self.Object.Benediction.EnergyGenerate(5, False)
                self.Possible = False