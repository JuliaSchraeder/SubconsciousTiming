#Load in library
library(lme4) # mixed
library(lmerTest) #to get p values
library(ggplot2) # graphics
library(interactions) 
library(tidyverse) # needed for data manipulation.#needed to view data
library(jtools)  # post hoc tests
#Load in dataset
data <- read.csv("/Users/julia/OneDrive - Uniklinik RWTH Aachen/Auswertung/Pilot2/GLMM/hddm_analyses_data.csv", sep=",")

#Remove missing values
data <-data[complete.cases(data), ]
view(data)

#Redefine data

data$response[data$response == "sad"] <- 1
data$response[data$response == "neutral"] <- 2
data$response[data$response == "happy"] <- 3


# Define variables
data$level <- as.factor(data$level)                                          
data$stim <- as.factor(data$stim)
data$subj_idx <- as.factor(data$subj_idx)
data$block <- as.factor(data$block)
data$response <- as.factor(data$response)
data$rt <- as.integer(data$rt)


#Transform trail numbers
data$real_trial_number <- as.integer(data$real_trial_number)
data$real_trial_number.z <- data$real_trial_number/sd(data$real_trial_number) # z transformation


model1 <- glmer(rt ~  stim + level + response 
                + real_trial_number.z 
                + block 
                + stim:response 
                + (1+real_trial_number.z|subj_idx) 
                + (1|real_trial_number.z),
                data = data,
                family = "poisson") 

model2 <- glmer(rt ~  stim + level + response 
               + real_trial_number.z 
               + block 
               + stim:response 
               + (1+real_trial_number.z|subj_idx),
               data = data,
               family = "poisson") 

model3 <- glmer(rt ~  stim + level + response 
                + stim:response 
                + (1|subj_idx),
                data=data,
                family = "poisson")

anova(model1,model2,model3)


model4 <- glmer(rt ~  stim + level 
                + stim:response 
                + (1|subj_idx),
                data=data,
                family = "poisson")

        
anova(model1,model2,model3,model4)              
                
#Get statistics
model1
anova(model1)
summary (model1)
dotplot(ranef(model1, condVar=TRUE))

plot(model1)

#Plot interaction 
interact_plot(model1,pred=response,modx=stim, mod2=level)
interact_plot(model1,pred=response,modx=stim, mod2=block)


lsm <-ls_means(model1)
res <- plot(lsm, mult=FALSE)
plot(res[[1]])


print(model1, corr=F)
