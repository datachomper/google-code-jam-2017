def flip (s,k,i):
   for j in xrange(i,i+k):
        if s[j] == "+":
            s[j] = '-'
        else:
            s[j] = '+'
 
def flipem(s,k):
    # <--- Go this way first, set all to -
    for i in xrange(len(s)-k, -1, -1):
        if s[i+k-1] == "+":
            flip(s,k,i)
        print s,k,i

    # ---> Go this way next, set all to +
    for i in xrange(0, len(s)-k+1):
        if s[i] == "-":
            flip(s,k,i)
        print s,k,i

#Import the data
tests = []
T = int(raw_input())
for i in xrange(1,T+1):
    tests.append((raw_input().split(" ")))
print tests
print len(tests)

# Loop over each data row
for s,k in tests:
    flipem(list(s),int(k))
