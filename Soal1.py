def change(asli, aslikata, pengganti):
    return asli.replace(aslikata, pengganti)
def hitungkata(asli, kata):
    return asli.count(kata)
print("====== Program Manipulasi string ======")
print("1. Hitung Kata")
print("2.  Ubah Kata")
pilihan =int(input("Masukan Pilihan Anda: "))
if pilihan in (1,2,3,4,5,6,7,8,9,0):
    if pilihan ==2:
        asli = input("Masukan Kalimat atau Kata: ")
        aslikata = input("Masukan Kata yang ingin diubah: ")
        pengganti = input("Masukan Kata pengganti: ")
        asli2 = asli.replace(aslikata, pengganti)
        print("String Berhasil diubah Menjadi: ",change (asli, aslikata, pengganti))
    elif pilihan == 1:
        asli = input("Masukan seuah kalimat atau kata: ")
        kata = input("Masukan kata yang ingin di hitung: ")
        print("Terdapat sebanyak",hitungkata(asli,kata))
    else: print("Kamu Nanya??")

    

