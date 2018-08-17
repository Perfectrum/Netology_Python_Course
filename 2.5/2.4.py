import os
import sys
import subprocess as sp

if not os.path.exists('Result'):
    os.makedirs('Result')

for img in os.listdir(path="Source"):
        sp.call('convert Source/{} -resize 200 Result/{}'.format(img, img))
