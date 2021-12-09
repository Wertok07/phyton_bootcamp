import os

curr_dir = os.getcwd()
print(curr_dir)
os.chdir("./tmp")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir("."))

print(os.listdir(os.path.join("./tmp", "test")))

files = os.listdir("./tmp")

for f in files:
    print(f"Plik: {f} jest katalog: {os.path.isfile(f)}")

# test_dir = "./tmp/test"
# if not os.path.exists(test_dir):
#     os.mkdir(test_dir)
# else:
#     os.rmdir(test_dir)
    #os.removedirs(test_dir)