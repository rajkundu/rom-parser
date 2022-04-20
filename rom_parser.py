import struct

def parse_rom(filename : str):
	"""
	Parses marker coordinates (X/Y/Z, in mm) from NDI .rom files

	Parameters
	----------
	filename : str
		The ROM file to parse; must end in '.rom' extension

	Returns
	-------
	list
		An n-by-3 matrix (i.e., a length-n list of length-3 lists) containing the X/Y/Z
		coordinates (in mm) of each of the body's n markers; or None if reading failed
	"""
	with open(filename, 'rb') as f:
		if filename.endswith(".rom"):
			bytedata = f.read()
		else:
			raise ValueError(f"Unable to parse file '{filename}'; only .rom files are supported")
		num_markers = int.from_bytes(bytedata[28:29], byteorder='little') # number of markers is stored in byte 28
		bytedata = bytedata[72:72+num_markers*3*4] # marker data is stored beginning at byte 72; each marker has 3 floating-point coordinates (X/Y/Z), each 4 bytes in size
		pos = 0
		markers = list()
		for n in range(num_markers):
			markers.append(list())
			for _ in range(3): # for each coordinate (X/Y/Z)
				coord = round(struct.unpack('<f', bytedata[pos:pos+4])[0], 2) # read 32-bit float, then round to 2 decimal places
				markers[n].append(coord if coord != 0.0 else 0.0) # set "-0.0" to +0
				pos += 4
		return markers

# example usage
if __name__ == "__main__":
	filename = "path/to/romfile.rom"
	markers = parse_rom(filename)

	print(f"Input File:\t{filename}")
	print(f"# Markers:\t{len(markers)}")
	print()

	# print marker data
	print("Marker\t\tX (mm)\t\tY (mm)\t\tZ (mm)")
	for i in range(len(markers)):
		print(f"{chr(ord('A') + i)}\t\t{markers[i][0]}\t\t{markers[i][1]}\t\t{markers[i][2]}")
