from flask import Flask # 載入 Flask
#from flask import request #仔入 request 物件
from flask import render_template
# 建立 Application 物件，可以設定靜態檔案的路徑處理
app=Flask(__name__,
    static_folder="templates", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址路徑
   ) 
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 /abc/檔案名稱

#建立路徑 /getSum 對應的處理方式
#利用要求字串  提供彈性: /getSum?min=最小數字&max=最大的數字
#@app.route("/getSum") # 1+2+3....+max
#def getSum():
 #   maxNumber=request.args.get("max",100)
  #  maxNumber=int(maxNumber)
   # minNumber=request.args.get("min",1)
    #minNumber=int(minNumber)
    #result=0
    #for n in range(minNumber,maxNumber+1):
     #   result+=n
    #return "結果 : "+str(result)


# 建立路徑 / 對應的回應方式
@app.route("/")  #  / 代表網站首頁
def index():  # 用來回應路徑/的處理函式
    #print("請求方法", request.method)
    #print("通訊協定", request.scheme)
    #print("主機名稱", request.host)
    #print("路徑", request.path)
    #print("完整的網址", request.url)  
    #print("瀏覽器和作業系統", request.headers.get("user-agent"))
    #print("語言偏好", request.headers.get("accept-language"))
    #print("引薦網址", request.headers.get("referrer"))
    #lang=request.headers.get("accept-language")
    #if lang.startswith("en"):

        #return "Hello Flask" #回傳網站首頁的內容
    #else:
        #return "你好，歡迎光臨"
    return render_template('/index3.html')

#建立路徑 /data 對應的處理函式
#@app.route("/data")
#def handleData():
 #   return "My Data"

#動態路由 : 建立路徑 /user/使用者名稱 對應的處理方式
#@app.route("/user/<username>")
#def handeUser(username):
#    if username=="葳葳":
 #       return "你好"+username
  #  else:
   #     return "Hello"+username

    # 啟動網站伺服器，可透過port參數指定埠號
app.run(port=3000)