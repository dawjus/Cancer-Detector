import tkinter as tk
import customtkinter
import os
import numpy as np
from LoadData import LoadData
from PIL import Image, ImageTk
from Model_to_image import Detection_tumor

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Cancer Detector")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_down = customtkinter.CTkFrame(master=self, height=60, corner_radius=0)
        self.frame_down.grid(row=4, columnspan=3, sticky="nswe")

        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.columnconfigure(0, weight=1)

        self.label_image = customtkinter.CTkLabel(master=self.frame_left, fg_color=("gray85", "gray30"),
                                                  justify=tk.LEFT, text="")
        self.label_image.grid(row=0, column=0, sticky="nswe", pady=10, padx=10)

        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.columnconfigure(0, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right, fg_color=("gray85", "gray30"))
        self.frame_info.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.frame_down.grid_columnconfigure(0, minsize=10)
        self.frame_down.grid_columnconfigure(5, weight=1)
        self.frame_down.grid_columnconfigure(8, minsize=20)
        self.frame_down.grid_columnconfigure(11, minsize=10)

        self.button_load_patient_data = customtkinter.CTkButton(master=self.frame_down, text="Load patient data",
                                                                fg_color=("gray75", "gray30"),
                                                                command=self.button_event)
        self.button_load_patient_data.grid(row=0, column=1, pady=10, padx=20)

        self.button_exit = customtkinter.CTkButton(master=self.frame_down, text="Exit", fg_color=("gray75", "gray30"),
                                                   command=lambda: exit())
        self.button_exit.grid(row=0, column=2, pady=10, padx=20)

        self.switch_mode = customtkinter.CTkSwitch(master=self.frame_down, text="Light Mode", command=self.change_mode, state='NORMAL' )
        self.switch_mode.grid(row=0, column=11, pady=10, padx=20, sticky="e")

    def button_event(self):
        self.detection_Tumor = Detection_tumor()
        img = self.detection_Tumor.get_image()
        img = ImageTk.PhotoImage(img)
        self.label_image.configure(image=img)
        self.label_image.image = img
        self.label_info = customtkinter.CTkLabel(master=self.frame_info, justify=tk.LEFT,
                                                 text=self.detection_Tumor.print_information(), anchor="nw", text_font=("Roboto Medium", -14),
                                                 width= 230)
        self.label_info.grid(row=0, column=0, sticky="nw", pady=20, padx=1)

    def change_mode(self):
        if self.switch_mode.get() == 0:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
