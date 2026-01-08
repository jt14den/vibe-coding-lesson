---
title: "Live Demo: Linear Regression"
teaching: 30
exercises: 20
---

## Building a Tool from Scratch

In this section, we will use the Gemini CLI to build a linear regression class in Python without using `scikit-learn`.

### Step 1: Initial Implementation

Open your terminal and run the following prompt (or save it to a file and paste it):

```text
Create a Python class called LinearRegression that implements
ordinary least squares from scratch.
Requirements:
- Use only NumPy (no sklearn)
- Methods: fit(X, y) and predict(X)
- Properties: coefficients, intercept, r_squared, standard_errors
- fit() should calculate all statistics
- Save as linear_regression.py
```

### Step 2: Adding Visualization

Once the file is created, ask for a visualization:

```text
Add a method called plot_fit() to the LinearRegression class that:
- Creates a scatter plot of the data points
- Overlays the fitted regression line
- Displays the equation and R-squared
- Uses matplotlib
- Saves the plot as regression_plot.png
```

### Step 3: Summary Statistics

Finally, request a formatted output:

```text
Add a method called summary() that prints a formatted table showing:
- Coefficient estimates, Standard errors, t-stats, and p-values.
- R-squared and adjusted R-squared.
Make it look similar to statsmodels output.
```
