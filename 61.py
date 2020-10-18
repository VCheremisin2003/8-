import time
class Trafficlight:
    #атрибуты
    __color = "red"
    #методы
    def running():
        print("red")
        time.sleep(7)
        print('green')
        time.sleep(7)
        print("yellow")
        time.sleep(3)
        Trafficlight.running()
c = Trafficlight
c.running()