#从Aminer提供的数据中挖掘出所有学者以及他们之间的关系

import json
def fetch_authors(lines):
    authors = []
    for line in lines:
        list = line.split("\"")
        author_pair = []
        author_pair.append(int(list[0].strip()))
        author_pair.append(list[1])
        author_pair.append(int(list[2].strip()))
        authors.append(author_pair)
    return authors
def fetch_d_relation(lines):
    coauthor_relation = []
    for i in range(len(lines)):
        list = lines[i].split()
        tid = int(list[0])
        sid = int(list[1])
        count = int(list[2])
        relation = []
        relation.append(i+1)
        relation.append(tid)
        relation.append(sid)
        relation.append(count)
        coauthor_relation.append(relation)
    return coauthor_relation
def fetch_t_relation(lines):
    return None
def segment(lines):
    i = 0
    j = 0
    for i in range(len(lines)):
        if 'Vertices' in lines[i]:
            v_begin = i
            break
    for j in range(i,len(lines)):
        if 'Edges' in lines[j]:
            d_re_begin = j
            break
    for k in range(j,len(lines)):
        if 'Triangles' in lines[k]:
            t_re_begin = k
            break
    # print("i:"+str(i)+"j:"+str(j)+"k:"+str(k))
    author_lines = lines[v_begin+1:d_re_begin]
    d_relation_lines = lines[d_re_begin+1:t_re_begin]
    t_relation_lines = lines[t_re_begin+1:]
    return [author_lines,d_relation_lines,t_relation_lines]
if __name__ == '__main__':
    topic_dict = {}
    topic_dict['graph-T16_sub0.net'] = "Data_Mining"
    topic_dict['graph-T107_sub1.net'] = "Web_Services"
    topic_dict['graph-T131_sub0.net'] = "Bayesian_Networks"
    topic_dict['graph-T144_sub4.net'] = "Web_Mining"
    topic_dict['graph-T145_sub0.net'] = "Semantic_Web"
    topic_dict['graph-T162_sub1.net'] = "Machine_Learning"
    topic_dict['graph-T24_sub0.net'] = "Database_Systems"
    topic_dict['graph-T75_sub0.net'] = "Information_Retrieval"
    for filename in topic_dict.keys():
        lines = []
        topic = topic_dict[filename]
        with open("./"+filename) as f:
            line = f.readline()
            while line:
                line = line.replace("\n","")
                lines.append(line)
                line = f.readline()
        # print(lines)
        [author_lines,d_relation_lines,t_relation_lines] = segment(lines)
        # print("author_lines")
        # print(author_lines)
        # print("d_relation_lines")
        # print(d_relation_lines)
        # print("t_relation_lines")
        # print(t_relation_lines)
        authors = fetch_authors(author_lines)
        # print(authors)
        coauthor_relation = fetch_d_relation(d_relation_lines)
        # print(coauthor_relation)
        field = {}
        field['field'] = topic
        field['author'] = authors
        field['relation'] = coauthor_relation
        field_json = json.dumps(field)
        with open(field['field']+".json","w")as f:
            f.write(field_json)

