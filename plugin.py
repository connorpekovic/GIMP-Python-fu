#!/usr/bin/env python

from gimpfu import *

def plugin_func(image, drawable):

    
    #resize image to 750x750
    pdb.gimp_image_scale(image, 750, 750)
    
    #desaturate
    pdb.gimp_drawable_desaturate(drawable, 2)

    #cartoonize
    #pdb.plug_in_cartoon(0, image, drawable, 10.000, 0.200)

    #export to .jpg
    #pdb.file_jpeg_save(1, image, drawable, , , , , , , , , ,)

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
