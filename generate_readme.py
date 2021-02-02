"""
Create module spec for readme.md
"""

from dansfunctions import fg


print('## dansfunctions/functions_general.py')
print('Version: %s (%s)' % (fg.__version__, fg.__date__))
print('\n#### Methods:')
print(fg.list_methods(fg, False, True))
