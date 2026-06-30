class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [0] * len(position)
        fleets = []

        for i in range(len(position)):
            cars[i] = (position[i], speed[i])
        
        cars = sorted(cars, key = lambda x: x[0], reverse = True )

        print(cars)

        for car in cars:

            fleets.append(car)

            if len(fleets) <= 1:
                continue
            else:
                timeToTargetCurrent = (target - car[0]) / car[1]
                timeToTargetPrevious = (target - fleets[-2][0]) / fleets[-2][1]

                if timeToTargetCurrent <= timeToTargetPrevious:
                    fleets.pop()
            print(fleets)
        # print(cars)
        # print(fleets)

        return len(fleets)
        