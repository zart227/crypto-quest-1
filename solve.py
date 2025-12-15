CIPHERTEXT = "2E3GX3C3U93E4JK545I35M69L6Q6N78F91PAF9D0CED0GEAF91GQHZRJ6K95LON1TN4QB2S0TMVVR"

def base36_to_int(pair: str) -> int:
    return int(pair, 36)

def caesar_shift(text: str, shift: int) -> str:
    result = []
    for c in text:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(c)
    return ''.join(result)

# 1. Remove every 5th character (noise)
cleaned = ''.join(c for i, c in enumerate(CIPHERTEXT, 1) if i % 5 != 0)

# 2. Split into base-36 pairs
pairs = [cleaned[i:i+2] for i in range(0, len(cleaned), 2)]

# 3. Decode with quadratic offset
decoded_chars = []
offset = 0

for idx, pair in enumerate(pairs):
    value = base36_to_int(pair)
    if idx >= 1:
        offset += (idx + 1) ** 2
    decoded_chars.append(chr(value - offset))

intermediate = ''.join(decoded_chars)

# 4. Caesar shift -3
result = caesar_shift(intermediate, -3)

print(result)
