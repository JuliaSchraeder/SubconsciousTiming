#Load in library
library(lme4) # mixed
library(lmerTest) #to get p values
library(ggplot2) # graphics
library(interactions) 
library(tidyverse) # needed for data manipulation.#needed to view data
library(jtools)  # post hoc tests

#Load in dataset
data <- read.csv("Path/GLMM_Model1_data.csv", sep=",")

#Remove missing values and additional column
data$X <- NULL
data <-data[complete.cases(data), ]
View(data)

# Define variables
data$correct[data$correct == "0"] <- 2
data$level <- as.factor(data$level)                                          
data$stim <- as.factor(data$stim)
data$subj_idx <- as.factor(data$subj_idx)
data$block <- as.factor(data$block)
data$response <- as.factor(data$response)
#data$rt <- as.integer(data$rt)
data$response <-as.numeric(data$response)

view(data)

#Transform trail numbers
data$real_trial_number <- as.integer(data$real_trial_number)
data$real_trial_number.z <- data$real_trial_number/sd(data$real_trial_number) # z transformation


Model1 <- glmer(correct ~  stim + level + response
               + real_trial_number.z 
               + (1+real_trial_number.z|subj_idx),
               data = data,
               family=Gamma(link="inverse"))

anova(Model1)
summary (Model1)
dotplot(ranef(Model1, condVar=TRUE))
print(Model1, corr=F)

#Plot
interact_plot(Model1,pred=response, modx=stim, mod2=level)


### Include Questionnaires ###
#Load in dataset
data<- read_excel("Path/GLMM_Model2_data.xlsx")
View(data)
data$TMT <- (data$TMT_A+data$TMT_B)/2


# Define variables
data$SERIAL<- as.factor(data$SERIAL)
#data$Age<- as.factor(data$Age)
#data$Sex<- as.factor(data$Sex)


#Questionnaires
TMT <- standardize(data$TMT)
BDI <- standardize(data$ScoreBDI)
BVAQ <- standardize(data$ScoreBVAQ_B)
View(data)


Model2 <- glmer (accuracy ~ TMT + BDI + BVAQ + Sex +
                   (1|SERIAL),
                 data=data,
                 family = Gamma(link = "inverse"))

summary(Model2)
Model2
print(Model2, corr=F)

#Plot
interact_plot(Model2,pred=TMT,modx=Sex)
interact_plot(Model2,pred=BDI,modx=Sex)
interact_plot(Model2,pred=BVAQ,modx=Sex)
