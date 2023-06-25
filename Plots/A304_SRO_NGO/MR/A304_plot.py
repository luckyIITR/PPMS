import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.DataFrame()

# Create a figure and axis for the plot
fig, axs = plt.subplots(2, 4, figsize=(18, 9))
axs = axs.flatten() 
(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = axs
def read_data():
    filename='C:\\Users\\Admin\\Desktop\\Data\\A304_MR\\A304_125K.csv'
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
    ax1.clear()  # Clear the previous plot
    ax2.clear()  # Clear the previous plot
    ax3.clear()  # Clear the previous plot
    ax4.clear()  # Clear the previous plot
    ax5.clear()  # Clear the previous plot
    ax6.clear()  # Clear the previous plot
    ax7.clear()  # Clear the previous plot
    ax8.clear()  # Clear the previous plot
    
    
    df = read_data()
    # Plot the data
    
    ax1.plot(df['B'], df['R1'], 'bo-')  # Replace 'x_column' and 'y_column' with your column names
    ax2.plot(df['B'], df['R2'], 'bo-')  # Replace 'x_column' and 'y_column' with your column names
    ax3.plot(df['B'], df['R3'], 'bo-')
    ax4.plot(df['B'], df['R4'], 'bo-')
    ax5.plot(df['B'], df['R5'], 'bo-')
    ax6.plot(df['B'], df['R6'], 'bo-')
    ax7.plot(df['B'], df['R7'], 'bo-')
    ax8.plot(df['B'], df['R8'], 'bo-')
    
    plt.draw()  # Redraw the plot

# Update the plot at a given interval (in milliseconds)
interval = 1000  # Update every second
ani = FuncAnimation(fig, update_plot, frames=None, interval=interval, cache_frame_data=False)

# Show the plot
plt.show()