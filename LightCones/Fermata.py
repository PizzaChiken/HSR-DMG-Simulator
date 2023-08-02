class Fermata: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 952
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 330
        self.Object.BaseStat['격파특수효과'] += [0.16, 0.2, 0.24, 0.28, 0.32][self.SuperImpose-1]
        self.Value1 = [0.16, 0.2, 0.24, 0.28, 0.32][self.SuperImpose-1]

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('데미지발동시작', '도트데미지발동시작'):
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    if any([debuff['디버프형태'] in ('감전', '풍화') for debuff in Target[0].DebuffList]):
                        self.Object.TempBuffList.append(('모든피해증가', self.Value1))