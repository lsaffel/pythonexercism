def latest(scores):
    # return the last score in the list, which would be the most recent
    return scores[-1]


def personal_best(scores):
    scores.sort()

    # return the last score in the sorted list, which would be the highest
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    num_of_scores = len(scores)
    scores_list = []

    # append only the last 3 scores to the list... up to 3 maximum
    for i in range(1, num_of_scores+1):
        if i < 4:
            scores_list.append(scores[-i])

    return scores_list
