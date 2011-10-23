import nose
import quint

def test_working():
    board = quint.quintago()
    board.set(0,0,True)
    board.set(1,0,True)
    board.set(2,0,True)
    board.set(5,0,True)
    board.set(5,1,True)
    board.rotate(3,True)
    
    board.set(1,1,False)
    board.set(2,2,False)
    board.set(3,3,False)
    board.set(4,4,False)
    board.set(5,5,False)

    print board
    assert board.winner()==2
    
def test_wierd_diagonal():
    board = quint.quintago()

    board.set(0,0,True)
    board.set(1,0,True)
    board.set(2,0,True)
    board.set(5,0,True)
    board.set(5,1,True)
    board.rotate(3,True)
    
    board.set(0,5,False)
    board.set(1,4,False)
    board.set(2,3,False)
    board.set(3,2,False)
    board.set(4,1,False)
    
    print board
    assert board.winner()==2
    
    
def test_nobody_has_won():
    board = quint.quintago()
    board.set(0,0,True)
    board.set(1,0,True)
    board.set(2,0,False)
    board.set(5,0,True)
    board.set(5,1,True)
    board.rotate(3,True)

    print board
    assert board.winner()==0
    
def test_one_has_won():
    board = quint.quintago()
    board.set(0,0,True)
    board.set(1,0,True)
    board.set(2,0,True)
    board.set(5,0,True)
    board.set(5,1,True)
    board.rotate(3,True)
    
    print board
    assert board.winner()==1
    
    
def sanitize(code):
    if code==0:
        return "No winners"                
    elif code==2:
        return "Tie game!"
    elif code==-1:
        return "-1 wins!"
    elif code ==1:
        return "1 wins!"
    
    
'''  

if __name__ == "__main__":
    import quint
    board = quint.quintago()
    board2 = quint.quintago()
    board3 = quint.quintago()
    board4 = quint.quintago()
    runnerfoo(board)
    test_wierd_diagonal(board2)
    test_nobody_has_won(board3)
    one_has_won(board4)

'''
    