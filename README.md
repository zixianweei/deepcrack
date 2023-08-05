<div align=center>
  <h1>deepcrack</h1>
</div>

## Note

Thanks for qinnzou's code, pretrained-models, and datasets. This repository is forked from qinnzou's deepcrack. If you are interested in the work, please cite his work. You can find his repo by this [link](https://github.com/qinnzou/DeepCrack).

My work is very simple. I wrote a Python script, which can generate a pytorch-jit-model, so that it can be loaded using LibTorch. Here is the script: [export.py](./export.py)

## Usage

If you want to have a try, please follow these steps:

```shell
# Create a conda virtual environment
conda create env -n deepcrack python=3.7
# Install dependencies using pip
pip install -r requirements.txt
# Download qinnzou's pretained-model or you own model, and put it in checkpoints directory.
# Modify the export.py, so that it can find the model.
# Run export.py script.
python export.py
```
