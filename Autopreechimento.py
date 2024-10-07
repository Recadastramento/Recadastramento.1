# autopreenchimento.py
import flet as ft

def atualizar_sugestoes(evento, lista_nomes, sugestoes, nomes_completos, pagina):
    texto_digitado = lista_nomes.value.strip().lower()
    sugestoes.controls.clear()

    if texto_digitado:
        nomes_filtrados = [
            nome for nome in nomes_completos if nome.lower().startswith(texto_digitado)
        ]
        sugestoes.controls.extend(
            ft.TextButton(nome, on_click=lambda e, n=nome: selecionar_nome(n, lista_nomes, sugestoes, pagina)) for nome in nomes_filtrados
        )

    pagina.update()

def selecionar_nome(nome, lista_nomes, sugestoes, pagina):
    lista_nomes.value = nome
    sugestoes.controls.clear()
    pagina.update()


