from time import sleep
from itertools import cycle
from colorama import Fore

dict_num = {0: "⓿", 1: "❶", 2: "❷", 3: "❸", 4: "❹", 5: "❺", 6: "❻", 7: "❼", 8: "❽", 9: "❾", 10: "❿"}

class TrafficLight:
    __color = cycle(["✋ red", "⌚ yellow", "⛹ green"])
    def running(self, n_times):
        for i in range(n_times):
            for ii in range(1, 4):
                print(Fore.RED if ii == 1 else Fore.YELLOW if ii == 2 else Fore.GREEN, next(TrafficLight.__color), sep="", flush=True)
                print(self.sleeper(7 if ii != 2 else 3), '\r', sep="", end="", flush=True)
        print(Fore.WHITE + f'Traffic light worked {n_times} times and finally switched off', '\r', end="")
    def sleeper(self, n):
        for i in range(n + 1):
            print('\r', "".join((dict_num.get(n - i), " seconds")), sep="", end="", flush=True)
            sleep(1)

svetofor = TrafficLight()
svetofor.running(3)