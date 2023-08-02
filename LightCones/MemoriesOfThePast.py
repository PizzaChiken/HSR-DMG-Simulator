class MemoriesOfThePast: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 952
        self.Object.BaseStat['기초공격력'] += 423
        self.Object.BaseStat['기초방어력'] += 396
        self.Object.BaseStat['격파특수효과'] += [0.28, 0.35, 0.42, 0.49, 0.56][self.SuperImpose-1]
        self.Value1 = [4, 5, 6, 7, 8][self.SuperImpose-1]
        self.Start = False
        self.Attack = False

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
                    self.Object.EnergyGenerate(self.Value1, False)
            self.Start = False
            self.Attack = False