

为了启动服务，你需要：

* 直接运行`./start.sh`

* 开启`mongodb`数据库，如：`./mongod -f /etc/mongodb.conf`

* 运行`./initdb.sh` 将所需数据文件导入`mongo`，或单独导入某个文件，如：`mongoimport -d flask -c field --jsonArray ./data/fields.json`

* 如文件发生改变需要重启数据库，需要先执行清除数据库操作:

  * mongo  #进入mongo shell
  *  /> show dbs           # 显示数据库
  * /> use flask              # 进入数据库
  * /> db.dropDatabase() #删除数据库  

  然后重新执行`initdb.sh`

* 最后启动服务`python app.py 3389`（3389只是为了在启动多个服务的时候为了识别添加的识别号，无其他用处）

