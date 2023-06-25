import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file selection dialog
filename = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])

if len(filename) == 0: exit()

# Prompt the user for a string input
T = simpledialog.askstring("String Input", "Temperature:")
# print("User string:", user_string)

# filename='/home/lucky/Documents/PPMS/Data/A304_MR/A304_125K.csv'
# filename='C:\\Users\\Admin\\Desktop\\Data\\A304_MR\\A304_150K.csv'


df = pd.DataFrame()

# Create a figure and axis for the plot
fig, axs = plt.subplots(2, 4, figsize=(18, 9))
axs = axs.flatten() 
def read_data():
    
    df = pd.read_csv(filename, names=["I", "B","T", "V1", "V2", "V3", "V4","V5","V6","V7","V8",'Rel_value'])
    df['multiplier'] = 10**6
    (df['V5'],df['V6']) = (df['V6'], df['V5'])
    (df['V7'],df['V8']) = (df['V8'], df['V7']) 
    
    def round_fun(a):
        step = 500
        if a > 0 : q = int((a+1)/step)
        else : q = int((a-1)/step)
        return q*step

    df['B_int'] = list(map(round_fun,df['B'].values))
    df['B'] = df['B_int']
    df = df[["I", "B","T", "V1", "V2", "V3", "V4","V5","V6","V7","V8",'Rel_value', 'multiplier']].copy()
    
    df['R1'] = df['V1']/(df['multiplier']*df['I'])
    df['R2'] = df['V2']/(df['multiplier']*df['I'])
    df['R3'] = df['V3']/(df['multiplier']*df['I'])
    df['R4'] = df['V4']/(df['multiplier']*df['I'])
    df['R5'] = df['V5']/(df['multiplier']*df['I'])
    df['R6'] = df['V6']/(df['multiplier']*df['I'])
    df['R7'] = df['V7']/(df['multiplier']*df['I'])
    df['R8'] = df['V8']/(df['multiplier']*df['I'])

    return df

# Function to update the plot
def update_plot(frame):
    
    df = read_data()
    for i in range(len(axs)):
        axs[i].clear()
        axs[i].plot(df['B'], df[f'R{i+1}'], 'bo-')
        axs[i].set_xlabel('B(Oe)')
        axs[i].set_ylabel(f'R{i+1}')
        
        
    
    # Plot the data
    plt.draw()  # Redraw the plot

# Update the plot at a given interval (in milliseconds)
interval = 1000  # Update every second
ani = FuncAnimation(fig, update_plot, frames=None, interval=interval, cache_frame_data=False)

# Adjust the spacing between subplots
fig.tight_layout(pad= 4)

# Set the overall title for the subplots
fig.suptitle(f'MR at T = {T}K', fontsize=14)

# Show the plot
plt.show()