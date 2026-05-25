from flask import Flask,render_template,request,url_for,redirect,jsonify


## craete flask application

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return f"<h1>welcome to the home page</h1>"

@app.route("/index",methods=["GET"])
def index():
    return f"This is index page"


@app.route("/success/<score>",methods=["GET"])
def success(score):
    return f"The parson has passed and the score is: {score}"

## Variable rules with string: <string:score>
@app.route("/fail/<score>",methods=["GET"])
def fail(score):
    return f"The person has failed and score is: {score}"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    elif request.method=="POST":
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        english = float(request.form["english"])
        average = (maths + science + english) / 3
        if average >= 50:
            return redirect(url_for("success", score=average))
        else:
            return redirect(url_for("fail", score=average))
        
@app.route("/api",methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val= float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)

if __name__=="__main__":
    app.run(debug=True)
