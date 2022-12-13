n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
country_power = input().split()
neighbors = {}
for i in range(m):
    nn = input().split()
    if nn[0] in neighbors:
        neighbors[nn[0]].append(nn[1])
    else:
        neighbors[nn[0]] = [nn[1]]

    if nn[1] in neighbors:
        neighbors[nn[1]].append(nn[0])
    else:
        neighbors[nn[1]] = [nn[0]]


def is_okey(num):
    ss = str(num)
    current_power = country_power[num]
    current_neighbors = neighbors[ss]
    dp = [current_power]
    while len(current_neighbors) > 0:
        for item in current_neighbors:
            if country_power[int(item)] < dp[-1]:
                dp.append(country_power[int(item)] + dp[-1])
                current_neighbors.remove(item)
                for val in neighbors[item]:
                    current_neighbors.append(val)
                break

    return dp


print(is_okey(1))
