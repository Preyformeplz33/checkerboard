from flask import Flask, render_template
from check import color
app = Flask(__name__)

@app.route('/')
def color(x,y):
    result = color(2,2)
    return render_template("index.html",result=result)
    
if __name__=="__main__":


    app.run(debug=True)