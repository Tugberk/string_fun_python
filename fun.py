s = input()
#piramit below

for i in range(len(s)+1):
    print(s[0:i])
    if(i == len(s)):
        for i in range(len(s)+1):
            print(s[0:-i])

print("---------------")
print("---------------")
print('')

#yukaridan asagi da asagidaki kod

#for odd numbers
if(len(s) % 2 != 0):
    mid = int((len(s) - 1) / 2)
    #print(s[mid])
    right = mid - 1
    left = mid + 2
    for aa in range(right+1):
        print('-', end='')
    print(s[mid], end='')
    for bb in range(len(s) - left+1):
        print('-', end='')
    print()


    
    uzunluk = int((len(s) + 1) / 2)
    
    for i in range(uzunluk-1):
        for j in range(right):
            print('-', end='')
        print(s[right:left], end='')
        #right = right - 1
        #left = left + 1
        for k in range(len(s) - left):
            print('-', end='')
        right = right - 1
        left = left + 1
        print('')

else:
    mid = int((len(s) /2) -1)
    #print(s[mid])
    right = mid - 1
    left = mid + 2
    for aa in range(right+1):
        print('-', end='')
    print(s[mid:mid+2], end='')
    for bb in range(len(s) - left):
        print('-', end='')
    print()
  
    uzunluk = int((len(s)) / 2)
    
    for i in range(uzunluk-1):
        for j in range(right):
            print('-', end='')
        print(s[right:left+1], end='')
        #right = right - 1
        #left = left + 1
        for k in range(len(s) - left-1):
            print('-', end='')
        right = right - 1
        left = left + 1
        print('')

        
