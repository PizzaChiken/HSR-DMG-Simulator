class GeniusOfBrilliantStars:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['양자속성피해증가'] += 0.1
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작'):
                if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                    if Attacker == self.Object:
                        self.Object.TempBuffList.append(('방어력무시', 0.1))
                        WeakList = Target[0].WeakList.copy()
                        for Debuff in Target[0].DebuffList:
                            if Debuff['디버프형태'] == '약점부여':
                                WeakList += Debuff['속성']
                        if '양자' in WeakList:
                            self.Object.TempBuffList.append(('방어력무시', 0.1))
