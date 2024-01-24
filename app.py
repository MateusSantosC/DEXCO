from biblioteca import * 
from pegar_id import *




usuario = []

# Inicio janela
menu_inicial = Tk()

# titulo da janela
menu_inicial.title('App Dexco')

menu_inicial.geometry(f'430x387+500+150')

menu_inicial.resizable(False, False)




'''FUNDO SUPERIOR'''
Rectangle_img = PhotoImage(file="imgs\Rectangle.png")
Rectangle = Label(
    menu_inicial, 
    image=Rectangle_img,
)
Rectangle.pack()
Rectangle.place(
    x=-1,
    y=-150,
)




'''lOGO DEXCO'''
logo_dexco_img = PhotoImage(file="imgs\logo_dexco.png")
logo_dexco = Label(
    menu_inicial, 
    image=logo_dexco_img,
    bg="#d9d9d9",
)
logo_dexco.pack()
logo_dexco.place(
    x=19,
    y=38,
)




'''PREENCHER USUARIO'''
entry_image_2 = PhotoImage(
    file=("imgs\\fundo_usuario.png"))
entry_bg_2 = Label(
    image=entry_image_2,
    bg="#d9d9d9",
)
entry_bg_2.pack()
entry_bg_2.place(
   x=19,
   y=178
)
entry_2 = Entry(
    bd=0,
    bg="#000000",
    fg="#d9d9d9",
    highlightthickness=0, 
    font="Arial 15",
    
)
entry_2.pack()
entry_2.place(
    x=130.0,
    y=195,
)




'''BOTÃO SALVAR USUARIO'''
btn_salvar_img = PhotoImage(
    file=("imgs\\btn_salvar.png"))
btn_salvar = Button(
    menu_inicial, 
    image=btn_salvar_img,
    bd=0,
    bg = "#000000",
    # command = btn_go,
)
btn_salvar.pack()
btn_salvar.place(
    x=295.0,
    y=194.0,
)




'''BOTÃO MACRO 01'''
btn_analise_inbound_img = PhotoImage(
    file=("imgs\\pegar_id.png"))
btn_analise_inbound = Button(
    menu_inicial, 
    image=btn_analise_inbound_img,
    bd=0,
    command = pegar_id.pegar,
)
btn_analise_inbound.pack()
btn_analise_inbound.place(
    x=19,
    y=300
)




'''BOTÃO BASE 01'''
btn_base_img = PhotoImage(
    file=("imgs\\btn_base.png"))
btn_base= Button(
    menu_inicial, 
    image=btn_base_img,
    bd=0,
    command = pegar_id.base,
)
btn_base.pack()
btn_base.place(
    x=291,
    y=300
)




menu_inicial.mainloop()