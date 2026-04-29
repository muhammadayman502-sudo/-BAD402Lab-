import sys

def nearest_neighbor_tsp(distances): 
    num_cities = len(distances) 
    tour = [0]  
    visited = set([0])  
    current_city = 0 
    total_distance = 0 

    while len(visited) < num_cities: 
        nearest_city = None 
        min_distance = sys.maxsize 

        for next_city in range(num_cities): 
            if next_city not in visited and distances[current_city][next_city] < min_distance: 
                nearest_city = next_city 
                min_distance = distances[current_city][next_city] 

        tour.append(nearest_city) 
        visited.add(nearest_city) 
        total_distance += min_distance 
        current_city = nearest_city 

    tour.append(0) 
    total_distance += distances[current_city][0] 

    return tour, total_distance 


def get_input_distances():
    n = int(input("Enter number of cities: "))
    
    cities = []
    print("Enter city names:")
    for _ in range(n):
        cities.append(input().strip())

    index = {city: i for i, city in enumerate(cities)}

    distances = [[0]*n for _ in range(n)]

    print("Enter distances (format: A B 2):")
    print(f"Enter {n*(n-1)//2} edges:")

    for _ in range(n*(n-1)//2):
        u, v, d = input().split()
        d = int(d)
        i, j = index[u], index[v]
        distances[i][j] = d
        distances[j][i] = d  

    return distances, cities


if __name__ == "__main__": 
    distances, cities = get_input_distances()

    tour, total_distance = nearest_neighbor_tsp(distances) 

    print("Tour:", [cities[i] for i in tour]) 
    print("Total Distance:", total_distance)