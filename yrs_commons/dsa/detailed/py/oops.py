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


import os
import re


if __name__ == "__main__":
    sample_folders = os.listdir("/Users/yogeshsharma/Projects/InterVuz/walkccc-LeetCode/solutions")
    # One-liner version
    compact_dict = {re.match(r'^(\d+)\.', f).group(1): f
                    for f in sample_folders
                    if re.match(r'^(\d+)\.', f)}
    compact_dict = {no: f"{f}/{no}.py" for no, f in compact_dict.items()}

    pprint({f"//{no}.py": f"{f}" for no, f in compact_dict.items()})



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


