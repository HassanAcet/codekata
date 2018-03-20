def to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(to_camel('dont_do'))
