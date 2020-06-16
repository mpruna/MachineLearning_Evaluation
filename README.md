### Machine Learning scorring

Most common **Machine-Learning** scoring metrics/KPI.

Created sysntetic data points using numpy. First I created a 2D line, then added noise:

```
x = np.linspace(0, 100, 50)
y = 2*x + 1

noise = np.random.normal(0, 7, y.shape)
y_2 = y + noise
```

### Machine-Learning errors

![IMG](errors_subplots.png)

Github project structure

```
├── environment.yml
├── eval_error.py
├── linear_regression.ipynb
├── plotly_linear_model.ipynb
└── README.md
```

### Description

* environment.yml contains the project specifications
* eval_error.py python script calculates the errors   
* .ipynb are two jupyter-notebooks mostly used for graphing


References:  
* https://docs.scipy.org/doc/numpy-1.13.0/user/basics.creation.html
* https://pythonbasics.org/matplotlib-line-chart/
* https://stackoverflow.com/questions/14058340/adding-noise-to-a-signal-in-python#14058425
