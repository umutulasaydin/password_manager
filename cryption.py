
letters = ("""ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuyvwxyz0123456789"é!'+%&/()=?_*-#${[]}\|@€,;><.:""")
key = ("""UFOKQMSHDWEZTBXJCIVAYLRNGPufokqmshdweztbxjcıvaylrngp%*>]:é}7['{$8)4_#9!."0/&@5=€;,(1-63?\+|2<""")


def crypte(string):

    crypted = str.maketrans(letters, key)
    crypted_string = string.translate(crypted)

    return crypted_string

def decrypte(string):
    
    decrypted = str.maketrans(key, letters)
    decrypted_string = string.translate(decrypted)

    return decrypted_string



print(crypte("AAAA"))