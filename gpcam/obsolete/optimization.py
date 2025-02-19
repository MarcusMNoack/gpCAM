import random
import numpy as np

import itertools
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution as devo
from functools import partial



def multi_start_gradient_descent(
    ParameterLimits, ObjectiveFunction, GradientFunction, mode=1, starts=10
):
    ####maximization mode = 1
    ####minimization mode = -1
    Population = InitPopulation(ParameterLimits, starts, len(ParameterLimits))
    dim = len(ParameterLimits[0])
    OptimaList = np.zeros((starts, dim))
    for i in range(0, starts):
        epsilon = np.inf
        x = np.copy(Population[i])
        step_counter = 0
        step = 1.0
        while epsilon > 1e-8:
            newton_step_counter += 1
            gradient = GradientFunction(x)
            x = x + mode * (gamma + step)
            epsilon = np.linalg.norm(gamma)
        OptimaList[i] = np.copy(x)
        Evaluations[i] = ObjectiveFunction(x)
        max_index = np.argmax(Evaluations)
    return OptimaList[max_index], Evaluations[max_index]


def compute_population_acquisition(Population, ObjectiveFunction, *args):
    ObjectiveFunctionEvaluation = np.zeros((len(Population)))
    for i in range(len(Population)):
        ObjectiveFunctionEvaluation[i] = ObjectiveFunction(
            np.array([Population[i]]), *args
        )
    return ObjectiveFunctionEvaluation


def out_of_bounds(x, bounds):
    for i in range(len(x)):
        if x[i] < bounds[i][0] or x[i] > bounds[i][1]:
            return True
    return False
