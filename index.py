import flet as ft
import criar_listas as crl
import containers as crc

def main (page: ft.Page):
    page.title = 'Loterias'
    lista = crl.criar_lista_de_numeros(6, 60)
    lista = crl.criar_lista_ordenada(lista)
    row = ft.Row(
            controls= crc.criar_lista_containers(lista)
    )
    page.add(row)
    
    
ft.app(target = main, assets_dir ='assets')