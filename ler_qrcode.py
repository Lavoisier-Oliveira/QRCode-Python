import tkinter as tk
import time, pyperclip
from tkinter import messagebox
from pyzbar.pyzbar import decode
from PIL import ImageGrab

def capturar_screenshot():
	janela.withdraw()
	time.sleep(0.3)
	screenshot = ImageGrab.grab()
	return screenshot

def encontrar_qr_code(image):
	decoded_objects = decode(image)
	for obj in decoded_objects:
		if obj.type == 'QRCODE':
			return obj.data.decode('utf-8')

global janela
janela = tk.Tk()
janela.withdraw()
janela.attributes("-topmost", True) 
janela.geometry("300x100")

resposta = messagebox.askokcancel("Posição da Tela", "Posicione a tela para capturar o QR code e clique em OK.")

if resposta:
	screenshot = capturar_screenshot()
	conteudo_qr_code = encontrar_qr_code(screenshot)
	if conteudo_qr_code:
		pyperclip.copy(conteudo_qr_code)
		messagebox.showinfo("Sucesso!!", "O link do QR code foi copiado para a área de transferência.")
	else:
		messagebox.showerror("Erro", "Não foi possível encontrar o QR code na imagem.")
janela.destroy()