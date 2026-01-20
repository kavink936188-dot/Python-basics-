try:
    a=int(input())
    b=int(input())
    c=input()
except ValueError as e:
    print("value Error ",e)
except TypeError as e:
    print("Type Error",e)
except Exception:
    print("somthing wrong")
finally :
    print("done")
