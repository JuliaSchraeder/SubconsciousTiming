#Load in library
library(lme4) # mixed
library(lmerTest) #to get p values
library(ggplot2) # graphics
library(interactions) 
library(tidyverse) # needed for data manipulation.#needed to view data
library(jtools)  # post hoc tests

#Load in dataset
data <- read.csv("/Users/juhoffmann/OneDrive - Uniklinik RWTH Aachen/Auswertung/Pilot2/GLMM/hddm_data.csv", sep=",")

#Remove missing values and additional column
data$X <- NULL
data <-data[complete.cases(data), ]
View(data)


data$correct[data$correct == "0"] <- 2
# Define variables
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



Model <- glmer(correct ~  stim + level + response
               + real_trial_number.z 
               + (1+real_trial_number.z|subj_idx),
               data = data,
               family=Gamma(link="inverse"))

Model_Block <- glmer(correct ~  stim + level + response
                     + block
                     + real_trial_number.z 
                     + (1+real_trial_number.z|subj_idx),
                     data = data,
                     family=Gamma(link="inverse"))


anova(Model, Model_Block)
#Get statistics

anova(Model_Block)
summary (Model_Block)
dotplot(ranef(Model_Block, condVar=TRUE))

plot(Model_Block)

#Plot interaction 
interact_plot(Model_Block,pred=response, modx=stim, mod2=level)
#Plot interaction 
interact_plot(Model_Block,pred=response, modx=stim, mod2=block)



print(Model, corr=F)
