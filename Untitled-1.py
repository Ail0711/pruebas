import platform
import login as mix

def conect():
      mix.main()

sistema = platform.system()
a=input("powershell bash Python")

if sistema == "Windows":
    print("ES windows")
    if a=="1":
        print("Bash")
        conect()
        
elif sistema == "Linux":
            if a=='bash':
                print("Si jalo")
                
            elif a=='Pyhton':
                print("Si jalo")
            