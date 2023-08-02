class TheMolesWelcomeYou: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 264
        self.Value1 = [0.12, 0.15, 0.18, 0.21, 0.24][self.SuperImpose-1]

        self.Stack = [0, 0, 0] # NA, BSkill, Ultimate

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동종료':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if Value[0] == '일반공격':
                        if self.Stack[0] == 0:
                            self.Stack[0] = 1
                            self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '두더지파공증', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('공격력%증가', sum(self.Stack) * self.Value1)]}, Except = self)
                    elif Value[0] == '전투스킬':
                        if self.Stack[1] == 0:
                            self.Stack[1] = 1
                            self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '두더지파공증', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('공격력%증가', sum(self.Stack) * self.Value1)]}, Except = self)
                    elif Value[2] == '필살기':
                        if self.Stack[2] == 0:
                            self.Stack[2] = 1
                            self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '두더지파공증', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('공격력%증가', sum(self.Stack) * self.Value1)]}, Except = self)
