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
        "Local 918",
        "Local 152",
        "Local 416",
        "Local 494",
        "Local 1049",
        "Local 322",
        "Local 518",
        "Local 279",
        "Local 1143",
        "Local 583",
        "Local 1092",
        "Local 300",
        "Local 673",
        "Local 354",
        "Local 516",
        "Local 647",
        "Local 1312",
        "Local 72",
        "Local 583",
        "Local 712",
        "Local 416",
        "Local 494",
        "Local 698",
        "Local 139",
        "Local 132",
        "Local 472",
        "Local 96",
        "Local 22",
        "Local 1039",
        "Local 312",
        "Local 1000",
        "Local 91",
        "Local 2266",
        "Local 62",
        "Local 64",
        "Local 329",
        "Local 337",
        "Local 124",
        "Local 968",
        "Local 787",
        "Local 1334",
        "Local 357",
        "Local 233",
        "Local 902",
        "Local 1986",
        "Local 2305",
        "Local 847",
        "Local 688",
        "Local 808",
        "Local 837",
        "Local 309",
        "Local 123",
    ]


