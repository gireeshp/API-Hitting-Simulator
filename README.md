### Kubernetes auto scaling demo

This is a simple simulator engine which can be used to hit a URL 'x' number of times with 'y' parallel hits. It shows the completed hits, current parallel attempts & the pending attempts.   


## Initial setup:
```
(base) API-Hitting-Simulator$ conda create -n simulator python=3.7 anaconda
(base) API-Hitting-Simulator$ conda activate simulator
(simulator) API-Hitting-Simulator$ conda install -c anaconda flask
(simulator) API-Hitting-Simulator$ conda install requests
```

## Run the app:
```
(simulator) API-Hitting-Simulator$ export FLASK_APP=api.py 
(simulator) API-Hitting-Simulator$ export FLASK_ENV=development
(simulator) API-Hitting-Simulator$ flask run
 * Serving Flask app "api.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 240-336-825
```


