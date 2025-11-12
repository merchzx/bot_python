def checking(text):
    result = {
        "Numbers": sum(ch.isdigit() for ch in text),
        "Letters": sum(ch.isalpha() for ch in text),
        "BIG letters": sum(ch.isupper() for ch in text),
        "SMALLS letters": sum(ch.islower() for ch in text),
        "Symbols": len(text)
    }
    return result

print(checking("123")["Symbols"])

