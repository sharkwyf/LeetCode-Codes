def encrypt(s, offset):
    arr = list(s)
    for i in range(len(arr)):
        if "a" <= arr[i] <= "z":
            arr[i] = chr(ord("A") + (ord(arr[i]) - ord("a") + offset) % 26)
        elif "A" <= arr[i] <= "Z":
            arr[i] = chr(ord("a") + (ord(arr[i]) - ord("A") + offset) % 26)
        elif "0" <= arr[i] <= "9":
            arr[i] = chr(ord("0") + (ord(arr[i]) - ord("0") + offset) % 26)
    return "".join(arr)


while True:
    try:
        s1 = input()
        print(encrypt(s1, 1))
        s2 = input()
        print(encrypt(s2, -1))
    except:
        break