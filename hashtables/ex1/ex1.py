#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    if length == 1:
        result = None

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        package_1 = weight
        package_2 = limit - package_1
        search = hash_table_retrieve(ht, package_2)

        if search is not None:
            if search > i:
                result = (search, i)
            elif search < i:
                result = (i, search)
                


    return print_answer(result)


def print_answer(answer):
    if answer is not None:
        print(f"{answer[0]} {answer[1]}")
        return answer
    else:
        print("None")
