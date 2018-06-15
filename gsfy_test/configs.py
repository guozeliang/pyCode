from configparser import ConfigParser

class configs(object):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini",encoding="utf-8-sig")
        self.tomcatDict = dict(self.config.items('tomcats_config'))
        self.testUrl = self.config.get('testurl_config', 'testurl')
        self.nginxName = self.config.get('nginx_config', 'nginxserivcename')
        self.nginxPath = self.config.get('nginx_config', 'nginxpath')
        self.tomcatUrlDict = dict(self.config.items('tomcats_url_config'))
        self.startTimeout = self.config.get('timout_config', 'tomcattimeout')
        self.titalTimeout = self.config.get('timout_config', 'titaltimeout')

    def getConfigs(self):
        return self.tomcatDict, self.testUrl, self.nginxName, self.nginxPath, self.tomcatUrlDict, self.startTimeout, self.titalTimeout

    def getTomcatConf(self):
        return self.tomcatDict

    def getSendInfo(self):
        sendInfo = dict(self.config.items('mail_send_config'))
        return sendInfo

    def getMailInfo(self):
        mailInfo = dict(self.config.items('mail_info_config'))
        return mailInfo

    def getMessgeUrl(self):
        messageurl = self.config.get('message_config', 'messageurl')
        return messageurl

    def getMessageInfo(self):
        messageInfo =dict(self.config.items('message_content_config'))
        return messageInfo

con = configs()
con.getMailInfo()
