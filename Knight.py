def knight_moves(position):
    column_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    row_map = {v: k for k, v in column_map.items()}
    
    col = column_map[position[0].lower()]
    row = int(position[1])
    
    
    offsets = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    
    possible_moves = []
    for offset in offsets:
        new_col = col + offset[0]
        new_row = row + offset[1]
        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            possible_moves.append(row_map[new_col] + str(new_row))
    
    return possible_moves



current_position = "e4"  
moves = knight_moves(current_position)
print(f"Possible moves for the knight from {current_position}: {moves}")