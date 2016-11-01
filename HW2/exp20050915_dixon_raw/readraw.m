function [d] = readraw(filename, type, ds, endian)
%
%  Read in "raw data".
%
%    filename - The filename of the data to read in.
%    type     - Data type (e.g., 'int16', 'float', 'int16=>int16')
%    ds       - Data size (e.g., [256 256 60])
%    endian   - Endian of the file (e.g., 'l' or 'b', def: native format)
%
%  For example, to read in an Analyze file bob.img of size 
%  256 by 256 with 37 slices:
%     >> d = readraw('bob.img', 'int16=>int16', [256 256 60], 'l');

%  Craig Jones (craig@mri.jhu.edu)  April 28, 2004

if( nargin == 3 )
	endian = 'n';
end

fp=fopen(filename, 'rb', endian);
 fseek(fp,159744,-1)
d = fread(fp, prod(ds), type);
fclose(fp);

d = reshape(d, ds);