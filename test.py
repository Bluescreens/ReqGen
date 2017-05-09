import os
'''
for root, dirs, files in os.walk('../../Desktop'):
    print(root)
    print(dirs)
    print(files)
'''
tokenized = "../../Desktop/"
for filename in os.listdir(tokenized):
    print("=" * 50)
    print(filename)
    if os.path.isdir(tokenized + "/" + filename):
        print("This is a Directory")
    else:
        print("This is a file")
