from abc import ABCMeta,abstractmethod
class Payment():
	@abstractmethod
	def do_pay(self):
		pass

class Bank(Payment):
	def __init__(self):
		self.card=None
		self.account=None 


	def __getAccount(self):
		self.account=self.card 
		return self.account

	def __hasFunds(self):
		print("Bank:: check if account",self.__getAccount(),"has enough funds")
		return True 


	def setCard(self,card):
		self.card=card 


	def do_pay(self):
		if self.__hasFunds():
			print ('bank paying the merchant')
			return True 

		else:
			print('bank sorry not enough funds')
			return False


class DebitCard(Payment):
	def __init__(self):
		self.bank=Bank()
	def do_pay(self):
		card=input("Proxy:punch in card num")
		self.bank.setCard(card)
		return self.bank.do_pay()


class You(object):
	def __init__(self):
		print("you:: lets buy the Denim shirt")
		self.debitCard=DebitCard()
		self.isPurchased=None 

	def make_payment(self):
		self.isPurchased=self.debitCard.do_pay()

	def __del__(self):
		if self.isPurchased:
			print('the shirt i mine)')
		else:
			print("you: i should earn more")



you=You()
you.make_payment()


