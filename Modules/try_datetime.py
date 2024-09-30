import datetime
import pytz

ct = datetime.datetime.now(pytz.timezone('US/Central'))
tpe = datetime.datetime.now(pytz.timezone('Asia/Taipei'))

print(ct.strftime('%Y-%m-%dT%H:%M:%S:%f%Z'))
print(tpe.strftime('%Y-%m-%dT%H:%M:%S:%f%Z'))