from random import choice


def match_participants(data):
    suitable = data[:]
    accept_array = []
    arr = []

    for i in data:
        min_arr = [i]
        arr.append(min_arr)

    for index, val in enumerate(arr):
        suitable2 = suitable[:]
        suitable2.remove(val[0])

        r = choice([a for a in suitable2 if a not in accept_array])
        accept_array.append(r)
        val.append(r)

    return arr
