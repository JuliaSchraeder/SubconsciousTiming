#Load in library
library(lme4) # mixed
library(lmerTest) #to get p values
library(ggplot2) # graphics
library(interactions) 
library(tidyverse) # needed for data manipulation.#needed to view data
library(jtools)  # post hoc tests


################## Trial-by-Trial Analysis with correct/incorrectness of response as dependent variable to find Model1


#Load in dataset
data <- read.csv("C:/Users/juhoffmann/OneDrive - Uniklinik RWTH Aachen/Auswertung/Pilot2/GLMM/GLMM_Model1_data.csv", sep=",")

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
data$response <-as.numeric(data$response)

#Transform trail numbers
data$real_trial_number <- as.integer(data$real_trial_number)
data$real_trial_number.z <- data$real_trial_number/sd(data$real_trial_number) # z transformation

view(data)




#Model selection:
Model1 <- glmer(correct ~  stim + level
                + (1|subj_idx),
                data = data,
                family=Gamma(link="inverse"))
# include trial number
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
Model4 <- glmer(correct ~  stim + level + response
               + real_trial_number.z 
               + (1+real_trial_number.z|subj_idx),
               data = data,
               family=Gamma(link="inverse"))
anova(Model1,Model2,Model3,Model4)


#Get Statistics:
anova(Model4)
summary (Model4)
print(Model4, corr=F)

#Plot
interact_plot(Model4,pred=response, modx=stim, mod2=level)




##################  Analysis of mean accuracy and Questionnaire Results to find Model2

#Load in dataset
data2<- read_excel("C:/Users/juhoffmann/OneDrive - Uniklinik RWTH Aachen/Auswertung/Pilot2/GLMM/GLMM_Model2_data.xlsx")

#Remove missing values and additional column
data2$X <- NULL
data2 <-data2[complete.cases(data2), ]
View(data2)


# Define variables
data2$subj_idx<- as.factor(data2$subj_idx)
#data2$Age<- as.factor(data2$Age)
#data2$Sex<- as.factor(data2$Sex)
data2$TMT <- (data2$TMT_A+data2$TMT_B)/2 #Mean TMT Results from A and B as variable "TMT"
TMT <- standardize(data2$TMT)
BDI <- standardize(data2$ScoreBDI)
BVAQ <- standardize(data2$ScoreBVAQ_B)
View(data2)


#Include all Questionnaire Results
Model9 <- glmer (accuracy ~ TMT + BDI + BVAQ + Sex
                 + (1|subj_idx),
                 data=data2,
                 family = Gamma(link = "inverse"))

summary(Model9)

print(Model9, corr=F)

#Plot
interact_plot(Model9,pred=TMT,modx=Sex)
interact_plot(Model9,pred=BDI,modx=Sex)
interact_plot(Model9,pred=BVAQ,modx=Sex)
