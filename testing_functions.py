import imgaug as ia
from imgaug import augmenters as iaa

#list of functions to be used in 'single augmentation per image' mode






#list of functions to be used in 'sequential augmentation per image' mode, preserving the order in the list


func_dictionary = {'func1': lambda a: str(a),
                   'func2': lambda a: a * 4,
                   'func3': lambda a: a * 3
                   }


def perform_in_order(order,initial_arg):

    order[0] = func_dictionary[order[0]](initial_arg)
    while True:
        try:
            order[1] = func_dictionary[order[1]](order[0])
            order.pop(0)
        except IndexError:
            break

    return order[0]


print(perform_in_order(['func3','func2','func1'],2))