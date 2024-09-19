import flet as ft


def criar_lista_containers(lista_numeros):
    lista_containers = []
    for c in range(0, len(lista_numeros)):
        if c % 2 == 0:
            cor = ft.colors.PINK_300
        else:
            cor = ft.colors.BLUE_300
        lista_containers.append(
            ft.Container(
                content = ft.Text(value=lista_numeros[c], 
                                  color=cor,
                                  size= 25,
                                  weight= ft.FontWeight.BOLD
                                 
                                  
                                  ),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                margin=ft.margin.all(5),
                border_radius=ft.border_radius.all(100),
                bgcolor=ft.colors.WHITE,
            )
        )
        
       
    return lista_containers   