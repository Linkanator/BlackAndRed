class move:

	''' Keeps an array of all the x-y coordinates corresponding
	    to a tile on the grid (e.g tile A1 has coordinates (x1,y1))

	    Then converts the user input to the corresponding
	    x-y values 
	'''

	def __init__(self, move_to, move_from):
		self.move_to = move_to
		self.move_fom = move_from
	
	def create_conversion_array(self):
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
            				array1[column][row][0] = (2*row +1) * 25
            				array1[column][row][1] = (2*column +1) * 25
				
			
			



	
