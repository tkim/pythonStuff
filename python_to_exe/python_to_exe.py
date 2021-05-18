from distutils.core import setup
import py2exe

# use the name of the file you want to conver to .exe and go to the directory where the .py file exists.
setup(console=['password_generator.py'])

# to create the executable run the following 
# py -3 python_to_exe.py py2exe
