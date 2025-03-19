from time import time_ns
i = 0
fulltime = 0
def benchmark(f):
    def _benchmark(*args, **kw):
        global i
        i += 1
        global fulltime
        start_time = time_ns()
        result = f(*args, **kw)
        elapsed_time = time_ns() - start_time
        fulltime += elapsed_time
        return result
    return _benchmark
@benchmark
def delen(chisl,system):
    global rezultat
    zal=chisl%system
    rez=chisl//system
    print(f"{chisl} / {system} = {rez} при залишку {zal}")
    if rezultat == None:
        rezultat = zal
    else:
        rezultat = str(zal)+str(rezultat)
    return rez
peremen = int(input("Введіть десяткове число: "))
system = int(input("Введіть бажану для переводу систему числення (2/8/16): "))
rezultat=None
while peremen >= 1:
    peremen=delen(peremen,system)
print(f"Число {peremen} в {system}-й системі:{rezultat}")
print(f"Функція налічує {i} дій")
print(f"Загальний час виконання всіх функцій:{fulltime} нс")
