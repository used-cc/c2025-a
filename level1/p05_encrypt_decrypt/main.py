def en(text):
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result

def de(cipher):
    result = ""
    for char in cipher:
        result += chr(ord(char) - 3)
    return result

if __name__ == "__main__":
    s = input("请输入待加密字符串：")
    en = en(s)
    print("加密后：", en)
    de = de(en)
    print("解密后：", de)