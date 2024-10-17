# Fungsi untuk mengalikan dua bilangan tanpa menggunakan operator *
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result

# Fungsi untuk menghitung pemangkatan tanpa menggunakan operator **
def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result = multiply(result, base)
    return result if exponent >= 0 else 1 / result

# Fungsi untuk memeriksa apakah suatu bilangan adalah prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contoh penggunaan
if __name__ == "__main__":
    # Menghitung perkalian
    print("Perkalian 7 dan 3:", multiply(7, 3))  # Output: 15
    
    # Menghitung pemangkatan
    print("4 pangkat 3:", power(4, 3))  # Output: 8
    
    # Memeriksa bilangan prima
    number = 8
    print(f"{number} adalah bilangan prima:", is_prime(number))  # Output: True
