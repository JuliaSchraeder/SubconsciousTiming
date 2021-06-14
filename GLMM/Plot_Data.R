# libraries laden
library(nlme)
library(lme4) # mixed
library(jtools)  # post hoc tests
library(ggplot2) # graphics
library(lattice) #graphics
library(interactions)
library(ggeffects)
library(emmeans)
library(piecewiseSEM)
library(tidyverse) # needed for data manipulation.
library(RColorBrewer) # needed for some extra colours in one of the graphs
library(lmerTest)# to get p-value estimations that are not part of the standard lme4 packages
library(arm)
library(MASS) # v7.3-50 #need to fit densities
library(car) # v3.0-2
library(mlmRev) # v1.0-6
library(agridat) # v1.16
library(MCMCglmm) # v2.26

#Load in dataset
data <- read.csv()


View(data)

#Remove missing values and additional column
data$X <- NULL
data <-data[complete.cases(data), ]
View(data)

#Plot Density
plot(density(data$rt),main="Density estimate of data")

x <- data$rt
den <- density(x)
dat <- data.frame(x = den$x, y = den$y)

#Fit distributions
library(fitdistrplus)
fit.weibull <- fitdist(x, "weibull")
fit.normal <- fitdist(x,"norm")
fit.gamma <- fitdist(x, "gamma", lower = c(0, 0))
#fit.poisson <- fitdist(x, "pois")
fit.negBin <- fitdistr(x,"negative binomial")

# Compare fits graphically
plot.legend <- c("Weibull", "Gamma","Normal")
par(mfrow = c(2, 2)) #show 4 pictures
denscomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)
qqcomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)
cdfcomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)
ppcomp(list(fit.weibull, fit.gamma, fit.normal), fitcol = c("red", "blue","green"), legendtext = plot.legend)


###### try fit Poisson 
#install.packages('vcd')
#library(vcd)
#fitp <- goodfit(x, "poisson")
#plot(fitp)

### qq Plots ###
# Plot Data
data$rt.t <- data$rt + 1
qqp(data$rt, "norm")
qqp(data$rt, "lnorm")

#PlotQQ Plot normaldist
z.norm<-(data$rt-mean(data$rt))/sd(data$rt) ## standardized data
qqnorm(z.norm) ## drawing the QQplot
abline(0,1) ## drawing a 45-degree reference line

#nbinom <- fitdistr(data$rt, "negative binomial")
#qqp(data$rt, "nbinom", size = nbinom$estimate[[1]], mu = nbinom$estimate[[2]])

poisson <- fitdistr(data$rt, "Poisson")
qqp(data$rt, "pois", lambda = poisson$estimate)

gamma <- fitdistr(data$rt, "gamma")
qqp(data$rt, "gamma", shape = gamma$estimate[[1]], rate = gamma$estimate[[2]])



#poisson looks like this
x.poi<-rpois(n=200,lambda=2.5)
hist(x.poi,main="Poisson distribution looks like this")
#gamma looks like this 
curve(dgamma(x, scale=1.5, shape=2),from=0, to=15, main="Gamma distribution looks like this")



############### Plot Reaction Time Data   ###############
#RT in Abhängigkeit von Stimulus und Response
ggplot(data  = data,
       aes(x = stim,
           y = rt,
           col = response,
           group = response))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. stimulus and response")



#RT in Abhängigkeit von Stimulus und Anzeigedauer (Level)
data$level <- factor(data$level)   
ggplot(data  = data,
       aes(x = stim,
           y = rt,
           col = level,
           group = level))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. stimulus and level")


#RT in Abhängigkeit von Response und Anzeigedauer (Level)
ggplot(data  = data,
       aes(x = response,
           y = rt,
           col = level,
           group = level))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. stimulus and level")



#RT in Abhängigkeit von trial Nummer und Stimulus 
data$real_trial_number <- numeric(data$real_trial_number) 

ggplot(data  = data,
       aes(x = real_trial_number,
           y = rt,
           col = stim,
           group = stim))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+ #stack
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. Trialnumber and Stimulus")


#RT in Abhängigkeit von trial Nummer mit bewusster Anzeigedauer (141ms) und Response 
data_conscious <- data[data$level=="141ms", ]
head(data_conscious)

ggplot(data  = data_conscious,
       aes(x = real_trial_number,
           y = rt,
           col = response,
           group = response))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. conscious trials and response")


#RT in Abhängigkeit von trial Nummer mit bewusster Anzeigedauer (141ms) und Stimulus 
ggplot(data  = data_conscious,
       aes(x = real_trial_number,
           y = rt,
           col = stim,
           group = stim))+ #to add the colours for different responses))+
  geom_point(size = 1.2,
             alpha = .8,
             position = "jitter")+
  theme_minimal()+
  geom_smooth(method = lm,
              se     = FALSE,
              size   = 1.5, 
              alpha  = .8)+ # to add regression line
  labs(title = "Reaction time vs. conscious trials and stimulus")
