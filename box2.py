class Box:
    def __init__(self, x, y, w, h):
        '''
        Create an instance of the box class whose lower-left corner is at (x,y)
        and whose width is w and height is h. The width w and height h must be
        positive.
        '''

        if w <= 0 or h <= 0:
            raise ValueError("cannot create box with nonpositive dimensions")
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def moveBy(self, dx, dy):
        '''
        Translates this box by dx units along the x axis and dy units along
        the y axis.
        '''
        self.x += dx
        self.y += dy

    def contains(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns true if and only if the box b is entirely contained
        within this box (they can share edges).
        '''
        return (self.x <= b.x and self.y <= b.y and
                self.x + self.w >= b.x + b.w and
                self.y + self.h >= b.y + b.h)

    def unionWith(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns the smallest box that contains both self and box b.
        '''
        new_x = min(self.x, b.x)
        new_y = min(self.y, b.y)
        new_w = max(self.x + self.w, b.x + b.w) - new_x
        new_h = max(self.y + self.h, b.y + b.h) - new_y
        return Box(new_x, new_y, new_w, new_h)

    def __str__(self):
        return "Box({}, {}, {}, {})".format(self.x, self.y,
                                            self.w, self.h)


def longest_sequence(boxes, i, memo = None):
    '''
    Assumes boxes is a list of boxes indexed by i ( 0  <= i < len(boxes) )
    and that no two boxes have identical (x, y, w, h),
    i.e., no two boxes are the same.

    This function returns the largest value m such that
    it is possible to find a list of length m of distinct boxes starting at boxes[i]
    where each box in the list contains the next box in the list
    (according to the contains() method).

    Note, the boxes in "chain" don't have to be in the same order
    as they appeared in the boxes list.

    Example:
    >>> boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    >>> longest_sequence(boxes, 1)
    2

    >>> boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    >>> longest_sequence(boxes2, 1)
    3

    For full marks, your algorithm should run in O(n^2) time where
    n = len(boxes). Use dynamic programming (top-down approach)
    to achieve this.
    '''

    if memo is None:
        memo = {}

    # now you finish it
    # if the box is already been found we don't have to do other stuff
    if boxes[i] in memo:
        return memo[boxes[i]]

    cantContain = True
    currMax = 0

    for j in range(len(boxes)):
        # Ignore looking for containment if the index self-references itself
        # they can't contain the same boxes
        if j != i:
            # Check if our chosen box can contain the box we are indexing
            if boxes[i].contains(boxes[j]):
                # Determine this new max by recursively calling with the current
                # j index plus one; where we add the one because we count the
                # current box itself to the "chain"
                calcMax = longest_sequence(boxes, j, memo) + 1
                # Find the new max "chain" and store in the current max
                currMax = max(calcMax, currMax)
                # Want to memoize this new max with the chosen box, meaning the
                # "i" box can contain this max number amount of boxes
                memo[boxes[i]] = currMax
                cantContain = False
    # Check if our "i" box couldn't contain any other boxes
    if cantContain:
        # Set currMax to 1, indicating the "i" box can't contain any other boxes
        currMax = 1
        # Memoize that our "i" box can no longer hold any other boxes
        memo[boxes[i]] = currMax
        return currMax
    # If we were able to determine that our "i" box can contain other boxes,
    # return the value that our boxes can contain
    return memo[boxes[i]]

# ADD COMMENT BELOW TO ANALYZE THE RUNNING TIME
# State the running time of your algorithm below here. Justify it in 2-3
# sentences. Remember the "running time analysis template"
# for dynamic programming problems from the lectures.


'''
The running time is O(n^2) because it should take n time to recursively call
the function if we assume that these calls occur in constant time. The other n
comes from the fact that we are performing a max operation of the values and
for larger values these operations are not constant. So our running time is
O(n*n) which is O(n^2) where n is the length of boxes
'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
