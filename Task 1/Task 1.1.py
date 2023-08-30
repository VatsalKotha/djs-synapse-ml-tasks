jumbled_superheros = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'huLK']

indices = []
decoded_names = []

for index, superhero in enumerate(jumbled_superheros):
    indices.append(index)

    decoded_name = superhero.lower().replace("_", " ")
    decoded_names.append(decoded_name)
print(indices)
print(decoded_names)

name_lengths = []

length_function = lambda x: len(x)
name_lengths = list(map(length_function, decoded_names))

indices = list(range(len(decoded_names))) 

indices.sort(key=lambda idx: name_lengths[idx])

print(indices)

print(name_lengths)

for index in indices:
    print(f"{decoded_names[index]}")

# for i in decoded_names:
#     print(i)