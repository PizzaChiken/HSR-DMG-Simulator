class PasserByOfWnderingCloud:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['치유량보너스'] += 0.1
        
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '게임시작':
                self.Object.Game.ChangeSkillPoint(1)