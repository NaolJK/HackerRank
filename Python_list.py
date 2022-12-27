def solve(N):
    new_list = []
    for i in range(N):
        input_ = input().split()
        # print(input_)
        if str(input_[0]) == "insert":
            new_list.insert(int(input_[1]),int(input_[2]))
        elif input_[0] == "print":
            print(new_list)
        elif input_[0] == "remove":
            new_list.remove(int(input_[1]))
        elif input_[0] == "sort":
            new_list.sort()
        elif input_[0] =="pop":
            new_list.pop()
        elif input_[0] == "reverse":
            new_list = new_list[::-1] 
        elif input_[0] == "append":
            new_list.append(int(input_[1]))
            
        else:
            print("no such operation" + f" {input_[0]}")
    
if __name__ == '__main__':
    N = int(input())
    solve(N)
        
    
    
