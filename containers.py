import flet as ft


def criar_lista_containers(lista_numeros):
    lista_containers = []
    for c in range(0, len(lista_numeros)):
        lista_containers.append(
            ft.Container(
                content = ft.Text(value=lista_numeros[c], color=ft.colors.PINK_300),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                border_radius=ft.border_radius.all(100),
                bgcolor=ft.colors.WHITE,
            )
        )
        
       
    return lista_containers   