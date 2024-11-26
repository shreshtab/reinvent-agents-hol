# Getting Started with Python

This baseline project shows how to get the most out of [Python](http://ipython.org)
on Cloudera Data Science Workbench.

## Files

Modify the default files to get started with your own project.

* `README.md` -- This project's readme in Markdown format.
* `analysis.py` -- An example Python analysis script.
* `requirements.txt` -- Dependencies that need to be manually installed if you
  are running analysis.py in ML Runtimes (not necessary if you are using Legacy
  Engines).
* `cdsw-build.sh` -- A custom build script used for models and experiments. This
will pip install our dependencies, primarily the scikit-learn library.
* `fit.py` -- A model training example to be run as an experiment. Generates the
model.pkl file that contains the fitted parameters of our model.
* `predict.py` --  A sample function to be deployed as a model. Uses `model.pkl`
produced by `fit.py` to make predictions about petal width.

## Instructions for Sessions
1. Click "Open Workbench".
2. Launch a new Python session.
3. Run `analysis.py` in the workbench.

## Instructions for Experiments and Models
1. Click "Open Workbench".
2. Run an experiment with `fit.py` as the input script.
3. Once the experiment is complete, save the `model.pkl` file to the project.
4. Deploy a model using `predict.py`. Specify `predict` as the input function.

For detailed instructions on how to run these scripts, see the [documentation](https://docs.cloudera.com/machine-learning/cloud/models/topics/ml-creating-and-deploying-a-model.html).
