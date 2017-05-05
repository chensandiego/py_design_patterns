import sqlite3
class MetaSingleon(type):
	_instances={}
	def __call__(cls,*args,**kwargs):
		if cls not in cls._instances:
			cls._instances[cls]=super(MetaSingleon,cls).__call__(*args,**kwargs)
		return cls._instances[cls]
		


class Database(metaclass=MetaSingleon):
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection=sqlite3.connect("db.sqlite3")
			self.cursorobj=self.connection.cursor()
		return self.cursorobj



db1=Database().connect()
db2=Database().connect()



print ("db obj db1",db1)

print ("db obj db2",db2)