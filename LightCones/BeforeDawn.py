class BeforeDawn: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582.12
        self.Object.BaseStat['기초방어력'] += 463.05
        self.Object.BaseStat['치명타피해'] += [0.36, 0.42, 0.48, 0.54, 0.6][self.SuperImpose-1]
        self.Object.BaseStat['전투스킬피해증가'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Object.BaseStat['필살기피해증가'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Value1 = [0.48, 0.56, 0.64, 0.72, 0.80][self.SuperImpose-1]
        self.SomnusCorpus = False
        self.Start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터전투스킬발동시작', '캐릭터필살기발동시작'):
            if Attacker == self.Object:
                self.SomnusCorpus = True
        
        elif Trigger == '캐릭터추가공격발동시작':
            if Attacker == self.Object:
                self.Start = True
        
        elif Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if self.Start == True:
                        if self.SomnusCorpus == True:
                            self.Object.TempBuffList.append(('추가공격피해증가', self.Value1))
        
        elif Trigger == '캐릭터추가공격발동종료':
            if Attacker == self.Object:
                if self.Start == True:
                    self.Start = False
                    self.SomnusCorpus = False
                else:
                    raise ValueError

                
                