from flask import Flask, redirect, render_template, request, url_for
import joblib
#import numpy as np
app = Flask(__name__)
solve = joblib.load('model')


@app.route('/', methods=['POST','GET'])
def home():
    eo = ''
    inp = ['post', 'const','approve','type','bhk','area','rtm','resale','long','lati']
    if request.method == 'POST' and (inp for inp in request.form):
        Post = float(request.form.get(inp[0]))
        Construction = float(request.form.get(inp[1]))
        Approval = float(request.form.get(inp[2]))
        Type = float(request.form.get(inp[3]))
        NoOfBHK = float(request.form.get(inp[4]))
        Area = float(request.form.get(inp[5]))
        RTM = float(request.form.get(inp[6]))
        Resale = float(request.form.get(inp[7]))
        Longitude = float(request.form.get(inp[8]))
        Latitude = float(request.form.get(inp[9]))
        m = [[Post,Construction,Approval,Type,NoOfBHK,Area,RTM,Resale,Longitude,Latitude]]
        eo = solve.predict(m)
    return render_template('index.html',eo = eo)

if __name__ == '__main__':
    app.run(debug=True)
