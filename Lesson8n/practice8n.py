userLogs=['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']
userPass=['111','abc','2345','45fg','dffdg']

for log, passw in zip(userLogs,userPass):
    print("login: {} — password: {}".format(log,passw))

