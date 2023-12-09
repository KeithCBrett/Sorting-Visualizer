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


generate_bars(10)
