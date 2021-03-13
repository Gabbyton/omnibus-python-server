# Omnibus Python Server
Flask development server for the Omnibus shuttle tracking app

## First time deployment

To deploy this app, clone this repository and run the module:

1. We recommend starting a virtual environment for development. You can find a great tutorial [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
2. Install the dependencies for this application. We use pip for dependency management. In the root folder, enter the following command to install all required packages:

```
pip install -r dependencies.txt
```
3. In the root folder, enter the following command in the terminal:

```
python3 -m omnibus
```

4. The terminal should now give you the ominous WSGI warning:
```
* Serving Flask app "omnibus.server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5003/ (Press CTRL+C to quit)
 ```

5. For subsequent deployments, just run the module as indicated in step 3.
