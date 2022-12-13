import pandas

df=pandas.read_csv("C:/Users/moslem/desktop/data/words.csv")

q1={}
q1["counts"]=0
for j in df.words:
    if j in q1:
        q1[j]+=1
    else:
        q1["counts"]+=1
        q1[j]=1

##17144
#to:4707 a:4805 and:6517:of:6742 the:14715
#quarrelsomely
#abednego abhorred abjectly abjectus abortion abounded abridged abruptly
current_length=0
current_word=""
for k in df.words:
    if k[0]=='q':
        if len(k)>current_length:
            current_length=len(k)
            current_word=k
print(current_word)

q4=[]
for l in df.words:
    if len(l)==8 and l not in q4:
        q4.append(l)
q4.sort()
print(q4[:8])




most_reapeted=sorted(q1.items(),key=lambda x:x[1])

#print(most_reapeted)

#to:4707 a:4805 and:6517:of:6742 the:14715
print(q1["counts"])
    
