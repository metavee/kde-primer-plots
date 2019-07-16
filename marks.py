import numpy as np


def gen_marks(seed=None):
    # set RNG state if specified
    if seed is not None:
        rng_state = np.random.get_state()
        np.random.seed(seed)

    exam_max = 60

    n_students = 100

    # bimodal distribution - first group higher mean/low variance, second group lower mean/high variance

    group1_prob = 0.6 # probability of being in group 1
    group1_mean = 48.
    group1_var = 4.

    group2_mean = 40.
    group2_var = 10.

    # randomly assign students to either group and give a mark
    in_group1 = np.random.random(n_students) < group1_prob
    in_group2 = ~in_group1
    marks = np.zeros(n_students)
    marks[in_group1] = np.random.normal(group1_mean, group1_var, int(in_group1.sum()))
    marks[in_group2] = np.random.normal(group2_mean, group2_var, int(in_group2.sum()))

    # round marks, cap, and convert to percentage
    marks = np.round(marks)
    marks[marks < 0] = 0
    marks[marks > exam_max] = exam_max
    marks_percent = 100 * marks / exam_max

    # restore RNG state
    if seed is not None:
        np.random.set_state(rng_state)

    return marks_percent
