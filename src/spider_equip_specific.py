from drission import DrissionPage
#todo 爬取职业需求的装备信息 装等是639 效果最好的

# 初始化一个 DrissionPage 对象，并使用浏览器模式
page = DrissionPage()

# 打开你想要访问的网页
page.get('https://example.com')  # 替换为你想抓取的 URL

# 等待页面完全加载，确保动态内容加载完成（如果需要，可以设置等待时间）
page.wait_load(10)  # 等待 10 秒或直到页面加载完成

# 查找指定的 div 元素，假设它的 id 是 'my-div'
div = page.ele('#bis')

# 在这个 div 里面查找 table
table = div.ele('table')

# 查找 table 内部所有 a 标签，并提取 href 链接
links = table.eles('a')  # 获取所有 a 标签元素

# 打印所有的 href 链接
for link in links:
    print(link.attr('href'))

# 关闭浏览器
page.close()
