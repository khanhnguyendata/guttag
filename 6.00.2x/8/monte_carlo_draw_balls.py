import random

def balls_of_same_color():
    """
    Draw 3 balls randomly from a bucket containing 3 red balls and 3 green balls.
    Return True if all three balls are of the same color, False otherwise.
    :return: True if all three balls are of the same color, False otherwise.
    """
    bucket = ['R'] * 3 + ['G'] * 3
    drawn_balls = []
    for i in range(3):
        random.shuffle(bucket)
        drawn_balls.append(bucket.pop())

    if 'R' in drawn_balls and 'G' in drawn_balls:
        return False
    else:
        return True


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    success_count = 0
    for trial in range(numTrials):
        if balls_of_same_color():
            success_count += 1

    return success_count/numTrials


print(noReplacementSimulation(1000000))