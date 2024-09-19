import flet as ft
import criar_listas as crl
import containers as crc

def main (page: ft.Page):
    page.title = 'Loterias'
    lista = crl.cria_lista_de_numeros_ordenados(6, 60)
    title = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
        controls=[ft.Text(
            value='LOTERIAS BOA SORTE'
        )
        ]
    )
    balls = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
            controls= crc.criar_lista_containers(lista),
            
    )
    button  = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value='Gerar números'),
            ft.IconButton(
            tooltip='Gerar números',
            icon = ft.icons.PLAY_ARROW,
        )]
    )
    page.add(title, balls, button)
    
    
ft.app(target = main, assets_dir ='assets')