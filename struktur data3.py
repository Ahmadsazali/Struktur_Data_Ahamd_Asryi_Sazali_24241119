# Data mahasiswa
mahasiswa = [
    {"nama": "Ahmad", "nilai": 87},
    {"nama": "Ars", "nilai": 75},
    {"nama": "Sazali", "nilai": 66},
    {"nama": "Awal", "nilai": 59},
    {"nama": "Udin", "nilai": 45},
    {"nama": "Sani", "nilai": 39}
]

# Fungsi konversi nilai ke huruf
def konversi_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 60:
        return "C+"
    elif nilai >= 55:
        return "C"
    elif nilai >= 50:
        return "D"
    elif nilai >= 40:
        return "E"
    else:
        return "E (Tidak Lulus)"

# Menampilkan tabel
print("{:<10} {:<10} {:<10}".format("Nama", "Nilai", "Grade"))
print("-" * 30)
for mhs in mahasiswa:
    grade = konversi_nilai(mhs["nilai"])
    print("{:<10} {:<10} {:<10}".format(mhs["nama"], mhs["nilai"], grade))