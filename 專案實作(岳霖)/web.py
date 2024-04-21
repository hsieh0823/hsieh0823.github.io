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

client = pymongo.MongoClient("mongodb+srv://hsieh20020823:boos7712031@cluster0.lfqqncs.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())

db = client.member_system #選擇操作 member_system 資料庫

print("資料庫連結建立成功")
collection=db.user
collection.remove({"nickname":215})