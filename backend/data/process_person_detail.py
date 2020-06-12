#将所有资源整合成Person_Detail文件，里面的最终的所有人的全面信息
#信息说明：https://git.tsinghua.edu.cn/cheng-zy17/storms/blob/dev/docs/API_convention.md
import json,os,re
class Setting():
    def __init__(self):
        self.fake_profile={}
        self.fake_profile["affiliation"]="unknown"
        self.fake_profile["position"] = "unknown"
        self.fake_profile["org"] = "unknown"
setting = Setting()
def collect_fixed_info(author_name,person):
    with open("./person_base_info/" + author_name + ".json")as f:
        data = json.load(f)
    name = data["name"]
    base_info = data["info"]
    with open("./person_paper_trend/" + author_name + ".json")as f:
        data = json.load(f)
    papers = data["papers"]
    paperTrend = data["paperTrend"]
    with open("./person_community_graph/" + author_name + ".json")as f:
        data = json.load(f)
    communityGraph = data["communityGraph"]
    # personalGraph ={}
    # nodes = []
    # links = []
    # field = "Data_Mining"
    # with open (field+".json")as f:
    #     detail_data = json.load(f)
    #     authors = detail_data["author"]
    #     relations = detail_data["relation"]
    # # personalGraph
    # #找到这个人的领域内id
    # for author in authors:
    #     if author[1] == author_name:
    #         person_id = author[0]
    # node = {}
    # node["id"] = person_id
    # node["name"] = author_name
    # node["field"] = field
    # nodes.append(node)
    # for relation in relations:
    #     if(relation[1]==person_id):
    #         link={}
    #         link["id"] = relation[0]
    #         link["name"] = field
    #         link["sid"] = person_id
    #         link["tid"] = relation[2]
    #         links.append(link)
    # for relation in relations:
    #     if(relation[2]==person_id):
    #         link={}
    #         link["id"] = relation[0]
    #         link["name"] = field
    #         link["sid"] = person_id
    #         link["tid"] = relation[1]
    #         links.append(link)
    # for link in links:
    #     node = {}
    #     node["id"] = link["tid"]
    #     node["name"] = authors[node["id"]-1][1]
    #     node["field"] = field
    #     nodes.append(node)
    # personalGraph["nodes"] = nodes
    # personalGraph["links"] = links
    # person["info"] = info
    person['name'] = name
    person['info'] = base_info
    person["papers"] = papers
    person["paperTrend"] = paperTrend
    person["communityGraph"] = communityGraph
    person["personalGraph"] = communityGraph
    return person


# def existed(persons,author_name):
#     existed_author = None
#     for person in persons:
#         if person["name"] == author_name.replace(" ",'_'):
#             existed_author = person
#     return existed_author
def collect_info(persons):
    author_names = []
    for filename in os.listdir('./person_html'):
        author_names.append(filename.replace('.html' ,''))
    index = 0
    for author_name in author_names:
        # index += 1
        # if index > 1:
        #     break
        print(author_name)
        # existed_author = existed(persons,author_name)
        # if(existed_author != None):
        #     existed_author["info"]["interests"].append(field)
        # else:
        person = {}
        # if(os.stat("./person_info/" +author_name+ ".json").st_size == 0):##文件信息为空
        #     info = {}
        #     person["name"]= re.sub(r'\\u.{4}','',author_name.replace(" ",'_'))
        #     person["am_id"] = "info_lost"
        #     info["institution"] = "info_lost"
        #     info["occupation"] = "info_lost"
        #     info["numberOfFollowers"] = 0
        #     info["interests"] = []
        #     info["summary"] = "info_lost"
        #     person["info"] = info
        #     person["papers"] = []
        #     trend = {}
        #     trend["publish"] = {}
        #     trend["publish"]["date"] = []
        #     trend["publish"]["amounts"] = []
        #     person["paperTrend"] = trend
        #     nodes = []
        #     links = []
        #     person["personalGraph"] = {}
        #     person["personalGraph"]["nodes"] = nodes
        #     person["personalGraph"]["links"] = links
        #     nodes = []
        #     links = []
        #     person["communityGraph"] = {}
        #     person["communityGraph"]["nodes"] = nodes
        #     person["communityGraph"]["links"] = links
        #     persons.append(person)
        #     continue
        # with open("./person_info/"+author_name+".json")as f:
        #     data = json.load(f)
        # author = data["authorList"][0]
        # person["name"] = re.sub(r'\\u.{4}','',author["name"].replace(" ",'_'))
        # person["am_id"] = author["id"]
        # info = {}
        # if "profile" not in author:
        #     author["profile"] = setting.fake_profile
        # if "affiliation" in author["profile"]:
        #     info["institution"] = author["profile"]["affiliation"]
        # else:
        #     info["institution"] = "unknown"
        # if "position" in author["profile"]:
        #     info["occupation"] = author["profile"]["position"]
        # else:
        #     info["occupation"] = "unknown"
        # if "org" in author["profile"]:
        #     info["org"] = author["profile"]["org"]
        # else:
        #     info["org"] = "unknown"
        # info["numberOfFollowers"] = 0
        # inte_list = []
        # inte_list.append(field)
        # for item in author["tags"]:
        #     inte_list.append(item)
        # info["interests"] = inte_list
        # summary = author["name"]+" works as a "+info["occupation"]+" in "+info["org"]+", "+info["institution"]+\
        #           ", and his\her h-index is "+str(author["indices"]["hindex"])+", g-index is "+str(author["indices"]["gindex"])+". His\Her interests are :\n"
        # for item in author["tags"]:
        #     summary+=" "+item+";"
        # info["summary"] = summary
        # person["info"] = info
        collect_fixed_info(author_name,person)
        persons.append(person)
if __name__ == '__main__':
    persons = []
    collect_info(persons)
    with open("Person_Detail.json",'w')as f:
        f.write(json.dumps(persons))

