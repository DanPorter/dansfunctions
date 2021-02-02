# dansfunctions
Various useful functions in python

#### Usage:
```python
import dansfunctions
dansfunctions.fg  # module of general mathematical, vector and string format functions
dansfunctions.fp  # module of matplotlib shortcuts
dansfunctions.widgets  # module of tkinter shortcuts
```

##### Requirements: *numpy*
##### Optional requirements: *matplotlib*, *tkinter*


## dansfunctions/functions_general.py
Version: 2.0.0 (02/Feb/2021)

#### Methods:
`ang(a, b, deg=False)`	*Returns the angle, in Radians between vectors a and b*

`array_str(A)`	*Returns a short string with array information*

`cart2sph(xyz, deg=False)`	*Convert coordinates in cartesian to coordinates in spherical*

`cell(lengths=[1, 1, 1], rotation=[0, 0, 0])`	*Returns a unit CELL with vectors defined by length and rotation (Deg)*

`complex2str(val, fmt='6.1f')`	*Convert complex number to string*

`detail(A)`	*Prints details about the given vector,*

`distance2line(line_start, line_end, point)`	*Calculate distance from a line between the start and end to an arbitary point in space*

`find_index(A, value)`	*Return the index of the closest number in array A to value*

`find_vector(A, V, difference=0.01)`	*Return the index(s) of vectors in array A within difference of vector V*

`findranges(scannos, sep=':')`	*Convert a list of numbers to a simple string*

`frange(start, stop=None, step=1)`	*Returns a list of floats from start to stop in step increments*

`gauss(x, y=None, height=1, cen=0, fwhm=0.5, bkg=0)`	*Define Gaussian distribution in 1 or 2 dimensions*

`get_methods(object, include_special=True)`	*Returns a list of methods (functions) within object*

`grid_intensity(points, values, resolution=0.01, peak_width=0.1, background=0)`	*Generates array of intensities along a spaced grid, equivalent to a powder pattern.*

`group(A, tolerance=0.0001)`	*Group similear values in an array, returning the group and indexes*

`index_coordinates(A, CELL)`	*Index A(x1,y1,1) on new coordinate system B(x2,y2,z2), defined by unit vectors CELL = [A,B,C]*

`inline_help(func, markdown=False)`	*Return function spec and first line of help in line*

`isincell(A, cell_centre=[0, 0, 0], CELL=array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]]))`	*Return boolean of whether vector xyx is inside a cell defined by position, size and rotation*

`lastlines(filename, lines=1, max_line_length=255)`	*Returns the last n lines of a text file*

`list_methods(object, include_special=False, markdown=False)`	*Return list of methods (functions) in class object*

`mag(A)`	*Returns the magnitude of vector A*

`map2grid(grid, points, values, widths=None, background=0)`	*Generates array of intensities along a spaced grid, equivalent to a powder pattern.*

`multi_replace(string, old=[], new=[])`	*Replace multiple strings at once*

`nice_print(precision=4, linewidth=300)`	*Sets default printing of arrays to a nicer format*

`norm(A)`	*Returns normalised vector A*

`numbers2string(scannos, sep=':')`	*Convert a list of numbers to a simple string*

`plane_intersection(line_point, line_direction, plane_point, plane_normal)`	*Calculate the point at which a line intersects a plane*

`print_arrays(arrays=[])`	*Prints values from several arrays with nice formatting*

`quad(A)`	*Returns +/-1 depending on quadrant of 3D vector A*

`quadmag(A)`	*Returns +/- mag depending on quadrant of a 3D vector A*

`readstfm(string)`	*Read numbers written in standard form: 0.01(2), return value and error*

`replace_bracket_multiple(name)`	*Replace any numbers in brackets with numbers multipled by bracket multiplyer*

`rot3D(A, alpha=0.0, beta=0.0, gamma=0.0)`	*Rotate 3D vector A by euler angles*

`rotate_about_axis(point, axis, angle)`	*Rotate vector A about vector Axis by angle*

`rotmat(a, b)`	*Determine rotation matrix from a to b*

`saveable(string)`	*Returns a string without special charaters.*

`search_dict_lists(d, **kwargs)`	*Search equal length lists in a dictionary for specific values*

`shortstr(string)`	*Shorten string by removing long floats*

`sphere_array(A, max_angle1=90, max_angle2=90, step1=1, step2=1)`	*Rotate points in array A by multiple angles*

`squaredata(xdata, ydata, data, repeat=None)`	*Generate square arrays from 1D data, automatically determinging the repeat value*

`stfm(val, err)`	*Create standard form string from value and uncertainty"*

`unique_vector(vecarray, tol=0.05)`	*Find unique vectors in an array within a certain tolerance*

`vector_intersection(point1, direction1, point2, direction2)`	*Calculate the point in 2D where two lines cross.*

`vector_intersection3d(point1, direction1, point2, direction2)`	*Calculate the point in 3D where two lines cross.*

`whererun()`	*Returns the location where python was run*

`you_normal_vector(eta=0, chi=90, mu=0)`	*Determine the normal vector using the You diffractometer angles*

