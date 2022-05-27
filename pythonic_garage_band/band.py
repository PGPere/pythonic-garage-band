class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar')

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'bass')

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drums')

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

