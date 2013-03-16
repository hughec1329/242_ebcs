STA 242 Project - computer vision w python - automatic body conditions scorign of dairy cattle.
=====

Discussion with duncan 20130222
----
- use established tools, dont try and reinvent wheel
- try to trow at wall w established techniques and see what sticks/works - harris edge detection?
- acquireing images and extracting variables will be most difficult. 
- big project but good to get into it.

### classification  methods
- he favour simple - decicion trees, PCA, LDA, clustering, KNN.

### variable creation - acwuire image then convert to list of variables for modelling.
- SO qustions - cant really just do pixels as in 135 digits project, need to establish landmarks and angles/distance between them.
-- good training at penn state slides for feature extraction.http://www.docstoc.com/docs/119431374/Learn-to-Score-Body-Condition-Step-by-Step
- need to get points, then establish angles between them
- volume? 
- fat fill?
- length rib detectable?
- nedd to prescale images?

### PLAN
- try see what harris gets out of raw cow pic,
- if no good try with outline and get edges


### WUESTIONS
- how get angles inside pins?

ALternative if cant get cow pics
----

- could create face index using similar criteria
- possible done before - predict fatness/BMI from image?

Variable creation
===
potentially useful usefule python mods 
---
### from Open CV - http://docs.opencv.org/2.4.4-beta/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html
- cv.FindContours / cv.DrawContours
- ectract moments - represetnation of shape class
http://www.sci.utah.edu/~gerig/CS7960-S2010/handouts/CS7960-AdvImProc-MomentInvariants.pdf
- cv.Moments, cv.HuMoments
- feature description - http://docs.opencv.org/doc/tutorials/features2d/feature_detection/feature_detection.html#feature-detection
- description extractor - http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_descriptor_extractors.html?highlight=surfdescriptorextractor#surfdescriptorextractor


- wavelets - extract edges and verticies to model on .
-- is this haar decompisition?
- cvHaarDetectObjects is implementation of violoia jones algorithm

### SIFT
* feature extraction w geometrical - size angle information form set of training images.
* http://jayrambhia.wordpress.com/2013/01/18/sift-keypoint-matching-using-python-opencv/

### SURF
* training w KNN to id.
* http://stackoverflow.com/questions/10984313/opencv-2-4-1-computing-surf-descriptors-in-python

Image collection
===

Could use high contrast background to get better image

trigger w laser a' la 
http://www.instructables.com/id/Laser-Triggered-High-Speed-Photography/step3/The-Circuit/
http://www.pixiq.com/article/camera-laser-trigger

3D?
===
- multiple views/angles - stereo/3d imaging??

- take mulitple views - angle on leg, side hip etc.

- kinect - 

http://blogs.msdn.com/b/kinectforwindows/archive/2012/11/05/kinect-fusion-coming-to-kinect-for-windows.aspx

http://www.cs.washington.edu/rgbd-dataset/index.html

Cowrecognition
===
- use patterns of cow hide to actually id cows - more reliable than RFID?


websites
===
http://www.shervinemami.info/faceRecognition.html
http://computer-vision-talks.com/2012/12/mastering-opencv-with-practical-computer-vision-projects/
http://www.pages.drexel.edu/~nk752/tutorials.html
http://www.simplecv.org/learn/examples/parking.html
http://www.aishack.in/
http://jayrambhia.wordpress.com/2013/01/18/sift-keypoint-matching-using-python-opencv/
