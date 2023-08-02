class EagleOfTwilightLine:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['바람속성피해증가'] += 0.1
        
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '캐릭터필살기발동시작':
                if Attacker == self.Object:
                    self.Object.ChangeActionGauge(2500)