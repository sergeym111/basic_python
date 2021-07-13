from time import sleep


class TrafficLight:
    __color = {1: ['red', 7],
               2: ['yellow', 2],
               3: ['green', 4]}

    def running(self):
        while True:
            for key in self.__color:
                print(self.__color[key][0])
                sleep(self.__color[key][1])


trafficlight_1 = trafficlight()
trafficlight_1.running()
