class TodayIsAnotherPeacefulDay: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 846
        self.Object.BaseStat['기초공격력'] += 529
        self.Object.BaseStat['기초방어력'] += 330
        self.Value1 = [0.002, 0.0025, 0.003, 0.0035, 0.004][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '게임시작':
            self.Object.BaseStat['모든피해증가'] += min(160, self.Object.BaseStat['에너지최대치']) * self.Value1
            self.Object.CalcCurrentStat()