# Import Matplotlib, this library has built-in functions for creating animations. We will be using it to draw the
# sorting animation to the screen.
# We will also import random so that we can mix up are bars so that they can be sorted.

import matplotlib.pyplot
import random


# This function will generate a random set of bars to be sorted using matplotlib. The number of bars generated will be
# equal to number_bar
def generate_bars(number_bars):
    x = [*range(1, (number_bars + 1), 1)]
    y = [*range(1, (number_bars + 1), 1)]
    random.shuffle(x)
    random.shuffle(y)
    matplotlib.pyplot.bar(x, y)
    matplotlib.pyplot.show()


def bubble_sort(input_list):
    list_length = len(input_list)
    # Traverse through all list elements
    for i in range(list_length):
        # When the last elements are in place we ignore them (list_length - i - 1)
        for j in range(0, list_length - i - 1):
            # Traverse the list from 0 to list_length-i-1, swap if the element found is greater than the next element
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                return input_list  # We will return only one iteration of the sort, so we can call this multiple times
                # to act as our animation frames.


generate_bars(10)
