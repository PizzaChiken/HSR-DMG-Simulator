class BeforeTheTutorialMissionStarts: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 463
        self.Object.BaseStat[f'효과명중'] += [0.2, 0.25, 0.3, 0.35, 0.4][self.SuperImpose-1]
        self.Value1 = [4, 5, 6, 7, 8][self.SuperImpose-1]
        self.Stack = 0
        self.Start = False
        self.Attack = False


    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터일반공격발동시작' or Trigger =='캐릭터전투스킬발동시작' or Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker == self.Object:
                        for Debuff in Target[0].DebuffList:
                            if Debuff['디버프형태'] == '스탯':
                                for stats in Debuff['효과']:
                                    if stats[0] == '방어력감소':
                                        self.Attack = True
            
        if Trigger == '캐릭터일반공격발동종료' or Trigger =='캐릭터전투스킬발동종료' or Trigger == '캐릭터필살기발동종료':
            if self.Start == True:
                if self.Attack == True:
                    self.Object.EnergyGenerate(self.Value1, False)
            self.Start = False
            self.Attack = False