class IncessantRain: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 463
        self.Object.BaseStat[f'효과명중'] += [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1]
        self.Value1 = [0.12, 0.14, 0.16, 0.18, 0.2][self.SuperImpose-1]
        self.Value2 = [0.12, 0.14, 0.16, 0.18, 0.2][self.SuperImpose-1]
        self.Stack = 0
        self.Start = False
        self.Targets = []


    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터일반공격발동시작' or Trigger =='캐릭터전투스킬발동시작' or Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '데미지발동시작':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker == self.Object:
                    Attacker.TempBuffList.append(('치명타확률', self.Value1))
                    if self.Start == True:
                        if all([Debuff['설명'] != '계속내리는비-에테르코드' for Debuff in Target[0].DebuffList]):
                            if Target[0] not in self.Targets:
                                self.Targets.append(Target[0])

        
        if Trigger == '캐릭터일반공격발동종료' or Trigger =='캐릭터전투스킬발동종료' or Trigger == '캐릭터필살기발동종료':
            if self.Start == True:
                for target in self.Targets:
                    self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = target, BaseProbability = 1.0, Debuff = {'디버프형태' : '스탯', '설명' : '계속내리는비-에테르코드', '남은턴' : 1, '효과' : [('받는피해증가', self.Value2)]}, Except = self)
            self.Start = False
            self.Targets = []