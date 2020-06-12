#从下载的每个学者的html中提取出他的base_info
from bs4 import BeautifulSoup
import os,json


if __name__ == '__main__':
    with open('person2id.json')as f:
        person2id = json.load(f)
    author_list = []
    for filename in os.listdir('./person_html'):
        author_list.append(filename.replace('.html' ,''))
    index = 0
    existed_author = []
    for filename in os.listdir('./person_base_info'):
        existed_author.append(filename.replace('.json', ''))
    rest_list = list(set(author_list).difference(set(existed_author)))
    # print(len(rest_list))
    for author_name in rest_list:
        index += 1
        print(author_name)
        # if index>2:
        #     break
        try:
            f_name = author_name + ".html"
            file = open('./person_html/'+f_name, 'rb')
            html = file.read()
            bs = BeautifulSoup(html, "html.parser")
            #提取base_info
            t_list = bs.find_all(class_="baseInfo")
            if len(t_list) == 1:
                occupation = "unknown"
                institution = t_list[0].string
            else:
                occupation = t_list[0].string
                institution = t_list[1].string
            #研究兴趣
            in_list = bs.find_all(class_="nv-legend-text")
            #h-g_index
            indexs = bs.find_all(class_="num")
            h_index = indexs[3].string
            g_index = indexs[4].string
            interests = []
            for interest in in_list:
                interests.append(interest.string)
            # print(interests)
            numberOfFollowers = 0
            org = "unknown"
            summary = author_name+" works as a "+occupation+" in "+institution+\
                      ", and his\her h-index is "+str(h_index)+", g-index is "+str(g_index)+". His\Her interests are :\n"
            for item in interests:
                summary+=" "+item+";"
            # print(summary)
        except:
            institution = "unknown"
            occupation = "unknown"
            summary = "unknown"
            org = "unknown"
            numberOfFollowers = 0
            interests = []
        with open("./person_base_info/" + author_name+".json", 'w')as f:
            info = {}
            base_info = {}
            base_info['institution'] = institution
            base_info['occupation'] = occupation
            base_info['summary'] = summary
            base_info['org'] = org
            base_info['numberOfFollowers'] = numberOfFollowers
            base_info['interests'] = interests
            info["info"] = base_info
            info['name'] = author_name
            info['am_id'] = person2id[author_name]
            # print(info)
            f.write(json.dumps(info))
