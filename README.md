CourseDiscussion
==
2020-Spring-SoftwareEngineering
--
#
搜索：

##
课程属性：
name:课程名称
teacher:授课教师
institute:开课学院
credit:学分
semester:开课学年
time:上课时间
location:上课地点
date_added:创建时间

##
反馈属性：
title:标题
text:内容
date_added:创建时间

##
当前可访问的页面：
http://127.0.0.1:8000/admin 后台管理
http://127.0.0.1:8000/ 搜索
http://127.0.0.1:8000/search/feedback/ 反馈

##
描述
搜索页面可跳转到反馈页面，反馈页面提交后出现提交成功页面，并提供返回至主页的超链接
在搜索主页进行搜索，目前可对课程名称、教师和学院三个属性进行检索   暂不支持模糊搜索功能
检索功能通过索引实现，并可对新添加的部分自动更新索引（注意：由于haystack rebuild_index功能的限制，只有在管理网站添加的课程可被自动更新，直接对数据库操作无法更新索引，也就无法查找到课程）

##
管理
管理员账户:123456
管理员密码：123456
