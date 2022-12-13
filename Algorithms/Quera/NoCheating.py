npq=input().split()
n=int(npq[0])
p=int(npq[1])
q=int(npq[2])


chance_words={}
for i in range(n):
    chance_word=input()

    chance_word2=chance_word[:p]+chance_word[len(chance_word)-q:]
    if chance_word2 in chance_words:
        continue
    else:
        chance_words[chance_word2]=1

count=0
for value in chance_words.values():
    count+=value

print(count)