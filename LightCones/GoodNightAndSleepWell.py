class GoodNightAndSleepWell: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 952
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 330
        self.Value1 = [0.12, 0.15, 0.18, 0.21, 0.24][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('데미지발동시작', '도트데미지발동시작'):
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    stack = len(Target[0].DebuffList)
                    if stack > 3:
                        stack = 3
                    self.Object.TempBuffList.append(('모든피해증가', self.Value1 * stack))