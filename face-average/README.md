# average-face-generation (MAJOR PROJECT)

### Quickstart guide
Clone the repo
```bash
git clone https://github.com/manuarora700/average-face-generation.git
```
Move to directory and execute run.py with appropriate parameters
```bash
cd ./average-face-generation
python ./run.py  -i "datasets/us-mp/president" -w -wt 200
```
This script will open a ```debug window``` showing the progress of the execution with 200ms frames, generate ```.ff``` files for every image and output average face as ```./results/us-mp-president.jpg```

### Requirements
- OpenCV 
- Dlib
- tqdm
- Python 3.6+ (preferably Anaconda distribution)

### Params
```
usage: run.py [-h] -i INPUT [-ow WIDTH] [-oh HEIGHT] [-e EXT [EXT ...]]
              [-o OUTPUT] [-w] [-nw] [-nc] [-wt WINDOWTIME]

  -h, --help            show this help message and exit
  -i INPUT, --input-dir INPUT
                        Specify the input directory
  -ow WIDTH, --output-width WIDTH
                        Specify the output file width. Default 300
  -oh HEIGHT, --output-height HEIGHT
                        Specify the output file height. Default 400
  -e EXT [EXT ...], --extensions EXT [EXT ...]
                        Specify the file extensions like *.jpg *.whatevs.file
  -o OUTPUT, --output-path OUTPUT
                        Specify the output path for writing result. Default
                        ./results/[input-dir-names].jpg
  -w, --window          Shows window if specified
  -nw, --no-warps       Hides warping stage if specified
  -nc, --no-caching     Ignores .ff file cache if specified
  -wt WINDOWTIME, --window-time WINDOWTIME
                        Duration of each frame in debug window
  -t TEMPLATE, --template TEMPLATE
                        Template input image to set as the main face shape
                        rather than the total average
```


### .ff file format
file format for storing facial features and landmarks 
- number of features 
- face detection rectangle coordinates (l,t,r,b) ~ (x1, y1) (x2, y2)
- 68 facial features as (x,y) 
```
[NUMBER OF FACES INT]
[LEFT INT] [TOP INT] [RIGHT INT] [BOTTOM INT]
[X INT] [Y INT]
.
.
.
[X INT] [Y INT]
[LEFT INT] [TOP INT] [RIGHT INT] [BOTTOM INT]
[X INT] [Y INT]
.
.
.
[X INT] [Y INT]
.
.
.
```



# Acknowledgement
- This project fixes couple of bugs, extends functionality and defines better cache file format.
- The github repo also hosts ```shape_predictor_68_face_landmarks.dat``` for ease of use which is part of larger open-source and publicly available project dlib (http://dlib.net/)


# Examples
![](https://github.com/georgegach/average-face-generation/blob/master/results/family.jpg)
