# USC_LBA_estimator

## Overview
Run ONNX inference on `.mgz` brain volumes using [main.py](main.py). The script loads a CSV (for metadata), scans a directory for `.mgz` files, and saves predictions as `.npy` files.

## Quick Start
1) Place your inputs:
- `.mgz` files in `./data/`

## Requirements
- Python 3.8+
- Dependencies used by [inference.py](inference.py): `onnx`, `onnxruntime`, `torch`, `numpy`, `scipy`, `nibabel`, `pandas`
2) Install dependencies in a virtual environment:
Linux/Mac:
```
python -m venv venv
source venv/bin/activate 
bash pip install --upgrade pip
pip install -r requirements.txt
```

Windows:
```
python -m pip install --upgrade pip
python -m venv .lbavenv 
.venv\Scripts\activate.bat
pip install -r requirements.txt
```




3) Run:
```bash
python main.py
```

4) Outputs:
- `.npy` prediction files in `./outFiles/`

## Configure Inputs
Edit the paths in [main.py](main.py):

```python
csvFileLoc = r"./data/ages.csv"
brainsDir = r"./data/"
saveFlag = True
saveLoc = r"./outFiles/"
```

## Optional: Run Inference Directly
[inference.py](inference.py) also exposes a CLI. Example:

```bash
python inference.py --brains-dir ./data/ --save-flag true --save-loc ./outFiles/ --model-path LBAmodel.onnx
```

utils.py contains helper functions for loading `.mgz` files and visualizing brain volumes. You can import and use these in your own scripts or notebooks.
plot3Views function in utils.py:
- Extracts three slices: axial (`z`), sagittal (`x`), and coronal (`y`).
- Plots them side-by-side with colorbars.
