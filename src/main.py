import time 
from turing_machine import calculate
from tape_hardcode import create_rules


rules = create_rules()

# Contoh 1: String kosong
start_time = time.time() # Catat waktu mulai
result = calculate("", rules)
end_time = time.time()   # Catat waktu selesai
print(f"Input: \"\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 2: String "0"
start_time = time.time()
result = calculate("0", rules)
end_time = time.time()
print(f"Input: \"0\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 3: String "1"
start_time = time.time()
result = calculate("1", rules)
end_time = time.time()
print(f"Input: \"1\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 4: String "00"
start_time = time.time()
result = calculate("00", rules)
end_time = time.time()
print(f"Input: \"00\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 5: String "11"
start_time = time.time()
result = calculate("11", rules)
end_time = time.time()
print(f"Input: \"11\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 6: String "01"
start_time = time.time()
result = calculate("01", rules)
end_time = time.time()
print(f"Input: \"01\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 7: String "00100"
start_time = time.time()
result = calculate("00100", rules)
end_time = time.time()
print(f"Input: \"00100\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 8: String "001001"
start_time = time.time()
result = calculate("001001", rules)
end_time = time.time()
print(f"Input: \"001001\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 9: String "10111011"
start_time = time.time()
result = calculate("10111011", rules)
end_time = time.time()
print(f"Input: \"10111011\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 10: String "0110010011"
start_time = time.time()
result = calculate("0110010011", rules)
end_time = time.time()
print(f"Input: \"0110010011\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")

# Contoh 11: String "1001110011"
start_time = time.time()
result = calculate("1001110011", rules)
end_time = time.time()
print(f"Input: \"1001110011\" -> Result: {result}, Time: {end_time - start_time:.6f} seconds")