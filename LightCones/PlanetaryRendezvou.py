class PlanetaryRendezvou: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 423
        self.Object.BaseStat['기초방어력'] += 330
        self.Value1 = [0.12, 0.15, 0.18, 0.21, 0.24][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker in self.Object.Game.Characters:
                    if Attacker.Element == self.Object.Element:
                        Attacker.TempBuffList.append(('모든피해증가', self.Value1))