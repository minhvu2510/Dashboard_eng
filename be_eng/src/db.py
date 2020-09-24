#! coding: utf-8
# code by vunm
import sys
sys.path.append('../')
from pymongo import MongoClient
import settings

client = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
DATABASE = client.mvp
def get_document(table,query,order=None,distinct=None,page=None,limit=None,incre=-1):
    if page:
        if not limit:
            limit = 20
        page = int(page)
        limit = int(limit)
        if order:
            res = DATABASE[table].find(query).sort(order, incre).skip((page-1)*limit).limit(limit)
        else:
            res = DATABASE[table].find(query).skip((page-1)*limit).limit(limit)
    else:
        if order:
            res = DATABASE[table].find(query).sort(order, incre)
        else:
            res = DATABASE[table].find(query)
    if distinct:
        res = res.distinct(distinct)
        res = filter(lambda r: r != '',res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return  message
def get_limit(table,query,limit):
    res = DATABASE[table].find(query).limit(limit)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return  message
def get_all(table):
    res = DATABASE[table].find()
    res = filter(lambda r: r != '', res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return  message
def get_sort(table,order,incre):
    res = DATABASE[table].find().sort(order,incre)
    res = filter(lambda r: r != '', res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return message
def get_records_top(table,order,incre,skip):
    res = DATABASE[table].find().sort(order, incre).skip(skip)
    # res = DATABASE[table].find().sort(order, incre).limit(skip)
    res = filter(lambda r: r != '', res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return message
def find_one(table,order,incre,skip):
    res = DATABASE[table].find_one().skip(skip)
    res = filter(lambda r: r != '', res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return message
def insert_document(table, query, file_unique=None):
    if file_unique:
        DATABASE[table].create_index(file_unique,unique = True)
    try:
        DATABASE[table].insert(query)
        message = {"status": True, "message": "Insert success"}
        if "id" in query:
            message.update({"id": query["id"]})
    except:
        message = {"status": False, "message": "{} is exists.".format(file_unique)}
    return message
def update_document(table, query, query_update):
    try:
        DATABASE[table].update(query, {"$set": query_update}, multi=True)
        message = {"status": True, "message": "Update success"}
    except:
        message = {"status": False, "message": "Update error"}
    return message
def delete_document(table, query):
    try:
        DATABASE[table].remove(query)
        message = {"status": True, "message": "Delete success"}
    except:
        message = {"status": False, "message": "Delete error"}
    return message


def count_document(table, query=None):
    if query:
        return DATABASE[table].find(query).count()
    else:
        return DATABASE[table].count()
def show_allcolection():
    allcolec = []
    for i in DATABASE.collection_names():
        allcolec.append(i)
    return allcolec
