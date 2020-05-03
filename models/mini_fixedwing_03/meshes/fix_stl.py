#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent/'tools'))
from stl_tools import openscad_stl_export, subdivide, decimate


parts = ['fuselage', 'aileron_left', 'aileron_right',
        'elevator', 'propeller', 'wheel_left', 'wheel_right']
in_dir = Path('stl_orig')
out_dir = Path('stl')

for part in parts:
    openscad_stl_export(
        scad_file='model.scad',
        part=part,
        out_dir=out_dir)

for part in ['fuselage']:
    for i in range(2):
        decimate(
            file_in=out_dir/(part + '.stl'), 
            file_out=out_dir/(part + '.stl'),
            ratio=0.12)
        subdivide(
            file_in=out_dir/(part + '.stl'), 
            file_out=out_dir/(part + '.stl'),
            n=1)


for part in ['wheel_left', 'wheel_right', 'propeller']:
    decimate(
        file_in=out_dir/(part + '.stl'), 
        file_out=out_dir/(part + '.stl'),
        ratio=0.02)


for part in ['aileron_left', 'aileron_right', 'elevator']:
    subdivide(
        file_in=out_dir/(part + '.stl'), 
        file_out=out_dir/(part + '.stl'),
        n=1)
    decimate(
        file_in=out_dir/(part + '.stl'), 
        file_out=out_dir/(part + '.stl'),
        ratio=0.5)


