import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'], marker='x')

    # Create first line of best fit
    reg = linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880, 2051)])
    y = reg.intercept + reg.slope * x
    plt.plot(x, y, label='first line of best fit')


    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    x2 = new_df['Year']
    y2 = new_df['CSIRO Adjusted Sea Level']
    reg2 = linregress(x2, y2)
    x_pred = pd.Series(i for i in range(2000, 2051))
    y_pred = reg2.slope * x_pred + reg2.intercept
    plt.plot(x_pred, y_pred,label='second line of best fit')


    # Add labels and title
    plt.legend()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()