from datetime import datetime

class MyDateTime(datetime):
    def __int__(self):
        return int(self.timestamp())
		
d = MyDateTime.now()
d
int(d)