print("Nama:Ahmad Arsyi Sazali: 24241119")

# Nilai angka yang ingin dicek (24 dan 19)
inputUser = 30
print("Masukkan angka yang bernilai antara 24 sampai 19:", inputUser)

# Pemeriksaan apakah bilangan berada di antara 16 dan 24
isDiAntara = (inputUser >= 24) and (inputUser <= 19)

# Output hasil pengecekan dengan penjelasan
if isDiAntara:
    print("Angka yang Anda masukkan VALID (berada di antara 24 dan 19).")
else:
    print("Angka yang Anda masukkan TIDAK VALID (di luar rentang 24 sampai 19).")