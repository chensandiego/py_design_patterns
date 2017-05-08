class EventManager(object):

	def __init__(self):
		print("Event Manager: Let me talk to the folds\n")

	def arrange(self):
		self.hotelier=Hotelier()

		self.hotelier.bookHotel()

		self.florist=Florist()
		self.florist.setFlowerRequirements()


		self.caterer=Caterer()
		self.caterer.setCuisine()


		self.musician=Musician()
		self.musician.setMusicType()




class Hotelier(object):
	def __init__(self):
		print('Arrange hotel for marriage')

	def __isAvailable(self):
		print('is the hotel free for the even on given day?')
		return True

	def bookHotel(self):
		if self.__isAvailable():
			print('reg the booking\n')


class Florist(object):
	def __init__(self):
		print('flower decoration for the event?')

	def setFlowerRequirements(self):
		print('Carnations,Roses and Lilies would be used for Decorations\n\n')
	

class Caterer(object):
	def __init__(self):
		print('Food Arrangement for the Event----')

	def setCuisine(self):
		print('Chinese & Continental Cuisine to be served\n\n')
	

class Musician(object):
	def __init__(self):
		print('Musical Arrangement for the Marriage')

	def setMusicType(self):
		print('Jazz and Classical will be played\n\n')


class You(object):
	def __init__(self):
		print("you::Whoa!! Marriage Arrangement?!!!!!")
	def askEventManager(self):
		print("you:lets contact event manager ")
		em=EventManager()
		em.arrange()

	def __del__(sself):
		print("you:thank to event manager,all done")

you=You()
you.askEventManager()

