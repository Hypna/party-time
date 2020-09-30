class Character:
    BASE_DAYS_NO_FOOD = 3
    RATION_RATE = {
        'FULL': 1.0,
        'HALF': 0.5,
        'NONE': 0.0
    }

    def __init__(self, name, constitution_mod=0):
        self.constitution_mod = constitution_mod
        self.ration = 'FULL'
        self.days_without_food = 0
        self.exhaustion_level = 0
        self.name = name

    def live_day(self, rest=True):
        if self.ration == 'FULL':
            self.days_without_food = 0
            if rest:
                self.exhaustion_level -= 1
        else:
            self.days_without_food += 1 - Character.RATION_RATE[self.ration]
            if self.char_days_no_food < self.days_without_food:
                self.exhaustion_level += 1
    
    def char_days_no_food(self):
        return Character.BASE_DAYS_NO_FOOD + int(self.constitution_mod)