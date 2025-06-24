# Turing_Machine_Repeated_String
# Penyelesaian Mesin Turing untuk Permasalahan Keputusan Verifikasi String Self-Copy 

## Deskripsi
Program Mesin Turing untuk memverifikasi apakah suatu string self-copy atau tidak.


### Langkah-langkah
1. **Clone Repository**
   ```bash
   git clone https://github.com/xinuzo/Turing_Machine_Repeated_String.git
   ```
2. **Jalankan Program**
   ```bash
   python src/main.py
   ```

## Format Input
```
print(calculate("00", rules)) # True
print(calculate("001001", rules)) # True
print(calculate("10111011", rules)) # True
print(calculate("01", rules)) # False
print(calculate("00100", rules)) # False
print(calculate("10111101", rules)) # False
```
## Format Output
```
Input: "" -> Result: False, Time: 0.000000 seconds
Input: "0" -> Result: False, Time: 0.000000 seconds
Input: "1" -> Result: False, Time: 0.000000 seconds
Input: "00" -> Result: True, Time: 0.000000 seconds
Input: "11" -> Result: True, Time: 0.000000 seconds
Input: "01" -> Result: False, Time: 0.000000 seconds
Input: "00100" -> Result: False, Time: 0.000000 seconds
Input: "001001" -> Result: True, Time: 0.000000 seconds
Input: "10111011" -> Result: True, Time: 0.001451 seconds
Input: "0110010011" -> Result: False, Time: 0.000000 seconds
Input: "1001110011" -> Result: True, Time: 0.001112 seconds
```
## Penulis
- Rendi Adinata (10123083)

Kelas K1

