#!/bin/bash

path_prefix=`pwd`

for svgfile in *.svg;
do
    name="${svgfile%.*}"
    echo "Converting $name.svg to $name.eps"
    inkscape $path_prefix/$svgfile --export-eps $path_prefix/$name.eps
done

