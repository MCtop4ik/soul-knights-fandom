import tkinter as tk

import pygame

import choose_player_window


def start_game():
    from level import Level
    from map_generation.room_factory import RoomFactory
    from settings.constants import Constants
    from settings.player_state import PlayerState
    pygame.init()
    pygame.display.set_caption("Pygame Window")
    Constants().name = PlayerState().levels[PlayerState().level_index]
    RoomFactory(Constants().name).load_assets()
    Level().start()


def button_clicked():
    print("Button clicked!")


def starting_window():
    root = tk.Tk()
    root.title("Starting Window")
    window_width, window_height = (300, 300)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Create a label widget
    label = tk.Label(root, text="Welcome to my application!", font=("Helvetica", 16))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.pack(pady=20)

    choose_player_button = tk.Button(root, text="Choose Your Player", command=choose_player_window.choose_player)
    choose_player_button.pack(pady=60)

    while True:
        root.update_idletasks()
        root.update()

