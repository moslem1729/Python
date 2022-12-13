def array_of_products(array):
    products_array = [item for item in array]
    for index in range(len(array)):
        products_array[index] = index_product(array, index)
    return products_array


def index_product(array, index):
    product = 1
    for i in range(len(array)):
        if i == index:
            continue
        else:
            product = product * array[i]
    return product


def array_of_products_ans(array):
    products=[1 for _ in array]
    for i in range(len(array)):
        running_product=1
        for j in range(len(array)):
            if j !=i:
                running_product=array[j]*running_product
        products[i]=running_product
    return products


def array_of_products_prettier(array):
    products=[1 for _ in array]

    left_running_product=1
    for i in range(len(array)):
        products[i]=left_running_product
        left_running_product *= array[i]
    right_running_product=1
    for i in reversed(range(len(array))):
        products[i] *=right_running_product
        right_running_product *=array[i]

    return products


arr = [5, 1, 2, 4]
print(array_of_products_ans(arr))
print(array_of_products(arr))
print(array_of_products_prettier(arr))