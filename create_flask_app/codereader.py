from configparser import ConfigParser
import os


# getting full path to the ini file
dir = os.path.dirname(__file__)
filename = os.path.join(dir, './code.ini')

# instancing ConfigParser
reader = ConfigParser()
# reading the code.ini file
reader.read(filename, encoding="ascii")


print(reader.get('saki', 'key'))
