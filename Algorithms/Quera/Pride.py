from collections import defaultdict
import copy
nandm = input()
n, m = nandm.split()
n = int(n)
m = int(m)
a_b = defaultdict(list)
b_a = defaultdict(list)
for i in range(m):
    rel = input().split()
    a = rel[0]
    b = rel[1]
    a_b[a].append(b)
    b_a[b].append(a)

visited = {}
queue = []


def cycle_detection(visited, a_b, node):
    cycle = []
    queue.append(node)
    visited[node] = []
    while len(queue) > 0:
        m = queue.pop(0)
        for item in a_b[m]:
            if item in visited:
                temp = copy.copy(visited[item])
                temp.append(item)
                cycle.append(temp)
            else:
                temp=copy.copy(visited[m])
                temp.append(m)
                visited[item] = copy.copy(temp)
                del  temp
                queue.append(item)
    return cycle


cycle = cycle_detection(visited, a_b, '1')
result = {}

for value in cycle:
    for item in value:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
output = []
for key in result.keys():
    if result[key] == len(cycle):
        output.append(key)

output1 = []
for item in output:
    item1 = int(item)
    output1.append(item1)

output1.sort()
res = ""
for item in output1:
    res += str(item) + " "

print(a_b)
print(len(output1))
print(res)
