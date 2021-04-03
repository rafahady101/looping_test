total = 0
while True:
    x = str(input("Masukkan angka? (ya/tidak): "))
    if x.upper() == "YA":
        data = int(input("Angka: "))
        total += 1
        if data % 2 == 0:
            print(data,"Merupakan angka genap")
        else:
            print(data,"Merupakan angka ganjil")
    elif x.upper() == "TIDAK":
        if total == 0:
            break
        print("Anda memasukkan angka sebanyak",total,"kali")
        break
    else:
        print("Input yang anda masukkan salah")
        True
