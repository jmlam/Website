from flask import Flask #importing flask class object

app=Flask(__name__) #instantiating flask object. __name__ gets value of the name of the python script
#when a script is run the script is given the name __main__
#when a script is imported the script is given the name of the file (here it is "script")


@app.route('/') #this signifies stage in the path. currently this is the home page, or just the beginning. 
def home():
    return 'Homepage goes here!'

@app.route('/Portfolio/')
def portfolio():
    return 'Look at my work!'


if __name__ == "__main__":  #if we are executing from the main script then the app will run. but if it is imported then the app will not run
    app.run(debug=True)     #the app will update if we add things without having to restart the script.

