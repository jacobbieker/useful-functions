from __future__ import division
import math
__author__ = 'Jacob Bieker'


def power_error(power, frac_uncertainty):
    return power * frac_uncertainty


def frac_error(error, true_value):
    return error / abs(true_value)


def quad_error(b_error, v_error):
    return math.sqrt((b_error ** 2) + (v_error ** 2))


def standard_dev(set_of_values, avg_value):
    #Finds Standard Deviation for V
    diffsquared = 0
    sum_diffsquared = 0
    std_dev = 0
    for value in set_of_values:
        diffsquared = (value-avg_value)**2
        sum_diffsquared += diffsquared
        std_dev = (((sum_diffsquared)/(len(set_of_values) - 1))**(1/2))
    return std_dev


def correlation(setX_of_values, setY_of_values, x_avg, y_avg, x_err, y_err):
    sum_of_points = 0
    for index, value in enumerate(setX_of_values):
        point = (((value - x_avg) / x_err) * ((setY_of_values[index] - y_avg) / y_err))
        sum_of_points += point
    return (1 / (len(setX_of_values) - 1)) * sum_of_points

def kB(D, f, T):
    return (D * f) / T


def f(R):
    return 6 * math.pi * .001 * R


def D(delta_t, avg_axis_r):
    return avg_axis_r / (4 * delta_t)


def standard_dev_sd(number_of_measurements):
    return 1 / (math.sqrt(2 * (number_of_measurements - 1)))