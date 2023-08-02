from Characters.BaseCharacter import BaseCharacter
import random
import numpy as np
class Luocha(BaseCharacter):
    def __init__(self, SkillLevel, Eidolons):
        super().__init__(SkillLevel, Eidolons)
        self.Name = '나찰'
        self.Element = '허수'
        self.SkillRange = {'일반공격' : '적지정', '전투스킬' : '아군지정', '필살기' : '적전체'} 

        # 기본
        self.BaseStat['기초HP'] += 1281
        self.BaseStat['기초공격력'] += 757
        self.BaseStat['기초방어력'] += 364
        self.BaseStat['기초속도'] += 101
        self.BaseStat['에너지최대치'] += 100  
        self.BaseStat['기초도발'] += 100
        # 추가
        self.BaseStat['공격력%증가'] += 0.04 + 0.08 + 0.04 + 0.06 + 0.06
        self.BaseStat['HP%증가'] += 0.04 + 0.08 + 0.06
        self.BaseStat['방어력%증가'] += 0.05 + 0.075 

        # 추가능력1
        self.BaseStat['속박저항'] += 0.7
        self.BaseStat['얽힘저항'] += 0.7
        self.BaseStat['빙결저항'] += 0.7
        self.BaseStat['도발저항'] += 0.7
        
        if self.Eidolons >= 3:
            self.SkillLevel[0] += 1
            self.SkillLevel[1] += 2
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
        
        self.BSkillHeal = np.array([[0, 0.4, 0],
                                    [0, 0.425, 0],
                                    [0, 0.45, 0],
                                    [0, 0.475, 0],
                                    [0, 0.5, 0],
                                    [0, 0.52, 0],
                                    [0, 0.54, 0],
                                    [0, 0.56, 0],
                                    [0, 0.58, 0],
                                    [0, 0.6, 0],
                                    [0, 0.62, 0],
                                    [0, 0.64, 0],
                                    [0, 0.66, 0],
                                    [0, 0.68, 0],
                                    [0, 0.7, 0],])[self.SkillLevel[1]-1]
        self.BSkillFlatHeal = np.array([200, 320, 410, 500, 560, 620, 665, 710, 755, 800, 845, 890, 935, 980, 1025])[self.SkillLevel[1]-1]

        self.TalentHeal = np.array([[0, 0.12, 0],
                                    [0, 0.1275, 0],
                                    [0, 0.135, 0],
                                    [0, 0.1425, 0],
                                    [0, 0.15, 0],
                                    [0, 0.156, 0],
                                    [0, 0.162, 0],
                                    [0, 0.168, 0],
                                    [0, 0.174, 0],
                                    [0, 0.18, 0],
                                    [0, 0.186, 0],
                                    [0, 0.192, 0],
                                    [0, 0.198, 0],
                                    [0, 0.204, 0],
                                    [0, 0.21, 0],])[self.SkillLevel[2]-1]
        self.TalentFlatHeal = np.array([60, 96, 123, 150, 168, 186, 199.5, 213, 226.5, 240, 253.5, 267, 280.5, 294, 307.5])[self.SkillLevel[2]-1]

        self.UltimateDMG = np.array([[0, 1.2, 0],
                                    [0, 1.28, 0],
                                    [0, 1.36, 0],
                                    [0, 1.44, 0],
                                    [0, 1.52, 0],
                                    [0, 1.6, 0],
                                    [0, 1.7, 0],
                                    [0, 1.8, 0],
                                    [0, 1.9, 0],
                                    [0, 2.0, 0],
                                    [0, 2.08, 0],
                                    [0, 2.16, 0],
                                    [0, 2.24, 0],
                                    [0, 2.32, 0],
                                    [0, 2.4, 0],])[self.SkillLevel[3]-1]
        self.TalentStack = 0
    
    def ChangeTalentStack(self, stack):
        beforeStack = self.TalentStack
        if not any([buff['설명']=='나찰결계' for buff in self.BuffList]):
            self.TalentStack += stack
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 나찰 백화의 순간 스택 {stack} 변화, 이전 : {beforeStack}, 현재 : {self.TalentStack}")
        if self.TalentStack == 2:
            self.Game.ApplyBuff(Attacker = self, Target = self, Buff ={'버프형태' : '기타', '설명' : '나찰결계', '시간타입' : 'A', '체크' : False, '남은턴' : 2})
            self.TalentStack = 0
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 나찰 백화의 순간 스택 {self.TalentStack} 로 조정")
        
    def AddToGame(self, Game):
        super().AddToGame(Game)
        self.Game.TriggerList.append(LuochaTalent(self))
        self.Game.TriggerList.append(LuochaAutoBSkill(self))
        if self.Eidolons >= 1 :
            self.Game.TriggerList.append(LuochaEidolon1(self))

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

        if len(target[0].DebuffList) > 0:
            RndDebuff = random.choice(target[0].DebuffList)
            if RndDebuff['디버프형태'] == '빙결':
                target[0].TurnSkip = False
            target[0].DeleteDebuff(RndDebuff)
        
        if self.Eidolons >= 2: 
            MaxHP = target[0].CurrentStat['기초HP'] * (1 + target[0].CurrentStat['HP%증가']) + target[0].CurrentStat['고정HP증가']
            if target[0].CurrentHP < 0.5 * MaxHP:
                self.Game.ApplyHeal(Attacker = self, Target = target[0], Multiplier = self.BSkillHeal, FlatHeal = self.BSkillFlatHeal, HealName = f'{self.Name}전투스킬', Multiple = (1 + self.CurrentStat['치유량보너스'] + 0.3)/(1 + self.CurrentStat['치유량보너스']))
            else:
                self.Game.ApplyHeal(Attacker = self, Target = target[0], Multiplier = self.BSkillHeal, FlatHeal = self.BSkillFlatHeal, HealName = f'{self.Name}전투스킬')
                self.Game.ApplyBuff(Attacker = self, Target = target[0], Buff = {'버프형태' : '실드', '설명' : '나찰2돌실드', '시간타입' : 'A', '체크' : False, '남은턴' : 2,  '계수' : [0.0, 0.18, 0.0], '고정' : 240})   
        else:
            self.Game.ApplyHeal(Attacker = self, Target = target[0], Multiplier = self.BSkillHeal, FlatHeal = self.BSkillFlatHeal, HealName = f'{self.Name}전투스킬')

        self.Game.ActiveTrigger('캐릭터전투스킬발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터전투스킬발동종료2', self, target, None)
        self.ChangeTalentStack(1)
    
    def Ultimate(self, target):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 필살기 발동")
        self.Game.ActiveTrigger('캐릭터필살기발동시작', self, target, None)

        self.CurrentEnergy = 0
        self.EnergyGenerate(5, Flat = False)
        for Enemy in self.Game.Enemys.copy():
            if len(Enemy.BuffList) > 0:
                Enemy.DeleteBuff(random.choice(Enemy.BuffList))
            self.Game.ApplyDamage(Attacker = self, Target = Enemy, Element = self.Element, DamageType = '필살기', Toughness = 60, Multiplier = self.UltimateDMG, FlatDMG = 0, DamageName = f'{self.Name}필살기공격')
            if self.Eidolons >= 6:
                self.Game.ApplyDebuff(Attacker = self, Target = Enemy, BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '나찰6돌저항깍', '남은턴' : 2, '효과' : [(f'모든속성저항증가', -0.2)]})
        

        self.Game.ActiveTrigger('캐릭터필살기발동종료', self, target, None)
        self.Game.ActiveTrigger('캐릭터필살기발동종료2', self, target, None)
        self.ChangeTalentStack(1)

    
    def BattleSkillIsPossible(self):
        if self.Game.SkillPoint > 0 and self.Game.SkillPoint <= 5:
            return True
        elif self.Game.SkillPoint == 0:
            return False    
        else:
            raise ValueError


class LuochaTalent:
    def __init__(self,Object):
        self.Object = Object
        self.Targets = []
        self.Start = False
        self.Attack = False
        self.Target = None
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker in self.Object.Game.Characters:
                self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker in self.Object.Game.Characters:
                        if any([buff['설명']=='나찰결계' for buff in self.Object.BuffList]):
                            self.Attack = True
                if self.Object.Eidolons >= 4:
                    if Target[0] in self.Object.Game.Characters and Attacker in self.Object.Game.Enemys:
                        if any([buff['설명']=='나찰결계' for buff in self.Object.BuffList]):
                            Attacker.TempBuffList.append(('모든피해증가', -0.12))

        
        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                if self.Attack == True:
                    self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Attacker, Multiplier = self.Object.TalentHeal, FlatHeal = self.Object.TalentFlatHeal, HealName = f'{self.Object.Name}결계메인힐', Except = self)
                    for Character in self.Object.Game.Characters:
                        if Character != Attacker:
                             self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Character, Multiplier = [0, 0.07, 0], FlatHeal = 93, HealName = f'{self.Object.Name}결계아군힐', Except = self)
            self.Start = False
            self.Attack = False

class LuochaEidolon1:
    def __init__(self,Object):
        self.Object = Object

    def Active(self, Trigger, Attacker, Target, Value):
        if self.Object.Eidolons >= 1:
            if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작', '힐발동시작' , '버프발동시작', '디버프발동시작'):
                if Attacker in self.Object.Game.Characters:
                    if any([buff['설명']=='나찰결계' for buff in self.Object.BuffList]):
                        Attacker.TempBuffList.append(('공격력%증가', 0.2))

class LuochaAutoBSkill:
    def __init__(self,Object):
        self.Object = Object
        self.Turn = 0
    
    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object:
                self.Turn = max(0, self.Turn-1)

        if Trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료','캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료', '캐릭터턴시작결산'):
            if self.Turn == 0:
                for Character in self.Object.Game.Characters:
                    MaxHP = Character.CurrentStat['기초HP'] * (1 + Character.CurrentStat['HP%증가']) + Character.CurrentStat['고정HP증가']
                    if Character.CurrentHP <= 0.5 * MaxHP:
                        self.Object.Game.AppendBattleHistory(f"\n시간 : {self.Object.Game.CurrentTime}, {self.Object.Name} 자동 전투스킬 발동, 타겟 : {Character.Name}")
                        self.Object.EnergyGenerate(30, Flat=False)
                        if len(Character.DebuffList) > 0:
                            RndDebuff = random.choice(Character.DebuffList)
                            if RndDebuff['디버프형태'] == '빙결':
                                Character.TurnSkip = False
                            Character.DeleteDebuff(RndDebuff)
                        if self.Object.Eidolons >= 2: 
                            if Character.CurrentHP < 0.5 * MaxHP:
                                self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Character, Multiplier = self.Object.BSkillHeal, FlatHeal = self.Object.BSkillFlatHeal, HealName = f'{self.Object.Name}자동전투스킬', Multiple = (1 + self.Object.CurrentStat['치유량보너스'] + 0.3)/(1 + self.Object.CurrentStat['치유량보너스']), Except = self)
                            else:
                                self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Character, Multiplier = self.Object.BSkillHeal, FlatHeal = self.Object.BSkillFlatHeal, HealName = f'{self.Object.Name}전투스킬', Except = self)
                                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Character, Buff = {'버프형태' : '실드', '설명' : '나찰2돌실드', '시간타입' : 'A', '체크' : False, '남은턴' : 2,  '계수' : [0.0, 0.18, 0.0], '고정' : 240}, Except = self)   
                        else:
                            self.Object.Game.ApplyHeal(Attacker = self.Object, Target = Character, Multiplier = self.Object.BSkillHeal, FlatHeal = self.Object.BSkillFlatHeal, HealName = f'{self.Object.Name}전투스킬', Except = self)
                        self.Object.ChangeTalentStack(1)
                        self.Turn = 2
                        break