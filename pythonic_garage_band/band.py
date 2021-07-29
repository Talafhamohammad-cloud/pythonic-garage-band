
class Musician:
    members = []

    def __init__(self, name):
        self.name = name
        Musician.members.append(self.name)


class Band(Musician):
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    