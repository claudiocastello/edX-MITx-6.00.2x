# Introduction

In this problem set, you will use regression analysis to model the climate of different areas and try to find evidence of global warming. You will create models to analyze and visualize climate change in terms of temperature. 

Download ps4.zip.

Please do not rename the files we provide you with, change any of the provided helper functions, change function/method names, or delete provided docstrings. You will need to keep data.csv in the same folder as ps4.py.

To model the change in climate of an area, you will need some data. For this problem set, we will use temperature data obtained from the National Centers for Environmental Information (NCEI). The data, stored in data.csv , contains the daily maximum and minimum temperatures observed in 21 U.S. cities from 1961 to 2015. Open the file, and take a look at the raw data.

In order to parse the raw data, in ps4.py w e have implemented a helper class Climate. You can initialize an instance of the Climate class by providing the filename of the raw data. Look over this class and read its docstrings to figure out how to get data for the following problems.


## Problem 1

Implement the generate_models function.

    x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points); for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], where x_i and y_i are the x and y coordinate of the i-th data points. In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997); each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius. This representation will be used throughout the entire problem set.
    degs is a list of integers indicating the degree of each regression model that we want to create. For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
    This function should return a list of models. A model is the numpy 1d array of the coefficients of the fitting polynomial curve. Each returned model should be in the same order as their corresponding integer in degs.

Example:

print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2]))

Should print something close to:

[array([ 1.10000000e+00, -2.15270000e+03]), array([ -8.86320195e-14, 1.10000000e+00, -2.15270000e+03])]

The above example was generating a linear and a quadratic curve on data samples (xi, yi ) = (1961, 4.4), (1962, 5.5), and (1963, 6.6). The resulting models are in the same order as specified in degs. Note that it is fine you did not get the exact number because of numerical errors.

Note: If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.


## Problem 2

After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.

Implement the function r_squared. This function will take in:

    list, y, that represents the y-coordinates of the original data samples
    estimated, which is a corresponding list of y-coordinates estimated from the regression model

This function should return the computed R^2 value. You can compute R^2 as follows, where ei
is the estimated y value for the i-th data point (i.e. predicted by the regression), yi is the y value for the ith data point, and mean is the mean of the original data samples.

![r2](https://d37djvu3ytnwxt.cloudfront.net/assets/courseware/v1/83df4c1c72ef01bd64e3ff4af2d2f60c/asset-v1:MITx+6.00.2x_6+3T2016+type@asset+block/r2.PNG)

If you are still confused about R^2 , its wikipedia page has a good explanation about its use/how to calculate it.

Note: If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.
