import random

def hash_string_2_universal(s, p=2147483647, m=10007):
    # Convert string to an integer (you can use any encoding)
    x = sum(ord(c) * (256 ** i) for i, c in enumerate(s))
    
    # Choose random a and b such that 1 <= a < p and 0 <= b < p
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    
    # Apply the 2-universal hash function
    hash_value = ((a * x + b) % p) % m
    
    return hash_value

# Example usage
string_to_hash = "example"
hash_value = hash_string_2_universal(string_to_hash)
print(f"Hash value for '{string_to_hash}': {hash_value}")
