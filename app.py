import json
from flask import Flask, request, jsonify

app = Flask(__name__)

#Initialisation Testings
# input_json = {"positions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}}
# input_json = {"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}
# input_json = {"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}}

# slug = "Knight"
# slug = "Queen"
# slug = "Rook"


def fetch_chess_moves(board, piece, valid_pieces, row, col, slug_move=False):
    mark_pos = []

    def mark_position(r, c):
        if(slug_move):
            pass
        else:
            if board[r][c] == '0':
                board[r][c] = '1'


    def pawn_moves():
        if (row>0):
            mark_position(row - 1, col)
            if (col>0) and slug_move:
                if(board[row-1][col-1] in valid_pieces):
                    temp =[]
                    temp.append(row-1)
                    temp.append(col-1)
                    mark_pos.append(temp)

                mark_position(row - 1, col - 1)
                
            if (col<7) and slug_move:
                if(board[row-1][col+1] in valid_pieces):
                    temp =[]
                    temp.append(row-1)
                    temp.append(col+1)
                    mark_pos.append(temp)

                mark_position(row - 1, col + 1)


    def rook_moves():
        c = col
        r = row 
        while(c>0):
            c-=1
            if(slug_move):
                if(board[row][c] == '0'):
                    mark_pos.append([c,row])
                if(board[row][c] in valid_pieces):

                    mark_pos.append([c,row])
            if(board[row][c] in valid_pieces):
                break
            mark_position(row,c)
            


        c = col
        r = row 
        while(c<7):
            c+=1
            if(slug_move):
                if(board[row][c] == '0'):
                    mark_pos.append([c,row])
                if(board[row][c] in valid_pieces):

                    mark_pos.append([c,row])
            if(board[row][c] in valid_pieces):
                break
            mark_position(row,c)
            
        c = col
        r = row
        while(r>0):
            r-=1
            if(slug_move):
                if(board[r][col] == '0'):
                    mark_pos.append([col,r])
                if(board[r][col] in valid_pieces):

                    mark_pos.append([col,r])
                    break
            if(board[r][col] in valid_pieces):
                break
            mark_position(r,col)
            
        c = col
        r = row
        while(r<7):
            r+=1
            if(slug_move):
                if(board[r][col] == '0'):
                    mark_pos.append([col,r])
                if(board[r][col] in valid_pieces):

                    mark_pos.append([col,r])
                    break
            if(board[r][col] in valid_pieces):
                break
            mark_position(r,col)
            

    def knight_moves():
        knight_moves = [(row + 2, col + 1), (row + 2, col - 1),
                        (row - 2, col + 1), (row - 2, col - 1),
                        (row + 1, col + 2), (row + 1, col - 2),
                        (row - 1, col + 2), (row - 1, col - 2)]
        if(slug_move):
            for r,c in knight_moves:
                if(r>=0 and c<8):
                    if(board[r][c] == '0'):
                        mark_pos.append([r,c])
                    if(board[r][c] in valid_pieces):
    
                        mark_pos.append([r,c])
        else:
            for r , c in knight_moves:
                if(r>=0 and c<8):
                    mark_position(r, c)

    def bishop_slug(r,c):
        check_if_can_attack = 0
        check_if_one = 0
        if(slug_move):
            if((board[r][c] in valid_pieces)):
                check_if_can_attack = 1
                mark_pos.append([c,r])
            if(board[r][c] == '1'):
                check_if_one = 1
            if(board[r][c] == '0'):
                # if(check_if_one == 0):
                mark_pos.append([c,r])
        
        return check_if_can_attack, check_if_one

    def bishop_moves():
        c = col 
        r = row
        while(c>0 and r>0):
            c = c-1
            r = r-1
            if(slug_move):
                check_if_can_attack, check_if_one = bishop_slug(r,c)
                if check_if_can_attack:
                    break
            if(board[r][c] in valid_pieces):
                break
            mark_position(r,c)
        
        c = col 
        r = row
        while(c<7 and r>0):
            c+=1
            r-=1
            if(slug_move):
                check_if_can_attack, check_if_one = bishop_slug(r,c)
                if check_if_can_attack:
                    break
            if(board[r][c] in valid_pieces):
                break
            mark_position(r,c)
            

        c = col 
        r = row
        while(c>0 and r<7):
            c-=1
            r+=1
            if(slug_move):
                check_if_can_attack, check_if_one = bishop_slug(r,c)
                if check_if_can_attack:
                    break
            if(board[r][c] in valid_pieces):
                break
            mark_position(r,c)
            

        c = col 
        r = row
        while(c<7 and r<7):
            c+=1
            r+=1
            if(slug_move):
                check_if_can_attack, check_if_one = bishop_slug(r,c)
                if check_if_can_attack:
                    break
            if(board[r][c] in valid_pieces):
                break
            mark_position(r,c)
            
                    

    def queen_moves():
        rook_moves()
        bishop_moves()

    def king_moves():
        king_moves = [(row + 1, col), (row - 1, col),
                        (row, col + 1), (row, col - 1),
                        (row + 1, col + 1), (row + 1, col - 1),
                        (row - 1, col + 1), (row - 1, col - 1)]
        if(slug_move):
            for r, c in king_moves:
                if(board[r][c] == '0'):
                        mark_pos.append([r,c])
                if(board[r][c] in valid_pieces):

                    mark_pos.append([r,c])
        else:
            for r, c in king_moves:
                mark_position(r, c)


    if piece == 'Pawn':
        pawn_moves()
    elif piece == 'Rook':
        rook_moves()
    elif piece == 'Knight':
        knight_moves()
    elif piece == 'Bishop':
        bishop_moves()
    elif piece == 'Queen':
        queen_moves()
    elif piece == 'King':
        king_moves()

    if(slug_move):
        return mark_pos


# Code start 

@app.route('/chess/<slug>', methods=['POST'])
def calculate_chess_moves(slug):
    columns = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    board = [['0' for _ in range(8)] for _ in range(8)]
    slug = slug.capitalize()
    valid_pieces = ["Queen", "Bishop", "Rook", "Knight", "King", "Pawn"]
    if slug not in valid_pieces:
        return jsonify({'error': 'Invalid chess piece'}), 400

    # input_json = {"positions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}}
    # input_json = {"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}
    # input_json = {"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}}
    
    input_json = request.get_json()
    if not input_json or 'positions' not in input_json:
        return jsonify({'error': 'Invalid input JSON'}), 400

    positions = input_json['positions']
    
    # Loop through positions and marking chess pieces on board
    for piece, position in positions.items():
        row = int(position[1]) - 1
        col = columns[position[0]]

        board[row][col] = piece


    # Loop through Black Pieces and mark their positions
    for piece, position in positions.items():
        row = int(position[1]) - 1
        col = columns[position[0]]
        if(piece != slug):
            fetch_chess_moves(board, piece, valid_pieces, row, col)


    #Now make move for Slug
    row = int(positions[slug][1]) - 1
    col = columns[positions[slug][0]]

    result = fetch_chess_moves(board, slug, valid_pieces, row, col,slug_move=True)

    assert(result)
    notarised_result = []
    for pos in result:
        col = pos[0]
        row = pos[1] + 1
        row_character = list(columns.keys())[col] 
        notarised_result.append(f"{row_character}{row}")

    assert(notarised_result)
    
    return jsonify({'valid_moves': notarised_result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # calculate_chess_moves("bishop")


