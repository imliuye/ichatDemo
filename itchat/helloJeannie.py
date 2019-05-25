import itchat
### 你想要给文件传输助手发一条信息，只需要这样：
##itchat.auto_login(hotReload=True)
##itchat.send('Hello HanBaoBao, this is an automatic test from itchat',\
##            toUserName='liuyucen1989')
##

##如果你想要回复发给自己的文本消息，只需要这样：
'''
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text + 'success'

itchat.auto_login()
itchat.run()
'''



##过打印itchat的用户以及注册消息的参数，可以发现这些值都是字典。
##
##但实际上itchat精心构造了相应的消息、用户、群聊、公众号类。
##
##其所有的键值都可以通过这一方式访问：
itchat.auto_login(hotReload=True)
itchat.send('Hello HanBaoBao, this is an automatic test from itchat',\
            toUserName='filehelper')

'''
@itchat.msg_register(TEXT)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)
##属性名为键值首字母小写后的内容。
authors = itchat.search_friends(nickName='LittleCoder')
print(authors)
if authors:
	print('author find');
	author = authors[0]
	author.send('greeting, Jeannie!')
'''
