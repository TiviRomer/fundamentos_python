def cuenta(n):
    print(n, end = "... ")
    n -= 1
    if n > 0:
        cuenta(n)
    else:
        print("Despegue!")
        return

cuenta(10)