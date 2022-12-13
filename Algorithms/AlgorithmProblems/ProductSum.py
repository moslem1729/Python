def product_sum(nested_list, coefficient=1):
    total=0
    for item in nested_list:
        if type(item)==list:
            total=total + product_sum(item,coefficient+1)
        else:
            total += item
    return total*coefficient

nested_list=[1,[1,[1,2],2,[1,2]],3]
print(product_sum(nested_list))

