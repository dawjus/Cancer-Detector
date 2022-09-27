import os
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import xlrd
import win32com.client as win32
from PIL import ImageGrab
from PIL import Image, ImageTk #python3-pil.imageth python3-imaging-tk
import cv2
import customtkinter

class LoadData:

    def __init__(self):
        self.__filepath__ = self.load_data()

    def load_data(self):
        file = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select Image File", filetypes=[("Excel files", "*.xlsx")])
        if file:
            filepath = os.path.abspath(file)
            return filepath

    def get_Image(self):
        excel = win32.gencache.EnsureDispatch ('Excel.Application')
        workbook = excel.Workbooks.Open (str(self.__filepath__))
        for sheet in workbook.Worksheets:
            for i, shape in enumerate (sheet.Shapes):
                if shape.Name.startswith ('Picture'):  # or try 'Image'
                    shape.Copy ()
                    img = ImageGrab.grabclipboard ().resize((650,650))
                    return img

    def get_Information(self):
        wb = xlrd.open_workbook (str(self.__filepath__))
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 1)
        patient_information = []

        for i in range(sheet.ncols):
            patient_information.append(str(sheet.cell_value(0,i)))

        return patient_information