import flet as ft
import pandas as pd
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googledrive import CadastroPIB
from Confirmado import confirmando
from preenchercampos import autopreencher
from Autopreechimento import atualizar_sugestoes
from dados import (matricula, nomecompleto, cpf,
        datanascimento, sexo, tipo_sanguineo, 
        estado_civil, datacasamento, profissao, 
        naturalidade, nacionalidade,rua, complemento,
        bairro, municipio, estado, cep, tel_residencial,
        tel_celular, email, nome_pai, pai_membro,
        nome_mae, mae_membro, nome_conjuge,
        datanascimento_conjuge, conjuge_membro,
        cargo_atual, databatismo, igrejabatismo,
        entradaPIB, formaentrada, 
        nome_filho1, datanascimento_filho1, filho1_membro, 
        nome_filho2, datanascimento_filho2, filho2_membro,
        nome_filho3, datanascimento_filho3, filho3_membro,
        nome_filho4, datanascimento_filho4, filho4_membro,
        nome_filho5, datanascimento_filho5, filho5_membro )

def main(pagina):
    Rc = ft.Text("Recadastramento")
    Usuarios = ["admin"]
    Senhas = ["123"]

    # Opção para menu de preenchimento automático
    sugestoes = ft.Column()

    nomes_completos = CadastroPIB["Nome Completo"].tolist()
    lista_nomes = ft.TextField(
    label="Nome Completo",on_change=lambda e: 
    atualizar_sugestoes(e, lista_nomes, sugestoes, nomes_completos, pagina))

    def preencherplanilha(evento):
        confirmando(evento)
        pagina.update()
        janela_recadastro.open = False
        concluir_janela.open = True
        pagina.update()
    Confirmar = ft.ElevatedButton("Confirmar", on_click=preencherplanilha)


    def completarinfo (evento):
        autopreencher(evento, lista_nomes)
        pagina.update()    

    
    # Criação da janela de recadastramento com scroll
    janela_recadastro = ft.AlertDialog(
    title=Rc,
    content=ft.Column(
        controls=[
            ft.Row(controls=[
                ft.Column(controls=[
                    matricula, nomecompleto, cpf,
                    datanascimento, sexo, tipo_sanguineo, 
                    estado_civil, datacasamento, profissao, 
                    naturalidade, nacionalidade,rua, complemento,
                    bairro, municipio, estado, cep, tel_residencial,
                    tel_celular, email, nome_pai, pai_membro,
                    nome_mae, mae_membro, nome_conjuge,
                    datanascimento_conjuge, conjuge_membro,
                    cargo_atual, databatismo, igrejabatismo,
                    entradaPIB, formaentrada, 
                    nome_filho1, datanascimento_filho1, filho1_membro, 
                    nome_filho2, datanascimento_filho2, filho2_membro,
                    nome_filho3, datanascimento_filho3, filho3_membro,
                    nome_filho4, datanascimento_filho4, filho4_membro,
                    nome_filho5, datanascimento_filho5, filho5_membro
                ]),
            ]),
            Confirmar
        ],
        scroll=True,
        width=300  # Define uma largura específica, mas ainda assim flexível
    )
    )
    pagina.overlay.append(janela_recadastro)
    # Função para abrir a janela de recadastramento
    def Recadastro(evento):
        pagina.overlay.append(janela_recadastro)  # Atribui a janela à página
        janela_recadastro.open = True  # Abre a janela
        pagina.update()  # Atualiza a página

    Iniciar_cadastro = ft.ElevatedButton("Cadastro", on_click=Recadastro)
    Completar = ft.ElevatedButton("Autopreenchimento", on_click=completarinfo)

    # LOGIN
    def Verificar(evento):
        if Nome_usuario.value in Usuarios:
            if Senha.value in Senhas:
                if Senhas.index(Senha.value) == Usuarios.index(Nome_usuario.value):
                    Nome_usuario.value = ""
                    Senha.value = ""
                    pagina.remove(Rc)
                    pagina.remove(botao_iniciar)
                    janela.open = False
                    pagina.add(lista_nomes)
                    pagina.add(sugestoes)
                    pagina.add(Completar)
                    pagina.add(Iniciar_cadastro)
                    
                    pagina.update()
                else:
                    Senha.value = "Senha Inválida"
                    pagina.update()                 
            else:
                Senha.value = "Senha Inválida"
                pagina.update()
        else:
            Nome_usuario.value = "Usuário Inválido"
            Senha.value = ""
            pagina.update()
#------------------------------------------------------------
#Janela confirmação de cadastro feito

    def fechar_ok(evento):
            concluir_janela.open = False
            pagina.update()

    titulo_concluir = ft.Text("Cadastro concluído")
    ok = ft.ElevatedButton("OK", on_click=fechar_ok)

    concluir_janela = ft.AlertDialog(
        title = titulo_concluir,
        actions=[ok]
    )
    pagina.overlay.append(concluir_janela)

#------------------------------------------------------------
#Janela Login
    titulo_janela = ft.Text("Bem-vindo ao sistema de Recadastramento")
    Nome_usuario = ft.TextField(label="Usuário")
    Senha = ft.TextField(label="Senha")
    botao_entrar = ft.ElevatedButton("Acessar Sistema", on_click=Verificar)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column(controls=[Nome_usuario, Senha]),
        actions=[botao_entrar]
    )
    
    # Função para abrir a janela de login
    def Abrir_popup(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()   

    
    botao_iniciar = ft.ElevatedButton("Login", on_click=Abrir_popup)
    pagina.add(Rc)
    pagina.add(botao_iniciar)

    # Função para verificar e modificar os valores vazios, interrompendo o processo

ft.app(main)