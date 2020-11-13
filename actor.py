import queue
import threading
import copy

class eventQ:
	def __init__(self):
		self.raq=queue.Queue()
	def send(self,event):
		self.raq.put(event)
	def get(self):
		return self.raq.get()

class Actor(threading.Thread):
	def setmq(self,mq):
		self.mq=mq
	def exit(self,exitcode):
		self.exitcode=exitcode
		self.running=False
	def run(self):
		self.running=True
		self.rstate={}
		while self.running:
			msg=self.mq.get()
			self.state=copy.deepcopy(self.rstate)
			self.resolve_msg(msg)
			self.rstate=copy.deepcopy(self.state)
	def resolve_msg(self,msg):
		pass
	def startactor(self):
		mq=eventQ()
		self.setmq(mq)
		self.start()
		return mq
