import math


class Street:
    def __init__(self, name, street_length):
        self.street_name = name
        self.street_length = street_length

    street_name = ''
    street_length = 0


class Intersection:
    def __init__(self, id, streets):
        self.intersection_id = id
        self.streets = streets

    intersection_id = 0
    streets = []


class Data:
    def __init__(self):
        self.intersections = []


def format_data(data, name):
    f = open("rendu{0}.txt".format(name), "w")

    f.write(str(len(data.intersections)) + '\n')
    for intersection in data.intersections:
        f.write(str(intersection.intersection_id) + '\n')
        f.write(str(len(intersection.streets)) + '\n')
        for street in intersection.streets:
            f.write(street.street_name + ' ' + str(street.street_length) + '\n')
    f.close()


filenames = ['f.txt']


def parse(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        D, I, S, V, F = lines[0].split()
        D, I, S, V, F = int(D), int(I), int(S), int(V), int(F)
        Streets = {}
        Vehicles = []
        StreetsUsed = []
        for i in range(1, S + 1):
            line = lines[i].split()
            Streets[line[2]] = (int(line[0]), int(line[1]), int(line[3]))
        for i in range(S + 1, S + 1 + V):
            line = lines[i].split()
            Vehicles.append((int(line[0]), line[1:]))
            StreetsUsed += line[1:]
        return D, I, S, V, F, Streets, Vehicles, StreetsUsed


def CalculTimeForTravel(Vehicles, Streets):
    res = []
    for v in Vehicles:
        tt = 0
        for s in v[1][1:]:
            tt += Streets[s][2]
        res.append(tt)
    return res

def average(Streets):
    avg = 0
    for S in Streets:
        avg += Streets[S][1]
    return avg / len(Streets)


def ponderation(duration, intersection, street, Streets, StreetsUsed, nbVehicles, driversInIntersection, numberOfStreetsOfIntersection):
    inter = math.ceil(StreetsUsed.count(street) / driversInIntersection) * average(Streets) / 2
    return max(1,math.ceil(inter))


def getWorstTimingForIntersection(duration, nbIntersection, Streets, StreetsUsed):
    return duration / nbIntersection



for f in filenames:
    print("Processing " + f + "...", end='')
    D, I, S, V, F, Streets, Vehicles, StreetsUsed = parse(f)
    result_streets = []
    inter = None
    number_of_streets_of_intersections = []
    number_of_drivers_of_intersections = []
    res = Data()
    for i in range(I):
        result_streets = []
        numberOfStreetsOfIntersection = 0
        driversInIntersection = 0
        for s in Streets:
            numberOfStreetsOfIntersection += 1
            if Streets[s][1] == i:
                driversInIntersection += StreetsUsed.count(s)
        number_of_drivers_of_intersections.append(driversInIntersection)
        number_of_streets_of_intersections.append(numberOfStreetsOfIntersection)
        for S in Streets:
            if Streets[S][1] == i and S in StreetsUsed:
                result_streets.append(Street(S, ponderation(D, i, S, Streets, StreetsUsed, V,
                                                            number_of_drivers_of_intersections[i],
                                                            number_of_streets_of_intersections[i])))
        if result_streets:
            inter = Intersection(i, result_streets)
            res.intersections.append(inter)
    format_data(res, f.split('.')[0])
    print(' Done!')
    res.intersections = []


def result(D, I, S, V, F, Streets, Vehicles):
    pass

# print(D, I, S, V, F, Streets, Vehicles, StreetsUsed, sep='\n', end='\n')
