#Model 1 = find effects on response correctness in rating the emotional face

#Load in library
library(lme4)       # mixed, version 1.1-26
library(lmerTest)   # to get p values, version 3.1-3 
library(ggplot2)    # graphics, version 3.3.5
library(interactions) #version 1.1.5
library(tidyverse)  # needed for data manipulation.#needed to view data, version 1.3.1
library(jtools)     # post hoc tests, version 2.1.4
library(readxl)     # read excel, version 1.3.1
library(lme4)       # load mixed model library
library(lmerTest)   # library providing p-values for mixed models in lme4
library(tidyverse)  # library with various tools (e.g. ggplot, pivot_long, pipes etc.)
library(emmeans)    # library for post-hoc tests
library(pbkrtest)   # needed for post-hoc tests in mixed models

#Load in dataset
data <- read.csv("/GLMM_Model1_data.csv", sep=",")

#Remove missing values and additional column
data$X <- NULL
data <-data[complete.cases(data), ]

#View Data
View(data)

#Get datatype
summary(data) 

#Define variables
data$study_number[data$study_number == "study2"] <- 2
data$study_number[data$study_number == "study1"] <- 1

data$response[data$response == "8.0"] <- 3                                       #neutral
data$response[data$response == "7.0"] <- 2                                       #sad
data$response[data$response == "9.0"] <- 1                                       #happy

data$response[data$response == "8"] <- 3                                         #neutral
data$response[data$response == "7"] <- 2                                         #sad
data$response[data$response == "9"] <- 1                                         #happy

data$response[data$response == "neutral"] <- 3                                   #neutral
data$response[data$response == "sad"]     <- 2                                   #sad
data$response[data$response == "happy"]   <- 1                                   #happy

data$stim[data$stim == "neutral"]  <- 3
data$stim[data$stim == "sad"]      <- 2
data$stim[data$stim == "happy"]    <- 1

data$level[data$level == "141ms"]  <- 4
data$level[data$level == "25ms"]   <- 3
data$level[data$level == "16ms"]   <- 2
data$level[data$level == "8ms"]    <- 1

#Transform trail numbers
data$real_trial_number <- as.integer(data$real_trial_number)
data$real_trial_number.z <- data$real_trial_number/sd(data$real_trial_number)    #z transformation


#Factorise variables
data$correct             <- factor(data$correct, ordered = FALSE)
data$level               <- factor(data$level, ordered = FALSE) 
data$subj_idx            <- factor(data$subj_idx, ordered = FALSE)
data$block               <- factor(data$block, ordered = FALSE)
data$study_number        <- factor(data$study_number, ordered = FALSE)
data$response            <- factor(data$response, ordered = FALSE)
data$stim                <- factor(data$stim, ordered = FALSE)

summary(data)

options('contrasts')

#Use type III analysis of variance
options(contrasts = c("contr.sum", "contr.poly"))

############################ Find Model 1 for response correctnes ##############
#glmm for binary outcome = correct/incorrect -> family = "binomial"


Model1 <- glmer(correct ~  stim + level 
                + (1|subj_idx),
                data = data,
                family = "binomial")

Model2 <- glmer(correct ~  stim * level 
               + (1|subj_idx),
               data = data,
               family = "binomial")


anova(Model2, Model2) 
#no difference, continue without interaction to get less complex models

#include stimulus response as interaction or as interaction with stimulus
Model3 <- glmer(correct ~  response:stim + level 
                + (1|subj_idx),
                data = data,
                family = "binomial")

Model4 <- glmer(correct ~  response + level + stim
                + (1|subj_idx),
                data = data,
                family = "binomial")

anova(Model1,Model2,Model3,Model4)
# Model 3 or 4  is best!

#include trial number as random intercept
Model6 <- glmer(correct ~  response + level + stim
                + (1+real_trial_number|subj_idx),
                data = data,
                family = "binomial")

Model6.z <- glmer(correct ~  response + level + stim
                + (1+real_trial_number.z|subj_idx),
                data = data,
                family = "binomial")

anova(Model1,Model2,Model3,Model4, Model6, Model6.z)

anova(Model6, Model6.z) #makes no difference if trial number is z transformed

#include random effect for study number
Model7 <- glmer(correct ~  response + level + stim
                + study_number
                + (1+real_trial_number|subj_idx),
                data = data,
                family = "binomial")

anova(Model1,Model2,Model3,Model4, Model6, Model7)
##with most factors still significant --> Model6

Model6 <- glmer(correct ~  response + level + stim
                + (1+real_trial_number|subj_idx),
                data = data,
                family = "binomial")
summary(Model6)




############################ Get Statistics ####################################

anova(Model6)
summary (Model6)
print(Model6, corr=F)




#["neutral"]  <- 3
#["sad"]      <- 2
#["happy"]    <- 1
#["141ms"]  <- 4
#["25ms"]   <- 3
#["16ms"]   <- 2
#["8ms"]    <- 1


#Get p-values from logit
fixef(Model6)

response1.logit <-fixef(Model6)[[2]]  
response2.logit <-fixef(Model6)[[3]]  
level1.logit    <-fixef(Model6)[[4]]    
level2.logit    <-fixef(Model6)[[5]]    
level3.logit    <-fixef(Model6)[[6]]  
stim1.logit     <-fixef(Model6)[[7]]  
stim2.logit     <-fixef(Model6)[[8]]

level4.logit    <- -(fixef(Model6)[[4]]+fixef(Model6)[[5]]+fixef(Model6)[[6]])
response3.logit <- -(fixef(Model6)[[2]]+fixef(Model6)[[3]])
stim3.logit     <- -(fixef(Model6)[[7]]+fixef(Model6)[[8]])


tapply(as.numeric(data$correct)-1,    data$subj_idx, sum) # number of correct responses per subject
tapply(-(as.numeric(data$correct)-2), data$subj_idx, sum) # number of false responses per subject

#Backtransform logit into p value
1/(1+exp(-level1.logit))    # probability of making a correct response during level1 trials
1/(1+exp(-level2.logit))    # probability of making a correct response during level2 trials
1/(1+exp(-level3.logit))    # probability of making a correct response during level3 trials
1/(1+exp(-level4.logit))    # probability of making a correct response during level4 trials
