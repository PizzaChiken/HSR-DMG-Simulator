class TheUnreachableSide: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1270
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 330
        self.Object.BaseStat['치명타확률'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Object.BaseStat['HP%증가'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1] 
        self.Value1 = [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1]
        self.Start = False
        self.Attacked = False
        self.Attack = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동종료':
            if Attacker.Type == '적' and Target[0].Type == '캐릭터':
                if self.Object in Target:
                    self.Attacked = True
        
        if Trigger == '캐릭터체력소모':
            if self.Object in Target:
                if Value >= 0:
                    self.Attacked = True
                else:
                    for History in self.Object.Game.BattleHistory:
                        print(History)
                    print(Value)
                    raise ValueError

        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if self.Attacked == True:
                        if Attacker == self.Object:
                            Attacker.TempBuffList.append(('모든피해증가', self.Value1))
                            self.Attack = True
        
        if  Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                self.Start = False
                if self.Attack == True:
                    self.Attack = False
                    self.Attacked = False