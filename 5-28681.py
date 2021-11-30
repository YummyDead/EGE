for i in range(128, 255):
    N = bin(i)[2:]
    N = N.replace('0','2').replace('1','0').replace('2', '1')
    N = int(N, 2)
    if i - N == 105:
        print(i)
        break
            
