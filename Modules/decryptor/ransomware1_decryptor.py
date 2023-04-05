def decrypt(input_file, output_file):
  with open(input_file, 'rb') as in_file, open(output_file, 'wb') as out_file:
    encrypted_file = in_file.read()
    decrypted_file = bytes([byte ^ 0x34 for byte in encrypted_file])
    
    out_file.write(decrypted_file)
   print(f"Decrypted File Can be Found at: {output_file}"
 decrypt("secret.txxt", "no_secret.txt")
