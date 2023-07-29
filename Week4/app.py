from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)

app.secret_key = "any string but secret"

#*處理index
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

#*處理sign in
@app.route("/signin", methods=["POST"])
def signin():
    #* 取得html中資料
    username = request.form["username"]
    password = request.form["password"] 

    session["signed_in"]=True
    session["username"] = username
    #* 驗證身分
    if username=="" or password == "":
        return redirect("/error?message=帳號或密碼空白")
    
    if username == "test" and password == "test":
        # *如果成功了就會到會員頁面
        return redirect("/member")
    else:
        #* 如果不成功就會
        return redirect("/error?message=帳號或密碼錯誤")



@app.route("/member", methods=["GET"])
def member():
    if not session.get("signed_in"):
        return redirect("/")
    #username = session.get("username")
    return render_template("member.html")

@app.route("/signout", methods=["GET"])
def signout():
    session["signed_in"]=False
    return redirect("/")

@app.route("/error", methods=["GET"])
def error():
    message = request.args.get("message")
    return render_template("error.html", message=f"{message}")

#*啟動網站伺服器
app.run(port=3000)