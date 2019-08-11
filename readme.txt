Opening
1. flask要求配置文件config.py中变量名必须大写，小写的后果是无法读取配置文件中的变量（读取时出错）
2. DEBUG是Flask对象默认有的变量app.config已经有DEBUG这个键，且对应的值为False，所以如果要设置为True，需要再配置文件中设置DEBUG = True来覆盖默认值

状态码只是一个标识，不会对内容显示有影响

测试urls:
http://t.yushu.im/v2/book/isbn/9787501524044
http://127.0.0.1:81/book/search?q=9787501524044&page=1

http://127.0.0.1:81/book/search?q=红楼梦
http://127.0.0.1:81/book/search?q=9787070511209

创建数据表的方式
1. Database first: 手工在MySql中创建数据表
2. Model first：用建模工具（如Navicat的Model功能）
3. Code first: 程序员建议使用


测试url
http://localhost:81/test
(0.0.0.0不工作)
http://localhost:81/book/search
http://127.0.0.1:81/book/search?q=红楼梦


项目思维导图：

鱼书
    搜索书籍（依靠外部API）
        关键字检索
        isbn检索
    选择要赠送的书籍
        向他人赠送书籍
    选择自己想要的书籍
        向他人索要书籍
    书籍详情页面
        默认显示所有赠书人的名字
        点击“赠送此书”- 确定用户身份为“赠书人” - 页面底部数据切换为索要人的名字
                                                   - 把书籍加入到赠送清单
        点击“加入到心愿清单” - 确定用户身份为索要者 - 把书籍加入到心愿清单
    用户系统
        登录
        注册-邮件作为账号
        找回密码
        修改密码

详情页面无法访问，仔细看详情页面的url为：http://127.0.0.1:81/book//detail
http://127.0.0.1:81/register