import math


class movieKNN:
	def __init__(self):
		# bag of words document vectors
		self.movieList{movieName: {} } #########this needs to hold the vector spaces for all of the features we want

	def predict(self, moviename):##### we need the name of the movie so we can make a new vector for it

		givenvector = {}

		######Need these to store the winning movie
		mov1 = "None"
		mov2 = "None"
		mov3 = "None"
		win1 = 0
		win2 = 0
		win3 = 0


		#####need to make our given movies vector space
		for movie in self.movieList:
			if movie == moviename:
				givenvector = self.movieList[movie]

		if givenvector == {}:#####just some basic error checking to make sure we found a movie
			print("Movie not found. Please check that you entered the official movie title.")
			quit()
		####this is the best way I found to set a value at a specific entry location in a dict
		key = list(givenvector)[0]
		givenvector[key] = 20######### we need to set to what ever value we want
		key = list(givenvector)[1]
		givenvector[key] = 5  ######### we need to set to what ever value we want
		key = list(givenvector)[2]
		givenvector[key] = 3  ######### we need to set to what ever value we want
		key = list(givenvector)[3]
		givenvector[key] = 10  ######### we need to set to what ever value we want
		key = list(givenvector)[4]
		givenvector[key] = 10  ######### we need to set to what ever value we want

		for movie in self.movieList:####now we need to set up the movie vectors and run the comparisons
			bmovie = self.movieList[movie]####get the dict for current movie
			if list(givenvector)[0] == list(bmovie)[0]:
				key = list(bmovie)[0]
				bmovie[key] = 1
			if list(givenvector)[1] == list(bmovie)[1]:
				key = list(bmovie)[1]
				bmovie[key] = 1
			if list(givenvector)[2] == list(bmovie)[2]:
				key = list(bmovie)[2]
				bmovie[key] = 1
			if list(givenvector)[3] == list(bmovie)[3]:
				key = list(bmovie)[3]
				bmovie[key] = 1
			if list(givenvector)[4] == list(bmovie)[4]:
				key = list(bmovie)[4]
				bmovie[key] = 1
			####start the knn equation
			abot = 0
			for word in givenvector:
				abot += givenvector[word] * givenvector[word]
			asbot = math.sqrt(abot)

			bbot = 0
			for word in bmovie:
				bbot += bmovie[word] * bmovie[word]
			bsbot = math.sqrt(bbot)

			bot = bsbot * asbot
			top = 0
			for word in givenvector:######this section might be scuffed or redundant since we already did a comparison
				for word2 in bmovie:
					if word == word2:
						top += givenvector[word] * bmovie[word]

			##########determine a minner
			simularity = top/bot
			if simularity > win1:
				win3 = win2
				mov3 = mov2
				win2 = win1
				mov2 = mov1
				win1 = simularity
				mov1 = movie
			elif simularity > win2:
				win3 = win2
				mov3 = mov2
				win2 = simularity
				mov2 = movie
			elif simularity > win3:
				win3 = simularity
				mov3 = movie

		#####print the winning movies
		print(mov1)
		print(mov2)
		print(mov3)