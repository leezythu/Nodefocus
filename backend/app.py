from flask_cors import  CORS
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
import logging,sys
from datetime import datetime
app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/flask'

CORS(app, supports_credentials=True)

api = Api(app)
mongo = PyMongo(app)


def error_handler(e):
    if e.message == 'TypeError':
        response = jsonify(e.to_dict())
        return response


def log_info(agent,created_time,id,ip,payload,src,target_name,target_type,type,process_time):
    app.logger.info("{"+"\"agent\":\""+agent+"\",\"created_time\":\""+created_time+"\",\"id\":\""+id+"\",\"ip\":\""+ip+"\",\"payload\":\""+payload +"\",\"src\":\""+src+"\",\"target_name\":\""+target_name+"\",\"target_type\":\""+target_type+"\",\"type\":\""+type+"\",\"process_time\":\""+process_time+"\"},")


def narrow(field_list):
    final_list = []
    for item in field_list:
        item.pop('_id')
        final_data = {}
        final_item = {}
        final_nodes = []
        final_links = []
        final_item["time"] = item["time"]
        data = item["data"]
        nodes = data["nodes"]
        links = data["links"]
        num_list = []
        num_set = set()
        for node in nodes:
            num_list.append(node["_size"])
        num_list = sorted(num_list,reverse=True)
        narrow_num = num_list[setting.narrow_size]
        for node in nodes:
            if node["_size"] > narrow_num:
                final_nodes.append(node)
                num_set.add(node["id"])
        for link in links:
            if link["sid"] in num_set and link["tid"] in num_set:
                final_links.append(link)
        final_data["largestNodeSize"] = data["largestNodeSize"]
        final_data["nodes"] = final_nodes
        final_data["links"] = final_links
        final_item["data"] = final_data
        final_list.append(final_item)
    return final_list


def switch_if(name):
    if name == "Data_Mining":
        return narrow(mongo.db.Data_Mining.find())
    elif name == "Web_Services":
        return narrow(mongo.db.Web_Services.find())
    elif name == "Semantic_Web":
        return narrow(mongo.db.Semantic_Web.find())
    elif name == "Bayesian_Networks":
        return narrow(mongo.db.Bayesian_Networks.find())
    elif name == "Web_Mining":
        return narrow(mongo.db.Web_Mining.find())
    elif name == "Machine_Learning":
        return narrow(mongo.db.Machine_Learning.find())
    elif name == "Database_Systems":
        return narrow(mongo.db.Database_Systems.find())
    elif name == "Information_Retrieval":
        return narrow(mongo.db.Information_Retrieval.find())
    else:
        return None


class Global_Setting():
    def __init__(self):
        self.narrow_size = 100
        self.pid = -1
setting = Global_Setting()


class MyError(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.code = status_code

    def to_dict(self):
        rv = {
            'error_message': self.message,
            'status_code': self.code,
        }
        return rv



class Count(Resource):
    def get(self):
    	return jsonify((mongo.db.Count.find()[0]).pop("_id"))
        # count.pop("_id")
        # return jsonify(count)
        # 不知道为什么得改成这个样子才可以跑

    def post(self):
        oldtime = datetime.now()
        count = mongo.db.Count.find()[0]
        count.pop('_id')
        old = int(count['count'])
        new = old + 1
        mongo.db.Count.update({'count': old}, {'count': new})
        # print(count)
        agent =str(request.user_agent)
        created_time = str(datetime.now())
        id = str(None)
        ip = str(request.remote_addr)
        payload = str(count)
        src = "public"
        target_name = ""
        target_type = "Count"
        type = "Count"
        newtime = datetime.now()
        process_time = str(newtime - oldtime)
        log_info(agent,created_time,id,ip,payload,src,target_name,target_type,type,process_time)
        return jsonify(count)





class Field(Resource):
    def get(self):
        oldtime = datetime.now()
        fields = mongo.db.fields.find()
        field_list = []
        for field in fields:
            field.pop('_id')
            field_list.append(field)
        agent =str(request.user_agent)
        created_time = str(datetime.now())
        id = str(None)
        ip = str(request.remote_addr)
        payload = str(field_list)
        src = "public"
        target_name = ""
        target_type = "Field"
        type = "Field"
        newtime = datetime.now()
        process_time = str(newtime - oldtime)
        log_info(agent,created_time,id,ip,payload,src,target_name,target_type,type,process_time)
        return field_list


class Field_Detail(Resource):
    def get(self,name):
        oldtime = datetime.now()
        narrow_size = request.args.get('limit', default=100, type=int)
        setting.narrow_size = narrow_size
        # print(narrow_size)
        data = switch_if(name)
        agent =str(request.user_agent)
        created_time = str(datetime.now())
        id = str(None)
        ip = str(request.remote_addr)
        simple_data = []
        try:
            for item in data:
                s_item = {}
                s_item["time"] = item["time"]
                s_item["data"] = {}
                s_item["data"]["largestNodeSize"] = item["data"]["largestNodeSize"]
                s_item["data"]['nodes'] = '...'
                s_item["data"]['links'] = '...'
                simple_data.append(s_item)
        except TypeError:
            logging.exception(TypeError)
            e = MyError("TypeError",500)
            ret = error_handler(e)
            return ret
        payload = str(simple_data)
        src = "public"
        target_name = name
        target_type = "Field_Detail"
        type = "Field_Detail"
        newtime = datetime.now()
        process_time = str(newtime - oldtime)
        log_info(agent,created_time,id,ip,payload,src,target_name,target_type,type,process_time)
        return data


class Person_Detail(Resource):
    def get(self):
        oldtime = datetime.now()
        person = request.args.get('name', default="Wei Wang", type=str)
        person = person.replace("_",' ')
        cursor = mongo.db.Person_Detail.find({"name":person})
        res = []
        print("this is cursor:")
        print(cursor)
        for item in cursor:
            item.pop('_id')
            res.append(item)
        agent =str(request.user_agent)
        created_time = str(datetime.now())
        id = str(None)
        ip = str(request.remote_addr)
        simple_data = []
        for item in res:
            s_item = {}
            s_item["name"] = item["name"]
            s_item["papers"] = item["papers"]
            s_item["paperTrend"] = item["paperTrend"]
            s_item["communityGraph"] = '...'
            s_item["personalGraph"] = '...'
            simple_data.append(s_item)
        payload = str(simple_data)
        src = "public"
        target_name = person
        target_type = "Person_Detail"
        type = "Person_Detail"
        newtime = datetime.now()
        process_time = str(newtime - oldtime)
        log_info(agent,created_time,id,ip,payload,src,target_name,target_type,type,process_time)
        return res


class Field_News(Resource):
    def get(self):
        oldtime = datetime.now()
        field = request.args.get('field', default="", type=str)
        person = request.args.get('person', default="", type=str)
        news = mongo.db.news.find()
        agent =str(request.user_agent)
        created_time = str(datetime.now())
        id = str(None)
        ip = str(request.remote_addr)
        src = "public"
        target_name = field +"&"+ person
        target_type = "Field_News"
        type = "Field_News"
        if field != "":
            news_list = []
            for doc in news:
                doc.pop('_id')
                if field in doc["fields"]:
                    news_list.append(doc)
            final_list = []
            if person != "":
                for doc in news_list:
                    if person in doc["person"]:
                        final_list.append(doc)
            else:
                final_list = news_list
            payload = str(final_list)
            newtime = datetime.now()
            process_time = str(newtime - oldtime)
            log_info(agent, created_time, id, ip, payload, src, target_name, target_type, type,process_time)
            return final_list
        elif person!="":
            news_list = []
            for doc in news:
                doc.pop('_id')
                if person in doc["person"]:
                    news_list.append(doc)
            payload = str(news_list)
            newtime = datetime.now()
            process_time = str(newtime - oldtime)
            log_info(agent, created_time, id, ip, payload, src, target_name, target_type, type,process_time)
            return news_list
        else:
            news_list = []
            for doc in news:
                doc.pop('_id')
                news_list.append(doc)
            payload = str(news_list)
            newtime = datetime.now()
            process_time = str(newtime - oldtime)
            log_info(agent, created_time, id, ip, payload, src, target_name, target_type, type,process_time)
            return news_list


class Pid(Resource):
    def get(self):
    	return jsonify({"pid":setting.pid})


api.add_resource(Field, '/fields')
api.add_resource(Field_Detail, '/fields/<name>')
api.add_resource(Field_News, '/news/')
api.add_resource(Person_Detail, '/person/')
api.add_resource(Count, '/count/')
api.add_resource(Pid, '/pid/')
if __name__ == '__main__':
    if len(sys.argv)==1:
        print("please input a pid for this process")
    else:
        setting.pid = sys.argv[1]
        app.debug = True
        log_f_path = 'G:\\Study_Study\\CS_4th\\soa\\storms\\backend\\flask.log'
        handler = logging.FileHandler(log_f_path, encoding='UTF-8')
        handler.setLevel(logging.DEBUG)
        app.logger.addHandler(handler)
        app.run(host='localhost', port=5000)
