#Write a function that replaces or adds key/value in a dictionary.


def update_dictionary(a_dictionary, key, value):
    new_dict = {**a_dictionary}
    new_dict[key]=value
    return new_dict


# def print_sorted_dictionary(my_dict):
#     """ Print sorted dictionary """
#     print(my_dict
