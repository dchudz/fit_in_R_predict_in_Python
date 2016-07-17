library(caret)
library(jsonlite)
args = commandArgs(trailingOnly=TRUE)
path_to_model <- args[1]
json_to_predict <- args[2]
path_to_prediction <- args[3]
fitted <- readRDS(path_to_model)
df_to_predict <- jsonlite::fromJSON(json_to_predict)

prediction <- predict(fitted, df_to_predict)
write(prediction, file=path_to_prediction)
