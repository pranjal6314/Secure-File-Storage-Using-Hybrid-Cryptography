# Secure-File-Storage-Using-Hybrid-Cryptography

## Objective: To Achieve a secure plateform for storing of files using Hybrid Cryptography.

# Methodology

=>To achieve the above goal, the following methodology needs to be followed:
1. Load the file on the server.
2. Dividing the uploaded file into N part of size 32Kb and max size of file that you can upload is of 1MB.
3. We use 5 cryptography algo Fernet ,ChaCha20Poly1305,AESGCM,AESCCM,MultiFernet  for generating key 
4. we generate 6 key and 2 nonce and 5 keys and 2 nonce are used for Encrypting and decrypting the file and the one key used for Encrypting and decrypting the all other keys .
5. Key which used for Encrypting other keys is given to user as public key .
6. Encrypting all the parts of the file using any one of the selected algorithms (Algorithm is changed with every part in round robin fashion) 
7. The keys for cryptography algorithms is then secured using a different algorithm and the key for this algorithm is provided to the user as public key.

After the above 7 steps you will have a N files which are in encrypted form which are stored on the server and a key which is downloaded as public key for decrypting the file and downloading it.</br>

=>To restore the file, follow the following steps:
1. Load the key on the server.
2. Decrypt the keys of the algorithms.
3. Decrypt all the N parts of the file using the same algorithms which were used to encrypt them.
4. Combine all the N parts to form the original file and provide it to the user for downloading.

# How to Run

**NOTE:** The project is based on Python 2.7.15 plateform running it on any other plateform might create some issues.

Step 1: Install Requirements
`pip install -r requirements.txt`

Step 2: Run the application
`python app.py`

Step 3: Visit the localhost:8000 from your browser

Step 4: Enjoy :)
 
[//]: <> (*IF YOU ENCOUNTER ANY BUGS OR FOR ANY SUGGESTIONS REGARDING THE IMPROVEMENT OF THE PROJECT FEEL FREE TO CONTACT ME :**)

**THE PROJECT HAS ENCOUNTERED A BUG BECAUSE OF THE CRYPTOGRAPHY LIBRARY version. IF YOU ARE INTRESTED IN COLLABORATING TO IMPROVE THIS PROJECT FEEL FREE TO CONTACT ME : pranjalchoudhary270@gmail.com 
if use python 2.7.15 it will work**

![image](https://user-images.githubusercontent.com/77271332/201308958-49792863-c8cc-44a4-94b0-58ce57e7ed63.png)
![image](https://user-images.githubusercontent.com/77271332/201309100-ade24fb5-3a4c-42d4-b1de-ba717e9d22d4.png)
