
# Linux Lab CSCI-213 Assignment

### What's a Caesar Cipher? 
The Caesar cipher is a simple method of encrypting messages by shifting each letter of the alphabet a certain number of positions down or up. It's named after Julius Caesar, who is said to have used this technique to protect his military communications.

### How it works?
Let's say we want to encrypt the word "HELLO" using a Caesar cipher with a shift of 3. We start by assigning numbers to each letter of the alphabet, starting from 0. So, A is 0, B is 1, C is 2, and so on.

To encrypt the word "HELLO," we shift each letter three positions to the right. H becomes K, E becomes H, L becomes O, and O becomes R. Therefore, the encrypted word is "KHOOR."

To decrypt the message, we do the reverse process. We shift each letter three positions to the left. K becomes H, H becomes E, O becomes L, and R becomes O. Thus, we have successfully decrypted the message back to "HELLO."


### To run the file:

```
python3 LinuxLab2023.py <shift_amt_integer>
<Hit Enter>
<Put the message you want to encode here>
<Hit Enter>
Ctrl + D (For macs) [Use Appropriate syntax to close stdin buffer 
					for your OS]
```
