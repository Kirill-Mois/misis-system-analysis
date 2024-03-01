import numpy as np

def calculate_entropy(matrix: np.ndarray) -> float:
    entropy = -np.sum(matrix * np.log2(matrix))
    return entropy

def task() -> list:
    min_score = 1
    max_score = 6
    all_variants_count = max_score * max_score
    mults_count = all_variants_count
    sums_count = max_score * 2 - min_score * 2 + 1

    variants = np.zeros((sums_count, mults_count))
    sum_norm = 2

    for i in range(min_score, max_score + 1):
        for j in range(min_score, max_score + 1):
            cur_mult = i * j
            cur_sum = i + j
            variants[cur_sum - sum_norm, cur_mult - 1] += 1

    used_cols = np.any(variants, axis=0)
    resized_variants = variants[:, used_cols]

    matrix = resized_variants / all_variants_count

    PA = np.sum(matrix, axis=1)
    PB = np.sum(matrix, axis=0)

    HA = calculate_entropy(PA)
    HB = calculate_entropy(PB)
    HAB = calculate_entropy(matrix)

    HaB = HAB - HA
    HI = HB - HaB

    # Return result
    return [round(HAB, 2), round(HA, 2), round(HB, 2), round(HaB, 2), round(HI, 2)]

print(task())
