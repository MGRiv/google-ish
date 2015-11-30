from flask import Flask, render_template, session, request, redirect, url_for
import utils

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "POST" and request.form.get('query') != "":
        q = request.form.get('query')
        return redirect(url_for("answer",query=q))
    else:
        return render_template("home.html")

@app.route("/answer",methods=["GET","POST"])
@app.route("/answer/<query>",methods=["GET","POST"])
def answer(query):
    s = utils.getQuery(query)
    return render_template("answer.html",ans=s)

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
