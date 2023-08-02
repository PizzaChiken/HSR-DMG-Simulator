class SomethingIrreplaceable: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1164
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 396
        self.Object.BaseStat['공격력%증가'] += [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1]
        self.Value1 = [0.08, 0.09, 0.1, 0.11, 0.12][self.SuperImpose-1]
        self.Value2 = [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1]
        self.Start = False
        self.Attacked = False
        self.Possible = True

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object:
                self.Possible = True
                
        if Trigger in ('적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
            self.Start = True

        if Trigger == '데미지발동종료':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Start == True:
                    if self.Object in Target:
                        self.Attacked = True

        if Trigger in ('적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료'):
            if self.Start == True:
                if self.Attacked == True:
                    if self.Possible == True:
                        self.Possible = False
                        self.Object.Game.ApplyHeal(self.Object, self.Object, [0, self.Value1, 0], 0, '대체할수없는것힐', Except = self)
                        self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '대체할수없는것피증', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.Value2)]}, Except = self)
            self.Start = False
            self.Attacked = False
        
        if Trigger in ('적사망', '적전원사망'):
            if Attacker == self.Object:
                if self.Possible == True:
                    self.Possible = False
                    self.Object.Game.ApplyHeal(self.Object, self.Object, [0, self.Value1, 0], 0, '대체할수없는것힐', Except = self)
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '대체할수없는것피증', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('모든피해증가', self.Value2)]}, Except = self)