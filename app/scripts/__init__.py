import os
# __all__ = ['reader', 'writer']
# List comprehension to get all Python files in the directory
__all__ = [os.path.splitext(f)[0] for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.py') and f != '__init__.py']
