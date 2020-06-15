import sys
import os
from PIL import Image
#grab 1st and 2nd file
in_file = sys.argv[1]
out_file = sys.argv[2]
#find if newfile exist
if not os.path.exists(out_file):
	os.makedirs(out_file)
for filename in os.listdir(in_file):
	img = Image.open(f'{in_file}{filename}')
	clean_name = os.path.splitext(filename)[0]#it splits the name,[0] take the 1st 
	img.save(f'{out_file}{clean_name}.png', 'png')
	print('all done babe')

