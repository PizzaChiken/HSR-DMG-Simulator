class OnTheFallOfAnAeon: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 529
        self.Object.BaseStat['기초방어력'] += 396
        self.Value1 = [0.08, 0.1, 0.12, 0.14, 0.16][self.SuperImpose-1]
        self.Value2 = [0.12, 0.15, 0.18, 0.21, 0.24][self.SuperImpose-1]
        self.Start = False
        self.Attack = False
        self.Stack = 0


    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker == self.Object:
                        self.Attack = True
        
        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                if self.Attack == True:
                    self.Stack = min(4, self.Stack+1)
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '에이언즈공증', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('공격력%증가', self.Stack * self.Value1)]}, Except = self)
            self.Start = False
            self.Attack = False
        
        if Trigger == '적격파됨':
            if Attacker == self.Object:
                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '에이언즈격파피증', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('모든피해증가', self.Value2)]}, Except = self)


