from flask import Flask,render_template,redirect,url_for,request
user={'b@gmail.com':123}
def check(uname,upass):
    if uname in user and user[uname]==upass:
        return True
    else:
        return False
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="GET":
        return render_template("J1.html")
@app.route('/login',methods=["GET"])
def login():
    if request.method=="POST":
        un=request.form['email']
        ps1=request.form['pwd']
      
        if check(un,int(ps1)):
            return render_template("ins.html",email=un,pwd=ps1)
        else:
            return "invalid"
    if request.method=="GET":
        return render_template("jlogin.html")


if __name__=="__main__" :
    app.run(debug=True)