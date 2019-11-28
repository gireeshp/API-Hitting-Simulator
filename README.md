### API-Hitting-Simulator

This is a simple simulator engine which can be used to hit a URL 'x' number of times with 'y' parallel hits. It shows the completed hits, current parallel attempts & the pending attempts.   


## Initial setup:
```
(base) K8-Auto-Scaling-Demo$ conda create -n k8-auto-scale-demo python=3.7 anaconda
(base) K8-Auto-Scaling-Demo$ conda activate k8-auto-scale-demo
(k8-auto-scale-demo) K8-Auto-Scaling-Demo$ conda install -c anaconda flask
(k8-auto-scale-demo) K8-Auto-Scaling-Demo$ conda install requests
```

## Run the app:
```
(k8-auto-scale-demo) K8-Auto-Scaling-Demo$ export FLASK_APP=api.py 
(k8-auto-scale-demo) K8-Auto-Scaling-Demo$ export FLASK_ENV=development
(k8-auto-scale-demo) K8-Auto-Scaling-Demo$ flask run
 * Serving Flask app "api.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 240-336-825
```


