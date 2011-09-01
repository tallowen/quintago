from numpy import array
from numpy import zeros
from numpy import rot90
class board:

    def __init__(self):
        self.board_array = array(36*(0,))
    	self.board_array.shape = (6,6)
                
    def set(self,y,x,color):       
        if x not in range(0,6):
            raise Exception("You can only have an x value within 0-5")
        if y not in range(0,6):
            raise Exception("You can only have an y value within 0-5")
        if color not in [True,False]:
            raise Exception("You can only have a color with True,False as a value in 0-5")
        self.board_array[y,x] = 1 if color else -1
     
    def rotate(self,quadrant_number,clockwise):
        if quadrant_number not in range(1,5):
            raise Exception("There is not such quadrant")
    	r = 3 if clockwise else 1
    	
    	if quadrant_number ==1:
    		self.board_array[0:3,0:3] = rot90(self.board_array[0:3,0:3].copy(),r)
    	elif quadrant_number == 2:
    		self.board_array[0:3,3:6] = rot90(self.board_array[0:3,3:6].copy(),r)
    	elif quadrant_number == 3:
    		self.board_array[3:6,0:3] = rot90(self.board_array[3:6,0:3].copy(),r)
    	else:
    		self.board_array[3:6,3:6] = rot90(self.board_array[3:6,3:6].copy(),r)
    		     
    def __repr__(self):
    	return self.board_array.__repr__()

 
class quintago(board):
    def winner(self):
        """
        Winner winner, chicken dinner
        Return codes:
        -1: negative one won
        0: Nobody has won
        1: positive one has won
        2: both players have won (tie!)
        
        
        """  
        rows=[]
        #Check rows
        for i in range(6):
            rows.append(self.board_array[i,0:6])
      
        #Check Columns
        for i in range(6):
            rows.append(self.board_array[0:6,i]) 
            
            
           
        start_points = [(0,0),(0,1),(1,0)]
        for point in start_points:
            row = []
            for i in range(5):
                row.append(self.board_array[point[0]+i,point[1]+i])
                 
            try:
                row.append(self.board_array[point[0]+5,point[1]+5])
            except IndexError:
                pass

            rows.append(row)
            
            
        start_points = [(0,6),(0,5),(1,6)]
        for point in start_points:
            row = []
            for i in range(5):
                row.append(self.board_array[point[0]+i,5-point[1]-i])       
            try:
                row.append(self.board_array[point[0]+5,5-point[1]-5])
            except IndexError:
                pass

            rows.append(row)
            
        
        minus_one = False
        positive_one = False    
        for row in rows:
            return_value = self.__check_row__(row)
            
            if not return_value[0]:
                continue    
            elif return_value[1]==-1:
                minus_one = True
            elif return_value[1]==1:
                positive_one=True
        
        if not minus_one and not positive_one:
            return 0                
        elif minus_one and positive_one:
            return 2
        elif minus_one:
            return -1
        elif positive_one:
            return 1
         
            

                    
    def __check_row__(self,row):
        """
        Checks if a set of numbers (row) contains a 5 in a row
        Return codes are as follows:
        (false,0) No winners
        (True, <winnin value>) Winner!
        """
        previous = 0
        count = 0
        for i, value in enumerate(row):
            if value == 0:
                count = 0
            elif value == previous:
                count += 1
                if count==5:
                    return (True,value)
            else:
                count=1
            
            
            previous = value
            
        return(False,0)
                    
            
        
        
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
        
        
        
