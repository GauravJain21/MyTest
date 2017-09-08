d, r = map(long, raw_input().split())
n = long(input())
ans = 0
for i in range(n):
    x, y, ri = map(long, raw_input().split())
    rin = ri + r - d
    rin *= rin
    rout = r - ri
    rout *= rout
    dist = x * x + y * y
    if(dist >= rin and dist <= rout): 
	    ans += 1	
print(ans)
