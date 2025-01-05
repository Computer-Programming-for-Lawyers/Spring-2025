# Scratch
# Import the data
# Identify and examine the data
# Clean the data (take a subset of rows and columns)
# Visualize with the data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# setting the dimensions of the plot
# Examine the data and return summary statistics

# Do some data cleaning with arbitrary logic.
# Read the data
# a Function that takes in the name/address of a .csv file 
# and turns it into a Pandas dataframe and returns it
def read_data(csvfile):
    raw_data_dataframe = pd.read_csv(csvfile)
    return raw_data_dataframe

def clean(raw_data_dataframe):
    # Exclude some states
    # Exclude some zipcodes
    # Rename some places . . . etc
    return clean_dataframe

def give_summary_stats(clean_dataframe):
    # Give some summary statistics
    avg_price_by_city = housedata.groupby('State').mean('Price')
    # Other summaries
    print(avg_price_by_city)
    return null

# Do some visualizations (each should be a function)
def visualize_data(clean_dataframe, chart_type='bar'):

# Bar
# Scatter/Bubble
# Histogram
    fig, ax = plt.subplots(figsize=(30, 5))
    barplot = sns.barplot(data=avg_price_by_city, x='State', y='Price', ax=ax)
    barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45)
    return null

def show(csvfile):
    rawdata = read_data(csvfile)
    clean_data = clean(rawdata)
    give_summary_stats(clean_data)
    visualize_data(clean_data)
    return null

