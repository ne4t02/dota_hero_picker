import questionary
import pyfiglet
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from random import sample
from rich import print

console = Console()

heroes_list = [
    h.strip().replace("'", "").replace('"', "")
    for h in open('heroes.txt', encoding='utf-8').read().splitlines()
]

items_list = [
    i.strip().replace("'", "").replace('"', "")
    for i in open('items.txt', encoding='utf-8').read().splitlines()
]

table_res = Table(show_header=True, header_style="bold magenta")
table_res.add_column("Герои", style="dim", width=30)
table_res.add_column("Предметы", style="dim", width=30)

def hero_picker():
    while True:
        try:
            hero_q = int(questionary.text(
                'Количество героев?: ',
                default='1'
                ).ask()
            )

            if hero_q > len(heroes_list):
                console.print(f"[red]Вы не можете выбрать больше {len(heroes_list)} героев![/red]") 
                continue

            if hero_q < 1:
                console.print("[red]Вы должны выбрать хотя бы одного героя![/red]")
                continue

            break 
        except ValueError:
            pass

    return (sample(heroes_list, k = hero_q))
        
    
    
def items_picker():
    while True:
        try:
            item_q = int(questionary.text(
                'Количество предметов?: ',
                default='1'
                ).ask()
            )

            if item_q > len(items_list):
                console.print(f"[red]Вы не можете выбрать больше {len(items_list)} предметов! [/red]")
                continue

            if item_q < 1:
                console.print("[red]Вы не можете выбрать меньше одного предмета![/red]")
                continue

            break
        except ValueError:
            pass 

    return (sample(items_list, k = item_q))
        
    

def main():
    console.print(
        Panel.fit(
        pyfiglet.figlet_format('HERO PICKER'),
        style='bold magenta'
        )
    )
    console.print(table)
        

    
    selected_mode = questionary.select(
        "Выберите режим:",
        choices=[
            'Выбирать героев',
            'Выбирать предметы',
            'Выбирать героев и предметы'
        ]).ask()
    if selected_mode == 'Выбирать героев':
        heroes = hero_picker()
        table_res.add_row("\n".join(heroes), "")
    elif selected_mode == 'Выбирать предметы':
        items = items_picker()
        table_res.add_row("", "\n".join(items))
    elif selected_mode == 'Выбирать героев и предметы':
        heroes = hero_picker()
        items = items_picker()
        table_res.add_row("\n".join(heroes), "\n".join(items))
    else:
        print('Что-то пошло не так...')
    console.print(table_res)


table = Table(show_header=True, header_style="bold magenta")
table.add_column("Режимы", style="dim", width=30)
table.add_row("Выбирать героев")
table.add_row("Выбирать предметы")
table.add_row("Выбирать героев и предметы")
table.add_column("Описание", style="dim", width=50)
table.add_row("Выбирать героев", "Рандомно выбирает героев из списка")
table.add_row("Выбирать предметы", "Рандомно выбирает предметы из списка")
table.add_row("Выбирать героев и предметы", "Рандомно выбирает героев и предметы из списков")


        


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")



