class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [0] * len(position)
        fleets = []

        for i in range(len(position)):
            cars[i] = (position[i], speed[i])
        
        cars = sorted(cars, key = lambda x: x[0], reverse = True )

        print(cars)

        for car in cars:

            if len(fleets) == 0:
                fleets.append(car)
            else:
                timeToTargetCurrent = (target - car[0]) / car[1]
                timeToTargetPrevious = (target - fleets[-1][0]) / fleets[-1][1]

                if timeToTargetCurrent > timeToTargetPrevious:
                    fleets.append(car)
        
            print(fleets)

        return len(fleets)
        