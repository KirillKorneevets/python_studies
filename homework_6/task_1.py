byte_value = b'r\xc3\xa9sum\xc3\xa9'

decoded_string = byte_value.decode('utf-8')
print(decoded_string)

latin1_encoded = decoded_string.encode('latin1')
print(latin1_encoded)

decoded_latin1 = latin1_encoded.decode('latin1')
print(decoded_latin1)
