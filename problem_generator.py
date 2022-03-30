from utils.problem_utility import ProblemFileManager
import constants as c

problemFileManager = ProblemFileManager()

problemFileManager.generateProblemSet(c.START_SIZE, c.SIZE_INCREMENT, c.N_SAME_SIZE_PROBLEMS, c.MAX_PROBLEM_RANGE)