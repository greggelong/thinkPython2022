def backstr(s):
    index = len(s)-1
    output = ""
    while index >=0:
        output += s[index]
        print(output)
        index-=1
        

    return output




print("hello")
print(backstr('greg'))