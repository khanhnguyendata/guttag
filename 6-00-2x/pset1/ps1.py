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
    spaceships = []
    remaining_cows = cows.copy()

    # Remove cows that can't be fit into any spaceship
    for cow, weight in cows.items():
        if weight > limit:
            del remaining_cows[cow]

    # Build list of cows sorted by their weights (highest to lowest)
    sorted_cows = sorted(remaining_cows, key=remaining_cows.get, reverse=True)

    # Build empty spaceships and load cows into each ship
    # (from heaviest to lightest, ignoring those that couldn't fit).
    # When all cows that could possibly fit one spaceship have been loaded,
    # store current spaceship and build next empty spaceship to load cows in.
    # Stop when there's no more cows to load
    while sorted_cows:
        spaceship = []
        spaceship_weight = 0
        for cow in sorted_cows[:]:  # Make copy of sorted cows to keep the iterator intact when removing cow from list
            cow_weight = remaining_cows[cow]

            # If there's still space for a cow, remove cow from list, add it to spaceship, and update spaceship weight
            if spaceship_weight + cow_weight <= limit:
                sorted_cows.remove(cow)
                spaceship.append(cow)
                spaceship_weight += cow_weight

        spaceships.append(spaceship)

    return spaceships


# Problem 2
def brute_force_cow_transport(cows,limit=20):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

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
    def valid_partitions(cows, partitions):
        """
        Determine if a collection of partitions is valid by checking if weight of each partition is within limit
        :param cows: dict of cow:weight
        :param partitions: collection of partitions as list of lists (e.g. [[a], [b, c, d]]
        :return: True if all partitions in the collection is within weight limit, False if any is above limit
        """
        for partition in partitions:
            partition_weight = sum(cows[cow] for cow in partition)
            if partition_weight > limit:
                return False
        return True

    # Get list of cow
    cow_list = list(cows.keys())

    # Generate permutations of partition collections from the cow list
    fewest_partitions = []
    fewest_partitions_count = len(cow_list)  # max value of partition count, will be updated with lower values

    # For each partition collection, if it's a valid collection and has fewer partitions
    # than current shortest partition collections, store it as the current shortest partition collections
    for partitions in get_partitions(cow_list):
        if valid_partitions(cows, partitions) and len(partitions) <= fewest_partitions_count:
            fewest_partitions = partitions
            fewest_partitions_count = len(partitions)

    # Return the partition collections with the lowest number of partitions
    return fewest_partitions


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
    greedy_partitions = greedy_cow_transport(cows, limit)
    end = time.time()
    print(greedy_partitions)
    print(end - start)

    start = time.time()
    brute_force_partitions = brute_force_cow_transport(cows, limit)
    end = time.time()
    print(brute_force_partitions)
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
def main():
    compare_cow_transport_algorithms()


if __name__ == '__main__':
    main()
