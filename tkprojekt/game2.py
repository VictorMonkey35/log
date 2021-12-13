import tkinter as tk

arena = tk.Tk()
arena.geometry('900x540')

rockimg = tk.PhotoImage(file = 'tkprojekt/bilder/rock.png')
paperimg = tk.PhotoImage(file = 'tkprojekt/bilder/paper.png')
scissorsimg = tk.PhotoImage(file = 'tkprojekt/bilder/scissors.png')
tableimg = tk.PhotoImage(file = 'tkprojekt/bilder/table.png')
jonasimg = tk.PhotoImage(file = 'tkprojekt/bilder/Jonas.png')

canvas = tk.Canvas(arena, width = 900, height = 540, bg = 'grey')
canvas.pack()

canvas.create_image(450, 240, anchor = tk.CENTER, image = jonasimg)
canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
canvas.create_image(450, 400, anchor = tk.CENTER, image = rockimg)
canvas.create_image(450, 400, anchor = tk.CENTER, image = paperimg)
canvas.create_image(450, 400, anchor = tk.CENTER, image = scissorsimg)

arena.mainloop()