class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        print(Musician.get_count())
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    @classmethod
    def get_count(cls):
        return Guitarist.count
        # Bassist.count + Drummer.count


class Guitarist(Musician):
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name):
        super().__init__(name, 'guitar')
        self.name = name
        Guitarist.count += 1

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'guitar'

    @classmethod
    def play_solo(cls):
        return "face melting guitar solo"


class Bassist(Musician):
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name):
        super().__init__(name, 'bass')
        self.name = name
        Bassist.count += 1

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'bass'

    @classmethod
    def play_solo(cls):
        return "bom bom buh bom"


class Drummer(Musician):
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name):
        super().__init__(name, 'drums')
        self.name = name
        Drummer.count += 1

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'drums'

    @classmethod
    def play_solo(cls):
        return "rattle boom crash"
