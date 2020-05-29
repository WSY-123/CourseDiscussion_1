CourseDiscussion
==
2020-Spring-SoftwareEngineering
--
# 搜索：

## 课程属性：
name:课程名称
teacher:授课教师
institute:开课学院
credit:学分
semester:开课学年
time:上课时间
location:上课地点
date_added:创建时间

## 反馈属性：
title:标题
text:内容
date_added:创建时间

## 当前可访问的页面：
http://127.0.0.1:8000/admin 后台管理
http://127.0.0.1:8000/ 搜索
http://127.0.0.1:8000/search/feedback/ 反馈

## 描述
- 搜索页面可跳转到反馈页面，反馈页面提交后出现提交成功页面，并提供返回至主页的超链接
- 在搜索主页进行搜索，目前可对课程名称、教师和学院三个属性进行检索   
- 支持模糊搜索功能
- 检索功能通过索引实现，并可对新添加的部分自动更新索引（注意：由于haystack rebuild_index功能的限制，只有在管理网站添加的课程可被自动更新，直接对数据库操作无法更新索引，也就无法查找到课程）
- 目前支持对开课院系（如：电院、机动）以及开课学年实现筛选功能

## 管理
管理员账户:123456
管理员密码：123456

---

# 问答

## 标签属性
|属性|说明|
|----|----|
|name|标签名|

## 问题属性
|属性|说明|
|----|----|
|title|标题|
|body|问题详情|
|tags|标签（多对多外键）|
|create_at|创建时间|
|asked_by|提问用户|
|views|被查看次数|

## 回答属性
|属性|说明|
|----|----|
|message|回答内容|
|question|所属问题|
|create_at|创建时间|
|create_by|回答用户|

## 评论属性
|属性|说明|
|----|----|
|message|评论内容|
|answer|所属回答|
|create_at|创建时间|
|create_by|评论用户|

## 当前可访问页面
- http://127.0.0.1:8000/discussion/ 问答主页
- http://127.0.0.1:8000/discussion/question/id/ 问题详情页，id为问题id
- http://127.0.0.1:8000/discussion/ask/ 提问表单

## 描述
主页左侧菜单栏：
- 最新问题按照提问时间排序，热门问题按照问题浏览次数排序。
  - 点击问题可跳转问题详情页，用户可创建新的回答，或点击回答下的`add a comment`添加评论。
  - 点击`Ask Question`按钮跳转至新建问题表单。问题提交后跳转至此问题详情页。
- 问题分类页
  显示问题标签，点击标签名跳转至此标签下的问题列表。

---
# 注册登陆功能
## 登陆
- 输入正确的用户名密码和验证码
- 输入错误会进行提示
- 登陆后跳转到主页
## 注册
- 提供邮箱、用户名、两次相同密码、验证码，且一个邮箱只能对应一个用户名
 在已登录情况下无法注册
- 注册后自动跳转到登录页面

## session
根据session状态判断是否登陆 

## 添加访问限制
未登录情况下无法访问：
- 提问页面
- 问题详情页
进入以上页面时系统出现警示框，提示用户先登录。

## 个人主页
个人主页入口改至登录后右上角的下拉菜单

|选项|说明|
|----|----|
|个人信息|展示用户名称、邮箱、学院、性别等基本信息|
|我的课程|展示用户所选课程|
|问答记录|显示当前用户所提出的问题，以及回答或评论过的问题|
  
---

**编写问题搜索功能的时候修改了haystack下的views.py和urls.py文件，附在根目录下，请注意替换更新本地文件**

**编写模糊查询功能时修改了haystack下的backends文件夹，将search目录下的Chineseanalyzer.py复制到backends中，删除backends中的whoosh_backends并将whoosh_cn_backends复制到backends**
