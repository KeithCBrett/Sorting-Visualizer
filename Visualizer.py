import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# Generate initial random bars
def generate_bars(number_bars):
    return random.sample(range(1, 100), number_bars)  # Need to change this to make all values sequential eventually


# Bubble sort algorithm
def bubble_sort(input_list):
    list_length = len(input_list)
    for i in range(list_length):
        for j in range(0, list_length - i - 1):  # Excludes already sorted elements (rightmost sorted elements)
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                yield input_list  # Yield the updated list for animation. We us yield instead of return because it
                # allows us to continue the sort at later time, doesn't return just one value.


# Initialize figure and axes
fig, ax = plt.subplots()
bars = ax.bar(range(len(generate_bars(25))), generate_bars(25))


# Function to update bars for each frame of the animation
def update(input_list):
    for bar, h in zip(bars, input_list): # Zip pairs the bars height to the values created in generate_bars
        bar.set_height(h)  # Update each bar's height on screen (once called by FuncAnimation)
    return bars


# Create animation
anim = animation.FuncAnimation(fig, update, frames=bubble_sort(generate_bars(25)), interval=1, blit=True)

plt.title('Bubble Sort Visualization')
plt.xlabel('Index')
plt.ylabel('Value')


# Should save in the same folder visualizer is located in
anim.save('sort.gif', writer='ffmpeg', fps=30)
# 60fps 2 min compile
