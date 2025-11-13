# Identifying the duration of emotional stimulus presentation for conscious versus subconscious perception via hierarchical drift diffusion models 

[![OSF DOI](https://img.shields.io/badge/DOI-10.17605/OSF.IO/mscz5-blue)](https://doi.org/10.17605/OSF.IO/mscz5)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Open Access](https://img.shields.io/badge/Status-Open%20Access-brightgreen.svg)](DOI_LINK_HERE)


https://doi.org/10.1016/j.concog.2023.103493


---


#### AUTHORS
Julia Schräder 1,2, Ute Habel 1,2, Han-Gue Jo 3, Franziska Walter 1, Lisa Wagels 1,2

* <sub><sup>1 Department of Psychiatry, Psychotherapy and Psychosomatics, Medical Faculty, Uniklinik RWTH Aa-chen University, Pauwelstraße 30, 52074 Aachen, Germany</sup></sub>
* <sub><sup>2 Institute of Neuroscience and Medicine: JARA-Institute Brain Structure Function Relationship (INM 10), Research Center Jülich, Jülich, Germany</sup></sub>
* <sub><sup>3 School of Computer Information and Communication Engineering, Kunsan National University, Gun-san, Korea</sup></sub>


---
## ✨ Abstract 

To investigate subliminal priming effects, different durations for stimulus presentation are applied ranging from 8 to 30 ms. This study aims to select an optimal presentation span which leads to a subconscious processing. 
40 healthy participants rated emotional faces (sad, neutral or happy expression) presented for 8.3 ms, 16.7 ms and 25 ms. Alongside subjective and objective stimulus awareness, task performance was estimated via hierarchical drift diffusion models. Participants reported stimulus awareness in 65 % of the 25 ms trials, in 36 % of 16.7 ms trials, and in 2.5 % of 8.3 ms trials. Emotion-dependent responses were reflected in decreased performance (drift rates, accuracy) during sad trials. The detection rate (probability of making a correct response) during 8.3 ms was 12.2 % and slightly above chance level (33.333 % for three response options) during 16.7 ms trials (36.8 %). The experiments suggest a presentation time of 16.7 ms as optimal for subconscious priming. An emotion-specific response was detected during 16.7 ms while the performance indicates a subconscious processing. 

## Experimental design
The participants completed 360 trials in 3 block where one short timing condition counterbalanced with the long timing condition appeared per block.
This paradigm leads to a 4x3 factorial design (4 timing conditions and 3 stimulus emotions) with 7 main effects (happy, neutral, sad, 8.3ms, 16.7ms, 25ms, 141.7ms) and 12 further conditions. The paradigms were programmed with PsychoPy [[2]](#2) and can be found on this respiratory in the `tasks`folder.

For both tasks, we used a backward mask paradigm which provides conscious and unconscious masked stimulus presentation. 
A total of 36 images (12 happy, 12 neutral, 12 sad) served as emotional stimuli. Pictures were gender balanced and taken from the FACES database (Ebner, Riediger, & Lindenberger, 2010). Each image was presented 10 times against a grey background at the center of a LCD monitor (120Hz).
At the beginning of each trial, a fixation cross appeared for 300ms (36 frames) followed by the stimulus. The mask stimulus appeared for 41.6ms (5 frames) followed by a response phase of maximal 1.5s. A blank screen served as an inter-stimulus-interval (ISI) ranging be-tween 1 and 2s. Participants complete 3 blocks of 120 trials in randomized order. 
#### Task one
For the strongly masked stimuli, the presentation time varied between blocks. The stimuli images were presented for 25ms (3 frames) in the first block, for 16.7ms (2 frames) in the second block and for 8.3ms (1 frame) in the third block. In each block, the number of strong-ly (8.3ms, 16.7ms or 25ms) and weakly masked trails (141.7ms) were counterbalanced.
#### Task two
Strongly (8.3ms, 16.7ms or 25ms) and weakly masked stimuli (150ms) were presented in randomized order regardless of the block number. First, participants rated the stimulus emo-tion. Second, they were asked to rate how well the stimulus was visible (“seen”, “not seen”, “don’t know”).

![Pilot_1+2](https://user-images.githubusercontent.com/54576554/204008729-5d3d16d1-6b93-4a4b-96ca-2b17e66a0614.png)

## Folder description
* `data` includes mean performance accuracy, mean reaction time during emotion classification and mean rating of subjective awareness. Mean accuracy and mean reaction time was additionally uploaded for each task
* `glmm` includes script and dataset for glmm analysis
* `statistics` includes scripts and results of descriptive statistics and comparison of mean accuracy and mean reaction time of all 40 participants within main effects and all conditions.
* `hddm` includes script and dataset for hddm analysis as well as statistical results
* `tasks` includes the paradigm, stimuli and datasheets to run the backward mask task
* `supplements` includes supplement information, e.g. glmm for Bias and Drift-Rates with BDI and BVAQ Score effects

## Technologies
Project is created with:
* PsychoPy3: Version v2020.2.4
* RStudio: Version 1.4.1106
* Python 3
* GraphPad Prism 9.1.1 (225)
	
## Setup
* To run the paradigm, install [PsychoPy](https://www.psychopy.org/download.html) and download the `tasks` folder. 

* To run hddm and statistical analysis install it locally using Python:

```
$ pip install pandas
$ pip install pymc
$ pip install kabuki
$ pip install hddm

```
For detailled instruction for hddm see [here](http://ski.clps.brown.edu/hddm_docs/)

* To run the glmm analysis install [R](https://www.rstudio.com/products/rstudio/download/)

## References
<a id="1">[1]</a> 
Ebner, N. C., Riediger, M., & Lindenberger, U. (2010). FACES—A database of facial expressions in young, middle-aged, and older women and men: Development and validation. Behavior research methods, 42(1), 351-362

<a id="2">[2]</a> 
Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
	


