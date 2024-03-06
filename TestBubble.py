import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    steps = []
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(list(arr))  # Append each step to visualize
    return steps

# Generate a random array
np.random.seed(0)
arr = np.random.randint(1, 100, 10)

# Perform bubble sort and get the steps
steps = bubble_sort(arr.copy())

# Generate random colors for the bars
bar_colors = sns.color_palette("husl", len(arr))

# Initialize the figure
fig, ax = plt.subplots()
sns.set_style("whitegrid")
bars = ax.bar(np.arange(len(arr)), arr, color=bar_colors)

# Function to update the plot for each step of the animation
def update(i):
    for bar, h in zip(bars, steps[i]):
        bar.set_height(h)
    return bars

# Create the animation
ani = FuncAnimation(fig, update, frames=len(steps), blit=True, interval=500)

plt.title('Bubble Sort Animation')
plt.show()