def Dec2Bin(dec):
    result=""
    if dec:
        print("%d" % dec)
        result=Dec2Bin(dec//2) # 地板除：先算除法，然后向下取整(丢失小数)
        print(result)
        return result+str(dec%2)
    else:
        return result
print(Dec2Bin(62))
