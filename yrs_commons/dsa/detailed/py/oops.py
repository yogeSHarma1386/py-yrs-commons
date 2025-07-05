from pprint import pprint


class GP:
    def __init__(self):
        print("[S] GP")
        super().__init__()
        print("[E] GP")

        self._unmangled = 1  # protected
        self.__mangled = 1  # private

class Mil2(GP):
    def __init__(self):
        print("[S] P2")
        super().__init__()
        print("[E] P2")

class Mil1(GP):
    def __init__(self):
        print("[S] P1")
        super().__init__()
        print("[E] P1")

class Genz(Mil2, Mil1):
    def __init__(self):
        print("[S] Genz")
        super().__init__()
        print("[E] Genz")


if __name__ == "__main0__":
    gp = GP()
    print(gp._unmangled)
    print(gp._GP__mangled)

    print()
    obj = Genz()
    print(obj._unmangled)

    print()
    print(dir())
    print('GP MRO: ', GP.__mro__)
    print('Gz MRO: ', Genz.__mro__)


