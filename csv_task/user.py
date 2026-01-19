def generate_id(number):
    count = 1
    ids = []
    for _ in range(number):
        ids.append(count)
        count +=  1
    return ids
    