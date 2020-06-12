#!/usr/bin/env python
# -*- coding: utf-8 -*-
#根据已经知道的每个学者的id,在Aminer上爬取其具体信息，包括community_graph等
import os,json,requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    author_list = []
    session = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    with open("person2id.json")as f:
        person2id = json.load(f)
    author_list = list(person2id.keys())
    # print(author_list)
    index = 0
    for author_name in author_list:
        index +=1
        # if index >2 :
        #     break
        f_name = author_name + ".json"
        print(author_name)
        print(index)
        id = person2id[author_name]
        url = "https://api.aminer.cn/api/person/ego/"+id+"?cache=true"
        req = session.get(url, headers=headers)
        bsObj = BeautifulSoup(req.text, 'lxml')
        # print(bsObj)
        str = bsObj.p.string
        # print(str)
        related_persons = json.loads(str)['nodes']
        # print(related_persons)
        with open("./person_community_graph/"+f_name,'w')as f:
            info = {}
            graph = {}
            graph['nodes'] = []
            graph['links'] = []
            graph_id = 1
            for person in related_persons:
                node = {}
                node['id'] = graph_id
                node['name'] = person['name']
                node['community'] = person['bole']
                graph['nodes'].append(node)
                graph_id += 1
            for i in range(2,graph_id):
                link = {}
                link['id'] = i-1
                link['name'] = 'influence'
                link['sid'] = 1
                link['tid'] = i
                graph['links'].append(link)
            info["communityGraph"] = graph
            f.write(json.dumps(info))
