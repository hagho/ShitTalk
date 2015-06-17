#coding=utf-8
import redis
import json
'''
class Redis_Talk:
    def __init__(self,id,content,like,comment_num):
        self.id=id
        self.content=content
        self.like=like
        self.comment_num=comment_num
    def print_talk(self):
        print self.id
        
    


def redis_write(room,talk):   
	key = room
	val = talk  
	r = redis.StrictRedis(host='127.0.0.1',port=6380)  
	r.sadd(key,talk)  

		
def redis_read(room):  

    key = room  
    r = redis.StrictRedis(host='127.0.0.1',port=6380)  
    value = r.smembers(room)

    if value==set():
        print "value is"
        print value
        return None
    	
	print value
    return value  

	
def redis_clean():
    r = redis.StrictRedis(host='127.0.0.1',port=6379)
    r.flushdb()
	
'''

class RedisCache(object):
    def __init__(self,keyname):
        self.keyName = keyname
        self.host = '127.0.0.1'
        self.port = 6380
        self.re =  redis.StrictRedis(host='127.0.0.1',port=6380)  
    
    def insertRedis(self,jsonStr):
        self.re =  redis.StrictRedis(host='127.0.0.1',port=6380)
        self.re.lpush(self.keyName,jsonStr)
        
    def getFromRedis(self):
        self.re = redis.StrictRedis(host='127.0.0.1',port=6380)

        #print self.re.get(self.keyName)
        #print 'fuck'
        #if self.re.get(self.keyName):
        #    return False
        arr = self.re.lrange(self.keyName,0,-1)

        #print 'fuck'
        if len(arr)==0:
            return False
        #for i in range(0,len(arr)):
            #arr[i] = json.loads(arr[i])
            #print arr[i] 
            #print arr[i]['id'],arr[i]['content'],arr[i]['like_num'],arr[i]['content_num'],'\n'				
        return arr
		
		
'''     
if __name__=='__main__':
    redisTest = RedisTest()
#    json = ['{"id":"1","src_ip":"1.1.1.1","dst_ip":"any","port":"8080"}','{"id":"2","src_ip":"1.1.1.1","dst_ip":"any","port":"8080"}']
#    for item in json:
#        redisTest.insertRedis(item)
#        print 'done!\n'
    redisTest.getFromRedis()
'''