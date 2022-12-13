def tandem_bicycle(red_shirt_speeds,blue_shirt_speeds,fastest):
    total_speed=0
    if fastest:
        red_shirt_speeds.sort(reverse=True)
        blue_shirt_speeds.sort()
        for idx in range(len(red_shirt_speeds)):
            total_speed+=max(red_shirt_speeds[idx],blue_shirt_speeds[idx])
    else:
        red_shirt_speeds.sort()
        blue_shirt_speeds.sort()
        for idx in range(len(red_shirt_speeds)):
            total_speed+=max(red_shirt_speeds[idx],blue_shirt_speeds[idx])

    return total_speed


r=[5,5,3,9,2]
b=[3,6,7,2,1]

print(tandem_bicycle(r,b,True))
