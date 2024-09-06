# Title ：凯撒密码 学生填写模板

# 凯撒密码加密函数
def caesar_encrypt(plaintext, key):
    cipher = ""
    # 将明文都转化为大写字符进行处理
    plaintext = plaintext.upper()
    # TODO 
    for i in range(len(plaintext)):
        cipher+=str(chr((ord(plaintext[i])+key-65)%26+65))
    # END
    # 对明文进行移位操作

    return cipher

# 凯撒密码解密函数
def caesar_decrypt(ciphertext, key):
    decrypted_text = ""

    # TODO
    for i in range(len(ciphertext)):
        decrypted_text+=str(chr((ord(ciphertext[i])-key-65)%26+65))
    # END
    return decrypted_text

plaintext = "hello, world"
# 将明文的其他字符进行去除， 只对英文进行处理
f = filter(str.isalpha, plaintext)
plaintext_strip = "".join(f)

# 凯撒密码移位是3
key = 3

# 加密
encrypted_text = caesar_encrypt(plaintext_strip, key)
print("Original text:", plaintext_strip)
print("Encrypted text:", encrypted_text)

# 解密
decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
