# imports
import pbp
from Crypto.PublicKey import RSA
import math as m
import string
import numpy as np

# global variables
EXP = 65537
GRANULARITY = 16

#------------------------------------------------------------
# Solution class for remainder and product tree calculations
class cryptop4:

    def remaindertree(treenode):
        print("Finding RTrees..")
        output = treenode[-1]
        temp_tree = treenode[::-1]
        for t in temp_tree:
            output = [output[m.floor(i/2)] % t[i] ** 2 for i in range(len(t))]
        return output

    def prodtree(nodes):
        print("Finding PTrees..")
        output = [nodes]
        while len(nodes) > 1:
            nodes = [np.prod(nodes[i*2:(i+1)*2]) for i in range(int((len(nodes)+1)/2))]
            output.append(nodes)
        return output

    def populateKeys(prodkeys, gcd):
        for i in range(len(mods)):
            if gcds[i] == 1:continue
            RSA_init = RSA.construct((mods[i], EXP, int(cryptop4.invmod(EXP, ((mods[i]//gcds[i])-1)*(gcds[i]-1)))))
            prodkeys.append(RSA_init)
        print("Populated keys")
        return prodkeys

    def populategcds(mods, RTrees, gcds):
        for i in range(len(mods)):
            p = RTrees[i]//mods[i]
            currgcd = m.gcd(mods[i], p)
            gcds.append(currgcd)
        print("Populated GCD list")
        return gcds

    # invmod function from stackoverflow user Don Hatch. 
    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    def invmod(a,b): return 0 if a==0 else 1 if b%a==0 else b - cryptop4.invmod(b%a,a)*b//a

#------------------------------------------------------------
# Implementing the algorithm to break the RSA
# Average runtime - 6 minutes


# for checking how long exec takes. Credit -
# https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
import timeit
start = timeit.default_timer()

f = open("3.2.4_ciphertext.enc.asc","r")
ciphertext = f.read()
f.close()

# I read that looping through each line was quicker, but not much of a time diff here compared to readlines()
f = open("./moduli.hex","r")
mods = f.readlines()[:-1] 
f.close()

print("Briefly Setting Up...")
mods = [int(elem, 16) for elem in mods]

# populating the GCD and p-keys lists
PTree = cryptop4.prodtree(mods)
RTrees = cryptop4.remaindertree(PTree)
gcds = []
gcds = cryptop4.populategcds(mods, RTrees, gcds)
prodkeys = []
prodkeys = cryptop4.populateKeys(prodkeys, gcds)

print("Beginning decryption")

# write results to output file
temp = ""
for elem in prodkeys:
    try:
        temp += pbp.decrypt(elem, ciphertext).decode("UTF-8")
        print(pbp.decrypt(elem, ciphertext).decode("UTF-8"))
        print(temp)
        break
    except:
        pass

f = open("sol_3.2.4.txt", "w")
f.write(temp)
f.close()
print("Done!")
stop = timeit.default_timer()
print('Run Time: ', stop - start)