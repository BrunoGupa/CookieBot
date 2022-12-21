import math

def exp_growth(total_elapsed_time, THRESHOLD_TO_GROW, MAX_CLICK_TIME):
    linear_decay = (THRESHOLD_TO_GROW - total_elapsed_time)/(THRESHOLD_TO_GROW)
    exp_fun = math.exp(-linear_decay)
    the_max = min(exp_fun * 3, MAX_CLICK_TIME)
    return the_max
