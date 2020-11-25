from flask import Flask, render_template, make_response, abort

#Prints a success message after the POST is successfully made.
#Refer to swagger.yml to see when this runs
def function():
    print("We've got a talking API!")
    return "200"