import moviepy, pkgutil, importlib
print('moviepy file:', getattr(moviepy, '__file__', None))
print('submodules:', [m.name for m in pkgutil.iter_modules(moviepy.__path__)])
try:
    importlib.import_module('moviepy.editor')
    print('moviepy.editor import: OK')
except Exception as e:
    print('moviepy.editor import: ERROR', e)
