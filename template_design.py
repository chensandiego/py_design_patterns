from abc import abstractmethod,ABCMeta


class Trip(metaclass=ABCMeta):
	@abstractmethod
	def setTransport(self):
		pass

	@abstractmethod
	def day1(self):
		pass


	@abstractmethod
	def day2(self):
		pass



	@abstractmethod
	def day3(self):
		pass
		

	@abstractmethod
	def returnHome(self):
		pass


	def itinerary(self):
		self.setTransport()
		self.day1()
		self.day2()
		self.day3()
		self.returnHome()


class VeniceTrip(Trip):
	def setTransport(self):
		print('take a boat and find your way in the grand canal')

	def day1(self):
		print("visit st mark basilica in st mark square")
		

	def day2(self):
		print("Appreciate dog palace")
		

	def day3(self):
		print("Enjoy food near the rialto bridge")

	def returnHome(self):
		print('get souvenirs for friends and get back')



class MaldivesTrip(Trip):
	def setTransport(self):
		print("on food,on any island")
		
	def day1(self):
		print("enjoy the marine life of banana reef")

		

	def day2(self):
		print("go for the water sports and snorkelling")
		

	def day3(self):
		print("relax on the beach and enjoy the sun")

	def returnHome(self):
		print('do not feel like leaving the beach')



class TravelAgency:
	def arrange_trip(self):
		choice=input('what kind of place you like to go historical or to a beach?')
		if choice=='historical':
			self.trip=VeniceTrip()
			self.trip.itinerary()
		if choice=='beach':
			self.trip=MaldivesTrip()
			self.trip.itinerary()

TravelAgency().arrange_trip()	
