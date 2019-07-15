from flask import Flask, render_template 
app = Flask(__name__)    






@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard_88():
    
    
    return render_template('index.html')






app.run(debug=True)    # Run the app in debug mode.
