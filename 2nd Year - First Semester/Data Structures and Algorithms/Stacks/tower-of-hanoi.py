# Name: Rhainer Mata
# note: tower of hanoi, wala mani na test 

def f(n,s,a,d):
    if n==1:
        print(f"move disk {n} from {s} to {d}")
        return
    f(n-1,s,d,a)
    print(f"move disk {n} from {s} to {d}")
    f(n-1,a,s,d)

n=3
f(n,'a','b','c')