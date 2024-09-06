# Title ：维吉尼亚密码 学生填写模板
import numpy as np

# 维吉尼亚密码加密函数
def vigenere_encrypt(plaintext, key):
    # 密钥全部大写处理
    key = key.upper()
    cipher = []
    plaintext = plaintext.upper() # 全部大写

    # TODO
    keylist=[ ord(key[i]) for i in range(len(key)) ]
    times=len(plaintext)//len(key)+1
    keylist=(keylist*times)[:len(plaintext)] if len(plaintext)//len(key) != 0 else keylist*times
    keyarray=np.array(keylist)
    plainarray=np.array([ord(letter) for letter in plaintext ])
    encode_result=list(keyarray+plainarray)
    cipher=[chr((letter-65)%26+65) for letter in encode_result]
    # END
    return ''.join(cipher) # 把列表形式的cipher转化为字符串形式

# 维吉尼亚密码解密函数
def vigenere_decrypt(ciphertext, key):
    # 密钥全部大写处理
    key = key.upper()
    plain = []
    ciphertext = ciphertext.upper()

    # TODO
    keylist=[ ord(key[i]) for i in range(len(key)) ]
    times=len(ciphertext)//len(key)+1
    keylist=(keylist*times)[:len(ciphertext)] if len(ciphertext)//len(key) != 0 else keylist*times
    keyarray=np.array(keylist)
    cipherarray=np.array([ord(letter) for letter in ciphertext ])
    decode_result=-keyarray+cipherarray
    plain=[chr((letter-65)%26+65) for letter in decode_result]
    # END
    
    return ''.join(plain)

plaintext = "hello, world"
# 将明文的其他字符进行去除， 只对英文进行处理
f = filter(str.isalpha, plaintext)
plaintext_strip = "".join(f)

key = "KEY"

# 加密
encrypted_text = vigenere_encrypt(plaintext_strip, key)
print("Plaintext:", plaintext_strip.upper())
print("Encrypted:", encrypted_text)

# 解密
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)