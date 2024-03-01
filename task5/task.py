import numpy as np

def create_matrix(data: list) -> np.ndarray:
    visited = set()
    matrix = []

    for elem in data:
        if isinstance(elem, list):
            for subelem in elem:
                visited.add(int(subelem))
        else:
            visited.add(int(elem))

    visited = sorted(visited)
    n = len(visited)

    for elem in data:
        if isinstance(elem, list):
            row = [1 if i + 1 in elem else 0 for i in range(n)]
        else:
            row = [1 if int(elem) == i + 1 else 0 for i in range(n)]
        matrix.append(row)

    return np.array(matrix)

def calculate_S(str1: str, str2: str) -> list:
    matrix1 = create_matrix(eval(str1))
    matrix2 = create_matrix(eval(str2))

    matrix12 = np.logical_and(matrix1, matrix2)
    matrix12T = np.logical_and(matrix1.T, matrix2.T)
    criterion = np.logical_or(matrix12, matrix12T)

    answer = []
    n = criterion.shape[0]

    for i in range(n):
        item = [j + 1 for j in range(n) if criterion[i][j] == 0]
        if item:
            item.append(i + 1)
            answer.append(item)

    return answer

def get_S_for_item(value: int, S_ab: list) -> list:
    for item in S_ab:
        if value in item:
            return item
    return []

def get_unused_items(S_item: list, used: list) -> bool:
    for item in S_item:
        if item in used:
            return True
    return False

def f2(str1: str, str2: str, is_str: bool) -> list:
    S_ab = calculate_S(str1, str2)
    A_L = [elem for sublist in eval(str1) for elem in sublist] if isinstance(eval(str1), list) else eval(str1)
    B_L = [elem for sublist in eval(str2) for elem in sublist] if isinstance(eval(str2), list) else eval(str2)
    S_L2 = [elem for sublist in S_ab for elem in sublist]

    used = []
    n = len(A_L)
    x = []

    for i in range(n):
        if A_L[i] not in S_L2 and A_L[i] not in x:
            x.append(A_L[i])
        if B_L[i] not in S_L2 and B_L[i] not in x:
            x.append(B_L[i])

    res_L = []

    for i in range(n):
        if A_L[i] not in used and A_L[i] in x:
            res_L.append(A_L[i])
            used.append(A_L[i])

        if B_L[i] not in used and B_L[i] in x:
            res_L.append(B_L[i])
            used.append(B_L[i])

        S_item_A = get_S_for_item(A_L[i], S_ab)
        S_item_B = get_S_for_item(B_L[i], S_ab)

        if A_L[i] not in used and not S_item_A:
            S_item_A = get_S_for_item(A_L[i], S_ab)
            if S_item_A:
                res_L.append(S_item_A)
                used.extend(S_item_A)

        if B_L[i] not in used and not S_item_B:
            S_item_B = get_S_for_item(B_L[i], S_ab)
            if S_item_B:
                res_L.append(S_item_B)
                used.extend(S_item_B)

        if A_L[i] not in used and B_L[i] not in used:
            common_elements = list(set(A_L[i]) & set(B_L[i]))
            common_unused_elements = [elem for elem in common_elements if elem not in S_L2 and elem not in x and elem not in used]

            if len(common_unused_elements) == 1:
                res_L.append(common_unused_elements[0])
                used.append(common_unused_elements[0])
            elif len(common_unused_elements) > 1:
                res_L.append(common_unused_elements)
                used.extend(common_unused_elements)

    return res_L

def task(str1: str, str2: str) -> list:
    return f2(str1, str2, isStrResultType(str1, str2))

def main():
    str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    str2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    str3 = '[3,[1,4],2,6,[5,7,8],[9,10]]'

    print(task(str1, str2))

if __name__ == "__main__":
    main()
