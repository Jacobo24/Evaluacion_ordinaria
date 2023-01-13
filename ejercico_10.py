def xbonacci(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]
    else:
        x = len(signature)
        for i in range(n-x):
            next_val = sum(signature[-x:])
            signature.append(next_val)
        return signature

if __name__ == '__main__':
    signature = [1, 1, 1]
    n = 10
    print(xbonacci(signature, n)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]