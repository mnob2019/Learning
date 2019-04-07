if __name__ == '__main__':
    
    n = int(input())
    arr = map(int, input().split())
    
    def max(arr):
        return sorted(set(arr))[-2]

    
    
    print (max(arr))