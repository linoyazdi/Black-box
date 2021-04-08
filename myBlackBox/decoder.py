str_to_dec=r'\x9d\x9f\xb1\x9e\x92\x9c\x10\xb0\x92\xb3\xb3\x9a\x9d\x9b\x9a\xb1'
str_to_dec=str(str_to_dec).replace("\\",'0')
num=str_to_dec.count("x")
j=0
ans = ''
for k in range(int(num)):
	letter=str_to_dec[j]+str_to_dec[j+1]+str_to_dec[j+2]+str_to_dec[j+3]
	j+=4
	an_integer = int(letter, 16)
	value = (bin(int((hex(int(letter, 16))), 16)).zfill(8))
	value=value.replace('b','0')
	value=value[2:]
	while len(value) < 8:
		value = '0' + value
	value = value[1] + value[0] + value[3] + value[2] + value[5] + value[4] + value[7] + value[6]
	value=''.join(chr(int(value[i*8:i*8+8],2)) for i in range(len(value)//8))
	ans+=value

print(ans)