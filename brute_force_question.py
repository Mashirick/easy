ciphertext = "KHOORZRUOG"

# 穷举26个密钥， 然后对密文进行解密， 并且把结果输出，
# 观察哪个结果是有语义的
def bruteforce(ciphertext):
    # TODO
    result=[]
    for key in range(26):
        cache_result=''
        for letter in ciphertext:
            cache_letter=chr((ord(letter)-key-65)%26+65)
            cache_result+=cache_letter
        result.append(cache_result)
    # END
    return result
    

result=bruteforce(ciphertext)
print(result)
#HELLOWORLD