#Model 2 = find effects on drift rate during response if stimulus was happy, sad or neutral


#Load in library
library(lme4)       # mixed, version 1.1-26
library(lmerTest)   # to get p values, version 3.1-3 
library(ggplot2)    # graphics, version 3.3.5
library(interactions) #version 1.1.5
library(tidyverse)  # needed for data manipulation.#needed to view data, version 1.3.1
library(jtools)     # post hoc tests, version 2.1.4
library(readxl)     # read excel, version 1.3.1
library(lme4)      # load mixed model library
library(lmerTest)  # library providing p-values for mixed models in lme4
library(tidyverse) # library with various tools (e.g. ggplot, pivot_long, pipes etc.)
library(emmeans)   # library for post-hoc tests
library(pbkrtest)  # needed for post-hoc tests in mixed models

options('contrasts')

#Use type III analysis of variance
options(contrasts = c("contr.sum", "contr.poly"))



#Load in Dataset
data <- read_excel("C:/Users/juhoffmann/OneDrive - Uniklinik RWTH Aachen/Paper/PilotStudie/Revision/GLMM/GLMM_Model2_3_data.xlsx")

data$DriftRate  <-as.numeric(data$DriftRate)
data$Bias       <-as.numeric(data$Bias)
data$stim       <-data$Emotion

#Transform values
data$stim[data$stim == "neutral"] <- 3
data$stim[data$stim == "sad"]     <- 2
data$stim[data$stim == "happy"]   <- 1


#Factorise variables

data$stim       <- factor(data$stim, ordered = FALSE)                                      
data$subj_idx   <- factor(data$subj_idx, ordered = FALSE)
data$age        <- as.integer(data$age, ordered = TRUE)
data$gender     <- factor(data$gender, ordered = FALSE)  # 1=female
data$BDI_Sum    <- factor(data$BDI_Sum, ordered = TRUE)
data$BVAQ_Sum   <- factor(data$BVAQ_Sum, ordered = TRUE)

data$BVAQ_Sum   <- as.integer(data$BVAQ_Sum)
data$BVAQ.z     <- data$BVAQ_Sum/sd(data$BVAQ_Sum)                                          #z transformation
data$BDI_Sum    <- as.integer(data$BDI_Sum)
data$BDI.z      <- data$BDI_Sum/sd(data$BDI_Sum)                                             #z transformation

data$BDI.z      <- factor(data$BDI.z, ordered = TRUE)
data$BVAQ.z     <- factor(data$BVAQ.z, ordered = TRUE)

#set "neutral" as reference
data$stim                <- relevel(data$stim , ref = "1")

view(data)

summary(data)




# Plot Data
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
abline(0,1)     



#Compare distributions for Drift Rate
x <- data$DriftRate
den <- density(x)
dat <- data.frame(x = den$x, y = den$y)

#Fit distributions
library(fitdistrplus)
fit.weibull <- fitdist(x, "weibull")
fit.normal <- fitdist(x,"norm")
fit.gamma <- fitdist(x, "gamma", lower = c(0, 0))


par(mfrow = c(1, 1)) #show 1 picture
# Compare fits graphically
plot.legend <- c("Weibull", "Gamma","Normal")
denscomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)

# Normal! 






################################ Study 1 #######################################

#remove rows where column 'task' is equal to 2
data_study1<- subset(data, task != 1) 


# Find Model 3 for Drift-Rate #

Model2.1.study1 <- lmer(DriftRate ~ BDI.z + BVAQ.z
              + (1|subj_idx),
              data = data_study1)

Model2.2.study1 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                 + (1|subj_idx),
                 data = data_study1)

anova(Model2.1.study1, Model2.2.study1) #  rescaled is better BUT convergence fail with rescaled values


Model2.3.study1 <- lmer(DriftRate ~ BDI_Sum + BDI_Sum
                 + age
                 + (1|subj_idx),
                 data = data_study1)

Model2.4.study1 <- lmer(DriftRate ~ BDI_Sum + BDI_Sum
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)



anova(Model2.1.study1, Model2.3.study1, Model2.4.study1)
# Model 4 close to significance

Model2.5.study1 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)

anova(Model2.2.study1, Model2.3.study1, Model2.4.study1, Model2.5.study1)


#Model2.5 wins!
Model2.6.study1 <- lmer(DriftRate ~ 
                 + stim*BDI_Sum
                 + stim*BVAQ_Sum
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)

anova(Model2.2.study1, Model2.3.study1, Model2.4.study1, Model2.5.study1, Model2.6.study1)
#Model2.5 wins!



Model2.7.study1 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + (1+gender|subj_idx),
                 data = data_study1)

anova(Model2.2.study1, Model2.3.study1, Model2.4.study1, Model2.5.study1, Model2.6.study1, Model2.7.study1)
#Model2.5 wins!

Model2.5 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)
summary(Model2.5.study1)




# Find Model 3 for Bias #


#Compare distributions for Bias
x <- data$Bias
den <- density(x)
dat <- data.frame(x = den$x, y = den$y)

#Fit distributions
library(fitdistrplus)
fit.weibull <- fitdist(x, "weibull")
fit.normal <- fitdist(x,"norm")
fit.gamma <- fitdist(x, "gamma", lower = c(0, 0))


par(mfrow = c(1, 1)) #show 1 picture

plot.legend <- c("Weibull", "Gamma","Normal")
denscomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)

#Normal



Model3.1.study1 <- lmer(Bias ~ BDI.z + BVAQ.z
                 + (1|subj_idx),
                 data = data_study1)

Model3.2.study1 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + (1|subj_idx),
                 data = data_study1)

anova(Model3.1.study1, Model3.2.study1) # not rescaled is better!


Model3.3.study1 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + age
                 + (1|subj_idx),
                 data = data_study1)

Model3.4.study1 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)

anova(Model3.2.study1, Model3.3.study1, Model3.4.study1)
#Model 3.4 better!

Model3.5.study1 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)

anova(Model3.2.study1, Model3.3.study1, Model3.4.study1, Model3.5.study1)
#Model3.5 wins!


Model3.6.study1 <- lmer(Bias ~ 
                   + stim*BDI_Sum
                 + stim*BVAQ_Sum
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study1)

anova(Model3.2.study1, Model3.3.study1, Model3.4.study1, Model3.5.study1, Model3.6.study1)
#Model3.5 wins!



Model3.7.study1 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + (1+gender|subj_idx),
                 data = data_study1)

anova(Model3.2.study1, Model3.3.study1, Model3.4.study1, Model3.5.study1, Model3.6.study1,Model3.7.study1)
#Model3.5 wins!


summary(Model2.5.study1)
summary(Model3.5.study1)






############################# Study 2 ##########################################


#remove rows where column 'task' is equal to 2
data_study2<- subset(data, task != 1) 


# Find Model 3 for Drift-Rate #

Model2.1.study2 <- lmer(DriftRate ~ BDI.z + BVAQ.z
                        + (1|subj_idx),
                        data = data_study2)

Model2.2.study2 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                        + (1|subj_idx),
                        data = data_study2)

anova(Model2.1.study2, Model2.2.study2) #  rescaled is better BUT convergence fail with rescaled values


Model2.3.study2 <- lmer(DriftRate ~ BDI_Sum + BDI_Sum
                        + age
                        + (1|subj_idx),
                        data = data_study2)

Model2.4.study2 <- lmer(DriftRate ~ BDI_Sum + BDI_Sum
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)



anova(Model2.1.study2, Model2.3.study2, Model2.4.study2)
# Model 4 close to significance

Model2.5.study2 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                        + stim
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)

anova(Model2.2.study2, Model2.3.study2, Model2.4.study2, Model2.5.study2)


#Model2.5 wins!
Model2.6.study2 <- lmer(DriftRate ~ 
                          + stim*BDI_Sum
                        + stim*BVAQ_Sum
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)

anova(Model2.2.study2, Model2.3.study2, Model2.4.study2, Model2.5.study2, Model2.6.study2)
#Model2.5 wins!



Model2.7.study2 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                        + stim
                        + age
                        + (1+gender|subj_idx),
                        data = data_study2)

anova(Model2.2.study2, Model2.3.study2, Model2.4.study2, Model2.5.study2, Model2.6.study2, Model2.7.study2)
#Model2.5 wins!

Model2.5.study2 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data_study2)
summary(Model2.5.study2)




# Find Model 3 for Bias #


#Compare distributions for Bias
x <- data$Bias
den <- density(x)
dat <- data.frame(x = den$x, y = den$y)

#Fit distributions
library(fitdistrplus)
fit.weibull <- fitdist(x, "weibull")
fit.normal <- fitdist(x,"norm")
fit.gamma <- fitdist(x, "gamma", lower = c(0, 0))


par(mfrow = c(1, 1)) #show 1 picture

plot.legend <- c("Weibull", "Gamma","Normal")
denscomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)

#Normal



Model3.1.study2 <- lmer(Bias ~ BDI.z + BVAQ.z
                        + (1|subj_idx),
                        data = data_study2)

Model3.2.study2 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                        + (1|subj_idx),
                        data = data_study2)

anova(Model3.1.study2, Model3.2.study2) # not rescaled is better!


Model3.3.study2 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                        + age
                        + (1|subj_idx),
                        data = data_study2)

Model3.4.study2 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)

anova(Model3.2.study2, Model3.3.study2, Model3.4.study2)
#Model 3.4 better!

Model3.5.study2 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                        + stim
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)

anova(Model3.2.study2, Model3.3.study2, Model3.4.study2, Model3.5.study2)
#Model3.5 wins!


Model3.6.study2 <- lmer(Bias ~ 
                          + stim*BDI_Sum
                        + stim*BVAQ_Sum
                        + age
                        + gender
                        + (1|subj_idx),
                        data = data_study2)

anova(Model3.2.study2, Model3.3.study2, Model3.4.study2, Model3.5.study2, Model3.6.study2)
#Model3.5 wins!



Model3.7.study2 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                        + stim
                        + age
                        + (1+gender|subj_idx),
                        data = data_study2)

anova(Model3.2.study2, Model3.3.study2, Model3.4.study2, Model3.5.study2, Model3.6.study2,Model3.7.study2)
#Model3.5 wins!


summary(Model2.5.study2)
summary(Model3.5.study2)



################## Study 1 + 2 ################## ################## ###########




Model2.5 <- lmer(DriftRate ~ BDI_Sum + BVAQ_Sum
                        + stim
                        + age
                        + gender
                        + task
                        + (1|subj_idx),
                        data = data)


Model3.5 <- lmer(Bias ~ BDI_Sum + BVAQ_Sum
                 + stim
                 + age
                 + gender
                 + task
                 + (1|subj_idx),
                 data = data)

summary(Model2.5)
summary(Model3.5)

anova (Model2.5, Model3.5)
