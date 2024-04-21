import pymongo
import certifi
import tkinter as tk
from tkinter import messagebox
from bson.objectid import ObjectId
import config
from flask import Flask
from flask import render_template,request,jsonify,session, url_for
from werkzeug.wrappers import Response
import json
from jinja2 import Markup
from bson.binary import Binary
import gridfs
import base64
import os
from flask_mail import Mail, Message
from datetime import datetime, date



root = tk.Tk()
root.withdraw()

client = pymongo.MongoClient("mongodb+srv://hsieh20020823:boos7712031@cluster0.lfqqncs.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())

db = client.member_system #選擇操作 member_system 資料庫

print("資料庫連結建立成功")

from flask import *
app=Flask(
    __name__
    #static_folder="public",
    #static_url_path="/"
)
app.secret_key="any string but secret"
app.config.from_object(config)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
UPLOAD_FOLDER = 'uploads'  
app.config['static/images/'] = UPLOAD_FOLDER

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'a0989600553@gmail.com'
app.config['MAIL_PASSWORD'] = 'kech mrix qzhz zrro'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


#處理路由
@app.route("/")
def index():
    return render_template("index3.html")

@app.route("/product",methods=["GET"])
def product():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find()
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("product.html",products=products)
    else:
        return render_template("/")
        

@app.route("/IMproduct",methods=["GET"])
def IMproduct():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "資管系"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("IM.html",products=products)
    else:
        return render_template("/")
    
@app.route("/LAW",methods=["GET"])
def LAW():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "法律系"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("LAW.html",products=products)
    else:
        return render_template("/")
    
@app.route("/LibEdu",methods=["GET"])
def LibEdu():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "通識課程"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("LibEdu.html",products=products)
    else:
        return render_template("/")
    
@app.route("/Fin",methods=["GET"])
def Fin():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "財管系"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("Fin.html",products=products)
    else:
        return render_template("/")
    
@app.route("/logistics",methods=["GET"])
def logistics():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "運籌系"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("logistics.html",products=products)
    else:
        return render_template("/")
    
@app.route("/other",methods=["GET"])
def other():
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"producttype": "其他"}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("other.html",products=products)
    else:
        return render_template("/")


@app.route("/caption")
def caption():
    if "nickname" in session:
        return render_template("caption.html")
    else:
        return render_template("/")
    

@app.route("/administrator")
def administrator():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    if nickname == "1130630215" or nickname == "1130630212":
        return render_template("administrator.html")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")

    
@app.route("/team")
def team():
    if "nickname" in session:
        return render_template("team.html")
    else:
        return render_template("/")
    
@app.route("/my4boss",methods=["GET"])
def my4boss():
    nickname = session['nickname']
    studentID = nickname
    collection=db.product #選擇操作 product 集合
    cursor = collection.find({
        "$and": [
            {"studentID": studentID}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("my4boss.html",products=products)
    else:
        return render_template("/")
    
@app.route("/sell")
def sell():
    if "nickname" in session:
        return render_template("sell.html")
    else:
        return render_template("/")
    
@app.route("/productinfo", methods=["GET","POST"])
def productinfo(): 
    request.method == "POST"
    # 從前端接受資料
    studentID = request.form['studentID']
    productname = request.form['productname']
    collection = db.product  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    cursor = collection.find({
        "$and": [
            {"studentID": studentID},
            {"productname": productname}
        ]
    })
        
    for doc in cursor:
        print(doc)
    request.method == "GET"
    if "nickname" in session:
        return render_template("productinfo.html",productinfo=doc)
    else:
        return render_template("/")
    

@app.route("/admin",methods=["GET"])
def admin():
    if 'nickname' in session:
        # 根據會員ID從數據庫中獲取會員資料
        nickname = session['nickname']
        collection=db.user 
        cursor = collection.find({
            "$and": [
                {"nickname": nickname},
            ]
        })
        for doc in cursor:
            print(doc)
        # 在這裡你可以使用會員ID查詢數據庫中的會員資料，然後將其傳遞給模板
        return render_template('admin.html', member=doc)
    else:
        # 如果會員未登錄，重定向到登錄頁面
        return render_template("/")
    
@app.route("/changeadmin",methods=["GET","POST"])
def changeadmin():
    if 'nickname' in session:
        if request.method == "GET":
            request.method == "GET"
            # 根據會員ID從數據庫中獲取會員資料
            nickname = session['nickname']
            collection=db.user #選擇操作 product 集合
            cursor = collection.find({
                "$and": [
                    {"nickname": nickname},
                ]
            })
            for doc in cursor:
                print(doc)
            return render_template('changeadmin.html', member=doc)
        elif request.method == "POST":
            request.method == "POST"

            department=request.form["department"]
            grade=request.form["grade"]
            password=request.form["password"]
            email=request.form["email"]

            nickname = session['nickname']
            collection=db.user #選擇操作 product 集合
            collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "department":department
                }
            })
            collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "grade":grade
                }
            })
            collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "password":password
                }
            })
            collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "email":email
                }
            })

            return redirect("/admin")
    else:
        # 如果會員未登錄，重定向到登錄頁面
        return render_template("/")

@app.route("/productdelete",methods=["POST"])
def productdelete():
    productname = request.form['productname']
    studentID = request.form['studentID']
    collection = db.product  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    result = collection.delete_one({
        "$and": [
            {"studentID": studentID},
            {"productname": productname}
        ]
    })
    print("總共刪除幾筆資料", result.deleted_count)
    if "nickname" in session:
        return redirect("/my4boss")
    else:
        return redirect("/")



# /error?msg=錯誤訊息
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤，請聯繫客服")
    return render_template("error.html",message=message)


@app.route("/addmylove",methods=["POST"])
def addmylove():
    #從前端接受資料
    studentID=request.form["studentID"]
    productname=request.form["productname"]
    productAuthor=request.form["productAuthor"]
    productpress=request.form["productpress"]
    productISBN=request.form["productISBN"]
    productdescribe=request.form["productdescribe"]
    productprice=request.form["productprice"]
    producttype=request.form["producttype"]
    productcall=request.form["productcall"]
    productimage=request.form["productimage"]
    nickname = session['nickname']
    #跟資料庫互動
    collection=db.mylove
    #把資料放進資料庫
    collection.insert_one({
        "studentID":studentID,
        "productname":productname,
        "productAuthor":productAuthor,
        "productpress":productpress,
        "productISBN": productISBN,
        "productdescribe": productdescribe,
        "productprice": productprice,
        "producttype": producttype,
        "productcall": productcall,
        "productimage": productimage,
        "nickname": nickname
    })

    return redirect("/product")


@app.route("/mylove",methods=["GET"])
def mylove():
    nickname = session['nickname']
    print(nickname)
    collection=db.mylove 
    cursor = collection.find({
        "$and": [
            {"nickname": nickname},
        ]
    })
    loves=[]
    for doc in cursor:
        loves.append(doc)
    if "nickname" in session:
        return render_template("mylove.html", loves=loves)
    else:
        return render_template("/")
    

@app.route("/mylovedelete",methods=["POST"])
def mylovedelete():
    productname = request.form['productname']
    studentID = request.form['studentID']
    nickname = request.form['nickname']
    collection = db.mylove  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    result = collection.delete_one({
        "$and": [
            {"studentID": studentID},
            {"productname": productname},
            {"nickname": nickname}
        ]
    })
    print("總共刪除幾筆資料", result.deleted_count)
    if "nickname" in session:
        return redirect("/mylove")
    else:
        return redirect("/")


@app.route("/signup",methods=["POST"])
def signup():
    #從前端接受資料
    nickname=request.form["nickname"]
    password=request.form["password"]
    email=request.form["email"]
    department=request.form["department"]
    grade=request.form["grade"]
    
    #跟資料庫互動
    collection=db.user
    #檢查是否有相同email的文件資料
    result=collection.find_one({
        "email":email
    })
    if result != None:  
        return redirect("/error?msg=信箱已經被註冊")
        
    #把資料放進資料庫
    collection.insert_one({
        "nickname":nickname,
        "password":password,
        "email":email,
        "department":department,
        "grade":grade,
        "status":"離線"
    })

    body = "<p>註冊帳號成功</p>" \
            '<a href="http://127.0.0.1:8000/">登入網站</a>'
    # 製作信件
    msg = Message('註冊帳號成功', sender = 'a0989600553@gmail.com', recipients = [email], html = body)
    # 送出信件
    mail.send(msg)

    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    #從前端接受資料
    nickname=request.form["nickname"]
    password=request.form["password"]
    #和資料庫互動
    collection=db.user
    #檢查信箱密碼是否正確
    result=collection.find_one({
        "$and":[
            {"nickname":nickname},
            {"password":password}
        ]
    })
    collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "status":"在線"
                }
            })
    #找不到對應資料
    if result==None:
        return redirect("/error?msg=帳號密碼輸入錯誤")
    #登入成功，在session紀錄會員資訊
    session["nickname"]=result["nickname"]
    print(session)
    return redirect("/product")


@app.route('/forgot', methods=['POST'])
def send_mail():
    email=request.form["email"]
    nickname=request.form["nickname"]
    collection=db.user
    result=collection.find_one({
        "$and":[
            {"nickname":nickname},
            {"email":email}
        ]
    })
    if result==None:
        return redirect("/error?msg=電子郵件輸入錯誤或尚未註冊")
    
    ''' 送出寄信 '''
    # 內容
    body = "<p>請點擊下方連結重設密碼：</p>" \
        '<a href="http://127.0.0.1:8000/resetpasswordhtml">重設密碼</a>'

    # 製作信件
    msg = Message('忘記密碼', sender = 'a0989600553@gmail.com', recipients = [email], html = body)

    # 送出信件
    mail.send(msg)
    return redirect("/")

@app.route("/resetpasswordhtml")
def resetpasswordhtml():
    return render_template("resetpassword.html")

@app.route("/resetpassword",methods=["POST"])
def resetpassword():
    email=request.form["email"]
    password=request.form["password"]
    password1=request.form["password1"]
    collection=db.user
    result=collection.find_one({
        "$and":[
            {"email":email}
        ]
    })
    if result==None:
        return redirect("/error?msg=電子郵件輸入錯誤或尚未註冊")
    elif password != password1:
        return redirect("/error?msg=新密碼輸入錯誤")
    else:
        collection.update_one({
            "email":email
        },{
            "$set":{
                "password":password
            }
        })
        # 內容
        body = "<p>重設密碼成功</p>" \
            '<a href="http://127.0.0.1:8000/">登入網站</a>'
        # 製作信件
        msg = Message('重設密碼成功', sender = 'a0989600553@gmail.com', recipients = [email], html = body)
        # 送出信件
        mail.send(msg)
        return redirect("/")


@app.route("/signout")
def signout():
    collection=db.user
    nickname = session['nickname']
    collection.update_one({
                "nickname":nickname
            },{
                "$set":{
                    "status":"離線"
                }
            })
    #移除session中的會員資訊
    if nickname in session:
        del session["nickname"]
    return redirect("/")


@app.route("/productadd",methods=["POST"])
def productadd():
    
    #從前端接受資料
    studentID=request.form["studentID"]
    productname=request.form["productname"]
    productAuthor=request.form["productAuthor"]
    productpress=request.form["productpress"]
    productISBN=request.form["productISBN"]
    productdescribe=request.form["productdescribe"]
    productprice=request.form["productprice"]
    producttype=request.form["producttype"]
    productcall=request.form["productcall"]
    productimage=request.form["productimage"]
    current_time = datetime.now()
    #跟資料庫互動
    collection=db.product

    #把資料放進資料庫
    collection.insert_one({
        "studentID":studentID,
        "productname":productname,
        "productAuthor":productAuthor,
        "productpress":productpress,
        "productISBN": productISBN,
        "productdescribe": productdescribe,
        "productprice": productprice,
        "producttype": producttype,
        "productcall": productcall,
        "productimage": productimage,
        "time":current_time
    })
    

    return redirect("/my4boss")


@app.route("/questions", methods=["POST"])
def questions():
    #從前端接受資料
    question=request.form["question"]
    nickname = session['nickname']
    #和資料庫互動
    collection=db.question
    collection.insert_one({
        "nickname":nickname,
        "question":question,
        "answer":"等待回覆中"
    })
    if "nickname" in session:
        return redirect("/Q_A")
    else:
        return redirect("/")


@app.route("/Q_A", methods=["GET"])
def Q_A():
    collection=db.question
    cursor = collection.find()
    questions=[]
    for doc in cursor:
        questions.append(doc)

    return render_template("Q_A.html",questionss=questions)


@app.route("/search", methods=["POST","GET"])
def search():

    #從前端接受資料
    search=request.form["search"]
    #和資料庫互動
    collection=db.product
    cursor = collection.find({
        "$and": [
            {"productname": {'$regex':search}}
        ]
    })
    products=[]
    for doc in cursor:
        products.append(doc)
    if "nickname" in session:
        return render_template("search.html",products=products)
    else:
        return render_template("/")


@app.route("/allproduct",methods=["GET"])
def allproduct():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.product #選擇操作 product 集合
    cursor = collection.find()
    products=[]
    for doc in cursor:
        products.append(doc)
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("allproduct.html",products=products)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")

@app.route("/allproductupdate",methods=["POST","GET"])
def allproductupdate():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    request.method == "POST"
    # 從前端接受資料
    studentID = request.form['studentID']
    productname = request.form['productname']
    collection = db.product  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    cursor = collection.find({
        "$and": [
            {"studentID": studentID},
            {"productname": productname}
        ]
    })
    for doc in cursor:
        print(doc)
    request.method == "GET"
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("allproductupdate.html",products=doc)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")

@app.route("/allproductsell")
def allproductsell():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("allproductsell.html")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/allproductadd",methods=["POST"])
def allproductadd():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    #從前端接受資料
    studentID=request.form["studentID"]
    productname=request.form["productname"]
    productAuthor=request.form["productAuthor"]
    productpress=request.form["productpress"]
    productISBN=request.form["productISBN"]
    productdescribe=request.form["productdescribe"]
    productprice=request.form["productprice"]
    producttype=request.form["producttype"]
    productcall=request.form["productcall"]
    productimage=request.form["productimage"]
    current_time = datetime.now()
    #跟資料庫互動
    collection=db.product

    #把資料放進資料庫
    collection.insert_one({
        "studentID":studentID,
        "productname":productname,
        "productAuthor":productAuthor,
        "productpress":productpress,
        "productISBN": productISBN,
        "productdescribe": productdescribe,
        "productprice": productprice,
        "producttype": producttype,
        "productcall": productcall,
        "productimage": productimage,
        "time":current_time
    })
    

    if nickname == "1130630215" or nickname =="1130630212":
        return redirect("/allproduct")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/productupdate",methods=["POST","GET"])
def productupdate():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    request.method == "POST"
    # 從前端接受資料
    studentID=request.form["studentID"]
    productname=request.form["productname"]
    productAuthor=request.form["productAuthor"]
    productpress=request.form["productpress"]
    productISBN=request.form["productISBN"]
    productdescribe=request.form["productdescribe"]
    productprice=request.form["productprice"]
    producttype=request.form["producttype"]
    productcall=request.form["productcall"]
    productimage=request.form["productimage"]
    time=request.form["time"]
    _id=request.form["_id"]
    print(_id)
    collection = db.product  # 選擇操作 product 集合
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "studentID":studentID
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productname":productname
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productAuthor":productAuthor
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productpress":productpress
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productISBN":productISBN
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productdescribe":productdescribe
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productprice":productprice
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "producttype":producttype
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productcall":productcall
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "productimage":productimage
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "time":time
                }
            })
    
    if nickname == "1130630215" or nickname =="1130630212":
        return redirect("/allproduct")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")



@app.route("/allproductdelete",methods=["POST"])
def allproductdelete():
    productname = request.form['productname']
    studentID = request.form['studentID']
    collection = db.user
    cursor=collection.find({
        "$and":[
            {"nickname": {'$regex':studentID}}
        ]
    })
    for doc in cursor:
        print(doc)
    print(doc["email"])
    # 內容
    body = "<p>您的商品《"+productname+"》已被管理員下架</p>" \
        "<p>被下架原因有以下可能:</p>"\
        '<ul><li>內容不當</li><li>價格過高</li><li>滯銷超過60天</li></ul>'\
        "<p>有疑問歡迎回覆!</p>"
    # 製作信件
    msg = Message('二手書網商品被下架通知', sender = 'a0989600553@gmail.com', recipients = [doc["email"]], html = body)
    # 送出信件
    mail.send(msg)
    collection = db.product  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    result = collection.delete_one({
        "$and": [
            {"studentID": studentID},
            {"productname": productname}
        ]
    })
    print("總共刪除幾筆資料", result.deleted_count)
    if "nickname" in session:
        return redirect("/allproduct")
    else:
        return redirect("/")
    

@app.route("/alladmin",methods=["GET"])
def alladmin():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.user #選擇操作 user 集合
    cursor = collection.find()
    users=[]
    for doc in cursor:
        users.append(doc)
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("alladmin.html",users=users)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")

@app.route("/alladminsignup")
def alladminsignup():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("alladminsignup.html")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/adminsignup",methods=["POST"])
def adminsignup():
    #從前端接受資料
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    nickname1=request.form["nickname"]
    department=request.form["department"]
    grader=request.form["grade"]
    password=request.form["password"]
    email=request.form["email"]
    status=request.form["status"]
    
    #跟資料庫互動
    collection=db.user
    #檢查是否有相同email的文件資料
    result=collection.find_one({
        "email":email
    })
    if result != None:  
        return redirect("/error?msg=信箱已經被註冊")
        
    #把資料放進資料庫
    collection.insert_one({
        "nickname":nickname1,
        "department":department,
        "grader":grader,
        "password":password,
        "email":email,
        "status":status
    })

    if nickname == "1130630215" or nickname =="1130630212":
        return redirect("/alladmin")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/alladminupdate",methods=["POST","GET"])
def alladminupdate():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    request.method == "POST"
    # 從前端接受資料
    nickname1 = request.form['nickname']
    email = request.form['email']
    collection = db.user  # 選擇操作 product 集合
    # 檢查賣家編號及書名是否正確
    cursor = collection.find({
        "$and": [
            {"nickname": nickname1},
            {"email": email}
        ]
    })
    for doc in cursor:
        print(doc)
    request.method == "GET"
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("alladminupdate.html",users=doc)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/adminupdate",methods=["POST","GET"])
def adminupdate():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    request.method == "POST"
    # 從前端接受資料
    nickname1=request.form["nickname"]
    department=request.form["department"]
    grade=request.form["grade"]
    password=request.form["password"]
    email=request.form["email"]
    status=request.form["status"]
    _id=request.form["_id"]
    collection = db.user
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "nickname":nickname1
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "department":department
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "grade":grade
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "password":password
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "email":email
                }
            })
    collection.update_one({
                "_id":ObjectId(_id)
            },{
                "$set":{
                    "status":status
                }
            })
    
    if nickname == "1130630215" or nickname =="1130630212":
        return redirect("/alladmin")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/alladmindelete",methods=["POST"])
def alladmindelete():
    nickname = request.form['nickname']
    email = request.form['email']
    collection = db.user
    cursor=collection.find({
        "$and":[
            {"nickname":nickname},
            {"email":email}
        ]
    })
    for doc in cursor:
        print(doc)
    print(doc["email"])
    # 內容
    body = "<p>您的帳號《"+nickname+"》已被管理員刪除</p>" \
        "<p>被刪除原因有以下可能:</p>"\
        '<ul><li>使用者已畢業</li><li>使用者超過兩年未登入</li></ul>'\
        "<p>有疑問歡迎回覆!</p>"
    # 製作信件
    msg = Message('二手書網帳號被刪除通知', sender = 'a0989600553@gmail.com', recipients = [doc["email"]], html = body)
    # 送出信件
    mail.send(msg)
    # 檢查賣家編號及書名是否正確
    result = collection.delete_one({
        "$and": [
            {"nickname":nickname},
            {"email":email}
        ]
    })
    print("總共刪除幾筆資料", result.deleted_count)
    if "nickname" in session:
        return redirect("/alladmin")
    else:
        return redirect("/")


@app.route("/allqa",methods=["GET"])
def allqa():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.question 
    cursor = collection.find()
    questions=[]
    for doc in cursor:
        questions.append(doc)
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("allqa.html",questions=questions)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/allqaincrease")
def allqaincrease():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("allqaincrease.html")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/qaincrease",methods=["POST"])
def qaincrease():
    #從前端接受資料
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    nickname1=request.form["nickname"]
    question=request.form["question"]
    answer=request.form["answer"]
    
    #跟資料庫互動
    collection=db.question
        
    #把資料放進資料庫
    collection.insert_one({
        "nickname":nickname1,
        "question":question,
        "answer":answer
    })

    if nickname == "1130630215" or nickname =="1130630212":
        return redirect("/allqa")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/Questionreply",methods=["GET","POST"])
def Questionreply():
    nicknamecheck = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.question 
    nickname = request.form['nickname']
    question = request.form['question']
    if nicknamecheck == "1130630215" or nicknamecheck =="1130630212":
        cursor=collection.find({
            "$and":[
                {"nickname":nickname},
                {"question":question}
            ]
        })
        questions=[]
        for doc in cursor:
            questions.append(doc)
        return render_template("Questionreply.html",questions=questions)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/qadelete",methods=["POST"])
def qadelete():
    nicknamecheck = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.question 
    collection1=db.user
    nickname = request.form['nickname']
    question = request.form['question']
    
    if nicknamecheck == "1130630215" or nicknamecheck =="1130630212":
        cursor=collection1.find({
            "$and":[
                {"nickname": {'$regex':nickname}}
            ]
        })
        for doc in cursor:
            print(doc)
        # 內容
        body = "<p>您的提問已被管理員刪除</p>" \
            "<p>被刪除原因有以下可能:</p>"\
            '<ul><li>已回覆提問並公布達一個月</li></ul>'\
            "<p>有疑問歡迎回覆!</p>"
        # 製作信件
        msg = Message('二手書網提問被刪除通知', sender = 'a0989600553@gmail.com', recipients = [doc["email"]], html = body)
        # 送出信件
        mail.send(msg)
        result = collection.delete_one({
            "$and": [
                {"nickname":nickname},
                {"question":question}
            ]
        })
        print("總共刪除幾筆資料", result.deleted_count)
        return redirect("/allqa")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")



@app.route("/reply",methods=["POST"])
def reply():
    nickname1 = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    question = request.form['question']
    nickname = request.form['nickname']
    answer = request.form['answer']
    collection=db.question 
    collection.update_one({
            "$and": [
                {"nickname":nickname},
                {"question":question}
            ] 
        },{
            "$set":{
                "answer":answer
            }
        })
    if nickname1 == "1130630215" or nickname1 =="1130630212":
        return redirect("/allqa")
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")
    

@app.route("/sendemail",methods=["GET"])
def sendemail():
    nickname = session['nickname']
    message=request.args.get("msg","權限不足請返回首頁")
    collection=db.user
    cursor = collection.find()
    users=[]
    for doc in cursor:
        users.append(doc)
    if nickname == "1130630215" or nickname =="1130630212":
        return render_template("sendemail.html",users=users)
    elif "nickname" in session:
        return render_template("error.html",message=message)
    else:
        return render_template("/")


@app.route("/send",methods=["POST"])
def send():
    subject = request.form['subject']
    recipient = request.form.getlist('recipient[]')
    content = request.form['content']
    for i in range(len(recipient)):
        msg = Message(subject, sender = 'a0989600553@gmail.com', recipients = [recipient[i]], html = content)
        # 送出信件
        mail.send(msg)
    success_message = "郵件已成功寄出!!"
    return jsonify({"message": success_message})

app.run(port=8000)

