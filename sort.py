import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import time




class Main():
        
    def __init__(self):
        super().__init__()

        #! Changeable variables
        self.example_bar_count = 100000 #* Amount of arrays for the test
        self.bubble_sort_percentage = 100 #* Percentage of amount of sorting bubble sort should do (100% = fully sorted)



        #* Create new numbers
        self.x = np.arange(1, self.example_bar_count + 1)
        self.y = np.random.permutation(np.arange(1, self.example_bar_count + 1))

        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        #* Button for selection sort algorithm
        self.selection_sort_buttonax = plt.axes([0.3, 0.05, 0.2, 0.1])
        self.selection_sort_button = Button(self.selection_sort_buttonax, "Selection sort")
        self.selection_sort_button.on_clicked(self.selection_sort)

        #* Button for bubble sort algorithm
        self.bubble_sort_buttonax = plt.axes([0.53, 0.05, 0.2, 0.1])
        self.bubble_sort_button = Button(self.bubble_sort_buttonax, "Bubble sort")
        self.bubble_sort_button.on_clicked(self.bubble_sort)
        
        #* Button for merge sort algorithm
        self.merge_sort_buttonax = plt.axes([0.76, 0.05, 0.2, 0.1])
        self.merge_sort_button = Button(self.merge_sort_buttonax, "Merge sort")
        self.merge_sort_button.on_clicked(self.start_merge_sort)

        #* Button to mix numbers
        self.mix_numbers_buttonax = plt.axes([0.025, 0.05, 0.2, 0.1])
        self.mix_numbers_button = Button(self.mix_numbers_buttonax, "Mix numbers",color="gray")
        self.mix_numbers_button.on_clicked(self.mix_numbers)

        self.bar = self.ax.bar(self.x, self.y)
        plt.show()

    def start_merge_sort(self, event):
        #* Starts the algorithm
        self.start_timer()
        self.y = self.merge_sort(self.y)
        self.end_timer("merge_sort")
        self.update()

    def merge_sort(self, array):
        length = len(array)
        if length <= 1: #* returns if list is already fully split
            return array

        mid = length // 2
        left = array[:mid]
        right = array[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right): # adds the numbers to the final list
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:]) 
        sorted_array.extend(right[j:])

        return sorted_array

    def bubble_sort(self, event):
        n = len(self.y)
        self.start_timer()

        for i in range((int) (n*(self.bubble_sort_percentage/100))):
            for j in range(0, n-i-1):# -1 because n starts at 1 but for loop starts at 0
                if self.y[j] > self.y[j+1]:
                    self.y[j], self.y[j+1] = self.y[j+1], self.y[j] # replace current number with next
    
        self.end_timer("bubble_sort")
        self.update()
        
    def selection_sort(self, event):
        n = len(self.x)
        self.start_timer()

        #* Main for loop
        for i in range(n): 
            min_idx = i
            for j in range(i+1, n): #for every non sorted number go through numbers
                if self.y[j] < self.y[min_idx]: #always look for lower number than on current spot.. if none found -> stays in place
                    min_idx = j 
                    
            self.y[i], self.y[min_idx] = self.y[min_idx], self.y[i] # replace the value with the right one

        self.end_timer("selection_sort")    
        self.update()
                
    def mix_numbers(self, event):
        #* Mix numbers and update bars
        self.y = np.random.permutation(np.arange(1, self.example_bar_count +1))

        self.update()
        
    def update(self):
        for bar, new_height in zip(self.bar, self.y):
            bar.set_height(new_height)
        self.fig.canvas.draw_idle()

    def end_timer(self,function_name):
        self.end_time = time.time() - self.starting_time
        print(f"{function_name} took {self.end_time:.5f} seconds")
    
    def start_timer(self):
        self.starting_time = time.time()


if __name__ == "__main__":
    Main()
