if __name__ == "__main__":
    # main function for the cipher
    def e_d():
        # getting inputs
        print("Hello. Would you like to encrypt or decrypt your text?")
        dn=input("Type \"e\" for encryption and \"d\" for decryption:\n")
        if dn != "e" and dn!= "d":
            raise ValueError("Input can only be e or d!")
            return
        text=input("Please input your text:\n")
        shift=int(input("Please, type in your key:\n"))
        
        # encrypt texts
        if dn=="e":
            result=encrypt(text,shift)
            print(f"The encrypted text of your input, {text} is {result}")
            return result
        
        # decrypt texts
        elif dn=="d":
            result=decrypt(text,shift)
            print(f"The decrypted text of your input, {text} is {result}")
            return result
        

    def encrypt(plaintext,shift):
        
        ciphertext=""
        for t in plaintext:
            if t.isalpha():
                base=ord("A") if t.isupper() else ord("a")
                newt=chr(((ord(t)-base)+shift)%26 + base)
                ciphertext+=newt
            elif ord(t) == 32:
                ciphertext+=""
            else:
                ciphertext+=t
        return ciphertext
    
    # To decipher text
    def decrypt(ciphertext,shift):
        
        plaintext=""
        for t in ciphertext:
            if t.isalpha():
                base=ord("A") if t.isupper() else ord("a")
                newt=chr(((ord(t)-base)-shift)%26 + base)
                plaintext+=newt
            elif ord(t) == 32:
                plaintext+=""
            else:
                plaintext+=t
        return plaintext
    e_d()
