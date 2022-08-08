import redis
r = redis.Redis(host='localhost', port=6379, db=0, password='root')
# r.set('username', 'ciao da python')
#gradi = r.get('gradi')
# print(gradi)
print( r.keys('*') )
r.close()