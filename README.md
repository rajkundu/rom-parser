# ROM Parser

The main code in this repository is a simple Python function in `rom_parser.py`, called `parse_rom`. This function, defined as follows, parses the passed Northern Digital, Inc. (NDI) `.rom` file and returns the X/Y/Z coordinates (in mm) of each marker.
```python
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
```

## Example Usage
The following code block:
```python
filename = "8700339.rom"
markers = parse_rom(filename)

# print marker data
print("Marker\t\tX (mm)\t\tY (mm)\t\tZ (mm)")
for i in range(len(markers)):
	print(f"{chr(ord('A') + i)}\t\t{markers[i][0]}\t\t{markers[i][1]}\t\t{markers[i][2]}")
```
prints the following output:
```
Marker		X (mm)		Y (mm)		Z (mm)
A		0.0		0.0		0.0
B		0.0		28.59		41.02
C		0.0		0.0		88.0
D		0.0		-44.32		40.45
```

## Contribution
Please fork, clone, or contribute however you like! All questions, comments, feedback, etc. are welcome!
