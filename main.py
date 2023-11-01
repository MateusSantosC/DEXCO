from back_end.bibliotecas import *
from back_end.pegar_id_v360 import *
from back_end.abrir_base import *
from back_end.extrair_descri import *
from back_end.mover_processo import *
from back_end.analise_inbound import *




sg.theme('Black')

layout = [
    [sg.Text('')],
    
    [sg.Text('DEXCO', font = ('Helvetica', 30), text_color = 'WHITE')],
    
    [sg.Text('')],
    
    [sg.Text('Usuario:',font = ('Helvetica', 12))],
    
    [sg.Input(key = 'usuario',size = (20,1))],
    
    [sg.Button('    Salvar    ', font = ('Helvetica', 8))],
    
    [sg.Text('', key ='msgusuario')],
    [sg.Text('')],
    [sg.Text('')],
    
    [sg.Text('Preencha o usuario do seu computador antes de realiza uma operação!!', font = ('Helvetica', 12), key = 'msg2')],
    
    [sg.Text('')],
    [sg.Text('')],
    
    
    [sg.Button('PEGAR ID',size = (13,2), font = ('Helvetica', 12))],
    
    
    [sg.Text('')],
    
    
    [sg.Button('EXTRAIR DESCRIÇÃO',size = (13,2), font = ('Helvetica', 12))],
    
    [sg.Text('')],
    
    [sg.Button('MOVER PROCESSO',size = (25,2), font = ('Helvetica', 12))],

    [sg.Text('')],
    
    [sg.Button('ANALISAR INBOUND',size = (20,2), font = ('Helvetica', 12))],

    [sg.Text('')],
    [sg.Text('')],
    
    [sg.Button('Base de dados',size = (13,1), font = ('Helvetica', 8))]
    # [sg.Button('Salvar')],
    # [sg.Button('Sair')]
]

janela = sg.Window('HOME', layout, element_justification='c')



while True:
    
    eventos, valores = janela.read()
    
    if eventos == sg.WIN_CLOSED:
        break
        
        
    if eventos == '    Salvar    ':
        usuario1.clear()
        usuario2.clear()
        usuario3.clear()
        usuario4.clear()
        
        usuario1.append(valores['usuario'])
        usuario2.append(valores['usuario'])
        usuario3.append(valores['usuario'])
        usuario4.append(valores['usuario'])
        
        
        janela['msgusuario'].update(f'Usuario "{usuario1[0]}"salvo!')
        janela['msg2'].update('Selecione a operação que deseja realizar:')
    
    if eventos =='PEGAR ID':
        pegar_id.pegar()
        
    if eventos == 'EXTRAIR DESCRIÇÃO':
        extrair_descri.extrair()
        
    if eventos == 'MOVER PROCESSO OUT.':
        mover_processo.mover()
        
    if eventos == 'ANALISAR INBOUND':
        analizar_in.analisar()
        
    
    if eventos == 'Base de dados':
        abrir_base.base()
    


    
