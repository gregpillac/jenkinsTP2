from datetime import datetime

now = date.time.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print "Date : " + dd + "/" + mm + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
