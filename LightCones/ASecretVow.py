class ASecretVow: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 264
        self.Object.BaseStat['모든피해증가'] += [0.2, 0.25, 0.3, 0.35, 0.4][self.SuperImpose-1]
        self.Value1 = [0.2, 0.25, 0.3, 0.35, 0.4][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    AttackerMaxHP = Attacker.CurrentStat['기초HP'] * (1 + Attacker.CurrentStat['HP%증가']) + Attacker.CurrentStat['고정HP증가']
                    AttackerHPRatio = Attacker.CurrentHP / AttackerMaxHP

                    TargetMaxHP = Target[0].CurrentStat['기초HP'] * (1 + Target[0].CurrentStat['HP%증가']) + Target[0].CurrentStat['고정HP증가']
                    TargetHPRatio = Target[0].CurrentHP / TargetMaxHP

                    if TargetHPRatio >= AttackerHPRatio:
                        Attacker.TempBuffList.append(('모든피해증가', self.Value1))                    
                    