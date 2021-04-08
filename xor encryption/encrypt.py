def xor_encrypt(key, data):
    encrypted = ""
    i = 0

    for letter in data:
        encrypted += str(ord(letter) ^ ord(key[i % len(key)])) + '-'
        i += 1
    
    return encrypted[0:-1]

def xor_decrypt(key, data):
    decrypted = ""
    i = 0

    for letter in data.split("-"):
        decrypted += chr(int(letter) ^ ord(key[i % len(key)]))
        i += 1
    
    return decrypted[0:-1]

print(xor_encrypt('LoveYou', '/"source:Berlin;dest:Iran;date:25.1.21;data:Sending corona vaccines"'))
print(xor_decrypt('LoveYou', '99-77-5-10-44-29-22-41-85-52-0-43-3-28-34-84-18-0-42-27-79-5-29-23-11-98-11-20-56-10-76-87-108-65-68-98-93-71-94-61-14-1-45-85-37-0-55-11-28-34-8-86-6-54-29-26-34-14-86-19-56-12-22-37-1-19-22-123'))