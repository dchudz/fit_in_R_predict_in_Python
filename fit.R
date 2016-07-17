library(randomForest)
library(ggplot2) # ("diamonds" dataset comes from ggplot2)
library(caret)

set.seed(0)
diamonds_small <- diamonds[1:300,] # Didn't want to wait for training so I used a small dataset
fitted <- caret::train(price ~ carat + cut + color + clarity, data=diamonds_small,
								 method = "rf")
saveRDS(fitted, "models/model1.RDS")

