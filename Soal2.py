def copyhuruf(str):
    strLegth = len(str)
    if strLegth % 2 == 0:
         return str[0] + str[1] + str[2] +' dan '+ str[-3] + str[-2] + str[-1]
    else:
        tengah = int(strLegth/2)
        return str[tengah - 1] + str[tengah] + str[tengah+1]

kata = input("Masukan Kata: ")
res = copyhuruf(kata)
print("Huruf yang diambil pada kata", kata,"adalah",res)