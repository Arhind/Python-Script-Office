#A simple Python script to remove duplicate files...Coded by MCoury AKA  python-scripter
import hashlib
import os

  
#dirList=os.listdir(path)

#define a function to calculate md5checksum for a given file:
def md5(f):
    """takes one file f as an argument and generates an md5checksum for that file"""
    return hashlib.md5(open(f,'rb').read()).hexdigest()

#define our main function:
def rm_dup(path):
    """relies on the md5 function above to remove duplicate files"""
    if not os.path.isdir(path):#make sure the given directory exists
        print('specified directory does not exist!')
    else:
        md5_dict={}
        for root, dirs, files in os.walk(path):#the os.walk function allows checking subdirectories too...
            for f in files:
                if not md5(os.path.join(root,f)) in md5_dict:
                    md5_dict.update({md5(os.path.join(root,f)):[os.path.join(root,f)]})
                else:
                    md5_dict[md5(os.path.join(root,f))].append(os.path.join(root,f))
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
        print('Done!')

if (__name__=='__main__'):
    print('=======A simple Python script to remove duplicate files===========')
    print()
    print('============Coded by MCoury AKA python-scripter===================')
    print()
    print('===========The script counts on the fact the fact=================')
    print('=========that if 2 files have the same md5checksum================')
    print('==========they most likely have the same content==================')
    print()
    #path=input(r'Please provide the target path\directory... for example: c: or c:\directory...')
    path="/home/arhind/flash"
    print()
    rm_dup(path)
