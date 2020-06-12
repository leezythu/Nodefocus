#手工整理出8个领域的对比，标准是领域内的学者数量,目前数量是直接看文件的
# 注意如果有多个时间点的数据集的话，largestNodeSize需要换一种计算方式
import json
if __name__ == '__main__':
    topic_dict = {}
    topic_dict['graph-T16_sub0.net'] = "Data Mining"
    topic_dict['graph-T107_sub1.net'] = "Web Services"
    topic_dict['graph-T131_sub0.net'] = "Bayesian Networks"
    topic_dict['graph-T144_sub4.net'] = "Web Mining"
    topic_dict['graph-T145_sub0.net'] = "Semantic Web"
    topic_dict['graph-T162_sub1.net'] = "Machine Learning"
    topic_dict['graph-T24_sub0.net'] = "Database Systems"
    topic_dict['graph-T75_sub0.net'] = "Information Retrieval"
    size_dict = {}
    size_dict["Data Mining"] = 679
    size_dict["Web Services"] = 400
    size_dict["Bayesian Networks"] = 554
    size_dict["Web Mining"] = 348
    size_dict["Semantic Web"] = 671
    size_dict["Machine Learning"] = 976
    size_dict["Database Systems"] = 1127
    size_dict["Information Retrieval"] = 657


    # 因为目前只有一个时间点的data，所以是1
    field = []
    for time in range(1):
        obj = {}
        # 而且并不知道该数据集收集的是什么时间的数据
        obj["time"] = "2020"
        obj["data"] = {}
        nodes = []
        index = 0
        largestNodeSize = 0
        for topic in topic_dict.values():
            index += 1
            single_node = {}
            single_node["id"] = index
            single_node["name"] = topic
            single_node["_size"] = size_dict[topic]
            single_node["_color"] = index
            nodes.append(single_node)
            largestNodeSize = max(largestNodeSize,size_dict[topic])
        
        obj["data"]["nodes"] = list(reversed(nodes))
        obj["data"]["largestNodeSize"] = largestNodeSize
        obj["data"]["links"] = []
    
        field.append(obj)
    with open("Fields.json", "w")as f:
        f.write(json.dumps(field))

