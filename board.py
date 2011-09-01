from numpy import array
from numpy import zeros
from numpy import rot90
class quintago:
    board = array(36*(0,))
    def __init__(self):
    	self.board.shape = (6,6)
                
    def place(self,y,x,color):       
        if x not in range(0,6):
            raise Exception("You can only have an x value within 0-5")
        if y not in range(0,6):
            raise Exception("You can only have an y value within 0-5")
        if color not in [True,False]:
            raise Exception("You can only have a color with True,False as a valuehin 0-5")
        self.board[y,x] = 1 if color else -1
     
    def rotate(self,quadrant_number,clockwise):
    	r = 3 if clockwise else 1
    	if quadrant_number ==1:
    		self.board[0:3,0:3] = rot90(self.board[0:3,0:3].copy(),r)
    	elif quadrant_number == 2:
    		self.board[0:3,3:6] = rot90(self.board[0:3,3:6].copy(),r)
    	elif quadrant_number == 3:
    		self.board[3:6,0:3] = rot90(self.board[3:6,0:3].copy(),r)
    	else:
    		self.board[3:6,3:6] = rot90(self.board[3:6,3:6].copy(),r)
    		     
    def __repr__(self):
    	return self.board.__repr__()

    
"""
    def get_quadrant(self, number):
        if number not in [1,2,3,4]:
            raise Exception("You can only choose a quadrant with [1,2,3,4] as value")
        
        #quadrant = zeros(shape(3,3),dtype='int')
        if number == 1:
        	return self.board[0:3,0:3]
    	elif number == 2:
    		return self.board[0:3,3:6]
    	elif number == 3:
    		return self.board[3:6,0:3]
    	else:
    		return self.board[3:6,3:6]
    		"""
        
        
        
