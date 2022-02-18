#coding: UTF-8
import tweepy
import datetime

CK=""
CS=""
AT=""
AS=""

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

TIME = {0:'子三',1:'丑一',2:'丑三',3:'寅一',4:'寅三',5:'卯一',6:'卯三',7:'辰一',8:'辰三',9:'巳一',10:'巳三',11:'午一',12:'午三',13:'未一',14:'未三',15:'申一',16:'申三',17:'酉一',18:'酉三',19:'戌一',20:'戌三',21:'亥一',22:'子一'}

today = datetime.date.today()
now = datetime.datetime.today()
hour = now.hour

#時間でコードを走らせるとする
time = int(hour)

#トゥイート
api.update_status('只今，'+TIME[time]+'津。Twitter for Huawei')