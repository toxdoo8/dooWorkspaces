import re

def xyz_there(str):
    if 'xyz' in str:
        for i in range(1,len(str)-3):
            print(str[i:i+4],str[i-1:i+1],str[i:i+2])
            if (str[i-1:i+1] != '.x' or str[i:i+2] != ".x") and 'xyz' in str[i:i+4]:
                print(str[i:i+4])
                return True
        else:
            return False
print(xyz_there('1.xyz.xyz2.xxyz'))
print(xyz_there('1.xyz.xyz2.xyz'))
