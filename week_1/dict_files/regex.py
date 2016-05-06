import re
str = 'My name is Ozymandias, King of Kings:'
def onionify():
    print re.sub(r'King', 'Onion', str)
onionify()
