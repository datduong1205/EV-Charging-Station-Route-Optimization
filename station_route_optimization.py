# EV Charging Station Route Optimization Project
# Group 3
# Quincy Chan -
# Mujtaba Hussaini -
# Le Minh Dat Duong - 100886108
# Shadman Shan -

import heapq

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

def dijkstra_alg(G, start):
    node_distance = {node: float('inf') for node in G}
    node_distance[start] = 0
    pass