class ResolutionShinesAsPearlsOfSweat: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 952
        self.Object.BaseStat['기초공격력'] += 476
        self.Object.BaseStat['기초방어력'] += 330
        self.Prob = [0.6, 0.7, 0.8, 0.9, 1.0][self.SuperImpose-1]
        self.Value = [0.12, 0.13, 0.14, 0.15, 0.16][self.SuperImpose-1]
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
                    if self.Start == True:
                        if all([Debuff['설명'] != '땀방울함락' for Debuff in Target[0].DebuffList]):
                            if Target[0] not in self.Targets:
                                self.Targets.append(Target[0])

        
        if Trigger == '캐릭터일반공격발동종료' or Trigger =='캐릭터전투스킬발동종료' or Trigger == '캐릭터필살기발동종료':
            if self.Start == True:
                for target in self.Targets:
                    self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = target, BaseProbability = self.Prob, Debuff = {'디버프형태' : '스탯', '설명' : '땀방울함락', '남은턴' : 1, '효과' : [('방어력감소', self.Value)]}, Except = self)
            self.Start = False
            self.Targets = []