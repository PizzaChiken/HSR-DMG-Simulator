class TimeWaitsForNoOne: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1270
        self.Object.BaseStat['기초공격력'] += 476.28
        self.Object.BaseStat['기초방어력'] += 463.05
        self.Object.BaseStat['HP%증가'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Object.BaseStat['치유량보너스'] += [0.12, 0.14, 0.16, 0.18, 0.2][self.SuperImpose-1]
        self.Value1 = [0.36, 0.42, 0.48, 0.54, 0.6][self.SuperImpose-1]
        self.CumulativeHeal = 0
        self.Start = True

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '힐발동종료':
            if Attacker == self.Object:
                self.CumulativeHeal += Value[0]

        if Trigger == '캐릭터턴시작':
            if Attacker == self.Object:
                self.Start = True
        
        if Trigger == '데미지발동종료':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if Attacker in self.Object.Game.Characters and Attacker != self.Object:
                    if self.Start == True:
                        DMG = self.CumulativeHeal * self.Value1
                        self.Object.Game.ApplyDamage(Attacker = self.Object, Target = Target[0], Element = '번개', DamageType = '추가피해', Toughness = 0, Multiplier = [0.0, 0.0, 0.0], FlatDMG = DMG, DamageName = '세월은흐를뿐', Except = self)
                        self.Start = False
                        self.CumulativeHeal = 0
                
                