# Charting Application

This project is designed to create pie chart and line chart charts in a web-based interface using Flask and Blazor. Users can visualize different data sets through a simple interface.

# Features

Pie Chart Creation: Users can create pie charts based on certain data sets.
Creating a Line Chart: Line charts can be created for time series or other data sets.
Interactive Charts: Creating interactive line charts using Plotly.

Technologies

Backend: Flask (Python)
Frontend: Blazor (C#)
Graphics Library: Matplotlib, Plotly
While starting

This section contains step-by-step instructions on how to set up and run the project.

Requirements
Python 3.6+
flask
matplotlib
Plotly

# Use
Once the application is running, you can access it via localhost/charts in your web browser. To create a chart, follow these steps:

Load Pie Chart: Click this button to create pie chart based on specific data sets.
Load Line Chart: Click this button to create a line chart.
Interactive Line Chart: You can use this feature for interactive charts.
API Endpoints

/piechart: A POST request is made to create a pie chart.

/linechart: A POST request is made to create a line chart.

/custompiechart: Used to create pie charts with customized colors.

/interactive-linechart: Used to create interactive line charts.
