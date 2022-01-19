# import the dependency we need
from flask import Flask

# Create a New Flask App Instance
# nstance" is a general term in programming to refer to a singular version of something.
# Add the following to your code to create a new Flask instance called app:

app = Flask(__name__)

# This __name__ variable denotes the name of the current function. You can use the __name__ variable to determine
# if your code is being run from the command line or if it has been imported into another piece of code.
# Variables with underscores before and after them are called magic methods in Python.

# Create Flask Routes
# First, we need to define the starting point, also known as the root. To do this, we'll use the function
# @app.route('/').
# the forward slash inside of the app.route? This denotes that we want to put our data at the root of our routes.
# The forward slash is commonly known as the highest level of hierarchy in any computer system.

# Next, create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in
# # that specific route below @app.route()
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our
# code. You should save this code in the same folder you've used in the rest of this module.
