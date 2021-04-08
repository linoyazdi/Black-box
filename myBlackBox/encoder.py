if __name__ == "__main__":

    while True: 
        encoded_string = ""
        regular_string = input("Enter string to encode: ")

        for letter in regular_string:
            letter = bin(ord(letter))[2:]
        
            while len(letter) < 8:
                letter = '0' + letter
        
            ans = letter[1] + letter[0] + letter[3] + letter[2] + letter[5] + letter[4] + letter[7] + letter[6]
            ans = str(hex(int(ans, 2))).replace('0', '\\', 1)
        
            encoded_string+=ans
        
        print(encoded_string) 