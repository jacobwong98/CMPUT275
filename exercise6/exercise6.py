def findValley(heights):
    """
    Assumption: 'heights' is a nonempty list of integers with the guarantee
    that there is some index 0 <= i < len(l) such that the sublist
    heights[0:i+1] is strictly decreasing and the sublist heights[i:len(l)] is
    strictly increasing. So heights[i] is the 'valley'.

    Return the index i of the valley. Your algorithm must run in O(log n) time.

    You can assume that we will only test your implementation with
    lists that satisfy the above property.

    Examples:
    >>> findValley([10, 7, 4, 1, 3, 6])
    3

    >>> findValley([4])
    0

    >>> findValley([3, 2, 1])
    2

    >>> findValley([9, 14])
    0

    >>> findValley([11, 2, 11, 12])
    1
    """
    lo = 0
    hi = len(heights) - 1

    while (hi >= lo):
        # Find the middle index
        i = lo + (hi - lo) // 2
        # If the valley only increases, return the first index
        if heights[i] == heights[0]:
            return 0
        # If the valley only decreases, return the last index in the list
        elif heights[i] == heights[-1]:
            return i
        # If the index to the left/right of the middle index is bigger
        # this would mean that the current i is the valley
        elif heights[i - 1] > heights[i] and heights[i + 1] > heights[i]:
            return i
        # If the left val > middle index > right index this means we are at the
        # downward right slope of the "hill" so we need to look at everything
        # to the right half of the middle
        elif heights[i + 1] < heights[i] and heights[i - 1] > heights[i]:
            lo = i + 1
        # We have reached the valley of an even number of indexes and the hi
        # and lo are the same so we can return the lo index by choice
        elif hi == lo:
            return lo
        # If left val < middle index < right val this means we are at the
        # downward left slope of the "hill" so we need to look at everything
        # to the left half of the middle
        else:
            hi = i - 1


def climbing(heights, rest, limit):
    """
    Assumption: 'heights' is a nonempty list of positive integers that are
    strictly increasing and both 'rest' and 'limit' are positive integers.

    The list 'heights' is the various heights (in feet) of ledges on a cliff.
    The value 'rest' represents how many seconds you have to rest between
      climbing "bursts" (see the description below).
    The value 'limit' is how many seconds you have to climb the cliff, and is
      guaranteed to be at least the last height in the list.

    Suppose you are able to climb 1 foot per second consecutively for a certain
    amount of time, let's call this time 'burst'. However, after at most 'burst'
    seconds you have to rest for 'rest' seconds on one of the ledges of the
    cliff to regain your stamina. You cannot rest while hanging on to the cliff,
    you have to be on a ledge when you rest. You rest the same amount of time
    even if your latest climb was not for 'burst' seconds.

    What is the minimum value of 'burst' such that you are able to reach the
    highest ledge in at most 'limit' seconds?

    Example 1:

    That is, if you can climb for 70 seconds consecutively between rests, then:
     In your first burst, you can reach ledge 70.
     In your second burst, you can reach ledge 120.
     In your final burst, you reach the top.
    In total, you spend 190 seconds climbing and 20 seconds resting, which is
     exactly the value of 'limit'

    However, if you can only climb for 69 seconds then the fastest you can
    climb the cliff is:
     In your first burst, you can only reach ledge 30.
     In your second burst, you reach ledge 95.
     In your third burst, you reach ledge 120.
     In your fourth burst, you reach ledge 145.
     Finally, you reach ledge 190.
    In total, you spent 190 seconds climbing and 40 seconds resting, too long!

    Example 2:

    That is, you can reach the top in a single burst if you can climb for 100
    seconds consecutively.

    However, if you can only climb for 99 seconds consecutively then the best
    you can do is reach ledge 50, rest for 1 second, then reach the top for a
    total of 101 seconds.

    Example 3:

    That is, if you can climb for 50 seconds consecutively then you can reach
    the ledge at height 50 in your first burst, rest for 1 second, then reach
    the top after 49 more seconds for a total of 100 seconds.

    But if you can only climb for 49 seconds consecutively then you can't even
    reach the first ledge!

    >>> climbing([30, 70, 95, 120, 145, 190], 10, 210)
    70

    >>> climbing([50, 100], 1, 100)
    100

    >>> climbing([50, 99], 1, 100)
    50
    """

    # Start the least possible burst as first index, used for restricting the min burst later
    low = heights[0]
    # High should be the last value of the list because you could travel in one burst
    # to the final location but this isn't necessarily the smallest burst
    high = heights[-1]
    while low != high:
        mid = (high + low) // 2
        # Use check_burst to see if there is a possible burst to obtain
        checkburst = check_burst(heights, rest, limit, mid)
        # If we can determine a burst then we want to reduce the high burst
        # to the middle index and look at next half i.e. divide and conquer
        if checkburst is True:
            high = mid
        # If no burst can be lower to, we must raise the low burst to make sure
        # we don't have bursts that are too low so that we can make it within
        # the time limit
        else:
            low = mid + 1
    # High should keep reducing until it is the minimum burst
    return high


# Used to determine if a burst can be found
def check_burst(heights, rest, limit, burst):
    k = 0  # Number of intervals we have created with our divide and conquer
    reached = 0  # This determines the highest height we have currently reached
    i = 0  # Index used to traverse the heights list

    while len(heights) > i:  # Run through the length of the heights list
        # For every index from the second one and on, we want to make sure
        # that our inputted burst can reach the current height from the previous
        # height, if not then there is no burst that can be found in this portion
        if i >= 1:
            if heights[i] - heights[i - 1] > burst:
                return False
        # Check if the current index height cannot be reached from the previous
        # highest point within the specified burst
        if heights[i] - reached > burst:
            k += 1  # Create a new interval to start counting in
             # Save the new highest height as the previous height because
             # burst can reach this height but not the current index height
            reached = heights[i - 1]
        # Move to next index
        i += 1
    # The total travel time is the last height reached plus the amount of intervals
    # we took times the rest time because the intervals are the number of times
    # we stopped to rest
    total = heights[-1] + k*rest
    # If we got a total travel time less than the time limit, return True
    if total <= limit:
        return True
    # Return false meaning the minimum burst can not be found in the current portion
    # of the heights list
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
