from .character import Character

class Party:
    def __init__(self):
        self.members = []
        self.rations = 0

    def add_char(self, name, con_mod=0):
        self.members.append(Character(name, con_mod))

    def set_char_ration(self, index, ration):
        self.members[index]