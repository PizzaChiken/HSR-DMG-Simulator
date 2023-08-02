class MusketeerOfWildWheat:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['공격력%증가'] += 0.12
        if self.SetCount >= 4:
            self.Object.BaseStat['속도%증가'] += 0.06
            self.Object.BaseStat['일반공격피해증가'] += 0.1
        
    def Active(self, Trigger, Attacker, Target, Value):
        pass