import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MAX_STEPS = 20000
SIZE_INCREMENT = 20
START_SIZE = 20
N_COLORS = 4
N_SAME_SIZE_PROBLEMS = 50
MAX_PROBLEM_SIZE = 600
N_DIFFERENT_SIZE_PROBLEMS = int((MAX_PROBLEM_SIZE - START_SIZE)/SIZE_INCREMENT) + 1
RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
PLOTS_DIR = os.path.join(ROOT_DIR, 'plots')
CSP_DIR = os.path.join(ROOT_DIR, 'csps')