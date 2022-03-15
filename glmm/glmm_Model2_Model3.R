#Model 2 = find effects on drift rate during response in rating the emotional face
#Model 3 = find effects on bias during response in rating the emotional face

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

options('contrasts')

#Use type III analysis of variance
options(contrasts = c("contr.sum", "contr.poly"))

#Load in Dataset
data <- read_excel("/GLMM_Model2_3_data.xlsx")

data$DriftRate  <-as.numeric(data$DriftRate)
data$Bias       <-as.numeric(data$Bias)
data$stim       <- data$Emotion

#Transform values
data$stim[data$stim == "neutral"] <- 3
data$stim[data$stim == "sad"]     <- 2
data$stim[data$stim == "happy"]   <- 1

#Factorise variables
data$stim       <- factor(data$stim, ordered = FALSE)                                      
data$subj_idx   <- factor(data$subj_idx, ordered = FALSE)
data$age        <- as.integer(data$age, ordered = TRUE)
data$gender     <- factor(data$gender, ordered = FALSE)  
data$BDI        <- factor(data$BDI, ordered = TRUE)
data$BVAQ       <- factor(data$BVAQ, ordered = TRUE)

#z-transform
data$BVAQ       <- as.integer(data$BVAQ)
data$BVAQ.z     <- data$BVAQ/sd(data$BVAQ)                                          
data$BDI        <- as.integer(data$BDI)
data$BDI.z      <- data$BDI/sd(data$BDI)                                           

data$BDI.z      <- factor(data$BDI.z, ordered = TRUE)
data$BVAQ.z     <- factor(data$BVAQ.z, ordered = TRUE)

view(data)
summary(data)




############################ Plot Data #########################################
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

# Chose normal distribution 





############################ Find Model 3 for Drift-Rate #######################

Model2.1 <- lmer(DriftRate ~ BDI.z + BVAQ.z
              + (1|subj_idx),
              data = data)

Model2.2 <- lmer(DriftRate ~ BDI + BVAQ
                 + (1|subj_idx),
                 data = data)

anova(Model2.1, Model2.2) # no difference if Questionnaires are rescaled!

#increase fixed effects
Model2.3 <- lmer(DriftRate ~ BDI + BVAQ
                 + age
                 + (1|subj_idx),
                 data = data)

Model2.4 <- lmer(DriftRate ~ BDI + BVAQ
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model2.2, Model2.3, Model2.4)
# Model 4 close to significance

Model2.5 <- lmer(DriftRate ~ BDI + BVAQ
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model2.2, Model2.3, Model2.4, Model2.5)
#Model2.5 wins!

Model2.6 <- lmer(DriftRate ~ 
                 + stim*BDI
                 + stim*BVAQ
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model2.2, Model2.3, Model2.4, Model2.5, Model2.6)
#Model2.5 wins!

Model2.7 <- lmer(DriftRate ~ BDI + BVAQ
                 + stim
                 + age
                 + (1+gender|subj_idx),
                 data = data)

anova(Model2.2, Model2.3, Model2.4, Model2.5, Model2.6, Model2.7)
#Model2.5 wins!

Model2.5 <- lmer(DriftRate ~ BDI + BVAQ
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)
summary(Model2.5)

############################ Find Model 3 for Bias #############################


Model3.1 <- lmer(Bias ~ BDI.z + BVAQ.z
                 + (1|subj_idx),
                 data = data)

Model3.2 <- lmer(Bias ~ BDI + BVAQ
                 + (1|subj_idx),
                 data = data)

anova(Model3.1, Model3.2) # no difference if Questionnaires are rescaled!


Model3.3 <- lmer(Bias ~ BDI + BVAQ
                 + age
                 + (1|subj_idx),
                 data = data)

Model3.4 <- lmer(Bias ~ BDI + BVAQ
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model3.2, Model3.3, Model3.4)
#Model 3.4 better!

Model3.5 <- lmer(Bias ~ BDI + BVAQ
                 + stim
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model3.2, Model3.3, Model3.4, Model3.5)
#Model3.5 wins!

Model3.6 <- lmer(Bias ~ 
                   + stim*BDI
                 + stim*BVAQ
                 + age
                 + gender
                 + (1|subj_idx),
                 data = data)

anova(Model3.2, Model3.3, Model3.4, Model3.5, Model3.6)
#Model3.5 wins!

Model3.7 <- lmer(Bias ~ BDI + BVAQ
                 + stim
                 + age
                 + (1+gender|subj_idx),
                 data = data)

anova(Model3.2, Model3.3, Model3.4, Model3.5, Model3.6,Model3.7)
#Model3.5 wins!

summary(Model3.5)
