import rpy2.robjects as ro
from rpy2.robjects import r
import json
from pandas.rpy.common import convert_to_r_dataframe
import pandas as pd

fitted_model = r.readRDS("models/model1.RDS")

# (in real life maybe the json comes from the front end):
json_to_predict = '[{"carat":0.23,"cut":"Ideal","color":"E","clarity":"SI2"}]'

# Method 1: convert pandas data frame to R data frame
to_predict_dict = json.loads(json_to_predict)
to_predict_pandas_df = pd.DataFrame(to_predict_dict)
to_predict_R_df = convert_to_r_dataframe(to_predict_pandas_df)

# Make predictons
[prediction] = r.predict(fitted_model, to_predict_R_df)
print("Prediction from pandas DF is %f" % prediction)


# Method 2: Send the JSON to R, convert to dataframe in R
jsonlite = ro.packages.importr("jsonlite")

# This gets you an R dataframe (a bit of a weird default for a fromJSON function, but alas):
to_predict_R_df_from_json = jsonlite.fromJSON(json_to_predict)

# Make predictions
[prediction] = r.predict(fitted_model, to_predict_R_df_from_json)
print("Prediction from JSON is %f" % prediction)
