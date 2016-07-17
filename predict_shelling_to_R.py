import subprocess
import tempfile

rscript_path = "predict_from_json.R"
json_to_predict = '[{"carat":0.23,"cut":"Ideal","color":"E","clarity":"SI2"}]'
path_to_model = "models/model1.RDS"

with tempfile.NamedTemporaryFile() as tf: # Using a tempfile is a bit hacky
    command_list = ["Rscript", rscript_path, path_to_model, "'" + json_to_predict + "'", tf.name]
    joined_command = " ".join(command_list)
    subprocess.getoutput(joined_command) # This is hacky but had some troubles with subprocess.call on command_list
    [prediction_string] = tf.read().splitlines()

print("The prediction is: %f" % float(prediction_string))
