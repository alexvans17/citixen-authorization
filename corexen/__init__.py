import importlib

__version__ = '0.36.0'


def _import_class_from_string(class_path):
    if not class_path:
        return None
    module_path, class_name = class_path.rsplit('.', 1)
    return getattr(importlib.import_module(module_path), class_name)
