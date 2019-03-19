class moves:

	''' Keeps an array of all the x-y coordinates corresponding
	    to a tile on the grid (e.g tile A1 has coordinates (x1,y1))

	    Then converts the user input to the corresponding
	    x-y values 
	'''

	"""Takes a move that the user inputs and determines the 'from' and 'to' tiles that the user entered. 
	It then converts each of these tiles in the form (a,b), where a and b are between 1 and 8 inclusive.
	E.g. if user wants to jump from A1 to B1, we would convert A1 to (1,1) and B1 to (2,1). We do this in order
	to go into our conversion array and obtain the correpsonding x,y coordinates for each tile.
	We also consider the situation where the user enters 1A or 1B.
	"""
	def convert_move(move_to, move_from):
		if(ord(move_to[0]) < 57 and move_to[0] > 48 ):
			to_y = ord(move_to[0] - 48)
		elif(ord(move_to[0]) < 73 and move_to[0] > 64):
			to_y = ord(move_to[0] - 64)
		if(ord(move_to[1]) < 57 and move_to[1] > 48 ):
			to_x = ord(move_to[1] - 48)
		elif(ord(move_to[1]) < 73 and move_to[1] > 64):
			to_x = ord(move_to[1] - 64)	

		if(ord(move_from[0]) < 57 and move_from[0] > 48 ):
			from_y = ord(move_from[0] - 48)
		elif(ord(move_from[0]) < 73 and move_from[0] > 64):
			from_y = ord(move_from[0] - 64)
		if(ord(move_from[1]) < 57 and move_from[1] > 48 ):
			from_x = ord(move_from[1] - 48)
		elif(ord(move_from[1]) < 73 and move_from[1] > 64):
			from_x = ord(move_from[1] - 64)	

		array = create_conversion_array()

		to_coord = array[to_x -1][to_from-1]
		from_coord = array[from_x-1][from_y-1]
		
		return to_coord, from_coord

	def create_conversion_array():
		array1 = []
		for column in range(0,8):
    			array1.append([])
			
		for column in range(0,8):
    			for count in range(0,8):
        			array1[count].append([])

		for column in range(0,8):
   			for row in range(0,8):
        			for coord in range (0,2):
            				array1[column][row].append([])
            
		for column in range(0,8):
    			for row in range(0,8):
        			for coord in range (0,2):
            				array1[column][row][0] = (2*row +1) * 37.5
            				array1[column][row][1] = (2*column +1) * 37.5
				
		return array1	
			



	
