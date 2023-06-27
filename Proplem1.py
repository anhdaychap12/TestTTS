def minStringLength(s):
    prevLength = len(s)
    
    while True:
        # Thay thế "AB" và "CD" bằng chuỗi rỗng
        s = s.replace("AB", "").replace("CD", "")
        
        if len(s) == prevLength:
            break
        
        prevLength = len(s)
    
    return len(s)



print (minStringLength("ACBBD"))