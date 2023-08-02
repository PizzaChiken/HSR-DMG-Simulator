class EchoesOfTheCoffin: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1164
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 396
        self.Object.BaseStat['공격력%증가'] += [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1] 
        self.Value1 = [3, 3.5, 4, 4.5, 5][self.SuperImpose-1]
        self.Value2 = [12, 14, 16, 18, 20][self.SuperImpose-1]
        self.Start = False
        self.Attack = False
        self.Targets = []

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                self.Start = True
                self.Targets = []

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker == self.Object:
                        if Target[0] not in self.Targets:
                            self.Targets.append(Target[0])
                        self.Attack = True
        
        if  Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                if self.Attack == True:
                    self.Object.EnergyGenerate(min(3, len(self.Targets)) * self.Value1, False)
            self.Start = False
            self.Attack = False
            self.Targets = []

        if Trigger == '캐릭터필살기발동종료':
            if Attacker == self.Object:
                for Character in self.Object.Game.Characters:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Character, Buff ={'버프형태' : '스탯', '설명' : '관의울림가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('고정속도증가', self.Value2)]}, Except = self)