# Matching Template Using OpenCV

We Use OpenCV's default **template matching** function to detect if there's a similar template in the picture we give.

## Single Template Matching
------------------------------
The results we get are pretty impressive.

![before](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/images/rick_morty.jpg)
 
![template](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/images/rm_template.jpg)
 
![after](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/results/Rick_Morty_main.PNG)


## Multiple Template Matching
------------------------------
For multiple template matching, we use the non maxima suprresion to avoid multiple bounding boxes around the same object. We can use a threshold of 0.8-0.95 for matching the exact given template. If the template's a little different, try playing around with the threshold values.

![image](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/images/2_diamonds.png)
 
![template](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/images/diamond.jpg)

![before NMS](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/results/before%20NMS.PNG)
 
![After NMS](https://github.com/vinzard11/Matching-Template-OpenCV/blob/main/results/After%20NMS.PNG)

To use your own image and template, download the .py file and execute it in the command prompt with the arguments _--image(path to the image)_ and _--template(path to the template)_.

Additionally, You could change the threshold by passing _--threshold(a value between 0 and 1)_ and you could scale your image using _-scale_per(a value between 0 and 100)_
