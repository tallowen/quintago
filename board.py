class quintago:
    board = []
    def __init__(self):
        for i in range(6):
            self.board.append([0,0,0,0,0,0])
            
    def place(self,x,y,color):       
        self.board[x][y] = 1 if color else -1
        
    def get_quadrant(self, number):
        if number not in [-1,0,1]:
            raise Exception("You can only have a value of -1, 0, 1 as the value")
            
        quadrant = []
        for i in (range(3) if number in [1,3] else range(3,6)):
            quadrant.append(self.board[i][0:3] if number in [1,2] else self.board[i][3:6])
            
        return quadrant
        
    def rotate(self, quadrant_number,clockwise):
        old = self.get_quadrant(quadrant_number)
        new = [[],[],[]]
        for x in range(3):
            for y in range(3):
                new[x].append(old[y][2-x])
                
        return new
    
        
    def to_console(self):
        row_number = 0
        for y in range(6):
            row = ''
            for x in range(6):
                row+=str(self.board[x][y])+' '
                if x ==2:
                    row +="| "
                
            print row
            if y == 2:
                print '------x-------'
        
        
        
        
