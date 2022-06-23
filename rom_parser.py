import struct

def parse_rom_data(rom_data : bytes):
	"""
	Parses marker coordinates (X/Y/Z, in mm) from NDI .rom file data

	Parameters
	----------
	rom_data : bytes
		The raw data of the ROM file to be parsed
	
	Returns
	-------
	list
		An n-by-3 matrix (i.e., a length-n list of length-3 lists) containing the X/Y/Z
		coordinates (in mm) of each of the body's n markers; or None if reading failed
	"""
	num_markers = int.from_bytes(rom_data[28:29], byteorder='little') # number of markers is stored in byte 28
	pos = 72 # marker coordinates are stored beginning at byte 72; each coordinate is a 32-bit (4-byte) float
	markers = list()
	for _ in range(num_markers):
		raw_xyz = tuple(round(f, 2) for f in struct.unpack('<3f', rom_data[pos:pos+12])) # read 3x 4-byte floats, rounding to 2 decimal places
		markers.append(tuple(f if f != 0.0 else 0.0 for f in raw_xyz)) # set "-0.0" to "+0.0"
		pos += 12
	return markers

# example usage
if __name__ == "__main__":
	with open("8700339.rom", 'rb') as rom_file:
		markers = parse_rom_data(rom_file.read())

	# print marker data
	print("Marker\t\tX (mm)\t\tY (mm)\t\tZ (mm)")
	for i in range(len(markers)):
		print(f"{chr(ord('A') + i)}\t\t{markers[i][0]}\t\t{markers[i][1]}\t\t{markers[i][2]}")
