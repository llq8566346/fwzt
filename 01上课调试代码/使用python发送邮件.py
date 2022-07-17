

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication # 附件
from email.mime.multipart import MIMEMultipart  #发送多邮件

"""
 账号：994682157@qq.com
 授权：tiwepgerqcbpbfeh
 QQ邮箱：smtp.qq.com  端口：465
"""

#第一步： 连接邮箱smtp服务器并登录
smtp = smtplib.SMTP_SSL(host="smtp.qq.com",port= 465)
smtp.login(user="994682157@qq.com",password="tiwepgerqcbpbfeh")

#第二步：构建一份邮件

#创建一封多组件的邮件
msg = MIMEMultipart()
with open("../report1.html", "rb") as f:
    content = f.read()

# 创建文本内容
text_msg = MIMEText(content,_subtype="html",_charset="utf-8")

# 创建多组件到邮件中
msg.attach(text_msg)

# 创建邮件的附近
report_file = MIMEApplication(content)
report_file.add_header('content-disposition', 'attachment', filename='林亮钦的测试报告.html')

# 将附件添加到多组件的邮件中
msg.attach(report_file)

msg["subject"] = "7月9号的邮件"
msg["from"] = "994682157@qq.com"
msg["To"] = "3247119728@qq.com"

# 第三步： 送邮件

smtp.send_message(msg,from_addr="994682157@qq.com",to_addrs="994682157@qq.com")


