import random
import copy

class HSRBattle:
    def __init__(self, SimulateTime, MaximumWave, Control, PrintTempBuff):
        self.SimulateTime = SimulateTime
        self.MaximumWave = MaximumWave
        self.PrintTempBuff = PrintTempBuff
        self.Control = Control
        self.MaxActionGauge = 10000
        self.CurrentTime = 0
        self.CurrentWave = 0
        self.SkillPoint = 3
        self.Terminal = False
        self.BattleHistory = []
        self.TriggerList = []
        self.Damage = {}
        self.TypeDamage = {}
        self.TriggerName = ['적턴시작', # Attacker = self, Target = None, value = None : 적 턴 시작시 
                            '적턴시작결산', # Attacker = self, Target = None, value = None : 적 턴 시작시 디버프 관리 이후
                            '적턴종료', # Attacker = self, Target = None, value = None : 적 턴 종료시
                            '적일반공격발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 적 일반공격 발동시작시
                            '적일반공격발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 적 일반공격 발동시종료시
                            '적일반공격발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 적 일반공격 발동시종료시
                            '적전투스킬발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 적 전투스킬 발동시작시
                            '적전투스킬발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 적 전투스킬 발동시종료시
                            '적전투스킬발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 적 전투스킬 발동시종료시
                            '적필살기발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 적 필살기 발동시작시
                            '적필살기발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 적 필살기 발동종료시
                            '적필살기발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 적 필살기 발동종료시
                            '적추가공격발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 적 추가공격 발동시작시
                            '적추가공격발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 적 추가공격 발동종료시
                            '적추가공격발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 적 추가공격 발동종료시
                            '적격파됨', #  Attacker = Attacker, Target = [self], value = None : 적이 격파될시
                            '적체력소모', # Attakcer = Attacker, Target = [self], value = ConsumedHP : 적 체력소모시
                            '캐릭터턴시작', # Attacker = self, Target = None, value = None : 캐릭터 턴 시작시 
                            '캐릭터턴시작결산', # Attacker = self, Target = None, value = None : 캐릭터 턴 시작시 디버프 관리 이후
                            '캐릭터턴종료', # Attacker = self, Target = None, value = None : 캐릭터 턴 종료시
                            '캐릭터일반공격발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 일반공격 발동시작시
                            '캐릭터일반공격발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 일반공격 발동시종료시
                            '캐릭터일반공격발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 일반공격 발동시종료시
                            '캐릭터전투스킬발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 전투스킬 발동시작시
                            '캐릭터전투스킬발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 전투스킬 발동시종료시
                            '캐릭터전투스킬발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 전투스킬 발동시종료시
                            '캐릭터필살기발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 필살기 발동시작시
                            '캐릭터필살기발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 필살기 발동종료시
                            '캐릭터필살기발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 필살기 발동종료시
                            '캐릭터추가공격발동시작', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 추가공격 발동시작시
                            '캐릭터추가공격발동종료', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 추가공격 발동종료시
                            '캐릭터추가공격발동종료2', # Attacker = self, Target = Target(스킬대상), value = None : 캐릭터 추가공격 발동종료시
                            '캐릭터체력소모', # Attakcer = Attacker, Target = [self], value = ConsumedHP : 캐릭터 체력소모시
                            '게임시작', # Attacker = None, Target = None, value = None : 게임 시작시 
                            '데미지발동시작', # Attacker = Attacker, Target = [Target], value = [데미지타입(ex '전투스킬'), 이름] : Game.ApplyDamage 발동시
                            '데미지발동종료', # Attacker = Attacker, Target = [Target], value = [데미지타입, 이름, 가한데미지] : Game.ApplyDamage 발동시
                            '도트데미지발동시작', # Attacker = Attacker, Target = [Target], value = [도트타입(ex '풍화'), 이름] : Game.ApplyDoTDamage 발동시
                            '도트데미지발동종료', # Attacker = Attacker, Target = [Target], value = [도트타입, 이름, 가한데미지] :Game.ApplyDoTDamage 발동시 
                            '격파데미지발동시작', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyBreakDamage 발동시
                            '격파데미지발동종료', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyBreakDamage 발동시
                            '버프발동시작', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyBuff 발동시
                            '버프발동종료', # Attacker = Attacker, Target = [Target], value = [Buff] : Game.ApplyBuff 발동시
                            '디버프발동시작', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyDebuff 발동시
                            '디버프적중시작', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyDebuff의 확률계산 이후 적중시
                            '디버프적중종료', # Attacker = Attacker, Target = [Target], value = [Debuff] : Game.ApplyDebuff의 확률계산 이후 적중시
                            '힐발동시작', # Attacker = Attacker, Target = [Target], value = None : Game.ApplyHeal 발동시
                            '힐발동종료', # Attacker = Attacker, Target = [Target], value = [힐량, OverHeal(True/False)] : Game.ApplyHeal 발동시
                            '아군사망', # Attacker = Attacker, Target = [Target], value = 데미지타입 : 아군 사망시
                            '적사망', # Attacker = Attacker, Target = [Target], value = 데미지타입 : 적 사망시
                            '적전원사망', # Attacker = Attacker, Target = ['Target], value = None : 적 전원 사망시         
                            '적리젠', # Attakcer = None, Target = None, value = None : 적 리젠시
                            ]
        
    
    def AddCharacter(self, Characters):
        self.Characters = Characters
        for Character in self.Characters:
            self.Damage[Character.Name] = 0
            self.TypeDamage[Character.Name] = {'일반공격' : 0, '전투스킬': 0, '필살기': 0, '추가공격': 0, '추가피해': 0, '지속피해': 0, '격파피해': 0}

            Character.AddToGame(self)
    
    def AddEnemy(self, Enemys):
        self.Regenerate  = Enemys
        self.Enemys = []
        for Enemy in self.Regenerate:
            enemy = Enemy[0](Enemy[1], Enemy[2])
            self.Enemys.append(enemy)
            enemy.AddToGame(self)

    def Init(self):
        self.TriggerList.append(Regenerate(self))
        self.TurnObject = self.Characters[0]
        self.Summons = []
        for Character in self.Characters:
            Character.Init()
        for Enemy in self.Enemys:
            Enemy.Init()
        self.AppendBattleHistory(f"게임시작, {self.CurrentWave+1}번째 웨이브\n")
        self.ActiveTrigger('게임시작', None, None, None)
        self.CalcTurn()

        
    def CalcTurn(self):
        MinTime = self.MaxActionGauge
        for Character in self.Characters:
            TimeRemain = max(0, (self.MaxActionGauge - Character.ActionGauge) / Character.CalcSpeed())
            if TimeRemain < MinTime:
                MinTime = TimeRemain
                self.TurnObject = Character
        for Enemy in self.Enemys:
            TimeRemain = max(0, (self.MaxActionGauge - Enemy.ActionGauge) / Enemy.CalcSpeed())
            if TimeRemain < MinTime:
                MinTime = TimeRemain
                self.TurnObject = Enemy
        for Summons in self.Summons:
            TimeRemain = max(0, (self.MaxActionGauge - Summons.ActionGauge) / Summons.CalcSpeed())
            if TimeRemain < MinTime:
                MinTime = TimeRemain
                self.TurnObject = Summons
        

        self.CurrentTime = min(self.CurrentTime + MinTime, self.SimulateTime)
        if self.CurrentTime >= self.SimulateTime:
            self.Terminal = True

        if self.Terminal == False:
            for Character in self.Characters:
                Character.ActionGauge += Character.CalcSpeed() * MinTime
            for Enemy in self.Enemys:
                Enemy.ActionGauge += Enemy.CalcSpeed() * MinTime
            for Summons in self.Summons:
                Summons.ActionGauge += Summons.CalcSpeed() * MinTime
                
            if self.TurnObject in self.Summons:
                self.TurnObject.Action()
                self.CalcTurn()
            else:
                self.TurnObject.StartTurn() # 객체 턴 스타트
                self.TurnStep = '행동전필살기선택'

    def GetPossibleAction(self): 
        while self.Terminal == False:
            if self.TurnStep == '행동전필살기선택':
                if self.TurnObject in self.Characters:# 캐릭터 턴
                    UltimateOnCharacter = []
                    for Character in self.Characters: 
                        if Character.CurrentEnergy >= Character.BaseStat['에너지최대치'] and Character.UltimateActiveCheck == False:
                            if Character.CheckFrozen() != True and Character.TurnSkip == False:  # 나중에 뜯어고쳐야함 현재 빙결시에만 스킵되는데 얽힘,속박시에도 스킵되어야함
                                UltimateOnCharacter.append(Character)
                    if len(UltimateOnCharacter) > 0:
                        self.GetUltimateAction(UltimateOnCharacter)
                        return self.PossibleAction, self.Terminal
                    
                self.TurnStep = '행동선택'
                for Character in self.Characters:
                    Character.UltimateActiveCheck = False

            elif self.TurnStep == '행동선택':
                if self.TurnObject in self.Characters:# 캐릭터 턴
                    if self.TurnObject.TurnSkip == True: #빙결이면 턴스킵
                        self.AppendBattleHistory(f'시간 : {self.CurrentTime}, {self.TurnObject.Name} 빙결로 인한 턴 스킵')
                        self.TurnStep = '행동종료'
                    else:
                        self.GetNormalAction(self.TurnObject)
                        return self.PossibleAction, self.Terminal
                
                elif self.TurnObject in self.Enemys: # 적 턴
                    self.TurnObject.Action()
                    self.TurnStep = '행동종료'

                else: # 턴시작시 도트뎀 맞고 죽어서 리스트에서 사라졌을때
                    self.TurnStep = '행동종료'
            
            elif self.TurnStep == '행동종료':
                if self.TurnObject in self.Characters:# 캐릭터 턴
                    UltimateOnCharacter = []
                    for Character in self.Characters: 
                        if Character.CurrentEnergy >= Character.BaseStat['에너지최대치'] and Character.UltimateActiveCheck == False:
                            if Character.CheckFrozen() != True and Character.TurnSkip == False:  # 나중에 뜯어고쳐야함 현재 빙결시에만 스킵되는데 얽힘,속박시에도 스킵되어야함
                                UltimateOnCharacter.append(Character)
                    if len(UltimateOnCharacter) > 0:
                        self.GetUltimateAction(UltimateOnCharacter)
                        return self.PossibleAction, self.Terminal

                self.TurnObject.EndTurn()
                self.TurnObject = '없음'
                
                self.TurnStep = '행동종료후필살기선택'
                for Character in self.Characters:
                    Character.UltimateActiveCheck = False
            
            elif self.TurnStep == '행동종료후필살기선택':
                UltimateOnCharacter = []
                for Character in self.Characters:
                    if Character.CurrentEnergy >= Character.BaseStat['에너지최대치'] and Character.UltimateActiveCheck == False:
                        if Character.CheckFrozen() != True and Character.TurnSkip == False:  # 나중에 뜯어고쳐야함 현재 빙결시에만 스킵되는데 얽힘,속박시에도 스킵되어야함
                            UltimateOnCharacter.append(Character)
                if len(UltimateOnCharacter) > 0:
                    self.GetUltimateAction(UltimateOnCharacter)
                    return self.PossibleAction, self.Terminal
                    
                for Character in self.Characters:
                    Character.UltimateActiveCheck = False
                
                self.CalcTurn()

            else: 
                raise ValueError
        self.AppendBattleHistory(f"\n시간 : {self.CurrentTime}, 시뮬레이션 종료, 총합 데미지 : {sum(self.Damage.values())}, 캐릭별 데미지 : {self.Damage}")
        for Character in self.Characters:
            self.AppendBattleHistory(Character.Name+' : '+str(self.TypeDamage[Character.Name]))
        return None, self.Terminal
    
    def ApplyCharacterAction(self, Action):
        if Action['스킬'] == '필살기':
            if Action['발동'] == True:
                Action['시전자'].Ultimate(Action['타겟'])
                Action['시전자'].UltimateActiveCheck = True
                
            elif Action['발동'] == False:
                for Character in self.Characters:
                    Character.UltimateActiveCheck = True

        elif Action['스킬'] == '일반공격':
            self.TurnStep = '행동종료'
            Action['시전자'].NormalAttack(Action['타겟'])
        elif Action['스킬'] == '전투스킬':
            self.TurnStep = '행동종료'
            Action['시전자'].BattleSkill(Action['타겟'])
        else:
            raise ValueError
    
    def GetUltimateAction(self, Characters):
        PossibleAction = [{'발동' : False, '시전자' : '전원', '스킬': '필살기'}]
        for Character in Characters:
            if Character.SkillRange['필살기'] == '적전체':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : self.Enemys, '스킬': '필살기'}]
            elif Character.SkillRange['필살기'] == '적지정':
                if Character.TargetEnemy == None:
                    PossibleAction += [{'발동' : True, '시전자' : Character, '타겟' :[TargetEnemy], '스킬' : '필살기'} for TargetEnemy in self.Enemys]
                elif Character.TargetEnemy in self.Enemys:
                    PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : [Character.TargetEnemy], '스킬': '필살기'}]
                else:
                    raise ValueError
            elif Character.SkillRange['필살기'] == '아군전체':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : self.Characters, '스킬': '필살기'}]
            elif Character.SkillRange['필살기'] == '아군지정':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟' : [TargetCharacter], '스킬' : '필살기'} for TargetCharacter in self.Characters]
            elif Character.SkillRange['필살기'] == '자신지정':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : [Character], '스킬': '필살기'}]
        self.PossibleAction = PossibleAction

    def GetNormalAction(self, Character):
        if Character.SkillRange['일반공격'] == '적지정':
            if Character.TargetEnemy == None:
                PossibleAction = [{'발동' : True, '시전자' : Character, '타겟' :[TargetEnemy], '스킬' : '일반공격'} for TargetEnemy in self.Enemys]
            elif Character.TargetEnemy in self.Enemys:
                PossibleAction = [{'발동' : True, '시전자' : Character, '타겟' :[Character.TargetEnemy], '스킬' : '일반공격'}]
            else:
                raise ValueError
        if Character.BattleSkillIsPossible() == True:
            if Character.SkillRange['전투스킬'] == '적전체':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : self.Enemys, '스킬': '전투스킬'}]
            elif Character.SkillRange['전투스킬'] == '적지정':
                if Character.TargetEnemy == None:
                    PossibleAction += [{'발동' : True, '시전자' : Character, '타겟' :[TargetEnemy], '스킬' : '전투스킬'} for TargetEnemy in self.Enemys] 
                elif Character.TargetEnemy in self.Enemys:
                    PossibleAction += [{'발동' : True, '시전자' : Character, '타겟' :[Character.TargetEnemy], '스킬' : '전투스킬'}] 
                else:
                    raise ValueError
            elif Character.SkillRange['전투스킬'] == '아군전체':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : self.Characters, '스킬': '전투스킬'}]
            elif Character.SkillRange['전투스킬'] == '아군지정':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟' : [TargetCharacter], '스킬' : '전투스킬'} for TargetCharacter in self.Characters]
            elif Character.SkillRange['전투스킬'] == '자신지정':
                PossibleAction += [{'발동' : True, '시전자' : Character, '타겟'  : [Character], '스킬': '전투스킬'}]
        self.PossibleAction = PossibleAction


    def ApplyDamage(self, Attacker, Target, Element, DamageType, Toughness, Multiplier, FlatDMG, DamageName, Multiple = 1, Except = None):
        '''
        목표 객체에게 가하는 데미지(DoT데미지 제외)를 계산하고 적용하는 함수

        Attacker -- 데미지를 가하는 객체
        Target -- 데미지가 가해지는 객체, 목표 객체들의 리스트아님! 단일 
        Element -- '물리', '화염', '얼음', '번개', '바람', '양자', '허수'
        DamageType -- '일반공격', '전투스킬', '필살기', '추가공격'
        Toughness -- 가해지는 강인성피해
        Multiplier -- [HP계수, 공격력계수, 방어력계수]
        Name -- 데미지 설명
        '''
        Attacker.TempBuffList = []
        Target.TempBuffList = []
        self.ActiveTrigger('데미지발동시작', Attacker, [Target], [DamageType, DamageName], Except=Except)
        Attacker.CalcTempStat()
        Target.CalcTempStat()

        CurrentHP = Attacker.TempStat['기초HP'] * (1 + Attacker.TempStat['HP%증가']) + Attacker.TempStat['고정HP증가']
        CurrentATK = Attacker.TempStat['기초공격력'] * (1 + Attacker.TempStat['공격력%증가']) + Attacker.TempStat['고정공격력증가']
        CurrentDEF = Attacker.TempStat['기초방어력'] * (1 + Attacker.TempStat['방어력%증가']) + Attacker.TempStat['고정방어력증가']
        if len(Multiplier) != 3:
            raise ValueError
        BaseDMG = CurrentHP * Multiplier[0] + CurrentATK * Multiplier[1] + CurrentDEF * Multiplier[2] + FlatDMG

        BaseDMG = BaseDMG * Multiple
        
        CritMultiplier = 1 + min(1, Attacker.TempStat['치명타확률']) * Attacker.TempStat['치명타피해']
        DMGBoostMultiplier = 1 + Attacker.TempStat[f'모든피해증가'] + Attacker.TempStat[f'{Element}속성피해증가'] + Attacker.TempStat[f'{DamageType}피해증가']
        TargetDEF = Target.TempStat['기초방어력'] * (1 + Target.TempStat['방어력%증가']) + Target.TempStat['고정방어력증가']
        TargetReductionDEF = TargetDEF * (1 - min(1, Attacker.TempStat['방어력무시'] + Target.TempStat['방어력감소']))
        DEFMultiplier = 1 - TargetReductionDEF/(TargetReductionDEF + 200 + 10 * Attacker.Level)
        ResMultiplier = 1 - (Target.TempStat[f'모든속성저항증가'] + Target.TempStat[f'{Element}속성저항증가'] - Attacker.TempStat[f'{Element}속성저항관통'] - Attacker.TempStat[f'모든속성저항관통'])
        VulnerbilityMultiplier = 1 + Target.TempStat['받는피해증가']
        if Target.IsBroken == True:
            BrokenMultiplier = 1.0
        elif Target.IsBroken == False:
            BrokenMultiplier = 0.9
        else:
            raise ValueError
        Damage = BaseDMG * CritMultiplier * DMGBoostMultiplier * DEFMultiplier * ResMultiplier * VulnerbilityMultiplier * BrokenMultiplier
        ToughnessDMG = Toughness * (1 + Attacker.TempStat['약점격파효율'])

        self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 공격자 : {Attacker.Name},  대상 {Target.Name} 에게 {Damage} {DamageName} 데미지 시전")
        FinalDamage = Target.GetDamage(Attacker, Damage, Element, ToughnessDMG, DamageType)
        self.ActiveTrigger('데미지발동종료', Attacker, [Target], [DamageType, DamageName, FinalDamage], Except=Except)
        return FinalDamage
    
    def ApplyBreakDamage(self, Attacker, Target, Element, Multiple = 1, Except=None):
        #목표 객체에게 가하는 도트 데미지를 계산하고 적용하는 함수, 카프카 때문에 Multiplier 변수 추가됨
        Attacker.TempBuffList = []
        Target.TempBuffList = []
        self.ActiveTrigger('격파데미지발동시작', Attacker, [Target], None, Except=Except)
        Attacker.CalcTempStat()
        Target.CalcTempStat()

        LM = 3767.5533
        MTM = 0.5 + Target.MaxToughness/120

        if Element == '물리':
            BaseDMG = 2 * LM * MTM
        elif Element == '화염':
            BaseDMG = 2 * LM * MTM
        elif Element == '얼음':
            BaseDMG = 1 * LM * MTM
        elif Element == '번개':
            BaseDMG = 1 * LM * MTM
        elif Element == '바람':
            BaseDMG = 1.5 * LM * MTM
        elif Element == '양자':
            BaseDMG = 0.5 * LM * MTM
        elif Element == '허수':
            BaseDMG = 0.5 * LM * MTM
        else:
            raise ValueError
        BaseDMG = BaseDMG * (1 + Attacker.TempStat['격파특수효과'])

        BaseDMG = BaseDMG * Multiple

        TargetDEF = Target.TempStat['기초방어력'] * (1 + Target.TempStat['방어력%증가']) + Target.TempStat['고정방어력증가']
        TargetReductionDEF = TargetDEF * (1 - min(1, Attacker.TempStat['방어력무시'] + Target.TempStat['방어력감소']))
        DEFMultiplier = 1 - TargetReductionDEF/(TargetReductionDEF + 200 + 10 * Attacker.Level)
        ResMultiplier = 1 - (Target.TempStat[f'모든속성저항증가'] + Target.TempStat[f'{Element}속성저항증가'] - Attacker.TempStat[f'{Element}속성저항관통'] - Attacker.TempStat[f'모든속성저항관통'])
        VulnerbilityMultiplier = 1 + Target.TempStat['받는피해증가']
        BrokenMultiplier = 0.9
  
        
        Damage = BaseDMG * DEFMultiplier * ResMultiplier * VulnerbilityMultiplier * BrokenMultiplier
        
        self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 공격자 : {Attacker.Name},  대상 {Target.Name} 에게 {Damage} 격파 데미지 시전")
        Target.GetDamage(Attacker, Damage, Element, 0, '격파피해')
        self.ActiveTrigger('격파데미지발동종료', Attacker, [Target], None, Except=Except)
    

    def ApplyDoTDamage(self, Target, DoT, Multiple = 1, Except=None):
        #목표 객체에게 가하는 도트 데미지를 계산하고 적용하는 함수, 카프카 때문에 Multiple 변수 추가됨
        Attacker = DoT['공격자']
        Attacker.TempBuffList = []
        Target.TempBuffList = []
        self.ActiveTrigger('도트데미지발동시작', Attacker, [Target], [DoT['디버프형태'], DoT['설명']], Except=Except)
        Attacker.CalcTempStat()
        Target.CalcTempStat()

        if DoT['디버프형태'] == '열상':
            element = '물리'
        elif DoT['디버프형태'] == '연소':
            element = '화염'
        elif DoT['디버프형태'] == '빙결':
            element = '얼음'
        elif DoT['디버프형태'] == '감전':
            element = '번개'
        elif DoT['디버프형태'] == '풍화':
            element = '바람'
        elif DoT['디버프형태'] == '얽힘':
            element = '양자'
        else:
            raise ValueError

        if DoT['발동타입'] == '격파':
            LM = 3767.5533
            MTM = 0.5 + Target.MaxToughness/120

            if DoT['디버프형태'] == '열상':
                TargetMaxHP = Target.TempStat['기초HP'] * (1 + Target.TempStat['HP%증가']) + Target.TempStat['고정HP증가']
                if Target.EnemyType == '일반':
                    BaseDMG = TargetMaxHP * 0.16
                elif Target.EnemyType == '정예':
                    BaseDMG = TargetMaxHP * 0.07
                else:
                    raise ValueError
                BaseDMG = min(2 * LM * MTM, BaseDMG)

            elif DoT['디버프형태'] == '연소':
                BaseDMG = 1 * LM 
            elif DoT['디버프형태'] == '빙결':
                BaseDMG = 1 * LM
            elif DoT['디버프형태'] == '감전':
                BaseDMG = 2 * LM
            elif DoT['디버프형태'] == '풍화':
                BaseDMG = 1 * DoT['중첩'] * LM
            elif DoT['디버프형태'] == '얽힘':
                BaseDMG = 0.6 * DoT['중첩'] * LM * MTM
            else:
                raise ValueError
            
            BaseDMG = BaseDMG * (1 + Attacker.TempStat['격파특수효과'])
            BaseDMG = BaseDMG * DoT['배율']
                    
        elif DoT['발동타입'] == '스킬':
            if DoT['디버프형태'] == '열상':
                TargetMaxHP = Target.TempStat['기초HP'] * (1 + Target.TempStat['HP%증가']) + Target.TempStat['고정HP증가']
                BaseDMG = TargetMaxHP * DoT['계수']

                CurrentHP = Attacker.TempStat['기초HP'] * (1 + Attacker.TempStat['HP%증가']) + Attacker.TempStat['고정HP증가']
                CurrentATK = Attacker.TempStat['기초공격력'] * (1 + Attacker.TempStat['공격력%증가']) + Attacker.TempStat['고정공격력증가']
                CurrentDEF = Attacker.TempStat['기초방어력'] * (1 + Attacker.TempStat['방어력%증가']) + Attacker.TempStat['고정방어력증가']
                if len(DoT['최대치계수']) != 3:
                    raise ValueError
                MaximumDMG = CurrentHP * DoT['최대치계수'][0] + CurrentATK * DoT['최대치계수'][1] + CurrentDEF * DoT['최대치계수'][2]
                BaseDMG = min(MaximumDMG, BaseDMG)
            
            else:
                CurrentHP = Attacker.TempStat['기초HP'] * (1 + Attacker.TempStat['HP%증가']) + Attacker.TempStat['고정HP증가']
                CurrentATK = Attacker.TempStat['기초공격력'] * (1 + Attacker.TempStat['공격력%증가']) + Attacker.TempStat['고정공격력증가']
                CurrentDEF = Attacker.TempStat['기초방어력'] * (1 + Attacker.TempStat['방어력%증가']) + Attacker.TempStat['고정방어력증가']
                if len(DoT['계수']) != 3:
                    raise ValueError
                BaseDMG = CurrentHP * DoT['계수'][0] + CurrentATK * DoT['계수'][1] + CurrentDEF * DoT['계수'][2]

            BaseDMG = BaseDMG * (1 + Attacker.TempStat[f'모든피해증가'] + Attacker.TempStat[f'{element}속성피해증가'] + Attacker.TempStat[f'지속피해피해증가'])
            if DoT['디버프형태'] in ('풍화', '얽힘'):
                BaseDMG = BaseDMG * DoT['중첩']
        else:
            raise ValueError
        
        BaseDMG = BaseDMG * Multiple
        
        TargetDEF = Target.TempStat['기초방어력'] * (1 + Target.TempStat['방어력%증가']) + Target.TempStat['고정방어력증가']
        TargetReductionDEF = TargetDEF * (1 - min(1, Attacker.TempStat['방어력무시'] + Target.TempStat['방어력감소']))
        DEFMultiplier = 1 - TargetReductionDEF/(TargetReductionDEF + 200 + 10 * Attacker.Level)
        ResMultiplier = 1 - (Target.TempStat[f'모든속성저항증가'] + Target.TempStat[f'{element}속성저항증가'] - Attacker.TempStat[f'{element}속성저항관통'] - Attacker.TempStat[f'모든속성저항관통'])
        VulnerbilityMultiplier = 1 + Target.TempStat['받는피해증가'] + Target.TempStat['받는지속피해증가']
        if Target.IsBroken == True:
            BrokenMultiplier = 1.0
        elif Target.IsBroken == False:
            BrokenMultiplier = 0.9
        else:
            raise ValueError
        
        Damage = BaseDMG * DEFMultiplier * ResMultiplier * VulnerbilityMultiplier * BrokenMultiplier
        
        self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 공격자 : {Attacker.Name},  대상 {Target.Name} 에게 {Damage} {DoT['설명']} 데미지 시전")
        FianlDamage = Target.GetDamage(Attacker, Damage, element, 0, '지속피해')
        self.ActiveTrigger('도트데미지발동종료', DoT['공격자'], [Target], [DoT['디버프형태'], DoT['설명'], FianlDamage], Except=Except)

        
    def ApplyHeal(self, Attacker, Target, Multiplier, FlatHeal, HealName, Multiple = 1, Except=None):
        # 목표 객체에게 가하는 힐량을 계산하고 적용하는 함수, Target -- 힐량이 적용되는 객체, 목표 객체들의 리스트아님! 단일!
        Attacker.TempBuffList = []
        self.ActiveTrigger('힐발동시작', Attacker, [Target], None, Except=Except)
        Attacker.CalcTempStat()
        
        CurrentHP = Attacker.TempStat['기초HP'] * (1 + Attacker.TempStat['HP%증가']) + Attacker.TempStat['고정HP증가']
        CurrentATK = Attacker.TempStat['기초공격력'] * (1 + Attacker.TempStat['공격력%증가']) + Attacker.TempStat['고정공격력증가']
        CurrentDEF = Attacker.TempStat['기초방어력'] * (1 + Attacker.TempStat['방어력%증가']) + Attacker.TempStat['고정방어력증가']
        Heal = CurrentHP * Multiplier[0] + CurrentATK * Multiplier[1] + CurrentDEF * Multiplier[2] + FlatHeal
        Heal = Heal * (1 + Attacker.TempStat['치유량보너스'])

        Heal = Heal * Multiple

        self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 발동자 : {Attacker.Name}, 대상 {Target.Name} 에게 {Heal} {HealName} 치유 시전")
        OverHeal = Target.GetHeal(Heal)
        self.ActiveTrigger('힐발동종료', Attacker, [Target], [Heal, OverHeal], Except=Except)


    def ApplyBuff(self, Attacker, Target, Buff, Except=None):
        # 목표 객체에게 버프를 적용하는 함수, Target -- 버프가 적용되는 객체, 목표 객체들의 리스트아님! 단일! 
        Attacker.TempBuffList = []
        self.ActiveTrigger('버프발동시작', Attacker, [Target], None, Except=Except)
        Attacker.CalcTempStat()


        for buff in Target.BuffList.copy():
            if buff['설명'] == Buff['설명']:
                Target.BuffList.remove(buff)

        if Buff['버프형태'] == '실드':
            CurrentHP = Attacker.TempStat['기초HP'] * (1 + Attacker.TempStat['HP%증가']) + Attacker.TempStat['고정HP증가']
            CurrentATK = Attacker.TempStat['기초공격력'] * (1 + Attacker.TempStat['공격력%증가']) + Attacker.TempStat['고정공격력증가']
            CurrentDEF = Attacker.TempStat['기초방어력'] * (1 + Attacker.TempStat['방어력%증가']) + Attacker.TempStat['고정방어력증가']
            Buff['수치'] = CurrentHP * Buff['계수'][0] + CurrentATK * Buff['계수'][1] + CurrentDEF * Buff['계수'][2] + Buff['고정']

        Target.BuffList.append(Buff)
        self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 시전자 : {Attacker.Name}, 대상 {Target.Name} 에게 {Buff['설명']} 버프({Buff['효과'] if Buff['버프형태'] == '스탯' else None}) 부여, 대상현재버프 : {[Buff['설명'] for Buff in Target.BuffList]}")
        Target.CalcCurrentStat()
        self.ActiveTrigger('버프발동종료', Attacker, [Target], [Buff], Except=Except)


    def ApplyDebuff(self, Attacker, Target, BaseProbability, Debuff, Except=None):
        # 목표 객체에게의 적중확률을 계산하고 그에 따라 버프를 적용하는 함수, Target -- 디버프가 가해지는 객체, 목표 객체들의 리스트아님! 단일!
        Attacker.TempBuffList = []
        Target.TempBuffList = []
        self.ActiveTrigger('디버프발동시작', Attacker, [Target], None, Except=Except) 
        Attacker.CalcTempStat()
        Target.CalcTempStat()

        if Debuff['디버프형태'] == '스탯' or Debuff['디버프형태'] == '약점부여':
            prob = BaseProbability * (1 + Attacker.TempStat['효과명중']) * (1 - Target.TempStat['효과저항'])
        else :
            prob = BaseProbability * (1 + Attacker.TempStat['효과명중']) * (1 - Target.TempStat['효과저항']) * (1 - Target.TempStat[f"{Debuff['디버프형태']}저항"])
        
        active = self.CheckActive(prob)

        if active == True:
            self.ActiveTrigger('디버프적중시작', Attacker, [Target], None, Except=Except)
            for debuff in Target.DebuffList.copy():
                if debuff['설명'] == Debuff['설명']:
                    if Debuff['디버프형태'] == '풍화':
                        Debuff['중첩'] += debuff['중첩']
                        if Debuff['중첩'] > 5:
                            Debuff['중첩'] = 5
                    elif Debuff['디버프형태'] == '얽힘':
                        Debuff['중첩'] = debuff['중첩']
                    Target.DebuffList.remove(debuff)
            if Debuff['디버프형태'] == '속박' or Debuff['디버프형태'] == '얽힘':
                Target.ChangeActionGauge(Debuff['행동게이지증감'])
            Target.DebuffList.append(Debuff)
            self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 시전자 : {Attacker.Name}, 대상 {Target.Name} 에게 {Debuff['설명']} 디버프 부여, 대상현재디버프 : {[Debuff['설명'] for Debuff in Target.DebuffList]}")
            Target.CalcCurrentStat()
            self.ActiveTrigger('디버프적중종료', Attacker, [Target], [Debuff], Except=Except)


    def ChangeSkillPoint(self, value):
        PreviousSkillPoint = self.SkillPoint
        self.SkillPoint += value
        if self.SkillPoint > 5:
            self.SkillPoint = 5
        if self.SkillPoint < 0:
            self.SkillPoint = 0
        self.AppendBattleHistory(f"시간 : {self.CurrentTime}. 이전 스킬포인트 : {PreviousSkillPoint}, 스킬포인트 변동 : {value}, 현재 스킬포인트 : {self.SkillPoint}")

    def IsDead(self, Attacker, Target, DamageType):
        if Target in self.Characters:
            self.ActiveTrigger('아군사망', Attacker, [Target], DamageType)
            if Target.IsDead == True:
                self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 캐릭터 {Target.Name} 사망")
                self.Characters.remove(Target)
                for trigger in self.TriggerList.copy():
                    if trigger.Object == Target:
                        self.TriggerList.remove(trigger)
                if len(self.Characters) == 0:
                    self.Terminal = True
                    self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 아군 전원 사망, 시뮬레이션 종료")

        elif Target in self.Enemys:
            if Target.IsDead == True:
                self.AppendBattleHistory(f"시간 : {self.CurrentTime}, 적 {Target.Name} 사망")
                Attacker.EnergyGenerate(10, False)
                self.Enemys.remove(Target)
                for trigger in self.TriggerList.copy():
                    if trigger.Object == Target:
                        self.TriggerList.remove(trigger)
                if len(self.Enemys) == 0:
                    self.ActiveTrigger('적전원사망', Attacker, [Target], None)
                else:
                    self.ActiveTrigger('적사망', Attacker, [Target], DamageType)

    
    def GetAggro(self):
        AggroList = []
        for Character in self.Characters:
            AggroList.append(Character.CurrentStat['기초도발'] * (1 + Character.CurrentStat['도발%증가']))
        return AggroList

    def GetNeighboringEnemy(self, Enemy):
        EnemyIndex = self.Enemys.index(Enemy)
        EnemyNum = len(self.Enemys)
        
        if EnemyIndex < 0 or EnemyIndex >= EnemyNum:
            raise IndexError 
        if EnemyIndex == 0:
            return [self.Enemys[EnemyIndex + 1]] if EnemyNum > 1 else []
        elif EnemyIndex == EnemyNum - 1:
            return [self.Enemys[EnemyIndex - 1]]
        else:
            return [self.Enemys[EnemyIndex - 1], self.Enemys[EnemyIndex + 1]]
    
    def GetCurrentRoundTime(self):
        if self.CurrentTime < 150:
            return 0.0
        else:
            return (self.CurrentTime - 150) // 100 * 100 + 150
    
    def CheckActive(self, Probability):
        if random.random()  < Probability:
            return True
        else:
            return False
    
    def ActiveTrigger(self, trigger, Attacker, Target, Value, Except = None):
        if trigger in self.TriggerName:
            for Trigger in self.TriggerList:
                if Trigger != Except:
                    Trigger.Active(trigger, Attacker, Target, Value)
        else:
            for history in self.BattleHistory:
                print(history)
            print('\n\n없는 트리거가 들어옴\n\n')
            raise ValueError

    def AppendBattleHistory(self, BattleHistory):
        if self.Control == True:
            print(BattleHistory)
        self.BattleHistory.append(BattleHistory)
    
        
class Regenerate:
    def __init__(self, Game):
        self.Game = Game
        self.Object = None
        self.Regenerate = False
    
    def Active(self, Trigger, Attacker, Target, Value):

        if Trigger == '적전원사망':
            self.Regenerate = True
        
        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료', '적턴시작결산'):
            if self.Regenerate == True:
                    self.Game.CurrentWave += 1
                    if self.Game.CurrentWave == self.Game.MaximumWave:
                        self.Game.Terminal = True

                    self.Regenerate = False
                    self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, 적 전원 사망, 적 리필, {self.Game.CurrentWave+1}번째 웨이브\n")
                    if self.Game.Terminal == False:
                        self.Game.Enemys = []
                        for Enemy in self.Game.Regenerate:
                            enemy = Enemy[0](Enemy[1], Enemy[2])
                            self.Game.Enemys.append(enemy)
                        for Enemy in self.Game.Enemys:
                            Enemy.AddToGame(self.Game)
                            Enemy.Init()
                        
                        self.Game.TriggerList.remove(self)
                        self.Game.TriggerList.append(Regenerate(self.Game))

                        if self.Game.TurnObject != '없음':
                            self.Game.TurnObject.EndTurn()
                        for Character in self.Game.Characters:
                            Character.ActionGauge = 0
                            Character.UltimateActiveCheck = False
                        for Summons in self.Game.Summons:
                            Summons.ActionGauge = 0

                        self.Game.CurrentTime = self.Game.GetCurrentRoundTime()
                        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 라운드 시간으로 게임 시간 조정, 모든 행동게이지 0으로 초기화 \n")
                        self.Game.CalcTurn()
                        self.Game.ActiveTrigger('적리젠', None, None, None)

        