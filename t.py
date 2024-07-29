import pygame
def t():
    # Initialize Pygame
    pygame.init()

    # Set up the window
    window_width = 300
    window_height = 300
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tic Tac Toe")

    # Set up the board
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    # Set up the players
    players = ["X", "O"]
    current_player = players[0]

    # Set up the colors
    BLACK = (0, 0, 0)
    GOLD = (238, 173, 14)
    WHITE = (255, 255, 255)

    # Set up the fonts
    font = pygame.font.Font(None, 50)

    # Set up the game loop
    game_over = False
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()
                row = pos[1] // 100
                col = pos[0] // 100
                # Make the move if it's valid
                if board[row][col] == " ":
                    board[row][col] = current_player
                    # Switch to the next player
                    current_player = players[(players.index(current_player) + 1) % len(players)]

        # Draw the board
        window.fill(BLACK)
        for row in range(3):
            for col in range(3):
                # Draw the cell
                pygame.draw.rect(window, GOLD, (col * 100, row * 100, 100, 100), 2)
                # Draw the player's mark if there is one
                mark = font.render(board[row][col], True, GOLD)
                mark_rect = mark.get_rect(center=(col * 100 + 50, row * 100 + 50))
                window.blit(mark, mark_rect)

        # Check for a winner
        winner = None
        # Check rows
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != " ":
                winner = board[row][0]
                break
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                winner = board[0][col]
                break
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            winner = board[0][2]
        # Display the winner if there is one
        if winner:
            message = f"{winner} wins!"
            message_rect = font.render(message, True, GOLD).get_rect(center=(window_width // 2, window_height // 2))
            window.blit(font.render(message, True, GOLD), message_rect)

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()