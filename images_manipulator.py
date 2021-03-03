#!/usr/bin/env python3

import os, glob
from PIL import Image
import re

newsize = 128, 128

for file in glob.glob("images/ic_*"):
       im = Image.open(file).convert('RGB')
       filename = re.search(r"(ic_[a-zA-Z\_]+48dp)", file)
       im.rotate(270).resize((newsize)).save("/opt/icons/"+filename.group(0),"JPEG")
       im.close()