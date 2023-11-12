# Python-for-Data-Analytics
This repository contains Python scripts and Jupyter notebooks for data analysis tasks. The scripts are designed to process and analyze various datasets using popular Python libraries such as Pandas, NumPy, Matplotlib and Seaborn. It covers various aspects of data analysis, including data cleaning, Exploratory Data Analysis (EDA), statistical analysis and visualization.

## Satellite Conjunction Data Analysis
This repository contains Python scripts for analyzing satellite conjunction data. The analysis is performed on provided datasets to derive insights regarding the conjunction scenarios among active satellites in space.



- Overview
The analysis consists of two main parts, as requested in the assignment:
1.	Question 1: Analyzing a sample dataset for a single day.
2.	Question 2: Analyzing the dataset spanning five days, focusing on the evolution of conjunctions for a specific NORAD ID.



- Requirements
•	Python 3.x
•	Libraries: pandas,matplotlib
•	Data files (csv file)




- Steps
- Question 1
1A: High-Level Analytics for a Single Day
•	Load the sample data and derive key analytics.
•	Analyze the total number of conjunctions, hourly distribution, and identify heavily involved satellites.
1B: Analytics for a Single Satellite
•	Choose a specific satellite and analyze its involvement in conjunctions.
•	Assess the risk by identifying maximum probability of collision and average relative speed at the closest approach.


- Question 2
•	Load and concatenate data from five separate days into a single DataFrame.
•	Filter data for the specific NORAD ID  and analyzing the evolution of conjunctions over the five days.




- Analysis Overview
 
- 	Question 1: Single-Day Analysis
•	A) High-Level Analytics
•	Calculated the total number of predicted conjunctions among active satellites.
•	Analyzed the distribution of conjunctions throughout the day.
•	Identified the most involved satellites.
•	Visualized analytics using bar charts.
•	B) Specific Satellite Analysis
•	Analyzed the number of conjunctions for a chosen satellite.
•	Assessed the severity of conjunctions, considering closest approach distance and relative speed.
•	Provided decision-making insights for satellite operators.
•	Visualized risk factors using histograms and scatter plots.



- 	Question 2: Five-Day Analysis
•	Analyzed the evolution of conjunctions for a specific satellite (NORAD ID ) over five days.
•	Plotted the count of conjunctions per day using a line plot.


