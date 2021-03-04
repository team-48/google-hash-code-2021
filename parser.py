def parse(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        D, I, S, V, F = lines[0].split()
        D, I, S, V, F = int(D), int(I), int(S), int(V), int(F)
        Streets = {}
        Vehicles = []
        StreetsUsed = []
        for i in range(1, S+1):
            line = lines[i].split()
            Streets[line[2]] = (int(line[0]), int(line[1]), int(line[3]))
        for i in range(S+1, S+1+V):
            line = lines[i].split()
            Vehicles.append((int(line[0]), line[1:]))
            StreetsUsed += line[1:]
        return D, I, S, V, F, Streets, Vehicles, StreetsUsed