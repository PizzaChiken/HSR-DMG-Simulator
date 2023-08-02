class LongevousDisciple:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        self.Start = False
        self.Attacked = False
        self.Stack = 0
        if self.SetCount >= 2:
            self.Object.BaseStat['HP%증가'] += 0.12
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger in ('적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
                self.Start = True

            if Trigger == '데미지발동종료':
                if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                    if self.Start == True:
                        if  (self.Object in Target):
                            self.Attacked = True

            if Trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료'):
                if self.Start == True:
                    if self.Attacked == True:
                        self.Stack = min(2, self.Stack + 1)
                        self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '장수를원하는제자치확', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('치명타확률', 0.08 * self.Stack)]}, Except = self)
                self.Start = False
                self.Attacked = False
            
            if Trigger == '캐릭터체력소모':
                if self.Object in Target:
                    self.Stack = min(2, self.Stack + 1)
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '장수를원하는제자치확', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('치명타확률', 0.08 * self.Stack)]}, Except = self)

            if Trigger == '캐릭터턴종료':
                if Attacker == self.Object:
                    if not any([buff['설명'] == '장수를원하는제자치확' for buff in self.Object.BuffList]):
                        self.Stack = 0
