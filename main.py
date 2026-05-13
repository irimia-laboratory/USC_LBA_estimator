import pandas as pd

from inference import run_inference

# User-configurable inputs
csvFileLoc = r"./data/ages.csv"
brainsDir = r"./data/"

# Load metadata if needed for downstream use
data_df = pd.read_csv(csvFileLoc)

saveFlag = True  # save predictions as csv
saveLoc = r"./outFiles/"

# Execute inference using explicit arguments
_ = data_df
run_inference(
    brains_dir=brainsDir,
    save_flag=saveFlag,
    save_loc=saveLoc,
)
