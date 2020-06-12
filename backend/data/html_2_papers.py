#从下载的每个学者的html中提取出他的papers和papertrend
from bs4 import BeautifulSoup
import os,json
def process_t(span,year_list,num_list):
    num = round(float(span.contents[0].attrs["style"].split(":")[1].replace("%;",""))/2.857145)
    num_list.append(num)
    year = span.contents[1].string
    year_list.append(year)


def process_p(span,papers):
    paper = {}
    id  = span.attrs['id']
    paper["id"] = str(id)
    title = span.find_all(class_="paper-title")[0].string
    paper["title"] = str(title)
    summary = span.find_all(class_="venue-line")[0].contents[0]
    paper["summary"] = str(summary)
    link = span.find_all(class_="title-link")[0].attrs["href"]
    paper["link"] = str(link)
    paper["influence"] = "0"
    paper["date"] = "none"
    papers.append(paper)



if __name__ == '__main__':
    author_list = []
    for filename in os.listdir('./person_html'):
        author_list.append(filename.replace('.html' ,''))
    index = 0
    for author_name in author_list:
        index += 1
        print(author_name)
        # if index>2:
        #     break
        try:
            f_name = author_name + ".html"
            file = open('./person_html/'+f_name, 'rb')
            html = file.read()
            bs = BeautifulSoup(html, "html.parser")
            #提取papertrend
            t_list = bs.find_all(class_="year_bar")
            year_list = []
            num_list = []
            for span in t_list:
                process_t(span,year_list,num_list)
            year_list.reverse()
            num_list.reverse()
            #提取paper
            papers = []
            p_list = bs.find_all(class_="paper-item end")
            # print(p_list)
            paper_index = 0
            for span in p_list:
                paper_index += 1
                if paper_index > 3:
                    break
                process_p(span, papers)
        except:
            papers = []
            year_list = []
            num_list = []
        with open("./person_paper_trend/" + author_name+".json", 'w')as f:
            info = {}
            trend = {}
            trend["publish"] = {}
            trend["publish"]["date"] = year_list
            trend["publish"]["amounts"] = num_list
            info["paperTrend"] = trend
            info["papers"] = papers
            # print(info)
            f.write(json.dumps(info))
