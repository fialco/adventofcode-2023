#Welcome to the Jank

def stager(ranges, start):

    source = None
    destinations = None
    for key, value in ranges.items():
        if start < key:
            break
        source = key
        
        destinations = value
    
    if source != None:
        if source <= start <= source + destinations[1]:
            return destinations[0] + start - source
            
    else:
        return None

def almanac(lines):
    lines = lines.split("\n")

    seed_to_soil = {}
    soil_to_fert = {}
    fert_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humid = {}
    humid_to_loc = {}

    stage = 0
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    result = []

    for line in lines:
        line = line.strip()
        if line[0:5] == "seeds": #collects seed numbers
            seeds = line
            seeds = seeds.split()[1:]
        
        if line == "":
            stage += 1
            continue
        
        if stage == 1: #seed_to_soil
            if line[0] in numbers:
                maps = line.split()
                seed_to_soil[int(maps[1])] = (int(maps[0]), int(maps[2]))

        elif stage == 2: #soil_to_fert
            if line[0] in numbers:
                maps = line.split()
                soil_to_fert[int(maps[1])] = (int(maps[0]), int(maps[2]))
        
        elif stage == 3: #fert_to_water
            if line[0] in numbers:
                maps = line.split()
                fert_to_water[int(maps[1])] = (int(maps[0]), int(maps[2]))
        
        elif stage == 4: #water_to_light
            if line[0] in numbers:
                maps = line.split()
                water_to_light[int(maps[1])] = (int(maps[0]), int(maps[2]))
        
        elif stage == 5: #light_to_temp
            if line[0] in numbers:
                maps = line.split()
                light_to_temp[int(maps[1])] = (int(maps[0]), int(maps[2]))
        
        elif stage == 6: #temp_to_humid
            if line[0] in numbers:
                maps = line.split()
                temp_to_humid[int(maps[1])] = (int(maps[0]), int(maps[2]))
        
        elif stage == 7: #humid_to_loc
            if line[0] in numbers:
                maps = line.split()
                humid_to_loc[int(maps[1])] = (int(maps[0]), int(maps[2]))

    for seed in seeds:
        
        seed_to_soil = dict(sorted(seed_to_soil.items()))
        soil_to_fert = dict(sorted(soil_to_fert.items()))
        fert_to_water = dict(sorted(fert_to_water.items()))
        water_to_light = dict(sorted(water_to_light.items()))
        light_to_temp = dict(sorted(light_to_temp.items()))
        temp_to_humid = dict(sorted(temp_to_humid.items()))
        humid_to_loc = dict(sorted(humid_to_loc.items()))

        seed = int(seed)

        if seed == 14:
            pass

        soil = stager(seed_to_soil, seed)
        if not soil:
            soil = seed
        
        fert = stager(soil_to_fert, soil)
        if not fert:
            fert = soil

        water = stager(fert_to_water, fert)
        if not water:
            water = soil

        light = stager(water_to_light, water)
        if not light:
            light = water

        temp = stager(light_to_temp, light)
        if not temp:
            temp = light

        humid = stager(temp_to_humid, temp)
        if not humid:
            humid = temp

        loc = stager(humid_to_loc, humid)
        if not loc:
            loc = humid

        result.append(loc)

    return min(result)

if __name__ == "__main__":
    s =  """seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4"""
    print(almanac(s))

    f = open("day5_input.txt")
    data = f.read().strip()
    print(almanac(data)) #510109797

    