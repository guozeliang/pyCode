import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
import os.path
from configs import configs
import time
import requests
import json

class alarm(object):
    def __init__(self):
        con = configs()
        sendInfo = con.getSendInfo()
        self.mysender = sendInfo['mysender']  # 发件人邮箱账号
        self.mypass = sendInfo['mypass']  # 发件人邮箱密码
        self.myuser = sendInfo['myuser']  # 收件人邮箱账号，我这边发送给自己
        mailInfo = con.getMailInfo()
        self.mailcontent = mailInfo['mailcontent']
        self.mailtitle = mailInfo['mailtitle']
        self.messageurl = con.getMessgeUrl()

    def sendmail(self):
        ret = True
        try:
            msg = MIMEText(self.mailcontent, 'plain', 'utf-8')
            msg['From'] = formataddr(["FromRunoob", self.mysender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["FK", self.myuser])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = self.mailtitle  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.mysender, self.mypass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.mysender, [self.myuser, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    def sendMutiMail(self):
        ret = True
        try:
            # 创建一个带附件的实例
            message = MIMEMultipart()
            message['From'] = Header(self.mysender, 'utf-8')# 括号里的对应发件人邮箱昵称、发件人邮箱账号
            message['To'] = Header(self.myuser, 'utf-8')# 括号里的对应收件人邮箱昵称、收件人邮箱账号
            message['Subject'] = Header(self.mailtitle, 'utf-8')# 邮件的主题，也可以说是标题

            # 邮件正文内容
            message.attach(MIMEText(self.mailcontent, 'plain', 'utf-8'))

            # 构造附件1，传送当前目录下的 test.txt 文件
            log_path = os.path.dirname(os.getcwd()) + '\\logs\\'
            # 创建一个handler，用于写入日志文件
            rq = time.strftime('%Y-%m-%d', time.localtime())
            log_name = log_path + rq + '.log'
            att1 = MIMEText(open(log_name, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="{}.log"'.format(rq)
            message.attach(att1)

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.mysender, self.mypass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.mysender, [self.myuser, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except:
            ret = False
        return ret

    def semdMessage(self):
        body = self.con.getMessageInfo()
        headers = {'content-type': "application/json"}
        data = json.dumps(body)
        response = requests.post(self.messageurl, data=json.dumps(body), headers=headers)
        # 也可以直接将data字段换成json字段，2.4.3版本之后支持
        # response  = requests.post(url, json = body, headers = headers)
        # 返回信息
        print(response.text)
        # 返回响应头
        print(response.status_code)


if __name__ == '__main__':
    sendmessage = alarm()
    # ret = sendmessage.sendmail()
    # if ret:
    #     print("邮件发送成功")
    # else:
    #     print("邮件发送失败")
    try:
        sendmessage.sendMutiMail()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")