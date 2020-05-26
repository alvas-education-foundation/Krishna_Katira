test_cases=int(input())
        for i in range(test_cases):
            N, K = map(int,input().split())
            array = list(map(int, input().split()))
            if K > min(array):
                print(K - min(array))
            else:
                print("\0")
      