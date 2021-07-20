# Timing for unconscious stimulus presentation

## Table of contents
* [General info](#general-info)
* [Experimental design](#experimental-design)
* [Folder descripion](#folder-description)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This study is about the perception of healthy individuals of emotional stimuli presented at an unconscious level.
On an 120Hz Screen, three drifferent timing options for unconscious presentation were elaborated (8.3ms, 16.6ms, 25ms) and compared to a conscious presentation time of 141ms. As stimuli, happy, neutral and sad faces taken from the FACE Database were used [[1]](#1).

## Experimental design
The participants completed 360 trials in 3 block where one short timing condition counterbalanced with the long timing condition appeared per block.
This paradigm leads to a 4x3 factorial design (4 timing conditions and 3 stimulus emotions) with 7 main effects (happy, neutral, sad, 8.3ms, 16.6ms, 25ms, 141,7ms) and 12 further conditions. The paradigm was programmed with PsychoPy [[2]](#2) and can be found on this respiratory `Backward_Mask_Paradigm.py` in the `paradigm`folder.


![BackwardMask_Pilot Kopie](https://user-images.githubusercontent.com/54576554/125072227-9c8da700-e0ba-11eb-9e70-c1a72198a427.jpg)

## Folder description

* `GLMM` includes script and dataset for glmm analysis
* `Statistics` includes scripts and results of descriptive statistics and comparison of mean accuracy and mean reaction time of all 20 participants within main effects and all conditions.
* `hddm` includes script and dataset for hddm analysis as well as statistical results
* `paradigm` includes the paradigm, stimuli and datasheets to run the backward mask task

## Technologies
Project is created with:
* PsychoPy3: Version v2020.2.4
* RStudio: Version 1.4.1106
* Python 3
	
	
## Setup
To run the paradigm, install [PsychoPy](https://www.psychopy.org/download.html) and download the `paradigm` folder. 

To run hddm and statistical analysis install it locally using Python:

```
$ pip install pandas
$ pip install pymc
$ pip install kabuki
$ pip install hddm

```
For detailled instruction for hddm see [here](http://ski.clps.brown.edu/hddm_docs/)

To run the glmm analysis install [R](https://www.rstudio.com/products/rstudio/download/)



## References
<a id="1">[1]</a> 
Ebner, N. C., Riediger, M., & Lindenberger, U. (2010). FACES—A database of facial expressions in young, middle-aged, and older women and men: Development and validation. Behavior research methods, 42(1), 351-362

<a id="2">[2]</a> 
Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
	


