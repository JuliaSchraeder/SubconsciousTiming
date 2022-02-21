#Skript to find and analyze glmm for backward mask task
#Model 1 = find effects on response correctness in rating the emotional face
#Model 2 = find effects on drift rate during response
#Model 3 = find effects on bias during response



#Load in library
library(lme4)       # mixed
library(lmerTest)   # to get p values
library(ggplot2)    # graphics
library(interactions) 
library(tidyverse)  # needed for data manipulation.#needed to view data
library(jtools)     # post hoc tests
library(readxl)     # read excel


#Load in dataset
data <- read.csv("/GLMM_Model1_data.csv", sep=",")

#Remove missing values and additional column
data$X <- NULL
data <-data[complete.cases(data), ]
View(data)

#Define variables
data$correct[data$correct == "0"] <- 2
data$study_number[data$study_number == "study2"] <- 2
data$study_number[data$study_number == "study1"] <- 1

data$response[data$response == "neutral"] <- 1
data$response[data$response == "sad"] <- 2
data$response[data$response == "happy"] <- 3

data$response[data$response == "8.0"] <- 1                                       #neutral
data$response[data$response == "7.0"] <- 2                                       #sad
data$response[data$response == "9.0"] <- 3                                       #happy

data$stim[data$stim == "neutral"] <- 1
data$stim[data$stim == "sad"] <- 2
data$stim[data$stim == "happy"] <- 3

#Transform trail numbers
data$real_trial_number <- as.integer(data$real_trial_number)
data$real_trial_number.z <- data$real_trial_number/sd(data$real_trial_number)    #z transformation

data$level <- as.factor(data$level)                                          
data$subj_idx <- as.factor(data$subj_idx)
data$block <- as.factor(data$block)
data$study_number <- as.factor(data$study_number)  
data$response <-as.numeric(data$response)

view(data)

#Plot Density 
plot(density(data$correct),main="Density estimate of data")

#### Find Model 1 ####
 
#Model Selection:

Model1 <- glmer(correct ~  stim + level 
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

#include trial number
Model2 <- glmer(correct ~  stim + level
                + real_trial_number.z 
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

#trial number as random slope
Model3 <- glmer(correct ~  stim + level
                + real_trial_number.z 
                + (1+real_trial_number.z|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

#include response 
Model4 <- glmer(correct ~  stim:response + level
                + real_trial_number.z 
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

Model5 <- glmer(correct ~  stim:response + level
               + real_trial_number.z 
               + (1+real_trial_number.z|subj_idx),
               data = data,
               family=Gamma(link="inverse"))


#include response as fixed effect
Model6 <- glmer(correct ~  stim + level
                + response
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

#include trial number
Model7 <- glmer(correct ~  stim + level
                + response
                + real_trial_number.z 
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

anova(Model1,Model2,Model3,Model4,Model5,Model6, Model7)

#warning model 4
#model3 wins!


#include random effect for study number
Model8 <- glmer(correct ~  stim + level
                + real_trial_number.z 
                + study_number
                + (1+real_trial_number.z|subj_idx),
                data = data,
                family=Gamma(link="inverse"))

#doenst make a huge difference if study is included or not 

anova(Model8,Model3)

#AIC estimates the relative amount of information lost by a given model:
#Model8 wins

#Get Statistics:
anova(Model8)
summary (Model8)
print(Model3, corr=F)





#### Find Model 2 and 3 ####


#Load in Dataset
data <- read_excel("GLMM_Model2_3_data.xlsx")
View(data)

#Transform values
data$DriftRate <-as.numeric(data$DriftRate)

data$Bias <-as.numeric(data$Bias)
data$Emotion[data$Emotion == "neutral"] <- 1
data$Emotion[data$Emotion == "sad"] <- 2
data$Emotion[data$Emotion == "happy"] <- 3

data$BVAQ <- as.integer(data$BVAQ)
data$BVAQ.z <- data$BVAQ/sd(data$BVAQ)                                          #z transformation
data$BDI <- as.integer(data$BDI)
data$BDI.z <- data$BDI/sd(data$BDI)                                             #z transformation
view(data)

#Plot Density 
par(mfrow = c(2, 2)) #show 4 pictures
plot(density(data$DriftRate),main="Density estimate of data")
plot(density(data$Bias),main="Density estimate of data")

#Plot Normal distribution
z.norm<-(data$DriftRate-mean(data$DriftRate))/sd(data$DriftRate)                #standardized data
qqnorm(z.norm)                                                                  #drawing the QQplot
abline(0,1)                                                                     #drawing a 45-degree reference line

z.norm<-(data$Bias-mean(data$Bias))/sd(data$Bias)                               #standardized data
qqnorm(z.norm)                                                                  #drawing the QQplot
abline(0,1)                                                                     #drawing a 45-degree reference line


#Model Selection

Model1 <- lmer(DriftRate ~ BDI.z*Emotion + Emotion*BVAQ.z
               + (1|subj_idx),
               data = data)


Model2 <- lmer(Bias ~ Emotion*BDI.z + Emotion*BVAQ.z
               + (1|subj_idx),
               data = data)
#boundary (singular) fit: see ?isSingular
#Your model did fit, but it generated that warning because your random effects are very small.


#+Age
Model3 <- lmer(DriftRate ~ BDI.z*Emotion + Emotion*BVAQ.z
               +age
               + (1|subj_idx),
               data = data)


Model4 <- lmer(Bias ~ Emotion*BDI.z + Emotion*BVAQ.z
               +age
               + (1|subj_idx),
               data = data)
anova(Model1, Model2, Model3, Model4)


#+ Gender
Model5 <- lmer(DriftRate ~ BDI.z*Emotion + Emotion*BVAQ.z
               +gender
               + (1|subj_idx),
               data = data)


Model6<- lmer(Bias ~ Emotion*BDI.z + Emotion*BVAQ.z
              +gender
              + (1|subj_idx),
              data = data)

anova(Model1,Model2,Model3,Model4,Model5,Model6)


#+age+gender
Model7 <- lmer(DriftRate ~ BDI.z*Emotion + Emotion*BVAQ.z
               +gender
               +age
               + (1|subj_idx),
               data = data)


Model8<- lmer(Bias ~ Emotion*BDI.z + Emotion*BVAQ.z
              +gender
              +age
              + (1|subj_idx),
              data = data)

anova(Model1,Model2,Model3,Model4,Model5,Model6,Model7,Model8)



#Get Statistics
anova(Model7)
anova(Model8, Model7)

summary(Model7)
summary(Model8)

print(Model7, corr=F)
print(Model8, corr=F)

#Plot
interact_plot(Model7,pred=BDI.z, modx=Emotion, modx.labels= c("neutral","sad","happy"), x.label="BDI")
interact_plot(Model7,pred=BVAQ.z, modx=Emotion, modx.labels= c("neutral","sad","happy"), x.label="BVAQ")

interact_plot(Model8,pred=BDI.z, modx=Emotion,modx.labels= c("neutral","sad","happy"), x.label="BDI")
interact_plot(Model8,pred=BVAQ.z, modx=Emotion, modx.labels= c("neutral","sad","happy"), x.label="BVAQ")

