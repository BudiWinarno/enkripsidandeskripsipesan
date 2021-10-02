from cryptography.fernet import Fernet

pesan = "Budi Winarno"

key = Fernet.generate_key()

fernet = Fernet(key)

enkripsiPesan = fernet.encrypt(pesan.encode())

print("Pesan Asli : ", pesan)
print("\nHasil Enkripsi ", enkripsiPesan)

deskripsiPesan = fernet.decrypt(enkripsiPesan).decode()

print("Hasil Deskripsi: ", deskripsiPesan)
