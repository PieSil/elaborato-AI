import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MAX_STEPS = 10000
SIZE_INCREMENT = 20
START_SIZE = SIZE_INCREMENT
N_COLORS = 4
N_SAME_SIZE_PROBLEMS = 50
MAX_PROBLEM_SIZE = 500
N_DIFFERENT_SIZE_PROBLEMS = 25
RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
PLOTS_DIR = os.path.join(ROOT_DIR, 'plots')
CSP_DIR = os.path.join(ROOT_DIR, 'csps')