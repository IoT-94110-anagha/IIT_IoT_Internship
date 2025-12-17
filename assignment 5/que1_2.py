import os
cwd=os.getcwd() 
print(f"current working directory is :{cwd}")
def current_dir():
  print(cwd=os.getcwd)
  print()

  #current_dir("current directory before:")
  #os.chdir('../')
  #current_dir("current directory after:")
path="/"
list_dir=os.listdir(path)
print("list of directory files:'",path,"'")
print(list_dir)