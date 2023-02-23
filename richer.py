import rich
from keypress_os import getchar

rich.print('[red]1 [blue]2 [green]3')
for i in range(3):
    c = getchar()
    if c == '1':
        color = 'red'
    elif c == '2':
        color = 'blue'
    elif c == '3':
        color = 'green'
    rich.print(f'[{color}]\u25cf', end='')
rich.print()