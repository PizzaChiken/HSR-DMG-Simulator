class InTheNameOfTheWorld: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582.12
        self.Object.BaseStat['기초방어력'] += 463.05
        self.Element = Object.Element
        self.Value1 = [0.24, 0.28, 0.32, 0.36, 0.4]
        self.Value2 = [0.18, 0.21, 0.24, 0.27, 0.3]
        self.Value3 = [0.24, 0.28, 0.32, 0.36, 0.4]
        self.Start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터전투스킬발동시작':
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '디버프발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if self.Start ==  True:
                        self.Object.TempBuffList.append(('효과명중', self.Value2[self.SuperImpose-1]))

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if len(Target[0].DebuffList) > 0 :
                        self.Object.TempBuffList.append((f'{self.Element}속성피해증가', self.Value1[self.SuperImpose -1]))
                    if self.Start == True:
                        self.Object.TempBuffList.append(('공격력%증가', self.Value3[self.SuperImpose-1]))
        
        if Trigger == '캐릭터전투스킬발동종료':
            if Attacker == self.Object:
                if self.Start == True:
                    self.Start = False