# Fitting in R, Predicting in Python

This demonstrates making predictions in Python for models fitted in R in a few different ways. In all cases it's actually R making the predictions (it's never Python code running the model).

Fit the model: `Rscript fit.R` (the fitted model is included, so this isn't necessary).

Predictions:

## With Rpy2 (`predict_with_Rpy2.py`)

To try it: `python predict_with_Rpy2.py`

## Without Rpy2 (`predict_shelling_to_R.py`)

To try it: `python predict_shelling_to_R.py`

To try the R script that this is calling: `Rscript predict_from_json.R models/model1.RDS '[{"carat":0.23,"cut":"Ideal","color":"E","clarity":"SI2"}]' temp.txt` (prediction goes to `temp.txt`)
