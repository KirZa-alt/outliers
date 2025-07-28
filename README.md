# Outlier Detection App

A simple and interactive web app to detect outliers in a dataset using Python and Streamlit.

This app supports two beginner-friendly methods:

* **IQR Method**: Uses interquartile range to identify data points outside 1.5×IQR from Q1 and Q3.
* **Median-Max Method**: Flags values significantly greater than the median (e.g., more than 1.5× median).

## Features

* Upload and view CSV data
* Choose your preferred outlier detection method
* View calculated thresholds and outlier values
* Clean and beginner-friendly interface

## How to Run

```bash
streamlit run app.py
```

## Requirements

* streamlit
* pandas
* numpy

Install them with:

```bash
pip install streamlit pandas numpy


## Author

Made by KirZa using Python and Streamlit.
