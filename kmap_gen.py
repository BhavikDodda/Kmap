import math

def NumberToBinArray(i,n0):

    return tuple(int(k) for k in list(str(bin(i)[2:]).zfill(n0))) if n0>0 else tuple([])

minTerms=[0,1,2,5,7,8,9,13,14]
N=math.floor(math.log2(max(minTerms)))+1
booleanFunc=[NumberToBinArray(i,N) for i in minTerms]

##
twoToTheN=[NumberToBinArray(i,N) for i in range(2**N)]
chooseCombinations=[]
for comb in twoToTheN:
    if sum(comb)>len(chooseCombinations)-1:
        chooseCombinations.append([])
    chooseCombinations[sum(comb)].append(comb)

#1:fixed, 0:vary and depending on number of 1s and 0s, we get pair, quads, octets etc.

def MapTwoListsOnBinTuple(list1,list2,binlist):
    ans=[]
    for i in binlist:
        if(i==1):
            ans.append(list1[0])
            list1=list1[1:]
        elif(i==0):
            ans.append(list2[0])
            list2=list2[1:]

    return tuple(ans)

#print(MapTwoListsOnBinTuple([1,2,3],[4,5],(1,0,1,0,1)))
minimization=[]
keepTrack=set([])
for categoryofTeTs in chooseCombinations:
    for tets in categoryofTeTs:
        Ones=sum(tets)
        Zeroes=N-Ones
        print(Ones)
        fixedParts=[NumberToBinArray(i,Ones) for i in range(2**Ones)]
        for fixedPartOfSpecificTet in fixedParts:
            print(tets)
            print(fixedPartOfSpecificTet)
            varyPart=[NumberToBinArray(i,Zeroes) for i in range(2**Zeroes)]
            
            elementsInTet=[MapTwoListsOnBinTuple(fixedPartOfSpecificTet,insideTet,tets) for insideTet in varyPart]
            if all(i in keepTrack for i in elementsInTet): #to see if a tet was a subset of another tet that has been already covered
                print('alr included')
                continue
            if all(i in booleanFunc for i in elementsInTet):
                print([-1 for i in range(len(tets)-len(fixedPartOfSpecificTet))])
                minimization.append(MapTwoListsOnBinTuple(fixedPartOfSpecificTet, [-1 for i in range(len(tets)-len(fixedPartOfSpecificTet))] ,tets))
                keepTrack.update(set(elementsInTet))
            print("tet")
            if len(keepTrack)==len(minTerms):
                print('break0')
                break
        print("----")
        if len(keepTrack)==len(minTerms):
            print('break1')
            break
    if len(keepTrack)==len(minTerms):
        print('break2')
        break

print(minimization)

varname=['a','b','c','d']


def printBoolFunc(boolfunc):
    temp1=[tuple(filter(lambda x:x!=0,[int((abs(term[i]+0.5)+abs(term[i])-2+0.5)*(i+1)) for i in range(N)])) for term in boolfunc]
    return(" + ".join(["".join([varname[abs(ele)-1]+("'" if ele<0 else "") for ele in tup]) for tup in temp1]))

print(printBoolFunc(booleanFunc))
print(printBoolFunc(minimization))