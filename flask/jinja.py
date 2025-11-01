### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this Flask world</h1></html>"

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



#Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html',results = res)

#for loop
@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {'score':score,'result':res}
    return render_template('result1.html',results = exp)

#if condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result2.html',results = score)

#Variable Rule
@app.route("/fail/<int:score>")
def fail(score):

    return render_template('result.html',results = score)

@app.route("/submit",methods = ['GET','POST'])
def submit():
    total_score = 0
    if request.method =="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['maths'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4

    else:
        return render_template('getresult.html')

    return redirect(url_for('successres',score = total_score))

if __name__=="__main__":
    app.run(debug = True)

