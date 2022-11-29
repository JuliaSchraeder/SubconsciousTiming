#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Tue Oct 27 14:47:00 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

Backward masked prime Paradigm - Pilot Study 
fixcross 300ms-> primer 43/140ms-> mask 43ms-> response 1.5
6 women 6 men, sad, happy and neutral -> 36 faces as prime and target
30 trials per condition --> 360 trials
12 conditions, 2x2x3, congruent/incongruend, strongly/weakly masked, happy/sad/neutral
Keyboard:
happy   = d 
neutral = s
sad     = a

experiment is designed for 120 Hz

120 Hz time must be a multiple of 1/120 = 8,3333 ms
(ms*0,12--> frames)
(frames/0,12) --> ms)
#used frames
1 frame     = 8,33 ms   Primer
2 frames    = 16,66 ms  Primer
3 frames    = 24,99 ms  Primer
5 frames    = 41.64 ms  Mask
17 frames   = 141,66 ms Primer
36 frames   = 300 ms    Fixcross
120 frames  = 1000 ms   Starttime before experiment starts, Jitter
180 frames  = 1.500 ms  Response time
240 frames  = 2.000 ms  Jitter
7200 frames = 60.000 ms Max break time between blocks

"""
from __future__ import absolute_import, division
#import pyglet                                                                  # Pyglet für den Windows-Rechner im Labor benötigt
#pyglet.options["shadow_window"]= False
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np                                                              # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os                                                                       # handy system and path functions
import sys                                                                      # to get file system encoding
from psychopy.hardware import keyboard
import random, xlrd                                                             # import random function and something to read in excel files
import numpy as np
from numpy.random import random, randint, normal, shuffle

# load in stimulus file, psychopy is searching in the directory in which the experiment is saved
infile_example = "DataSheet_example.xlsx" 
infile_study = "DataSheet_AllSti_360_rand.xlsx"

num_possible_example = 9                                                        # total number of example images in the study
num_example = 5                                                                 # number of example items used
num_items = 360                                                                 # total number of experiment images in the study
num_study = 120                                                                 # number of study items used in one block#later 120 pro block
block_ans = 3                                                                   # number of blocks, starting with block 1

# set timing
startTime = 360                                                                 # 3.000 ms/1s    welcome time and time before starting the first block
instruction = 600                                                               # 5 s            text that can be pressed away (intro, intro2)
cross = 36                                                                      # 300ms          fixcross
primeTime1 = 3                                                                  # 24,99 ms       primer strongly masked
primeTime2 = 17                                                                 # 141 ms         primer weakly maked
scrambledTime = 5                                                               # 41,6 ms        mask time
# different  prime timings for different blocks can be difined in block loop
responseTime = 180                                                              # 1.500 ms 
jittermintime = 120                                                             # 1.000 ms
jittermaxtime = 240                                                             # 2.000 ms
maxBreakTime = 7200                                                             # 60.000 ms/1min break between blocks
ende = 1200                                                                    # 10.000 ms       Endbildschirm wird angezeigt
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'EmoCon_Pilot_120Hz'                                            # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()                                                                 # user pressed cancel
expInfo['date'] = data.getDateStr()                                             # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='W:\Fmri_Forschung\Allerlei\JuliaH\Paradigma\EmoCon_Paradigma\EmoCon_Pilot_120Hz_final.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.ERROR)
logging.console.setLevel(logging.WARNING)                                       # this outputs to the screen, not a file

endExpNow = False                                                               # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001                                                          # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0                                                       # could not measure, so guess

defaultKeyboard = keyboard.Keyboard()                                           # create a default keyboard (e.g. to check for escape)
win.mouseVisible = False                                                        # hide mouse

#Set Example Stimuli
inbook_example = xlrd.open_workbook(infile_example)                             # open example datasheet
insheet_example = inbook_example.sheet_by_index(0)                              # go in inbook and find the first sheet

#arrays for our example stimuli
person_prime_example = []
gender_prime_example = []
prime_example = []
emotion_prime_example = []
corrAns_prime_example = []

#read stimuly from our example sheet
for rowx in range(1,num_possible_example+1):                                    # range from 0 to num_possible_example
    #read in the values of all columns on this row
    row_example = insheet_example.row_values(rowx)                              # taking all row values for rowx. row will be a list with everythin within the row (rowx starts with one and end with num_items) 
    #saving the image in the image array
    person_prime_example.append(row_example[0]) 
    gender_prime_example.append(row_example[1])
    prime_example.append(row_example[2])
    emotion_prime_example.append(row_example[3])
    corrAns_prime_example.append(row_example[4])

#array for our final example stimuli
person_item_prime_example = []
gender_item_prime_example = []
prime_item_example = []
emotion_item_prime_example = []
corrAns_item_prime_example = []

for i in range(num_example):                                                    # lists items you want to show
    person_item_prime_example.append(person_prime_example[i])
    gender_item_prime_example.append(gender_prime_example[i])
    prime_item_example.append(prime_example[i])
    emotion_item_prime_example.append(emotion_prime_example[i])
    corrAns_item_prime_example.append(corrAns_prime_example[i])

#Set Study Stimuli
#access the study stimulus file
inbook_study = xlrd.open_workbook(infile_study)                                 # open study datasheet   
insheet_study = inbook_study.sheet_by_index(0)                                  # go in inbook and find the first sheet

#arrays for our study stimuli
person_prime_study = []
gender_prime_study = []
prime_study = []
emotion_prime_study = []
corrAns_prime_study = []

#read stimuly from our study sheet, read in the whole 432 items
for rowy in range(1,num_items+1):                                               # range from 0 to num_items
    #read in the values of all columns on this row
    row_study = insheet_study.row_values(rowy)                                  # taking all row values for rowx. row will be a list with everythin within the row (rowx starts with one and end with num_items) 
    #saving the image in the image array
    person_prime_study.append(row_study[0])
    gender_prime_study.append(row_study[1])
    prime_study.append(row_study[2])
    emotion_prime_study.append(row_study[3])
    corrAns_prime_study.append(row_study[4])

#array for our final study stimuli will be set before each block - see block loop

def thiscomponent():                                                            # Prepare to start Routine
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    
################################ Initialisation  ###########################

text_height = 0.07

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Wilkommen!',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "into"
intoClock = core.Clock()
text_intro = visual.TextStim(win=win, name='text_intro',
    text='Bewerten Sie bitte die Emotion der gezeigten Gesichter nach:\n\n\ntraurig      neutral      glücklich',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_intro = keyboard.Keyboard()                                            # initialise keyboard to press forward

# Initialize components for Routine "into2"
into2Clock = core.Clock()
text_intro2 = visual.TextStim(win=win, name='text_intro2',
    text='Es geht los mit einer Proberunde.\n\nDrücken Sie eine Taste zum Starten…\n',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_intro2 = keyboard.Keyboard()                                           # initialise keyboard to press forward

# Initialize components for Routine "primer_example"
primer_exampleClock = core.Clock()
image_primer_example = visual.ImageStim(
    win=win,
    name='image_primer_example', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.625),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "Scrambled"
ScrambledClock = core.Clock()
scrambled = visual.ImageStim(
    win=win,
    name='scrambled', 
    image='10px.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "response_example"
response_exampleClock = core.Clock()
text_response_example = visual.TextStim(win=win, name='text_response_example',
    text='Das Gesicht war...\n\n\ntraurig      neutral      glücklich',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_example = keyboard.Keyboard()                                          # initialise keyboard for response

# Initialize components for Routine "fixcrossJitter"
fixcrossJitterClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(text_height, text_height),
    ori=0, pos=(0, 0),
    lineWidth=text_height, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "start"
startClock = core.Clock()
text_start = visual.TextStim(win=win, name='text_start',
    text='Jetzt geht es los...\n',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_pause = visual.TextStim(win=win, name='text_pause',
    text='Drücken Sie eine Taste wenn Sie bereit sind fortzufahren\n',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_pause = keyboard.Keyboard()

# Initialize components for Routine "primer_study"
primer_studyClock = core.Clock()
image_primer_study = visual.ImageStim(
    win=win,
    name='image_primer_study', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.625),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "response_study"
response_studyClock = core.Clock()
text_response_study = visual.TextStim(win=win, name='text_response_study',
    text='Das Gesicht war...\n\n\ntraurig      neutral      glücklich',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_study = keyboard.Keyboard()                                            # initialise keyboard for response

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Das war´s!\n\n Vielen Dank für Ihre Teilnahme!',
    font='Arial',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()                                                      # to track the time since experiment started
routineTimer = core.CountdownTimer()                                            # to track time remaining of each (non-slip) routine 

################################ Experiment Starts  ########################

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# keep track of which components have finished
welcomeComponents = [text_welcome]
for thisComponent in welcomeComponents:
    thiscomponent()                                                             # previous definded function
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)                                          # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1                                                         # number of completed frames (so 0 is the first frame)
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN                                       # exact frame index
        text_welcome.tStart = t                                                 # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal                            # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')                           # time at next scr refresh
        text_welcome.setAutoDraw(True)
    if text_welcome.status == STARTED:
        if frameN >= startTime:
            # keep track of stop time/frame for later
            text_welcome.tStop = t                                              # not accounting for scr refresh
            text_welcome.frameNStop = frameN                                    # exact frame index
            text_welcome.tStopRefresh = tThisFlipGlobal                         # on global time
            win.timeOnFlip(text_welcome, 'tStopRefresh')                        # time at next scr refresh
            text_welcome.setAutoDraw(False)
            
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:                                                     # a component has requested a forced-end of Routine
        break
    continueRoutine = False                                                     # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break                                                               # at least one component has not yet finished
    # refresh the screen
    if continueRoutine:                                                         # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.addData('text_welcome.started', text_welcome.tStartRefresh)
thisExp.addData('text_welcome.stopped', text_welcome.tStopRefresh)              # inserted

# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "into"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_intro.keys = []
key_resp_intro.rt = []
_key_resp_intro_allKeys = []
# keep track of which components have finished
intoComponents = [text_intro, key_resp_intro]
for thisComponent in intoComponents:
    thiscomponent()                                                             # previous definded function
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intoClock.reset(-_timeToFirstFrame)                                             # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = intoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1                                                         # number of completed frames (so 0 is the first frame)
    
    # *text_intro* updates
    if text_intro.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        text_intro.frameNStart = frameN                                         # exact frame index
        text_intro.tStart = t                                                   # local t and not account for scr refresh
        text_intro.tStartRefresh = tThisFlipGlobal                              # on global time
        win.timeOnFlip(text_intro, 'tStartRefresh')                             # time at next scr refresh
        text_intro.setAutoDraw(True)
    if text_intro.status == STARTED:
        if frameN >= instruction:
            # keep track of stop time/frame for later
            text_intro.tStop = t                                                # not accounting for scr refresh
            text_intro.frameNStop = frameN                                      # exact frame index
            text_intro.tStopRefresh = tThisFlipGlobal                           # on global time
            win.timeOnFlip(text_intro, 'tStopRefresh')                          # time at next scr refresh
            text_intro.setAutoDraw(False)
    # *key_resp_intro* updates 
    waitOnFlip = False
    if key_resp_intro.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        key_resp_intro.frameNStart = frameN                                     # exact frame index
        key_resp_intro.tStart = t                                               # local t and not account for scr refresh
        key_resp_intro.tStartRefresh = tThisFlipGlobal                          # on global time
        win.timeOnFlip(key_resp_intro, 'tStartRefresh')                         # time at next scr refresh
        key_resp_intro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_intro.clock.reset)                              # t=0 on next screen flip
        win.callOnFlip(key_resp_intro.clearEvents, eventType='keyboard')        # clear events on next screen flip
    if key_resp_intro.status == STARTED:
        if frameN >= instruction:
            # keep track of stop time/frame for later
            key_resp_intro.tStop = t                                            # not accounting for scr refresh
            key_resp_intro.frameNStop = frameN                                  # exact frame index
            key_resp_intro.tStopRefresh = tThisFlipGlobal                       # on global time
            win.timeOnFlip(key_resp_intro, 'tStopRefresh')                      # time at next scr refresh
            key_resp_intro.status = FINISHED
    if key_resp_intro.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_intro.getKeys(keyList=None, waitRelease=False)
        _key_resp_intro_allKeys.extend(theseKeys)
        if len(_key_resp_intro_allKeys):
            key_resp_intro.keys = _key_resp_intro_allKeys[0].name               # just the first key pressed
            key_resp_intro.rt = _key_resp_intro_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
        # if routine is forced to end by keypress, times have to be saved here
    if continueRoutine == False:                                                # if routine is forced to end by keypress, times have to be saved here
        # keep track of stop time/frame for later
        text_intro.tStop = t                                                    # not accounting for scr refresh
        text_intro.frameNStop = frameN                                          # exact frame index
        text_intro.tStopRefresh = tThisFlipGlobal                               # on global time
        win.timeOnFlip(text_intro, 'tStopRefresh')                              # time at next scr refresh
        text_intro.setAutoDraw(False)
        # keep track of stop time/frame for later
        key_resp_intro.tStop = t                                                # not accounting for scr refresh
        key_resp_intro.frameNStop = frameN                                      # exact frame index
        key_resp_intro.tStopRefresh = tThisFlipGlobal                           # on global time
        win.timeOnFlip(key_resp_intro, 'tStopRefresh')                          # time at next scr refresh
        key_resp_intro.status = FINISHED
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:                                                     # a component has requested a forced-end of Routine
        break
    continueRoutine = False                                                     # will revert to True if at least one component still running
    for thisComponent in intoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break                                                               # at least one component has not yet finished
    # refresh the screen
    if continueRoutine:                                                         # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "into"-------
for thisComponent in intoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_intro.started', text_intro.tStartRefresh)
thisExp.addData('text_intro.stopped', text_intro.tStopRefresh)                  # inserted
# check responses
if key_resp_intro.keys in ['', [], None]:                                       # No response was made
    key_resp_intro.keys = None
thisExp.addData('key_resp_intro.keys',key_resp_intro.keys)
if key_resp_intro.keys != None:                                                 # we had a response
    thisExp.addData('key_resp_intro.rt', key_resp_intro.rt)
thisExp.addData('key_resp_intro.started', key_resp_intro.tStartRefresh)
thisExp.addData('key_resp_intro.stopped', key_resp_intro.tStopRefresh)          #inserted
thisExp.nextEntry()
# the Routine "into" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "into2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_intro2.keys = []
key_resp_intro2.rt = []
_key_resp_intro2_allKeys = []
# keep track of which components have finished
intoComponents = [text_intro2, key_resp_intro2]
for thisComponent in intoComponents:
    thiscomponent()                                                             # previous definded function
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intoClock.reset(-_timeToFirstFrame)                                             # t0 is time of first possible flip
frameN = -1

# -------Run Routine "into2"-------
while continueRoutine:
    # get current time
    t = into2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=into2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1                                                         # number of completed frames (so 0 is the first frame)
    
    # *text_intro2* updates
    if text_intro2.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        text_intro2.frameNStart = frameN                                        # exact frame index
        text_intro2.tStart = t                                                  # local t and not account for scr refresh
        text_intro2.tStartRefresh = tThisFlipGlobal                             # on global time
        win.timeOnFlip(text_intro2, 'tStartRefresh')                            # time at next scr refresh
        text_intro2.setAutoDraw(True)
    if text_intro2.status == STARTED:
        if frameN >= instruction:
            # keep track of stop time/frame for later
            text_intro2.tStop = t                                               # not accounting for scr refresh
            text_intro2.frameNStop = frameN                                     # exact frame index
            text_intro2.tStopRefresh = tThisFlipGlobal                          # on global time
            win.timeOnFlip(text_intro2, 'tStopRefresh')                         # time at next scr refresh
            text_intro2.setAutoDraw(False)
    # *key_resp_intro2* updates 
    waitOnFlip = False
    if key_resp_intro2.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        key_resp_intro2.frameNStart = frameN                                    # exact frame index
        key_resp_intro2.tStart = t                                              # local t and not account for scr refresh
        key_resp_intro2.tStartRefresh = tThisFlipGlobal                         # on global time
        win.timeOnFlip(key_resp_intro2, 'tStartRefresh')                        # time at next scr refresh
        key_resp_intro2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_intro2.clock.reset)                             # t=0 on next screen flip
        win.callOnFlip(key_resp_intro2.clearEvents, eventType='keyboard')       # clear events on next screen flip
    if key_resp_intro2.status == STARTED:
        if frameN >= instruction:
            # keep track of stop time/frame for later
            key_resp_intro2.tStop = t                                           # not accounting for scr refresh
            key_resp_intro2.frameNStop = frameN                                 # exact frame index
            key_resp_intro2.tStopRefresh = tThisFlipGlobal                      # on global time
            win.timeOnFlip(key_resp_intro2, 'tStopRefresh')                     # time at next scr refresh
            key_resp_intro2.status = FINISHED
    if key_resp_intro2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_intro2.getKeys(keyList=None, waitRelease=False)
        _key_resp_intro2_allKeys.extend(theseKeys)
        if len(_key_resp_intro2_allKeys):
            key_resp_intro2.keys = _key_resp_intro2_allKeys[0].name             # just the first key pressed
            key_resp_intro2.rt = _key_resp_intro2_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
        # if routine is forced to end by keypress, times have to be saved here
    if continueRoutine == False:                
        # keep track of stop time/frame for later
        text_intro2.tStop = t                                                   # not accounting for scr refresh
        text_intro2.frameNStop = frameN                                         # exact frame index
        text_intro2.tStopRefresh = tThisFlipGlobal                              # on global time
        win.timeOnFlip(text_intro2, 'tStopRefresh')                             # time at next scr refresh
        text_intro2.setAutoDraw(False)
        # keep track of stop time/frame for later
        key_resp_intro2.tStop = t                                               # not accounting for scr refresh
        key_resp_intro2.frameNStop = frameN                                     # exact frame index
        key_resp_intro2.tStopRefresh = tThisFlipGlobal                          # on global time
        win.timeOnFlip(key_resp_intro2, 'tStopRefresh')                         # time at next scr refresh
        key_resp_intro2.status = FINISHED
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:                                                     # a component has requested a forced-end of Routine
        break
    continueRoutine = False                                                     # will revert to True if at least one component still running
    for thisComponent in intoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break                                                               # at least one component has not yet finished
    # refresh the screen
    if continueRoutine:                                                         # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "into2"-------
for thisComponent in intoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_intro2.started', text_intro2.tStartRefresh)
thisExp.addData('text_intro2.stopped', text_intro2.tStopRefresh)                #inserted
# check responses
if key_resp_intro2.keys in ['', [], None]:                                      # No response was made
    key_resp_intro2.keys = None
thisExp.addData('key_resp_intro2.keys',key_resp_intro2.keys)
if key_resp_intro2.keys != None:                                                # we had a response
    thisExp.addData('key_resp_intro2.rt', key_resp_intro2.rt)
thisExp.addData('key_resp_intro2.started', key_resp_intro2.tStartRefresh)
thisExp.addData('key_resp_intro2.stopped', key_resp_intro2.tStopRefresh)        #inserted
thisExp.nextEntry()
# the Routine "into" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_example = data.TrialHandler(nReps=num_example, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_example')
thisExp.addLoop(trials_example)                                                 # add the loop to the experiment
thisTrials_example = trials_example.trialList[0]                                # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_example.rgb)
if thisTrials_example != None:
    for paramName in thisTrials_example:
        exec('{} = thisTrials_example[paramName]'.format(paramName))

################################ Examole Starts  ###########################
example_trial = 0

#Prime time setting, two drifferent mask times are possible 
time = []
call_primeTime1 = 0                                                             # count used prime, see Begin Routine
call_primeTime2 = 0 

for thisTrials_example in trials_example:
    currentLoop = trials_example
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_example.rgb)
    if thisTrials_example != None:
        for paramName in thisTrials_example:
            exec('{} = thisTrials_example[paramName]'.format(paramName))
    
    # Choose Mask Timing, randomly distributed, and 50:50
    # in 50 % and if primeMask1 is not chosen for over the half of the study trials
    decision = random()
    if decision < 0.5 and call_primeTime1 < num_example/2 or call_primeTime2 == num_example/2: 
        time = primeTime1
        call_primeTime1 = call_primeTime1 + 1
    else: 
        time = primeTime2
        call_primeTime2 = call_primeTime2 + 1
    
    # assigning the example images
    personPrimeExample = person_item_prime_example[example_trial] 
    genderPrimeExample = gender_item_prime_example[example_trial] 
    primeExample = prime_item_example[example_trial]
    emotionPrimeExample = emotion_item_prime_example[example_trial]
    corrAnsPrimeExample = corrAns_item_prime_example[example_trial]
    
    # log study information
    thisExp.addData("example trial", example_trial)
    thisExp.addData("personPrimeExample", personPrimeExample)
    thisExp.addData("genderPrimeExample",genderPrimeExample)
    thisExp.addData("primeExample", primeExample)
    thisExp.addData("emotionPrimeExample", emotionPrimeExample)
    thisExp.addData("corrAnsPrimeExample", corrAnsPrimeExample)
    thisExp.addData("example mask time", time)
    
    # increment the current study item counter
    example_trial = example_trial + 1                                           # was set to 0 in the beginning
    
    # ------Prepare to start Routine "fixcross"-------
    continueRoutine = True
    
    # keep track of which components have finished
    fixcrossJitterComponents = [polygon]
    for thisComponent in fixcrossJitterComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixcrossJitterClock.reset(-_timeToFirstFrame)  
    frameN = -1
    
    # -------Run Routine "fixcross"-------
    while continueRoutine:
        # get current time
        t = fixcrossJitterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixcrossJitterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  
            polygon.tStart = t  
            polygon.tStartRefresh = tThisFlipGlobal  
            win.timeOnFlip(polygon, 'tStartRefresh')  
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if frameN >= cross:
                # keep track of stop time/frame for later
                polygon.tStop = t  
                polygon.frameNStop = frameN  
                polygon.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(polygon, 'tStopRefresh')  
                polygon.setAutoDraw(False)
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False  
        for thisComponent in fixcrossJitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine: 
            win.flip()
    
    # -------Ending Routine "fixcross"-------
    for thisComponent in fixcrossJitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_example.addData('fix300_example.started', polygon.tStartRefresh)
    trials_example.addData('fix300_example.stopped', polygon.tStopRefresh)      # inserted
    routineTimer.reset()
    
    # ------Prepare to start Routine "primer_example"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_primer_example.setImage(primeExample)
    # keep track of which components have finished
    primer_exampleComponents = [image_primer_example]
    for thisComponent in primer_exampleComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    primer_exampleClock.reset(-_timeToFirstFrame)  
    frameN = -1
    
    # -------Run Routine "primer_example"-------
    while continueRoutine:
        # get current time
        t = primer_exampleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=primer_exampleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *image_primer_example* updates
        if image_primer_example.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image_primer_example.frameNStart = frameN  
            image_primer_example.tStart = t  
            image_primer_example.tStartRefresh = tThisFlipGlobal  
            win.timeOnFlip(image_primer_example, 'tStartRefresh')  
            image_primer_example.setAutoDraw(True)
        if image_primer_example.status == STARTED:
            if frameN >= time:
                # keep track of stop time/frame for later
                image_primer_example.tStop = t  
                image_primer_example.frameNStop = frameN  
                image_primer_example.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(image_primer_example, 'tStopRefresh')  
                image_primer_example.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False  
        for thisComponent in primer_exampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine:  
            win.flip()
    
    # -------Ending Routine "primer_example"-------
    for thisComponent in primer_exampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_example.addData('image_primer_example.started', image_primer_example.tStartRefresh)
    trials_example.addData('image_primer_example.stopped', image_primer_example.tStopRefresh) # inserted
    # the Routine "primer_example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Scrambled"-------
    continueRoutine = True
    # keep track of which components have finished
    ScrambledComponents = [scrambled]
    for thisComponent in ScrambledComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ScrambledClock.reset(-_timeToFirstFrame)  
    frameN = -1
    
    # -------Run Routine "Scrambled"-------
    while continueRoutine:
        # get current time
        t = ScrambledClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ScrambledClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *scrambled* updates
        if scrambled.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            scrambled.frameNStart = frameN  
            scrambled.tStart = t  
            scrambled.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(scrambled, 'tStartRefresh')  
            scrambled.setAutoDraw(True)
        if scrambled.status == STARTED:
            if frameN >= scrambledTime:
                # keep track of stop time/frame for later
                scrambled.tStop = t  
                scrambled.frameNStop = frameN  
                scrambled.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(scrambled, 'tStopRefresh')  
                scrambled.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False 
        for thisComponent in ScrambledComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine:  
            win.flip()
    
    # -------Ending Routine "Scrambled"-------
    for thisComponent in ScrambledComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_example.addData('scrambled.started', scrambled.tStartRefresh)
    trials_example.addData('scrambled.stopped', scrambled.tStopRefresh)         # inserted
    # the Routine "Scrambled" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response_example"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_example.keys = []
    key_resp_example.rt = []
    _key_resp_example_allKeys = []
    # keep track of which components have finished
    response_exampleComponents = [text_response_example, key_resp_example]
    for thisComponent in response_exampleComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_exampleClock.reset(-_timeToFirstFrame)  
    frameN = -1
    
    # -------Run Routine "response_example"-------
    while continueRoutine:
        # get current time
        t = response_exampleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_exampleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *text_response_example* updates
        if text_response_example.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            text_response_example.frameNStart = frameN  
            text_response_example.tStart = t  
            text_response_example.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(text_response_example, 'tStartRefresh') 
            text_response_example.setAutoDraw(True)
        if text_response_example.status == STARTED:
            if frameN >= responseTime:
                # keep track of stop time/frame for later
                text_response_example.tStop = t  
                text_response_example.frameNStop = frameN  
                text_response_example.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(text_response_example, 'tStopRefresh')  
                text_response_example.setAutoDraw(False)
        # *key_resp_example* updates
        waitOnFlip = False
        if key_resp_example.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            key_resp_example.frameNStart = frameN  
            key_resp_example.tStart = t  
            key_resp_example.tStartRefresh = tThisFlipGlobal  
            win.timeOnFlip(key_resp_example, 'tStartRefresh')  
            key_resp_example.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_example.clock.reset)  
            win.callOnFlip(key_resp_example.clearEvents, eventType='keyboard')  
        if key_resp_example.status == STARTED:
            if frameN >= responseTime:
                # keep track of stop time/frame for later
                key_resp_example.tStop = t  
                key_resp_example.frameNStop = frameN  
                key_resp_example.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(key_resp_example, 'tStopRefresh')  
                key_resp_example.status = FINISHED
        if key_resp_example.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_example.getKeys(keyList=['a', 's', 'd'], waitRelease=False)
            _key_resp_example_allKeys.extend(theseKeys)
            if len(_key_resp_example_allKeys):
                key_resp_example.keys = _key_resp_example_allKeys[0].name  
                key_resp_example.rt = _key_resp_example_allKeys[0].rt
                # was this correct?
                if (key_resp_example.keys == str(corrAnsPrimeExample)) or (key_resp_example.keys == corrAnsPrimeExample):
                    key_resp_example.corr = 1
                else:
                    key_resp_example.corr = 0
                # a response ends the routine
                continueRoutine = False
        # if routine is forced to end by keypress, times have to be saved here
        if continueRoutine == False: 
            # keep track of stop time/frame for later
            text_response_example.tStop = t  
            text_response_example.frameNStop = frameN  
            text_response_example.tStopRefresh = tThisFlipGlobal  
            win.timeOnFlip(text_response_example, 'tStopRefresh')  
            text_response_example.setAutoDraw(False)
            # keep track of stop time/frame for later
            key_resp_example.tStop = t  
            key_resp_example.frameNStop = frameN  
            key_resp_example.tStopRefresh = tThisFlipGlobal  
            win.timeOnFlip(key_resp_example, 'tStopRefresh')  
            key_resp_example.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False  
        for thisComponent in response_exampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine:  
            win.flip()
    
    # -------Ending Routine "response_example"-------
    for thisComponent in response_exampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_example.addData('text_response_example.started', text_response_example.tStartRefresh)
    trials_example.addData('text_response_example.stopped', text_response_example.tStopRefresh) # inserted
    # check responses
    if key_resp_example.keys in ['', [], None]:  
        key_resp_example.keys = None
        # was no response the correct answer?!
        if str(corrAnsPrimeExample).lower() == 'none':
           key_resp_example.corr = 1;                                           # correct non-response
        else:
           key_resp_example.corr = 0;                                           # failed to respond (incorrectly)
    # store data for trials_example (TrialHandler)
    trials_example.addData('key_resp_example.keys',key_resp_example.keys)
    trials_example.addData('key_resp_example.corr', key_resp_example.corr)
    if key_resp_example.keys != None:                                           # we had a response
        trials_example.addData('key_resp_example.rt', key_resp_example.rt)
        thisExp.addData('key_resp_example.rt in ms', key_resp_example.rt * 1000)# save reaction time in miliseconds
    trials_example.addData('key_resp_example.started', key_resp_example.tStartRefresh)
    trials_example.addData('key_resp_example.stopped', key_resp_example.tStopRefresh) # inserted
    # the Routine "response_example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixcrossJitter"-------
    continueRoutine = True
    
    #use the random() function which returns a float between 0.0 and 1.0,and then add and multiply 
    jitterrange = random() * (jittermaxtime - jittermintime) + jittermintime    # fixcross jitter = 1-2 s also 120 frames - 240 frames 
    jitter = round(jitterrange)                                                 # round to 1 decimal place 
    
    # keep track of which components have finished
    fixcrossJitterComponents = [polygon]
    for thisComponent in fixcrossJitterComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixcrossJitterClock.reset(-_timeToFirstFrame) 
    frameN = -1
    
    # -------Run Routine "fixcrossJitter"-------
    while continueRoutine:
        # get current time
        t = fixcrossJitterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixcrossJitterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  
            polygon.tStart = t  
            polygon.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(polygon, 'tStartRefresh')  
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if frameN >= jitter:
                # keep track of stop time/frame for later
                polygon.tStop = t  
                polygon.frameNStop = frameN  
                polygon.tStopRefresh = tThisFlipGlobal 
                win.timeOnFlip(polygon, 'tStopRefresh')  
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False  
        for thisComponent in fixcrossJitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixcrossJitter"-------
    for thisComponent in fixcrossJitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_example.addData('Jitter_example.started', polygon.tStartRefresh)
    trials_example.addData('Jitter_example.stopped', polygon.tStopRefresh)      # inserted
    # the Routine "fixcrossJitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
# completed num_example repeats of 'trials_example'

# get names of stimulus parameters
if trials_example.trialList in ([], [None], None):
    params = []
else:
    params = trials_example.trialList[0].keys()
# save data for this loop
trials_example.saveAsExcel(filename + '.xlsx', sheetName='trials_example',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

########################################## Study starts ####################

# ------Prepare to start Routine "start"-------
continueRoutine = True
# keep track of which components have finished
startComponents = [text_start]
for thisComponent in startComponents:
    thiscomponent()                                                             # previous definded function
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame) 
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  
    
    # *text_start* updates
    if text_start.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        text_start.frameNStart = frameN  
        text_start.tStart = t  
        text_start.tStartRefresh = tThisFlipGlobal  
        win.timeOnFlip(text_start, 'tStartRefresh')  
        text_start.setAutoDraw(True)
    if text_start.status == STARTED:
        if frameN >= startTime:
            # keep track of stop time/frame for later
            text_start.tStop = t  
            text_start.frameNStop = frameN  
            text_start.tStopRefresh = tThisFlipGlobal  
            win.timeOnFlip(text_start, 'tStopRefresh')  
            text_start.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  
        break
    continueRoutine = False  
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  
    # refresh the screen
    if continueRoutine:  
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_start.started', text_start.tStartRefresh)
thisExp.addData('text_start.stopped', text_start.tStopRefresh)                  # inserted
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

###################### Study block starts ##################################

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=block_ans, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)                                                          # add the loop to the experiment
thisBlock = block.trialList[0]                                                  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

block_num = 0                                                                   # start with the first block

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    win.mouseVisible = False                                                        # hide mouse
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_pause.keys = []
    key_resp_pause.rt = []
    _key_resp_pause_allKeys = []
    
    #array for our  stimuli, clear lists for every block so items do not append on previous block items
    person_item_prime_study = []
    gender_item_prime_study = []
    prime_item_study = []
    emotion_item_prime_study = []
    corrAns_item_prime_study = []
    
    #create a order in wich to show study items
    if block_num == 0:
        i=0
        while i<num_study:                                              # list ranges from 0 to num_study 
            person_item_prime_study.append(person_prime_study[i])
            gender_item_prime_study.append(gender_prime_study[i])
            prime_item_study.append(prime_study[i])
            emotion_item_prime_study.append(emotion_prime_study[i])
            corrAns_item_prime_study.append(corrAns_prime_study[i])
            primeTime1 = 3 #25 ms
            primeTime2 = 17
            #print(i)
            i=i+1
    if block_num == 1:
        i=num_study
        while i<(num_study*2):                              # ranges from num_study + 1 to next number of num_study
            person_item_prime_study.append(person_prime_study[i])
            gender_item_prime_study.append(gender_prime_study[i])
            prime_item_study.append(prime_study[i])
            emotion_item_prime_study.append(emotion_prime_study[i])
            corrAns_item_prime_study.append(corrAns_prime_study[i])
            primeTime1 = 2 #16 ms
            primeTime2 = 17
            #print(i)
            i=i+1
    if block_num == 2:
        i=num_study*2
        while i<(num_study*3):  # searches the remaining items (range = number of num_study)
            person_item_prime_study.append(person_prime_study[i])
            gender_item_prime_study.append(gender_prime_study[i])
            prime_item_study.append(prime_study[i])
            emotion_item_prime_study.append(emotion_prime_study[i])
            corrAns_item_prime_study.append(corrAns_prime_study[i])
            primeTime1 = 1 #8 ms
            primeTime2 = 17
            #print(i)
            i=i+1
            
    block_num = block_num + 1                                                   # count block number
    study_trial = 0                                                             # run first trial
    
    #Prime time setting
    time = []                                                                   # list for chosen times
    call_primeTime1 = 0                                                         # set counter to zero for the next block
    call_primeTime2 = 0
    
    # keep track of which components have finished
    pauseComponents = [text_pause, key_resp_pause]
    for thisComponent in pauseComponents:
        thiscomponent()                                                         # previous definded function
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)                                        # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        
        # *text_pause* updates
        if text_pause.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            text_pause.frameNStart = frameN  
            text_pause.tStart = t  
            text_pause.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(text_pause, 'tStartRefresh')  
            text_pause.setAutoDraw(True)
        if text_pause.status == STARTED:
            if frameN >= maxBreakTime:
                # keep track of stop time/frame for later
                text_pause.tStop = t  
                text_pause.frameNStop = frameN  
                text_pause.tStopRefresh = tThisFlipGlobal 
                win.timeOnFlip(text_pause, 'tStopRefresh')  
                text_pause.setAutoDraw(False)
        
        # *key_resp_pause* updates
        waitOnFlip = False
        if key_resp_pause.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            key_resp_pause.frameNStart = frameN 
            key_resp_pause.tStart = t 
            key_resp_pause.tStartRefresh = tThisFlipGlobal  
            win.timeOnFlip(key_resp_pause, 'tStartRefresh') 
            key_resp_pause.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_pause.clock.reset)  
            win.callOnFlip(key_resp_pause.clearEvents, eventType='keyboard') 
        if key_resp_pause.status == STARTED:
            if frameN >= maxBreakTime:
                # keep track of stop time/frame for later
                key_resp_pause.tStop = t  
                key_resp_pause.frameNStop = frameN  
                key_resp_pause.tStopRefresh = tThisFlipGlobal 
                win.timeOnFlip(key_resp_pause, 'tStopRefresh')  
                key_resp_pause.status = FINISHED
        if key_resp_pause.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_pause.getKeys(keyList=None, waitRelease=False)
            _key_resp_pause_allKeys.extend(theseKeys)
            if len(_key_resp_pause_allKeys):
                #key_resp_pause.keys = _key_resp_pause_allKeys[-1].name  # just the last key pressed
                #key_resp_pause.rt = _key_resp_pause_allKeys[-1].rt
                key_resp_pause.keys = _key_resp_pause_allKeys[0].name  # just the first key pressed
                key_resp_pause.rt = _key_resp_pause_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        # if routine is forced to end by keypress, times have to be saved here
        if continueRoutine == False: 
            # keep track of stop time/frame for later
            text_pause.tStop = t                                                # not accounting for scr refresh
            text_pause.frameNStop = frameN                                      # exact frame index
            text_pause.tStopRefresh = tThisFlipGlobal                           # on global time
            win.timeOnFlip(text_pause, 'tStopRefresh')                          # time at next scr refresh
            text_pause.setAutoDraw(False)
            # keep track of stop time/frame for later
            key_resp_pause.tStop = t                                            # not accounting for scr refresh
            key_resp_pause.frameNStop = frameN                                  # exact frame index
            key_resp_pause.tStopRefresh = tThisFlipGlobal                       # on global time
            win.timeOnFlip(key_resp_pause, 'tStopRefresh')                      # time at next scr refresh
            key_resp_pause.status = FINISHED
            
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  
            break
        continueRoutine = False  
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        # refresh the screen
        if continueRoutine:  
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_pause.started', text_pause.tStartRefresh)
    block.addData('text_pause.stopped', text_pause.tStopRefresh)                # inserted
    # check responses
    if key_resp_pause.keys in ['', [], None]:                                   # No response was made
        key_resp_pause.keys = None
    block.addData('key_resp_pause.keys',key_resp_pause.keys)
    if key_resp_pause.keys != None:                                             # we had a response
        block.addData('key_resp_pause.rt', key_resp_pause.rt)
        block.addData('key_resp_pause.rt in ms', key_resp_pause.rt * 1000)      # save reaction time in miliseconds
    block.addData('key_resp_pause.started', key_resp_pause.tStartRefresh)
    block.addData('key_resp_pause.stopped', key_resp_pause.tStopRefresh)        # inserted
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    ############################ Trials in block start #####################
    
    # set up handler to look after randomisation of conditions etc
    trials_study = data.TrialHandler(nReps=num_study, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_study')
    thisExp.addLoop(trials_study)                                               # add the loop to the experiment
    thisTrials_study = trials_study.trialList[0]                                # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_study.rgb)
    if thisTrials_study != None:
        for paramName in thisTrials_study:
            exec('{} = thisTrials_study[paramName]'.format(paramName))
    
    for thisTrials_study in trials_study:
        currentLoop = trials_study
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_study.rgb)
        if thisTrials_study != None:
            for paramName in thisTrials_study:
                exec('{} = thisTrials_study[paramName]'.format(paramName))
        
        # randomly distributed, and 50:50
        # in 50 % and if primeTime1 is not chosen for over the half of the study trials
        decision = random()                                                     # random number between 0 and 1
        if decision < 0.5 and call_primeTime1 < num_study/2 or call_primeTime2 == num_study/2: 
            time = primeTime1
            call_primeTime1 = call_primeTime1 + 1
        else: 
            time = primeTime2
            call_primeTime2 = call_primeTime2 + 1
        
        #assigning the study images
        personPrimeStudy = person_item_prime_study[study_trial]
        genderPrimeStudy = gender_item_prime_study[study_trial]
        primeStudy = prime_item_study[study_trial]
        emotionPrimeStudy = emotion_item_prime_study[study_trial]
        corrAnsPrimeStudy = corrAns_item_prime_study[study_trial]
        
        #log study information
        thisExp.addData("study trial", study_trial)
        thisExp.addData("personPrimeStudy", personPrimeStudy)
        thisExp.addData("genderPrimeStudy",genderPrimeStudy)
        thisExp.addData("primeStudy", primeStudy)
        thisExp.addData("emotionPrimeStudy", emotionPrimeStudy)
        thisExp.addData("corrAnsPrimeStudy", corrAnsPrimeStudy)
        thisExp.addData("study mask time", time)
        thisExp.addData("Block", block_num)
        
        #increment the current study item counter
        study_trial = study_trial + 1
        
        # ------Prepare to start Routine "fixcross"-------
        continueRoutine = True
        
        # keep track of which components have finished
        fixcrossJitterComponents = [polygon]
        for thisComponent in fixcrossJitterComponents:
            thiscomponent()                                                     # previous definded function
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixcrossJitterClock.reset(-_timeToFirstFrame)    
        frameN = -1
        
        # -------Run Routine "fixcross"-------
        while continueRoutine:
            # get current time
            t = fixcrossJitterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossJitterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  
                polygon.tStart = t  
                polygon.tStartRefresh = tThisFlipGlobal  
                win.timeOnFlip(polygon, 'tStartRefresh')  
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                if frameN >= cross:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  
                    polygon.frameNStop = frameN 
                    polygon.tStopRefresh = tThisFlipGlobal  
                    win.timeOnFlip(polygon, 'tStopRefresh')  
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            # check if all components have finished
            if not continueRoutine:  
                break
            continueRoutine = False  
            for thisComponent in fixcrossJitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  
            # refresh the screen
            if continueRoutine:  
                win.flip()
        
        # -------Ending Routine "fixcross"-------
        for thisComponent in fixcrossJitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_study.addData('fix300_study.started', polygon.tStartRefresh)
        trials_study.addData('fix300_study.stopped', polygon.tStopRefresh)      # inserted
        # the Routine "fixcrossJitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "primer_study"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_primer_study.setImage(primeStudy)
        # keep track of which components have finished
        primer_studyComponents = [image_primer_study]
        for thisComponent in primer_studyComponents:
            thiscomponent()                                                     # previous definded function
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        primer_studyClock.reset(-_timeToFirstFrame)  
        frameN = -1
        
        # -------Run Routine "primer_study"-------
        while continueRoutine:
            # get current time
            t = primer_studyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=primer_studyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1 
            
            # *image_primer_study* updates
            if image_primer_study.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                image_primer_study.frameNStart = frameN  
                image_primer_study.tStart = t  
                image_primer_study.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(image_primer_study, 'tStartRefresh') 
                image_primer_study.setAutoDraw(True)
            if image_primer_study.status == STARTED:
                if frameN >= time:
                    # keep track of stop time/frame for later
                    image_primer_study.tStop = t  
                    image_primer_study.frameNStop = frameN  
                    image_primer_study.tStopRefresh = tThisFlipGlobal  
                    win.timeOnFlip(image_primer_study, 'tStopRefresh')  
                    image_primer_study.setAutoDraw(False)
                    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            # check if all components have finished
            if not continueRoutine:  
                break
            continueRoutine = False  
            for thisComponent in primer_studyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  
            # refresh the screen
            if continueRoutine:  
                win.flip()
        
        # -------Ending Routine "primer_study"-------
        for thisComponent in primer_studyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_study.addData('image_primer_study.started', image_primer_study.tStartRefresh)
        trials_study.addData('image_primer_study.stopped', image_primer_study.tStopRefresh) # inserted
        # the Routine "primer_study" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Scrambled"-------
        continueRoutine = True
        # keep track of which components have finished
        ScrambledComponents = [scrambled]
        for thisComponent in ScrambledComponents:
            thiscomponent()                                                     # previous definded function
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ScrambledClock.reset(-_timeToFirstFrame)  
        frameN = -1
        
        # -------Run Routine "Scrambled"-------
        while continueRoutine:
            # get current time
            t = ScrambledClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ScrambledClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  
            
            # *scrambled* updates
            if scrambled.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                scrambled.frameNStart = frameN  
                scrambled.tStart = t  
                scrambled.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(scrambled, 'tStartRefresh')  
                scrambled.setAutoDraw(True)
            if scrambled.status == STARTED:
                if frameN >= scrambledTime:
                    # keep track of stop time/frame for later
                    scrambled.tStop = t  
                    scrambled.frameNStop = frameN  
                    scrambled.tStopRefresh = tThisFlipGlobal 
                    win.timeOnFlip(scrambled, 'tStopRefresh')  
                    scrambled.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            # check if all components have finished
            if not continueRoutine:  
                break
            continueRoutine = False  
            for thisComponent in ScrambledComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  
            # refresh the screen
            if continueRoutine:  
                win.flip()
        
        # -------Ending Routine "Scrambled"-------
        for thisComponent in ScrambledComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_study.addData('scrambled_study.started', scrambled.tStartRefresh)
        trials_study.addData('scrambled_study.stopped', scrambled.tStopRefresh)     # inserted
        # the Routine "Scrambled" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response_study"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_study.keys = []
        key_resp_study.rt = []
        _key_resp_study_allKeys = []
        # keep track of which components have finished
        response_studyComponents = [text_response_study, key_resp_study]
        for thisComponent in response_studyComponents:
            thiscomponent()                                                     # previous definded function
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_studyClock.reset(-_timeToFirstFrame)  
        frameN = -1
        
        # -------Run Routine "response_study"-------
        while continueRoutine:
            # get current time
            t = response_studyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_studyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  
            
            # *text_response_study* updates
            if text_response_study.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                text_response_study.frameNStart = frameN  
                text_response_study.tStart = t  
                text_response_study.tStartRefresh = tThisFlipGlobal  
                win.timeOnFlip(text_response_study, 'tStartRefresh')  
                text_response_study.setAutoDraw(True)
            if text_response_study.status == STARTED:
                if frameN >= responseTime:
                    # keep track of stop time/frame for later
                    text_response_study.tStop = t  
                    text_response_study.frameNStop = frameN 
                    text_response_study.tStopRefresh = tThisFlipGlobal  
                    win.timeOnFlip(text_response_study, 'tStopRefresh')  
                    text_response_study.setAutoDraw(False)
            
            # *key_resp_study* updates
            waitOnFlip = False
            if key_resp_study.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                key_resp_study.frameNStart = frameN  
                key_resp_study.tStart = t  
                key_resp_study.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(key_resp_study, 'tStartRefresh')  
                key_resp_study.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_study.clock.reset)  
                win.callOnFlip(key_resp_study.clearEvents, eventType='keyboard')  
            if key_resp_study.status == STARTED:
                if frameN >= responseTime:
                    # keep track of stop time/frame for later
                    key_resp_study.tStop = t  
                    key_resp_study.frameNStop = frameN 
                    key_resp_study.tStopRefresh = tThisFlipGlobal 
                    win.timeOnFlip(key_resp_study, 'tStopRefresh')  
                    key_resp_study.status = FINISHED
            if key_resp_study.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_study.getKeys(keyList=['a', 's', 'd'], waitRelease=False)
                _key_resp_study_allKeys.extend(theseKeys)
                if len(_key_resp_study_allKeys):
                    key_resp_study.keys = _key_resp_study_allKeys[0].name       # just the first key pressed
                    key_resp_study.rt = _key_resp_study_allKeys[0].rt
                    # was this correct?
                    if (key_resp_study.keys == str(corrAnsPrimeStudy)) or (key_resp_study.keys == corrAnsPrimeStudy):
                        key_resp_study.corr = 1
                    else:
                        key_resp_study.corr = 0
                    # a response ends the routine
                    continueRoutine = False
                    
            # if routine is forced to end by keypress, times have to be saved here
            if continueRoutine == False:                                        
                # keep track of stop time/frame for later
                text_response_study.tStop = t  
                text_response_study.frameNStop = frameN  
                text_response_study.tStopRefresh = tThisFlipGlobal 
                win.timeOnFlip(text_response_study, 'tStopRefresh')  
                text_response_study.setAutoDraw(False)
                # keep track of stop time/frame for later
                key_resp_study.tStop = t  
                key_resp_study.frameNStop = frameN  
                key_resp_study.tStopRefresh = tThisFlipGlobal  
                win.timeOnFlip(key_resp_study, 'tStopRefresh')  
                key_resp_study.status = FINISHED
                
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            # check if all components have finished
            if not continueRoutine:  
                break
            continueRoutine = False 
            for thisComponent in response_studyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  
            # refresh the screen
            if continueRoutine:  
                win.flip()
        
        # -------Ending Routine "response_study"-------
        for thisComponent in response_studyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_study.addData('text_response_study.started', text_response_study.tStartRefresh)
        trials_study.addData('text_response_study.stopped', text_response_study.tStopRefresh) # inserted
        # check responses
        if key_resp_study.keys in ['', [], None]:                               # No response was made
            key_resp_study.keys = None
            # was no response the correct answer?!
            if str(corrAnsPrimeStudy).lower() == 'none':
               key_resp_study.corr = 1;                                         # correct non-response
            else:
               key_resp_study.corr = 0;                                         # failed to respond (incorrectly)
        # store data for trials_study (TrialHandler)
        trials_study.addData('key_resp_study.keys',key_resp_study.keys)
        trials_study.addData('key_resp_study.corr', key_resp_study.corr)
        if key_resp_study.keys != None:                                         # we had a response
            trials_study.addData('key_resp_study.rt', key_resp_study.rt)
            trials_study.addData('key_resp_study.rt in ms', key_resp_study.rt * 1000)
        trials_study.addData('key_resp_study.started', key_resp_study.tStartRefresh)
        trials_study.addData('key_resp_study.stopped', key_resp_study.tStopRefresh) 
        # the Routine "response_study" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixcrossJitter"-------
        continueRoutine = True
        # update component parameters for each repeat
        jitterrange = random() * (jittermaxtime - jittermintime) + jittermintime # fixcross jitter = 1-2 s also 120 frames - 240 frames 
        jitter = round(jitterrange)                                             # round to 1 decimal place
        
        # keep track of which components have finished
        fixcrossJitterComponents = [polygon]
        for thisComponent in fixcrossJitterComponents:
            thiscomponent()                                                     # previous definded function
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixcrossJitterClock.reset(-_timeToFirstFrame)  
        frameN = -1
        
        # -------Run Routine "fixcrossJitter"-------
        while continueRoutine:
            # get current time
            t = fixcrossJitterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossJitterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  
                polygon.tStart = t  
                polygon.tStartRefresh = tThisFlipGlobal  
                win.timeOnFlip(polygon, 'tStartRefresh')  
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                if frameN >= jitter:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  
                    polygon.frameNStop = frameN  
                    polygon.tStopRefresh = tThisFlipGlobal  
                    win.timeOnFlip(polygon, 'tStopRefresh')  
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            # check if all components have finished
            if not continueRoutine:  
                break
            continueRoutine = False  
            for thisComponent in fixcrossJitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  
            # refresh the screen
            if continueRoutine:  
                win.flip()
        
        # -------Ending Routine "fixcrossJitter"-------
        for thisComponent in fixcrossJitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_study.addData('Jitter_study.started', polygon.tStartRefresh)
        trials_study.addData('Jitter_study.stopped', polygon.tStopRefresh)      # inserted
        # the Routine "fixcrossJitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
    # completed num_study repeats of 'trials_study'
    
    # get names of stimulus parameters
    if trials_study.trialList in ([], [None], None):
        params = []
    else:
        params = trials_study.trialList[0].keys()
    # save data for this loop
    trials_study.saveAsExcel(filename + '.xlsx', sheetName='trials_study',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed block_ans repeats of 'block'

# ------Prepare to start Routine "end"-------
continueRoutine = True
# keep track of which components have finished
endComponents = [text_end]
for thisComponent in endComponents:
    thiscomponent()                                                              # previous definded function
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1 
    # *text_end* updates
    if text_end.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  
        text_end.tStart = t 
        text_end.tStartRefresh = tThisFlipGlobal  
        win.timeOnFlip(text_end, 'tStartRefresh') 
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        if frameN >= ende:
            # keep track of stop time/frame for later
            text_end.tStop = t  
            text_end.frameNStop = frameN 
            text_end.tStopRefresh = tThisFlipGlobal 
            win.timeOnFlip(text_end, 'tStopRefresh') 
            text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine: 
        break
    continueRoutine = False  
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  
    # refresh the screen
    if continueRoutine:  
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)                      # inserted

routineTimer.reset()                                                            # the Routine "end" was not non-slip safe, so reset the non-slip timer
thisExp.nextEntry()

win.flip()                                                                      # Flip one final time so any remaining win.callOnFlip() 

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='tab')
thisExp.saveAsPickle(filename)
logging.flush()

# make sure everything is closed down
thisExp.abort()                                                                 # or data files will save again on exit
win.close()                                                                     # close window
core.quit()                                                                     # end experiment
