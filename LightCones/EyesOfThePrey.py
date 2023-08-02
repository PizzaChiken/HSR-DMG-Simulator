class EyesOfThePrey: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 952
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 330
        self.Object.BaseStat['효과명중'] += [0.2, 0.25, 0.3, 0.35, 0.4][self.SuperImpose-1]
        self.Object.BaseStat['지속피해피해증가'] += [0.24, 0.3, 0.36, 0.42, 0.48][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        pass