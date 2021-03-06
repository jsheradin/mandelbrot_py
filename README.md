# mandelbrot_py

##About
This is a basic generator of the Mandelbrot Set made in Python 3.

##[mandelbrot_calc.py](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot_calc.py)
###About
Program features basic multithreading and calculates the mandelbrot set.

###Method
* Calculates via iteration to 255 pixel by pixel
* Save to file

###Output
[mandelbrot.txt](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot.txt)

##[mandelbrot_down.py](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot_down.py)
###About
Reads mandelbrot_big.txt and averages blocks of pixels to pixels. Useful for generating a massive mandelbrot.txt and scaling it back to useable size.

###Output
[mandelbrot 5000x5000.png](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot%2010000x10000.png) generated from a 30000x30000 mandelbrot.txt.

##[mandelbrot_draw.py](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot_draw.py)
###About
Reads from file and generates an image

###Method
* Read mandelbrot.txt
* Generate image pixel by pixel
* Save to file

###Output
[mandelbrot 10000x10000.png](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot%2010000x10000.png)

![screenshot](https://github.com/jsheradin/mandelbrot_py/blob/master/mandelbrot%201000x1000.png?raw=true)
