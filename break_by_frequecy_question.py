from math import sqrt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ciphertext = "RQFHXSRQDWLPHWKHUHZDVDQROGPRWKHUSLJZKRKDGWKUHHOLWWOHSLJVDQGQRWHQRXJKIRRGWRIHHGWKHPVRZKHQWKHBZHUHROGHQRXJKVKHVHQWWKHPRXWLQWRWKHZRUOGWRVHHNWKHLUIRUWXQHVWKHILUVWOLWWOHSLJZDVYHUBODCBKHGLGQWZDQWWRZRUNDWDOODQGKHEXLOWKLVKRXVHRXWRIVWUDZWKHVHFRQGOLWWOHSLJZRUNHGDOLWWOHELWKDUGHUEXWKHZDVVRPHZKDWODCBWRRDQGKHEXLOWKLVKRXVHRXWRIVWLFNVWKHQWKHBVDQJDQGGDQFHGDQGSODBHGWRJHWKHUWKHUHVWRIWKHGDBWKHWKLUGOLWWOHSLJZRUNHGKDUGDOOGDBDQGEXLOWKLVKRXVHZLWKEULFNVLWZDVDVWXUGBKRXVHFRPSOHWHZLWKDILQHILUHSODFHDQGFKLPQHBLWORRNHGOLNHLWFRXOGZLWKVWDQGWKHVWURQJHVWZLQGVWKHQHAWGDBDZROIKDSSHQHGWRSDVVEBWKHODQHZKHUHWKHWKUHHOLWWOHSLJVOLYHGDQGKHVDZWKHVWUDZKRXVHDQGKHVPHOOHGWKHSLJLQVLGHKHWKRXJKWWKHSLJZRXOGPDNHDPLJKWBILQHPHDODQGKLVPRXWKEHJDQWRZDWHU"

# 计算两个序列的向量角度 cosine
def cosangle(x,y):
    numerator = 0
    lengthx2 = 0
    lengthy2 = 0
    for i in range(len(x)):
        numerator += x[i]*y[i]

        lengthx2 += x[i]*x[i]
        lengthy2 += y[i]*y[i]
    return numerator / sqrt(lengthx2*lengthy2)

# 英文单词的频率表
# https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
monofrequencies = [0]*26
monofrequencies[0] = 0.0812
monofrequencies[1] = 0.0149
monofrequencies[2] = 0.0271
monofrequencies[3] = 0.0432
monofrequencies[4] = 0.1202
monofrequencies[5] = 0.0230
monofrequencies[6] = 0.0203
monofrequencies[7] = 0.0592
monofrequencies[8] = 0.0731
monofrequencies[9] = 0.0010
monofrequencies[10] = 0.0069
monofrequencies[11] = 0.0398
monofrequencies[12] = 0.0261
monofrequencies[13] = 0.0695
monofrequencies[14] = 0.0768
monofrequencies[15] = 0.0182
monofrequencies[16] = 0.0011
monofrequencies[17] = 0.0602
monofrequencies[18] = 0.0628
monofrequencies[19] = 0.0910
monofrequencies[20] = 0.0288
monofrequencies[21] = 0.0111
monofrequencies[22] = 0.0209
monofrequencies[23] = 0.0017
monofrequencies[24] = 0.0211
monofrequencies[25] = 0.0007

# 凯撒密码解密函数
def caesar_decrypt(ciphertext, key):
    decrypted_text = ""

    # TODO
    for i in ciphertext:
        cache_letter=(ord(i)-65-key) % 25 + 65
        decrypted_text+=chr(cache_letter)
    # END

    return decrypted_text

# 统计密文的词频表
frequencies = [0]*26
# TODO
for i in range(26):
    frequencies[i]=ciphertext.count(chr(65+i))/len(ciphertext)
#  END

# 计算词频移位与英文词频的cosine值， 
# 26个 cosine 值里最大的即为最可能的移位
# 由此确定凯撒密码的密钥
# TODO
key = ''
cache_per=[]
for i in range(26):
    cache_cent=cosangle(monofrequencies,frequencies)
    cache_per.append(cache_cent)
    frequencies.append(frequencies.pop(0))
    
    
key=cache_per.index(max(cache_per))


# 最后解密
decrypted_text = caesar_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Best Shift:", key)
print("Decrypted Text:", decrypted_text)