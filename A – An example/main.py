import sys
import math


class Street:
    def __init__(self, name, B, E, L):
        self.name = name
        self.B = B
        self.E = E
        self.L = L

    def toString(self) -> str:
        return "{} {}".format(self.name, str(self.Time))


class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self) -> str:
        return str(self.path)


def getCarsOnThisStreet(street):
    count = 0
    for car in cars:
        if street.name in car.path:
            count += 1
    return count


def carsStartingAtThisStreet(street):
    count = 0
    for car in cars:
        if street.name == car.path[0]:
            count += 1
    return count


def getCarsOnThisStreetNotCount(street):
    print("Here")
    newCarsList = list()
    for car in cars:
        print(car.path)
        if street.name in car.path:
            newCarsList.append(car)
    return newCarsList


def getStreetByName(streetName):
    for street in streets:
        if street.name == streetName:
            return street


def getTotalTimeForThisCar(car):
    time = 0
    for street in car.path:
        time += getStreetByName(street).L
    return time


def getTotalTimeOfCarsOnThisStreetKaSummation(street):
    time = 0

    for car in getCarsOnThisStreetNotCount(street):

        time += car.TotalTime
    return time


if __name__ == "__main__":
    with open(sys.argv[1], "r") as inputFile:
        D, I, S, V, F = [int(x) for x in inputFile.readline().split()]
        streets = list()
        intersections = dict()
        for _ in range(S):
            streetDetails = inputFile.readline().split()
            street = Street(streetDetails[2], int(streetDetails[0]), int(
                streetDetails[1]), int(streetDetails[3]))
            streets.append(street)
            streetsAtIntersection = intersections.get(street.E, list())
            streetsAtIntersection.append(street)
            intersections[street.E] = streetsAtIntersection
        cars = list()
        for _ in range(V):
            cars.append(Car(inputFile.readline().split()[1::]))
            cars[-1].TotalTime = getTotalTimeForThisCar(cars[-1])
            # print(cars[-1].TotalTime)

    for street in streets:

        x = getTotalTimeOfCarsOnThisStreetKaSummation(street)
        # print(x)
        street.priority = 0
        if x:
            street.priority = 1/x
        street.carsStartingHere = carsStartingAtThisStreet(street)

    # sortedStreets = sorted(streets, key=lambda x: x.priority, reverse=True)

    result = dict()

    for id in intersections.keys():
        streetsAtThisIntersection = [
            street for street in intersections[id] if street.priority > 0]
        for street in streetsAtThisIntersection:
            street.Time = math.ceil(
                street.priority/(len(streetsAtThisIntersection) + street.L))
        streetsAtThisIntersection = sorted(
            streetsAtThisIntersection, key=lambda x: x.carsStartingHere, reverse=True)
        if(len(streetsAtThisIntersection) > 0):
            result[id] = streetsAtThisIntersection

    with open(sys.argv[1].split(".")[0] + "1.result", "w") as outputFile:
        outputFile.write("{}\n".format(str(len(result.keys()))))
        for id in result.keys():
            outputFile.write("{}\n".format(id))
            outputFile.write("{}\n".format(str(len(result[id]))))
            outputFile.write("{}\n".format(
                "\n".join([x.toString() for x in result[id]])))
            pass
        pass
