import math


lines = """Time:        58     81     96     76
Distance:   434   1041   2219   1218"""


def calc_distance(T, x):
    return (T - x) * x

def dist_solution(T, d):
    return ((T - math.sqrt(T ** 2 - 4 * d)) * 0.5, (T + math.sqrt(T ** 2 - 4 * d)) * 0.5)

def part1():    
    [times, distances] = [list(map(int, line.split()[1:])) for line in lines.split("\n")]
    
    product = 1
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        
        sols = dist_solution(time, distance)        
        wins = math.floor(sols[1]) - math.ceil(sols[0]) + (1 if calc_distance(time, math.ceil(sols[0])) > distance else -1)
        
        product *= wins
     
    print(product)
        

def part2():    
    time = int(lines.split("\n")[0].split(":")[1].replace(" ", ""))
    distance = int(lines.split("\n")[1].split(":")[1].replace(" ", ""))
    
    sols = dist_solution(time, distance)        
    wins = math.floor(sols[1]) - math.ceil(sols[0]) + (1 if calc_distance(time, math.ceil(sols[0])) > distance else -1)
       
    print(wins)
  
    
if __name__ == "__main__":
    part1()
    part2()
