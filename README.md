# scatter-anim-3D

Animation of the motion of **N** gravitons in space.

## Requirements

* **Python 2.7**
* **Matplotlib** (version 2.2.5 onwards)

## Installation

After installing the required packages, execute the following commands:
```
$ git clone http://github.com/aborquez/scatter-anim-3D
$ cd scatter-anim-3D
```

## Usage

In the same folder, an additional text file is required. It must be called `out.txt` and it has to be filled with the following format, specifying time and position coordinates:
```
time1:x1:y1:z1:x2:y2:z2:...:xN:yN:zN
time2:x1:y1:z1:x2:y2:z2:...:xN:yN:zN
time3:x1:y1:z1:x2:y2:z2:...:xN:yN:zN
```

To reproduce the animation, you must execute the `scatter-anim.py` program, strictly like this:
```
$ python ./scatter-anim-3D.py
```

## Documentation

For more information on the **Matplotlib** package, check its [webpage](https://matplotlib.org/index.html).
