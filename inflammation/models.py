"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
   """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of max values of measurements for each day.
   """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of minimum values of measurements for each day.
   """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    max_data = np.nanmax(data, axis=1)

    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]

    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

def attach_names(data, names):
    """Attach names to data

    :param data: A 2D data array each row contains an entry to be annotated.
    :param names: List of strings, one for each row in data
    :returns: A dictionary of annotated data.
    """
    assert len(data) == len(names)
    output = []

    for i in range(len(data)):
        output.append({'name': names[i],
                       'data': data[i]})

    return(output)


data = np.array([[1., 2., 3.], [4., 5., 6.]])
names = ['Alice', 'Bob']

output = attach_names(data, ['Alice', 'Bob'])
print(output)



class Book:
    """ A book and its author """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

book = Book('A book', 'Me')
print(book)



class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Doctor(Person):
    """ A doctor who looks after patients """
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, patient):
        """ Adds a new patient to the doctor
            Checks to see if they have already been added """
        for pat in self.patients:
            if pat.name == patient.name:
                print('Patient already added')
                return
        self.patients.append(patient)

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation



alice = Patient('Alice')
alice.add_observation(3)
alice.add_observation(3, day=5)
alice.add_observation(10, day=10)
bob = Patient('Bob')

print(alice)
for obs in alice.observations:
    print('Day = ' + str(obs.day) + ', Value = ' + str(obs.value))

doc1 = Doctor('Hugh Montgomery')
doc1.add_patient(alice)
doc1.add_patient(alice)
doc1.add_patient(bob)

print(doc1)
for pat in doc1.patients:
    print(pat.name)




