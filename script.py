import zipfile 
print("\n********************")
print("Welcome to PyCracker")
print("********************\n")

filename = input('Enter the name of zip file: ')
wordlist = input('Enter the name of wordlist: ')
 
password = '' 
file = zipfile.ZipFile(filename) 
with open(wordlist, 'r') as f:
   print("\nTrying passwords: \n")
   for line in f.readlines(): 
         password = line.strip('\n') 
         try: 
               file.extractall(pwd=bytes(password, 'utf-8')) 
               print("\n[+] Password found: ",password)
               print("\n[+] File Extracted successfully...\n")
               break
         except: 
               pass
               print(password)