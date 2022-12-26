import textwrap

def wrap(string, max_width):
    newstr = ""
    # print(max_width)
    for i in  range(0,len(string)):
        if i!=0 and  i % (max_width) == 0:
            newstr+="\n"
        newstr+=string[i]    
    return newstr

if __name__ == '__main__':
