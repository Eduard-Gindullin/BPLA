import tkinter as tk


window = tk.Tk()
window.geometry("700x700")
window.title("Arcanoid")
window.resizable(False, False)
board = tk.Canvas(window, bg="silver")
board.pack(fill="both", expand=True)


def create_game():
    ball = {"x": 500, "y": 30}
    move_side = {"x": True, "y": True}
    platform_x = [310, 390]
    game_active = True
    score = 0

    def draw(event):
        platform_x[0] = event.x - 40
        platform_x[1] = event.x + 40

    def move():
        nonlocal ball, move_side, platform_x, game_active, score

        board.delete("all")

        if move_side["x"]:
            ball["x"] += 5
        else:
            ball["x"] -= 5

        if move_side["y"]:
            ball["y"] += 5
        else:
            ball["y"] -= 5

        if ball["x"] > 680:
            move_side["x"] = not move_side["x"]
        if ball["x"] < 20:
            move_side["x"] = not move_side["x"]

        if ball["y"] > 680:
            game_active = False
        if ball["y"] < 20:
            move_side["y"] = not move_side["y"]

        if ball["y"] == 640 and platform_x[0] <= ball["x"] <= platform_x[1]:
            move_side["y"] = not move_side["y"]
            score += 1

        board.create_oval(
            ball["x"] - 10, ball["y"] - 10, ball["x"] + 10, ball["y"] + 10, fill="red"
        )

        board.create_text(50, 20, text=f"Счет: {score}", fill="black")

        board.create_rectangle(platform_x[0], 640, platform_x[1], 660, fill="blue")

        if game_active:
            board.after(10, move)

    board.bind("<Motion>", draw)
    move()


create_game()
window.mainloop()
