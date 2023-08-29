from ClassList import ManageRelic
import copy

class BaseCharacter:
    def __init__(self, SkillLevel, Eidolons):
        self.Type = '캐릭터'
        self.Level = 80
        self.UltimateActiveCheck = False
        self.IsBroken = False
        self.IsDead = False
        self.TurnSkip = False
        self.TargetEnemy = None
        self.BuffList = [] # 캐릭터 턴 종료시 남은턴 줄어듬
        self.DebuffList = [] # 캐릭터 턴 시작시 남은턴 줄어듬
        self.TempBuffList = [] # 트리거로인해 공격 또는 디버프 또는 힐 부여시 한시적으로 추가되는 버프들 (ex 웰트 전무 전투스킬 피증) 
        self.TriggerList = [EntanglementCheck(self)]
        self.SkillLevel = SkillLevel # [일반공격레벨, 전투스킬레벨, 특성레벨, 필살기레벨] 리스트
        self.Eidolons = Eidolons # 성흔 레벨

        self.BaseStat = {'기초HP' : 0,
                         'HP%증가' : 0,
                         '고정HP증가' : 0,
                         '기초공격력': 0,
                         '공격력%증가' : 0,
                         '고정공격력증가' : 0,
                         '기초방어력': 0,
                         '방어력%증가' : 0,
                         '고정방어력증가' : 0,
                         '방어력무시' : 0,
                         '방어력감소' : 0,
                         '기초속도' : 0,
                         '속도%증가' : 0,
                         '고정속도증가' : 0,
                         '치명타확률' : 0.05,
                         '치명타피해' : 0.5,
                         '격파특수효과' : 0,
                         '약점격파효율' : 0,
                         '치유량보너스' : 0,
                         '에너지최대치' : 0,
                         '에너지회복효율' : 1,
                         '효과명중' : 0,
                         '효과저항' : 0,
                         '모든피해증가' : 0,
                         '물리속성피해증가' : 0,
                         '화염속성피해증가' : 0,
                         '얼음속성피해증가' : 0,
                         '번개속성피해증가' : 0,
                         '바람속성피해증가' : 0,
                         '양자속성피해증가' : 0,
                         '허수속성피해증가' : 0,
                         '일반공격피해증가' : 0,
                         '전투스킬피해증가' : 0,
                         '필살기피해증가' : 0,
                         '추가공격피해증가' : 0,
                         '추가피해피해증가' : 0,
                         '지속피해피해증가' : 0,
                         '모든속성저항증가' : 0,
                         '물리속성저항증가' : 0,
                         '화염속성저항증가' : 0,
                         '얼음속성저항증가' : 0,
                         '번개속성저항증가' : 0,
                         '바람속성저항증가' : 0,
                         '양자속성저항증가' : 0,
                         '허수속성저항증가' : 0,
                         '모든속성저항관통' : 0,
                         '물리속성저항관통' : 0,
                         '화염속성저항관통' : 0,
                         '얼음속성저항관통' : 0,
                         '번개속성저항관통' : 0,
                         '바람속성저항관통' : 0,
                         '양자속성저항관통' : 0,
                         '허수속성저항관통' : 0,
                         '열상저항' : 0,
                         '연소저항' : 0,
                         '감전저항' : 0,
                         '풍화저항' : 0,
                         '빙결저항' : 0,
                         '속박저항' : 0,
                         '얽힘저항' : 0,
                         '도발저항' : 0,
                         '받는피해증가' : 0,
                         '받는지속피해증가' : 0,
                         '기초도발' : 0,
                         '도발%증가' : 0,
                         '실드%증가' : 0}
        
        
        # self.BaseStat : 캐릭 기본 + 광추 + 유물
        # self.CurrentStat : BaseStat + Buff + Debuff, 버프 디버프 변동시마다 새로 계산됨
        # self.TempStat : CurrentStat + TempBuff, Game.ApplyDamage/Game.ApplyBreakDamage/Game.ApplyDoTDamage/Game.ApplyDebuff/Game.ApplyHeal 발동시 계산됨
        
    def AddToGame(self, Game):
        self.Game = Game
        for Trigger in self.TriggerList:
            self.Game.TriggerList.append(Trigger)

    def AddLightCone(self, LightCone, SuperImpose):
        self.TriggerList.append(LightCone(self, SuperImpose))

    def AddRelic(self, RelicList):
        ManageRelic(self, RelicList)
        
    def Init(self):
        self.CalcCurrentStat()
        self.ActionGauge = 0
        self.CurrentEnergy = 0.5 * self.CurrentStat['에너지최대치']
        self.CurrentHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']

        
    def NormalAttack(self, target):
        pass
    
    def BattleSkill(self, target):
        pass

    def Ultimate(self, target):
        pass

    def BattleSkillIsPossible(self):
        pass
        
    def CalcCurrentStat(self):
        self.CurrentStat = self.BaseStat.copy()
        for Buff in self.BuffList:
            if Buff['버프형태'] == '스탯':
                for BuffStat in Buff['효과']:
                    self.CurrentStat[BuffStat[0]] += BuffStat[1]
        for Debuff in self.DebuffList:
            if Debuff['디버프형태'] == '스탯' or Debuff['디버프형태'] == '속박' or Debuff['디버프형태'] == '약점부여':
                for DebuffStat in Debuff['효과']:
                    self.CurrentStat[DebuffStat[0]] += DebuffStat[1]

    def CalcSpeed(self):
        CurrentSpeed = self.CurrentStat['기초속도'] * (1 + self.CurrentStat['속도%증가']) + self.CurrentStat['고정속도증가']
        return CurrentSpeed

    def CalcTempStat(self):
        self.TempStat = self.CurrentStat.copy()
        if self.Game.PrintTempBuff == True:
            self.Game.AppendBattleHistory(self.Name + ' '+ str(self.TempBuffList))
        for TempBuff in self.TempBuffList:
            self.TempStat[TempBuff[0]] += TempBuff[1]

    def CheckBuffDuration(self, type):
        for Buff in self.BuffList:
            if Buff['시간타입'] == type:
                Buff['체크'] = True

    def ManageBuff(self):
        for Buff in self.BuffList.copy():
            if Buff['체크']:
                Buff['남은턴'] -= 1
                Buff['체크'] = False
            if Buff['남은턴'] == 0:
                self.DeleteBuff(Buff)
        
    def DeleteBuff(self, Buff):
        self.BuffList.remove(Buff)
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 버프 {Buff['설명']} 종료, 대상현재버프 : {[Buff['설명'] for Buff in self.BuffList]}")
        self.CalcCurrentStat()

    def ManageDebuff(self):
        for debuff in self.DebuffList.copy():
            if debuff['디버프형태'] == '빙결':
                self.TurnSkip = True
            if debuff['디버프형태'] == '도발':
                self.TargetCharacter = debuff['공격자']
            if debuff['디버프형태'] in('열상', '풍화',  '감전', '연소', '빙결', '얽힘'):
                self.Game.ApplyDoTDamage(self, debuff)
            debuff['남은턴'] -= 1
            if debuff['남은턴'] ==0:
                self.DeleteDebuff(debuff)


    def DeleteDebuff(self, Debuff):
        self.DebuffList.remove(Debuff)
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 디버프 {Debuff['설명']} 종료, 대상현재디버프 : {[Debuff['설명'] for Debuff in self.DebuffList]}")
        self.CalcCurrentStat()

    
    def StartTurn(self):
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 턴 시작")
        self.Game.ActiveTrigger('캐릭터턴시작', self, None, None)
        self.CheckBuffDuration('A')
        self.ManageDebuff()
        self.Game.ActiveTrigger('캐릭터턴시작결산', self, None, None)
        
    def EndTurn1(self):
        if self.TurnSkip == True:
            self.ActionGauge = 5000
        else:
            self.ActionGauge = 0
    
    def EndTurn2(self):
        self.TurnSkip = False
        self.TargetEnemy = None
        self.CheckBuffDuration('B')
        self.ManageBuff()
        self.Game.ActiveTrigger('캐릭터턴종료', self, None, None)
        self.Game.AppendBattleHistory(f"\n시간 : {self.Game.CurrentTime}, {self.Name} 턴 종료")
        self.Game.AppendBattleHistory(f"객체별 현재 속도       : {[char.Name + ' : ' + str(char.CalcSpeed()) for char in self.Game.Characters] + [Enemy.Name + ' : ' + str(Enemy.CalcSpeed()) for Enemy in self.Game.Enemys] + [Summons.Name + ' : ' + str(Summons.CalcSpeed()) for Summons in self.Game.Summons]}")
        self.Game.AppendBattleHistory(f"객체별 현재 행동게이지 : {[char.Name + ' : ' + str(char.ActionGauge) for char in self.Game.Characters] + [Enemy.Name + ' : ' + str(Enemy.ActionGauge) for Enemy in self.Game.Enemys] + [Summons.Name + ' : ' + str(Summons.ActionGauge) for Summons in self.Game.Summons]} \n")

    def EndTurn(self):
        self.EndTurn1()
        self.EndTurn2()
        
    def GetDamage(self, Attacker, Damage, Element, ToughnessDMG, Type):
        if self.IsDead == False:
            ShieldList = []
            for  Buff in self.BuffList:
                if Buff['버프형태'] == '실드':
                    ShieldList.append(Buff)

            MiNRemainDamage = Damage
            for Shield in ShieldList:
                RemainDamage = Damage - Shield['수치']
                if RemainDamage > 0:
                    self.DeleteBuff(Shield)
                else:
                    Shield['수치'] -= Damage
                    RemainDamage = 0
                if RemainDamage < MiNRemainDamage:
                    MiNRemainDamage = RemainDamage
            
            MaxHP = self.TempStat['기초HP'] * (1 + self.TempStat['HP%증가']) + self.TempStat['고정HP증가']
            if self.CurrentHP > MaxHP:
                self.CurrentHP = MaxHP # 만약 디버프로 인해 최대 HP값이 현재 HP보다 줄어들었다면 현재 HP는 최대 HP값으로 조정된다
            self.CurrentHP -= MiNRemainDamage
            self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {MiNRemainDamage} 감소, 현재 HP : {self.CurrentHP}, 최대 HP : {MaxHP}")

            if self.CurrentHP <= 0:
                self.CurrentHP = 0
                self.IsDead = True
                self.Game.IsDead(Attacker, self, Type)
            return MiNRemainDamage

    def ConsumesHP(self, Attacker, Multiplier, Flat):
        MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
        ConsumedHP = MaxHP * Multiplier + Flat
        if 0< self.CurrentHP <= 1:
             self.CurrentHP = 1
        ConsumedHP = min(self.CurrentHP-1, ConsumedHP)
        self.CurrentHP -= ConsumedHP
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {ConsumedHP} 소모, 현재 HP : {self.CurrentHP}, 최대 HP : {MaxHP}") 
        self.Game.ActiveTrigger('캐릭터체력소모', Attacker, [self], ConsumedHP)
        return ConsumedHP
        
        
    def GetHeal(self, Heal):
        MaxHP = self.CurrentStat['기초HP'] * (1 + self.CurrentStat['HP%증가']) + self.CurrentStat['고정HP증가']
        if self.CurrentHP > MaxHP:
            self.CurrentHP = MaxHP # 만약 디버프로 인해 최대 HP값이 현재 HP보다 줄어들었다면 현재 HP는 최대 HP값으로 조정된다
        RemainHeal = Heal
        if MaxHP-self.CurrentHP < Heal:
            RemainHeal = MaxHP-self.CurrentHP
            OverHeal = True
        else:
            OverHeal = False
        self.CurrentHP += RemainHeal
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 체력 {RemainHeal} 회복, 현재 HP : {self.CurrentHP}, 최대 HP : {MaxHP}")
        return OverHeal

    
    def EnergyGenerate(self, Value, Flat):
        if Flat == False:
            Value = Value * self.CurrentStat['에너지회복효율']
        self.CurrentEnergy += Value
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 에너지 {Value} 회복, 현재 에너지 : {self.CurrentEnergy}, 최대 에너지 : {self.CurrentStat['에너지최대치']}")

    def ChangeActionGauge(self, Value):
        self.ActionGauge += Value
        self.Game.AppendBattleHistory(f"시간 : {self.Game.CurrentTime}, 대상 : {self.Name}, 행동게이지 {Value} 변화, 현재 행동게이지 : {self.ActionGauge}")

    def CheckFrozen(self):
        for debuff in self.DebuffList:
            if debuff['디버프형태'] == '빙결':
                return True
            
    def NAIsPossible(self):
        return True

    def BattleSkillIsPossible(self):
        return True
            
class EntanglementCheck: #피격시 얽힘 중첩을 추가하고 # 스킬 1번에 여러번 피격당해도 1회만 적용
    def __init__(self, Object):
        self.Object = Object
        self.Start = False
        self.Attacked = False

    def Active(self, trigger, Attacker, Target, Value):
        if trigger in ('적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
            self.Start = True

        if trigger == '데미지발동시작':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Start == True:
                    if self.Object in Target:
                        self.Attacked = True
        
        if trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료'):
            if self.Start == True:
                if self.Attacked == True:
                    # 얽힘 중첩 추가
                    for Debuff in self.Object.DebuffList:
                        if Debuff['디버프형태'] == '얽힘':
                            Debuff['중첩'] +=1
                            if Debuff['중첩'] > 5:
                                Debuff['중첩'] = 5
            self.Start = False
            self.Attacked = False