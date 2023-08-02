class SprightlyVonwacq:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount == 2:
            self.Object.BaseStat['에너지회복효율'] += 0.05
        else:
            raise ValueError
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount == 2:
            if Trigger == '게임시작':
                if self.Object.CalcSpeed() >= 120:
                    self.Object.ChangeActionGauge(4000)