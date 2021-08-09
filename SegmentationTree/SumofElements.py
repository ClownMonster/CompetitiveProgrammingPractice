from math import ceil, log2

def getSumHelper(st, sp, ep, sr, er, cur):
    if sr <= sp and er >= ep:
        return st[cur]
    if ep < sr or sp > er: return 0
    mid = sp + (ep - sp)//2
    return getSumHelper(st,sp,mid,sr,er,2*cur+1)+getSumHelper(st,mid+1,ep,sr,er,cur*2+2)
    


def getSum(st, n , sr, er):
    if sr < 0 and er > n-1 or sr > er:
        return -1
    return getSumHelper(st,0,n-1,sr,er,0)
    

def updateHelper(st,sp,ep,i,diff,cur):
    if i < sp or i > ep:
        return
    st[cur] = st[cur]+diff
    
    if sp != ep:
        mid = sp + (ep-sp)//2
        updateHelper(st,sp,mid,i,diff,cur*2+1)
        updateHelper(st,mid+1,ep,i,diff,cur*2+2)


def update(arr,st,n,i,new_val):
    if i < 0 or i > n-1:
        return -1
    diff = new_val - arr[i]
    arr[i] = new_val
    updateHelper(st,0,n-1,i,diff,0)
    

def constructHelper(arr,st,sp,ep,cur):
    if sp == ep:
        st[cur] = arr[sp]
        return arr[sp]
    mid = sp + (ep-sp)//2
    st[cur] = constructHelper(arr,st,sp,mid,cur*2+1) + constructHelper(arr,st,mid+1,ep,cur*2+2)
    return st[cur]
    

def constructST(arr, n):
    height = ceil(log2(n))
    max_size = 2 * (2**height) -1
    st = [0]*max_size
    constructHelper(arr,st,0,n-1,0)
    return st

if __name__ == "__main__":
    arr = [1,3,5,7,9,11]
    st = constructST(arr,len(arr))
    print(arr)
    n = len(arr)
    print(st)
    update(arr, st, n, 1, 4)
    print(arr)
    print(st)
    print(getSum(st,n,1,3))

