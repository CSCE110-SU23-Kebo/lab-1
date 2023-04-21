class Engine:

    def __init__(self):
        self.__price = 4600

    def setPrice(self, value):
        self.__price = value


class Aircraft:
    def __init__(self, model):
        self.model = model


class Helicopter(Aircraft):
    engine_grade = 600

    def __init__(self, propellers):
        self.power = propellers * self.engine_grade


class Jet:

    def takeOff(self):
        print("A jet can take off on a runway")

    def land(self):
        print("A jet can land vertically")


class Helicopter:

    def takeOff(self):
        print("A helicopter can take off vertically")

    def land(self):
        print("A helicopter can land vertically")
