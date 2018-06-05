'''
基于用户名密码连接
'''
import paramiko
'''
#创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='172.16.10.86',port=22,username='root',password='root123')
#执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
#获取命令结果
result = stdout.read()
print(result)
#关闭连接
ssh.close()
'''
#  SSHClient 封装 Transport

transport = paramiko.Transport(('172.16.10.86',22))
transport.connect(username='root',password='root123')
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()




