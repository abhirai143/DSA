def recursive(n):
    if(n<1):
        print("less than 1")
    else:
        recursive(n-1)
        print(n)
        
recursive(80)
