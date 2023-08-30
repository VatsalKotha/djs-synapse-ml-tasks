def explode_chains(encoded_lists):
    def has_consecutive_three(sequence):
        for i in range(len(sequence) - 2):
            if sequence[i] + 1 == sequence[i + 1] and sequence[i + 1] + 1 == sequence[i + 2]:
                return True
        return False

    def explode_sequence(sequence):
        i = 0
        while i < len(sequence) - 2:
            if sequence[i] + 1 == sequence[i + 1] and sequence[i + 1] + 1 == sequence[i + 2]:
                sequence.pop(i)
                sequence.pop(i)
                sequence.pop(i)
            else:
                i += 1

    for encoded_list in encoded_lists:
        while has_consecutive_three(encoded_list):
            explode_sequence(encoded_list)

    return encoded_lists

encoded_list = [
    [1, 2, 3, 4, 6],
    [5, 7, 8, 9, 15],
    [12, 14, 16, 18],
    [10, 11, 12, 13, 16, 17, 18, 20]
]
result = explode_chains(encoded_list)
print(result)