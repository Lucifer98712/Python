# Program to encrypt and decrypt using caesar cipher
def convertTextToNum(Text,alp):
    pTNo = [] 
    for i in range(len(Text)):
        j=0
        while(alp[j] != Text[i]):
            j+=1

        pTNo.append(j)    

    return pTNo

def Encryption(PlainText,key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherText = ''
    ct = 0
    pTNo = []
    pTNo = convertTextToNum(PlainText,alphabet)
    for i in range(len(PlainText)):
        ct = (pTNo[i] + int(key)) % 26
        cipherText+=alphabet[ct]

    return cipherText



plainText = input('Enter PlainText: ')
key = input('Enter Key: ')
encryptedText = Encryption(plainText.upper(),key)
print('The Encrypted Text is: ' + encryptedText)    
