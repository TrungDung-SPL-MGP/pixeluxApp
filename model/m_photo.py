import tkinter as tk
from tkinter import font
import qrcode
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
from PIL import Image, ImageTk

class Photo():
    photoSave = PhotoImage(file="assets/images/save/Web/1.png")
    photoReview = PhotoImage(file="assets/images/eye/Web/1.png")
    photoLeft=PhotoImage(file="assets/images/left/Web/1.png")
    photoRight=PhotoImage(file="assets/images/right/Web/1.png")
    photo123=PhotoImage(file="assets/images/123/Web/1.png")
    photoCenter=PhotoImage(file="assets/images/center/Web/1.png")
    photobgFont=PhotoImage(file="assets/images/bgFont/Web/1.png")
    photofgFont=PhotoImage(file="assets/images/fgFont/Web/1.png")
    photoB=PhotoImage(file="assets/images/b/Web/1.png")
    photoI=PhotoImage(file="assets/images/i/Web/1.png")
    photoU=PhotoImage(file="assets/images/u/Web/1.png")
    photoService=PhotoImage(file="assets/images/service/Web/1.png")
    photoPicture=PhotoImage(file="assets/images/picture/Web/1.png")
    photoUpload=PhotoImage(file="assets/images/photobackground/upload.png")