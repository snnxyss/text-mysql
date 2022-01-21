import re,pymysql
conn = pymysql.connect(host="127.0.0.1", database='user', user='user', password='123123')
conn.query("set names utf8")
db = 'x3'#可以扩展成动态表名，这里写死了
if __name__ == "__main__":
    f = open("apache.txt", "r")
    lines = f.read()
    f.close()
    flag = True
    for line in lines.split("\n"):
        content = re.sub(r'\s+', " ", line).split(" ")
        if flag:
            sql = ",\n".join(["\t" + i + " text null" for i in content])
            sql = f"create table {db}({sql});"
            conn.query(sql)
            flag = False##默认读取第一行内容为字段名并创建，可自定义读取字段名创建
            continue
        sql = "insert into `" + db + "` values('" + "','".join(content) + "')"
        conn.query(sql)
