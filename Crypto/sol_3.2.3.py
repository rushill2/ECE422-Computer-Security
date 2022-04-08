import urllib.request, urllib.error
url = "http://192.17.103.142:8080/mp3/rushill2/?"
GRANULARITY = 16

#-----------------------------------------------------------
# Functions: 1. get_status - returns error or success code
#            2. xorhandler - gets the plaintext using the XOR hack
#            3. answerparser - returns string from plaintext
class cryptocp2:
    def get_status(u):
        try:
            resp = urllib.request.urlopen(u)
            print(resp.code)
            return resp.code
        except urllib.error.HTTPError as e:
            return e.code

    def xorhandler(guessvectors, ans, testvectors):
            checkpadding = GRANULARITY-1
            ptext = guessvectors[i]
            ptext ^= int(prevblock[i],16)
            ptext ^= 16
            testvectors[i] = guessvectors[i] ^ 16
            guessvectors[i] = testvectors[i]
            for k in range(i, 16):
                guessvectors[k] = testvectors[k] ^ checkpadding
                checkpadding -= 1
            ans.insert(0,ptext)

    def answerparser(decrypted, temp):
        out = ""
        for x in decrypted:
            for j in range(16):
                if x[j] >= GRANULARITY*2:
                    if x[j] < GRANULARITY*8:
                        out += chr(x[j])
        print(out)
        return out

# begin code to acquire plaintext


with open("3.2.3_ciphertext.hex") as f:
    stringin = f.read()

#-----------------------------------------------------------
# Variables
cbytes = bytes.fromhex(stringin)
cipher = stringin.strip()
ctext = []
count = 0
correct = []
decrypted = []

#-----------------------------------------------------------
# Block setup
block_dict = {}
block_dict[0] = cipher[0:32]
for i in range(int(len(cipher)/32)):
    block_dict[i] = cipher[i*32:(i+1)*32]


#-----------------------------------------------------------
# Retrieving the string
for i in range(1, len(block_dict)):
    ans = []
    currblock = [block_dict[i][k:k + 2] for k in range(0, len(block_dict[i]), 2)]
    prevblock = [block_dict[i-1][k:k + 2] for k in range(0, len(block_dict[i]), 2)]
    guessvectors = [0]*16
    testvectors = [0]*16
    for i in range(15, -1, -1):
        for test in range(256):
            guessvectors[i] = test
            response = cryptocp2.get_status(url + ''.join(["{:02x}".format(elem) for elem in guessvectors])+''.join([elem for elem in currblock]))
            if(response == 404):
                correct.append(test)
                break
        cryptocp2.xorhandler(guessvectors, ans, testvectors)
    decrypted.append(ans)

#-----------------------------------------------------------
# Final Things
output = ""
output = cryptocp2.answerparser(decrypted, output)
with open("sol_3.2.3.txt", "w") as f:
    f.write(output)
    
