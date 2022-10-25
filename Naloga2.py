our_list = [1,2,3,4,5,6,7]
izbrana = our_list[4]
our_list.remove(our_list[4])


our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": izbrana,
    "e": 357,
    "f": 12
}

new_tuple = tuple(our_dict.values())
our_tuple = (357, 12, 12, 8, 5, 2, 2)

if new_tuple == our_tuple:
    print(True)
else:
    print(False)


