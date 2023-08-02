class InTheNight: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582.12
        self.Object.BaseStat['기초방어력'] += 463.05
        self.Object.BaseStat['치명타확률'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Value1 = [0.06, 0.07, 0.08, 0.09, 0.1][self.SuperImpose-1]
        self.Value2 = [0.12, 0.14, 0.16, 0.18, 0.2][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    speed = self.Object.CalcSpeed()
                    if speed >= 100:
                        stack = (speed - 100)//10
                        if stack > 6:
                            stack = 6
                        self.Object.TempBuffList.append(('일반공격피해증가', self.Value1 * stack))
                        self.Object.TempBuffList.append(('전투스킬피해증가', self.Value1 * stack))
                        if Value[0] == '필살기':
                            self.Object.TempBuffList.append(('치명타피해', self.Value2 * stack))
                    
                