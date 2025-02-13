import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen width and height
width = 600
height = 400

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_gray = (40, 40, 40)  # New color for background pattern

# Create game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake block size
block_size = 10

# Clock for controlling speed
clock = pygame.time.Clock()
# Define speeds for different modes
EASY_SPEED = 10
MEDIUM_SPEED = 15
HARD_SPEED = 25
speed = MEDIUM_SPEED  # default speed

# Font for messages
font = pygame.font.SysFont("bahnschrift", 25)
title_font = pygame.font.SysFont("bahnschrift", 50)

def message(msg, color, x, y):
    text = font.render(msg, True, color)
    screen.blit(text, [x, y])

def show_score(score):
    # Create score text
    score_text = font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect()
    
    # Create box dimensions
    padding = 10
    box_width = score_rect.width + (padding * 2)
    box_height = score_rect.height + (padding * 2)
    
    # Position box in top-right corner
    box_x = width - box_width - 20
    box_y = 20
    
    # Draw box
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, dark_gray, box_rect)
    pygame.draw.rect(screen, white, box_rect, 2)  # Border
    
    # Draw score text inside box
    screen.blit(score_text, (box_x + padding, box_y + padding))

def draw_snake(snake_list):
    # Draw body segments (all except head)
    for block in snake_list[:-1]:
        pygame.draw.circle(screen, green, (int(block[0] + block_size/2), int(block[1] + block_size/2)), block_size/2)
    # Draw head (last segment) in blue
    if snake_list:
        head = snake_list[-1]
        pygame.draw.circle(screen, blue, (int(head[0] + block_size/2), int(head[1] + block_size/2)), block_size/2)

def draw_background():
    # Draw a grid pattern for a classier look
    cell_size = 20
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, dark_gray, rect, 1)

def draw_mode_box(text, color, x, y, selected=False):
    # Create text
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    # Create box dimensions
    padding = 15
    box_width = text_rect.width + (padding * 2)
    box_height = text_rect.height + (padding * 2)
    
    # Center box at given x, y coordinates
    box_x = x - box_width/2
    box_y = y - box_height/2
    
    # Draw box
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, dark_gray, box_rect)
    pygame.draw.rect(screen, color, box_rect, 2)  # Border
    
    # Draw text inside box
    screen.blit(text_surface, (box_x + padding, box_y + padding))

def select_mode():
    mode_selected = False
    while not mode_selected:
        screen.fill(black)
        draw_background()
        
        # Draw title higher up with more margin
        message("Select Difficulty:", white, width/3, height/6)  # Changed from height/4
        
        # Draw mode boxes with increased vertical spacing
        center_x = width/2
        draw_mode_box("Press 1 for Easy", green, center_x, height/2 - 60)
        draw_mode_box("Press 2 for Medium", blue, center_x, height/2)
        draw_mode_box("Press 3 for Hard", red, center_x, height/2 + 60)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return EASY_SPEED
                if event.key == pygame.K_2:
                    return MEDIUM_SPEED
                if event.key == pygame.K_3:
                    return HARD_SPEED

def welcome_screen():
    welcome = True
    while welcome:
        screen.fill(black)
        draw_background()
        
        # Draw title
        title_text = title_font.render("Welcome to Snake Game", True, green)
        title_rect = title_text.get_rect(center=(width/2, height/3))
        screen.blit(title_text, title_rect)
        
        # Draw "Press SPACE to start" message
        message("Press SPACE to start", white, width/3, height/2 + 50)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

def show_scoreboard(scores):
    screen.fill(black)
    draw_background()
    
    # Draw title
    title_text = title_font.render("High Scores", True, green)
    title_rect = title_text.get_rect(center=(width/2, height/6))
    screen.blit(title_text, title_rect)
    
    # Display scores
    start_y = height/3
    for i, score in enumerate(sorted(scores, reverse=True)[:5]):  # Show top 5 scores
        score_text = font.render(f"{i+1}. {score}", True, white)
        score_rect = score_text.get_rect(center=(width/2, start_y + i*40))
        screen.blit(score_text, score_rect)
    
    message("Press SPACE to continue", white, width/3, height*3/4)
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def show_game_over(score):
    screen.fill(black)
    draw_background()
    
    # Draw "Game Over" title
    title_text = title_font.render("Game Over", True, red)
    title_rect = title_text.get_rect(center=(width/2, height/4))
    screen.blit(title_text, title_rect)
    
    # Draw final score
    score_text = title_font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect(center=(width/2, height/2))
    screen.blit(score_text, score_rect)
    
    # Draw restart button
    draw_mode_box("Press SPACE to Restart", green, width/2, height*3/4)
    
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def game_loop():
    game_over = False
    game_close = False
    
    while True:  # Main game loop
        x = width / 2
        y = height / 2
        x_change = 0
        y_change = 0
        
        snake_list = []
        snake_length = 1
        
        # Show welcome screen
        welcome_screen()
        
        # Get speed from mode selection
        global speed
        speed = select_mode()
        
        food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        
        game_over = False
        game_close = False
        
        while not game_over:
            while game_close:
                show_game_over(snake_length - 1)
                game_close = False
                game_over = True  # Break out to restart the game
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = block_size
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -block_size
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = block_size
                        x_change = 0
            
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True
            
            x += x_change
            y += y_change
            screen.fill(black)
            draw_background()
            pygame.draw.circle(screen, red, (int(food_x + block_size/2), int(food_y + block_size/2)), block_size/2)
            show_score(snake_length - 1)
            
            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)
            
            if len(snake_list) > snake_length:
                del snake_list[0]
            
            # Check for self collision with any segment except the head
            for segment in snake_list[:-1]:
                if [x, y] == segment:  # Compare current head position with each body segment
                    game_close = True
            
            draw_snake(snake_list)
            pygame.display.update()
            
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
                food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
                snake_length += 1
            
            clock.tick(speed)
        
    pygame.quit()
    quit()

game_loop()
