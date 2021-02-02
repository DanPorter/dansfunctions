"""
dansfunctions - various useful functions in python
usage:
>>import dansfunctions
>>dansfunctions.fg  # module of general mathematical, vector and string format functions
>>dansfunctions.fp  # module of matplotlib shortcuts
>>dansfunctions.widgets  # module of tkinter shortcuts

Requirements: numpy
Optional requirements: matplotlib, tkinter
"""

from . import functions_general as fg

try:
    import matplotlib
    matplotlib.use('TkAgg')
    from . import functions_plotting as fp
except ImportError:
    fp = None
    print('Matplotlib may not be available')

try:
    from .tkgui import basic_widgets as widgets
except ImportError:
    widgets = None
    print('tkinter may not be available')


def version_info():
    return 'dansfunctions version %s (%s)' % (fg.__version__, fg.__date__)


def module_info():
    import sys
    out = 'Python version %s' % sys.version
    out += '\n%s' % version_info()
    # Modules
    out += '\n     numpy version: %s' % fg.np.__version__
    try:
        import matplotlib
        out += '\nmatplotlib version: %s' % matplotlib.__version__
    except ImportError:
        out += '\nmatplotlib version: None'
    try:
        import tkinter
        out += '\n   tkinter version: %s' % tkinter.TkVersion
    except ImportError:
        out += '\n   tkinter version: None'
    return out


def check_general_functions():
    print('dansfunctions/functions_general.py')
    print('Version: %s (%s)' % (fg.__version__, fg.__date__))
    print('Methods:')
    print(fg.list_methods(fg, False))


def check_plotting_functions():
    print('dansfunctions/functions_plotting.py')
    if fp is None:
        print('Matplotlib may not be available')
        return
    print('Version: %s (%s)' % (fp.__version__, fp.__date__))
    print('Methods:')
    print(fg.list_methods(fp, False))


def check_tkinter_functions():
    print('dansfunctions/tkgui/basic_widgets.py')
    if widgets is None:
        print('tkinter may not be available')
        return
    print('Version: %s (%s)' % (widgets.__version__, widgets.__date__))
    print('Methods:')
    print(fg.list_methods(widgets, False))
