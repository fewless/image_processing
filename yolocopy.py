import glob
import os
import sys

path = os.getcwd()

_, infile, outfile, inline = sys.argv # target_file, output_file, target_number

for nowtxt in glob.glob(infile + "/*.txt"):
	textline = []
	with open(nowtxt) as f:
		l_strip = [s.strip() for s in f.readlines()]
		for k in l_strip:
			if str(k[0]) == str(inline):
				textline.append(k)
	basename = os.path.basename(nowtxt) #get name
	with open(outfile +'/'+ basename, mode='a') as f:
		for k in textline:
			f.write('\n' + str(k))
	
	trueline = []
	with open(outfile +'/'+ basename) as f:
		l_strip = [s.strip() for s in f.readlines()]
		for k in l_strip:
			if len(str(k))>0:
				trueline.append(k)
	#os.remove(outfile +'/'+ basename)
	with open(outfile +'/'+ basename, mode='w') as f:
		f.write('\n'.join(trueline))

