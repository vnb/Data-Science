###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
#    # TODO: Your code here
#    pass
    #initialize trip list
    #helper function sub_set
    selected_cows = []
    cow_names = [x for x in cows]
    available_cows = [cows[x] for x in cows]
    cows_remaining = [cows[x] for x in cows]
    set_limit = limit
    trip_list = []
    cow_list = []
    cow_trip_list = []
    while len(available_cows) > 0:
        limit = set_limit
        cows_remaining = available_cows[:]
        selected_cows = []
        sub_list = []
        while limit > 0:
            if len(cows_remaining) == 0:
                break
            a = max(cows_remaining)
            cows_remaining.remove(a)
            if a <= limit:
                limit -= a
                selected_cows.append(a)
                available_cows.remove(a)
        trip_list.append(selected_cows)
        for i in selected_cows:
            for name in cows:
                if cows[name] == i:
                    if name in cow_names:
                        cow_list.append(name)
                        cow_names.remove(name)
                        break
        cow_trip_list.append(cow_list)
        cow_list = []
           
    return cow_trip_list


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute forc
    e.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def count_sum(listofcows, cows):
        weight = 0
        for i in listofcows:
            weight += cows[i]
            if weight > limit:
                return False
                break
        return True
    cow_list = list(cows.keys())
    
    flight_list = []
    all_partitions = get_partitions(cow_list)
    
    for i in all_partitions:
        switch = 'green'
        for j in i:
            if count_sum(j, cows) == False:
                switch = 'red'
                break
        if switch == 'green':
            flight_list.append(i)
            
    trip_len_list = [len(i) for i in flight_list]
    
    for i in flight_list:
        if len(i) == min(trip_len_list):
            ideal_trip = i
            break
    return ideal_trip

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    start = time.time()
    ans_a = greedy_cow_transport(cows, limit)
    end = time.time()
    print(end-start)
    start = time.time()
    ans_b = brute_force_cow_transport(cows, limit)    
    end = time.time()
    print(end-start)
    return


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#print(cows)
#
#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
print(compare_cow_transport_algorithms())
