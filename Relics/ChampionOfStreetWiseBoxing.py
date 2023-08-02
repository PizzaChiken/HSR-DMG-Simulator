class ChampionOfStreetWiseBoxing:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        self.Start = False
        self.Attacked = False
        self.stack = 0
        if self.SetCount >= 2:
            self.Object.BaseStat['물리속성피해증가'] += 0.1
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작', '적일반공격발동시작', '적전투스킬발동시작', '적필살기발동시작', '적추가공격발동시작'):
                self.Start = True

            if Trigger == '데미지발동시작':
                if self.Start == True:
                    if (Attacker == self.Object) or (self.Object in Target) :
                        self.Attacked = True
            
            if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료', '적일반공격발동종료', '적전투스킬발동종료', '적필살기발동종료', '적추가공격발동종료'):
                if self.Start == True:
                    if self.Attacked == True:
                        self.stack = min(self.stack + 1, 5)
                        self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '스트리트격투왕', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('공격력%증가', 0.05 * self.stack)]}, Except = self)
                self.Start = False
                self.Attacked = False