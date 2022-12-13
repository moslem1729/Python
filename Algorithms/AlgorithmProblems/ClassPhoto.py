def class_photo(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)
    back_row = red_shirt_heights if red_shirt_heights[0] > blue_shirt_heights[0] else blue_shirt_heights
    front_row = blue_shirt_heights if red_shirt_heights[0] > blue_shirt_heights[0] else red_shirt_heights
    print(back_row[0])
    for index, height in enumerate(back_row):
        if height < front_row[index]:
            return False
    return True


print(class_photo([7, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
