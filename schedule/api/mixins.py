
"""
Remove 'patch' from http_method_names list
"""
class NotPatchMixin:
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']
