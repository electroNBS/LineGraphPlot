# Plotting a line graph about cases over time in different countries
# Importing the pandas module in python using alias "pd" so that we don't have to write "pandas"
# every time we want to use the pandas module
import pandas as pd
# Importing the express submodule from plotly module in python using alias "pd" so that we don't
# have to write "pandas" every time we want to use the pandas module
import plotly.express as px

# pandas module helps to read data from tables(csv files) and store it as a dataframe(a kind of datatype)
# Reading a csv file and storing its values in a data variable.
data = pd.read_csv("data.csv")
# px has a predefined function called line that helps to plot a line graph
# We assign the data variable that contains the values to be plotted as an argument.
# Assigning the independent and dependent values from the csv file to the x and y axes respectively.
# Assigning another property color to the country values so that each country in the graph has a
# different color.
figure = px.line(data, x="date", y="cases", color="country")
# Showing the graph
figure.show()
