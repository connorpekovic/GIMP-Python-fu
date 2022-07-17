#!/usr/bin/env python

from gimpfu import *

def plugin_func(image, drawable):
    return
              
# do what plugins do best

register(
    "plugin_function",
    "blurb",
    "help message",
    "author",
    "copyright",
    "year",
    "<Image>/Functionality/PythonFunction",
    "*",
    [

    ],
    [],
    plugin_func)

main()