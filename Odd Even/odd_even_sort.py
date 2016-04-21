# multiprocessing is a package that supports spawning processes
import multiprocessing

def compare(x):
    change = False
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
        change = True
    # if a comparison were true then change the change variable to True
    # and then return both, the changed pair and the value of the change
    # variable. eg: [5, 3] returns [(3, 5), True] indicating exchange.
    return (x, change)

# Odd even sort works by first comparing the elements at the even
# indices with their neighbours, and then exchanging them if the
# number at the even indice is greater than its neighbour (first phase).
# Now in the second phase, the elements with odd indices are compared
# with their neighbours and they are exchanged if found greater.
# These 2 phases continue until there are no exchanges in the even and
# odd phases which would mean that the list has been sorted.
# refer pseudocode at -> https://en.wikipedia.org/wiki/Odd-even_sort

def oddevensort(x):
    # phase is the variable used to store the current phase
    phase, flag = 0, 0    # 0 is even phase and 1 is odd phase
    # flag is used to store the number of phases without an exchange
    # taking place. When 2 phases have taken place without any exchanges,
    # the list will have been sorted and the oddevensort function returns.
    while (flag != 2):
        # suppose we assume that the input given is [3, 5, 1, 45, 6]
        # then this input will be split according to phase which is
        # initially zero into 2 sublists with even indices + neighbours
        # i.e. [[3, 5], [1, 45]]
        # the split is performed using list comprehension
        split = [[x[i], x[i+1]] for i in range(phase, len(x)-1, 2)]
        # assign 2 processes to do the comparisons in parallel
        process_pool = multiprocessing.Pool(2)
        split_after_comparison = process_pool.map(compare, split)
        # close pool to prevent further tasks from execution
        process_pool.close()

        # temp is going to contain our final merged list
        temp = []
        if len(x)%2 == 0:
            if (phase == 1):
            # if the list is even in length and it is an odd phase currently
            # ongoing, then the split_after_comparison list would not
            # contain the first element of the original list, so we append
            # that to temp. An example of such a phase + length combination
            # like [1, 3, 5, 34, 6, 12] after split -> [[3, 5], [34, 6]]
                temp.append(x[0])
                # add each element in the split_after_comparison to the
                # temp list by list concatenation
                # eg. if temp = [3, 5] then temp + [34, 6] = [3, 5, 34, 6]
                for i in split_after_comparison:
                    # remember that we use i[0] as i[1] contains the
                    # the True of False value telling us whether a
                    # comparison took place or not; refer to the comments
                    # in the compare section
                    temp += i[0]
                # in the odd phase, the last element of an even length list
                # would be omitted as 12 is omitted in the above example
                # example split and we therefore append that too to temp
                temp.append(x[-1])
            else:  # phase = 0 and its therefore an even phase
                # for an even sized list with phase = 0, like eg.
                # [5, 4, 3, 2] the split would be -> [[5, 4], [3, 2]]
                # since we have all the elements of our original list in
                # the split, we can directly concatenate all of the split
                # elements to get our original list
                for i in split_after_comparison:
                    temp += i[0]
        else:                  # x is odd in length
            if (phase == 1):   # odd phase
                temp.append(x[0])
                for i in split_after_comparison: # get back original list
                    temp += i[0]
            else:              # even phase
                for i in split_after_comparison: # get back original list
                    temp += i[0]
                temp.append(x[-1])
        # x now finally contains the original list after one phase
        x = temp
        phase = (phase + 1)%2
        # if any comparison in split_after_comparison is True
        if any([i[1] for i in split_after_comparison]):
            flag = 0
        else:
            flag += 1
    # done with the while loop i.e. list is sorted
    print "The sorted list", x
    return x
    
