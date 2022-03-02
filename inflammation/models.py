"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename) -> np.array:
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: Numpy array
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data) -> np.array:
    """Calculate the daily mean of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
   """
    return np.mean(data, axis=0)


def daily_max(data) -> np.array:
    """Calculate the daily maximum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of max values of measurements for each day.
   """
    return np.max(data, axis=0)


def daily_min(data) -> np.array:
    """Calculate the daily minimum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of minimum values of measurements for each day.
   """
    return np.min(data, axis=0)

