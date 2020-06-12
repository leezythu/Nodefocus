* 可以通过访问

  ```python
  http://101.200.241.8:3389/authors
  http://101.200.241.8:3389/links
  ```

  分别获取json格式的学者和关联信息。

  author数据格式如下,其中$node\_size$表示学者的影响力大小，可以用作显示的像素大小：

  ```
  {
  [field: "Data mining", id: 0, name: "Sreangsu Acharyya",node_size: 22],
  [field: "Data mining", id: 1, name: "Francois Rioult",node_size: 23],
  ...
  }
  ```

  Link信息格式如下：

  ```
  {
  [field: "Data mining", id: 0, name: “0”，sid: 16, tid: 4],
  [field: "Data mining", id: 1, name: “1”，sid: 1, tid: 16],
  ...
  }
  ```

* 注:以上格式是后端目前提供的小规模数据的数据格式，最新处理好的数据一方面规模较大，另外在link中多加入了一个“count”属性，表示两个学者之间的合著的论文篇数。

* 整个处理流程：

  * 步骤一：用process_data.py从graph-T16_sub0.net等原生数据集提取出Data_Mining.json
  * 步骤二：process_fields.py手工构造出了Fields.json，这个步骤其实是独立的
  * 步骤三：process_field_detail.py用Data_Mining.json构造出了Data_Mining_detail.json，是详细数据
  * 步骤四：person2id.py     ，根据Data_Mining.json等八个文件夹中的作者名，形成person_id.json，包含所有作者名到Aminer     id的映射
    * 根据person_id.json下每个学者的id，在Aminer上爬取community_graph信息，存到      /person_community_graph文件夹下。
    * crawel_person_htmls.py根据person_id.json下每个学者的id，在Aminer上爬取整个人的页面，存到/person_html下
    * html2papers.py      从每个学者的html中提取出他的papers和papertrend，存到/person_paper_trend文件夹下
    * html2base_info.py 从每个学者的html中提取出他的base_info，存到/person_base_info文件夹下

- 步骤五：process_person_detail.py集成使用了person_base_info     \person_paper_trend、person_community_graph下的每个人的数据整合成了Person_Detail.json
- process_news.py     ，目前手工收集构造了9条新闻