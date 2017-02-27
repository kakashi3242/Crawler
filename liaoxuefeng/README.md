# 一些问题的解决方案

1. 解决中文输出是unicode的问题

```python
FEED_EXPORT_ENCODING = 'utf-8'
```

2. 数据库配置

> setting.py里面设置

```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_DBNAME = 'crawler'

ITEM_PIPELINES = {
    # 保存到mysql数据库
    'liaoxuefeng.pipelines.MySQLStorePipeline': 300,
}
```

> 然后在pipeline.py里面实现 __MySQLStorePipeline__ 这个类方法

```python
# 连接数据库,类名要跟settings里面设置的名字一致
class MySQLStorePipeline(object):
    
    # 数据库配置
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('pymysql',
                                            db='crawler',
                                            user='root',
                                            passwd='123456',
                                            cursorclass=pymysql.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )
                                            
    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    # 将每行写入数据库中
    def _conditional_insert(self, tx, item):
        # item里面的跟数据库表一一对应
        tx.execute('INSERT INTO liaoxuefeng (title, href) VALUES (%s, %s)',
                   (item['title'], item['href']))
```

> 然后直接 __scrapy crawl projectname__ 运行
>> __scrapy crawl projectname -o data.json__ 可将内容保存到 __data.json__ 文件中


