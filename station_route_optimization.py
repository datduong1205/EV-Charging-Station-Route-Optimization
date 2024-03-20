# EV Charging Station Route Optimization Project
# Group 3
# Quincy Chan - 100891459
# Mujtaba Hussaini - 100827655
# Le Minh Dat Duong - 100886108
# Shadman Shan - 100867403

import heapq

def dijkstra_alg(G, start):
    node_distance = {node: float('inf') for node in G} # set all distance to inf
    node_distance[start] = 0 # set distance of the starting node to 0

    priority_queue = [(0, start)] # priority queue to go to the next nearest node

    while len(priority_queue) > 0:
        
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > node_distance[current_node]:
            continue # if the new distance is larger than the existing one, skip it

        for neighbour, weight in G[current_node].items(): # calculate the distance of all neighbours node and push to the priority queue
            distance = current_distance + weight

            if distance < node_distance[neighbour]:
                node_distance[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))
    
    charging_station = [(station, length) for station, length in node_distance.items() if station in ['H', 'K', 'Q', 'T'] ] 

    return sorted(charging_station, key= lambda x: x[1])

if __name__ == '__main__':

    # Graph Construction
    G = {
        'A': {'B': 6, 'F': 5},
        'B': {'A': 6, 'C': 5, 'G': 6},
        'C': {'B': 5, 'D': 7, 'H': 5}, 
        'D': {'C': 7, 'E': 7, 'I': 8},
        'E': {'D': 7, 'I': 6, 'N': 15},
        'F': {'A': 5, 'G': 8, 'J': 7},
        'G': {'F': 8, 'B': 6, 'K': 8, 'H': 9},
        'H': {'G': 9, 'C': 5, 'I': 12}, # Charging Station
        'I': {'H': 12, 'D': 8, 'E': 6, 'M': 10},
        'J': {'F': 7, 'K': 5, 'O': 7},
        'K': {'J': 5, 'G': 8, 'L': 7}, # Charging Station
        'L': {'K': 7, 'P': 7, 'M': 7},
        'M': {'L': 7, 'I': 10, 'N': 9},
        'N': {'M': 9, 'E': 15, 'R': 7},
        'O': {'J': 7, 'S': 9, 'P': 13},
        'P': {'O': 13, 'L': 7, 'U': 11, 'Q': 8},
        'Q': {'P': 8, 'R': 9}, # Charging Station
        'R': {'Q': 9, 'N': 7, 'W': 10}, 
        'S': {'O': 9, 'T': 9},
        'T': {'S': 9, 'U': 8}, # Charging Station
        'U': {'T': 8, 'P': 11, 'V': 8},
        'V': {'U': 8, 'W': 5},
        'W': {'V': 5, 'R': 10}
    }

    while True:
        node_list = 'ABCDEFGHIJKLMNOPQRSTUVW'
        choice = int(input('Options:\n1. Find nearest charging station\n2. Exit\nChoose: ').strip())

        if choice == 1:
            starting_node = input('Specify your location (A->W): ').upper().strip()
            
            if starting_node in node_list:
                dijkstra  = dijkstra_alg(G, starting_node)
                print(f'Length from {starting_node} to: ')
                for i, (j, k) in enumerate(dijkstra, 1): # rank charging station from nearest to highest
                    print(f'{i}. Charging station {j}: {k}')
                
                print('-----------------------------------------------------------------------------------------')
            
            else:
                print('Location does not exist! Please choose again.')
        
        elif choice == 2:
            print('Program End!')
            print('-----------------------------------------------------------------------------------------')
            break
        
        else:
            print('Option does not exist! Please choose again.')
