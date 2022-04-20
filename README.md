# ROM Parser

The main code in this repository is a simple Python function in `rom_parser.py`, called `parse_rom_data`. This function, defined as follows, parses raw byte data from a Northern Digital, Inc. (NDI) `.rom` file and returns the X/Y/Z coordinates (in mm) of each marker.
```python
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
```

## Example Usage
The following code block:
```python
from rom_parser import parse_rom_data

with open("8700339.rom", 'rb') as rom_file:
	rom_data = rom_file.read()
	markers = parse_rom_data(rom_data)

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

## Other File Formats
The `parse_rom_data` function accepts raw ROM data, which most often will come directly from a `.rom` file. However, some file formats store ROM data encoded within them. In this case, first open and parse.decode the file, then pass its "raw" ROM data (casting to a `bytes` object as necessary) to the `parse_rom_data` function.

E.g., for a file that looks like this:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ROMData</key>
	<data>{...ROM data...}</data>
</dict>
</plist>
```
You might do something like this:
```python
import plistlib # for parsing PLIST files
from rom_parser import parse_rom_data

with open("myToolFile.tool" 'rb') as plist_file:
	rom_data = plistlib.load(plist_file)['ROMData'] # extract raw ROM data from PLIST
	markers = parse_rom_data(rom_data) # parse ROM data
```

## Contribution
Please fork, clone, or contribute however you like! All questions, comments, feedback, etc. are welcome!
