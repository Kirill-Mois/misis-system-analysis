import json
import numpy as np

def list_of_reviews_from_json(reviews_str, template):
    reviews = json.loads(reviews_str)
    reviews_list = [0] * len(template)

    for i, review in enumerate(reviews):
        if isinstance(review, list):
            for el in review:
                reviews_list[template[el]] = i + 1
        else:
            reviews_list[template[review]] = i + 1
    
    return reviews_list

def task(*args):
    experts_count = len(args)
    template = {}
    reviews_count = 0

    for reviews_str in args:
        reviews = json.loads(reviews_str)
        for review in reviews:
            if isinstance(review, list):
                for elem in review:
                    template[elem] = reviews_count
                    reviews_count += 1
            else:
                template[review] = reviews_count
                reviews_count += 1
        
    matrix = [list_of_reviews_from_json(reviews_str, template) for reviews_str in args]
    matrix = np.array(matrix)

    # Compute the sum of each column
    column_sums = np.sum(matrix, axis=0)

    # Calculate dispersion
    D = np.var(column_sums) * len(column_sums) / (len(column_sums) - 1)
    D_max = experts_count ** 2 * (len(column_sums) ** 3 - len(column_sums)) / 12 / (len(column_sums) - 1)

    return format(D / D_max, ".2f")

A = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
B = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
C = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

print(task(A, B, C))
