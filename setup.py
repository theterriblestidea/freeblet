from cx_Freeze import setup, Executable 

# python setup.py build
setup(name = "HelloWorld" , 
      version = "0.1" , 
      description = "" ,
      executables = [Executable("gui.py")])