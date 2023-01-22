""" from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--line', nargs='+', action='append', help="Prints the WORD")
subparser = parser.add_subparsers(title='sub-arg-ing')
parser_b = subparser.add_parser('b')
parser_b.add_argument('item_C')
args=parser.parse_args() # ('--line word --line number --line name count'.split())
if args.line:
    for line in args.line:
        print(*line, sep=', ')
print(args) """

from argparse import ArgumentParser
parser = ArgumentParser(description="To-do app. Loosly based upon rptodo.",
 usage="%(prog)s [options]")
parser.add_argument('-v', action='version', version='Command line to-do 1.2')

file_group_parent = parser.add_argument_group('File operations')
file_group= file_group_parent.add_mutually_exclusive_group(required=False)
file_group.add_argument('-n', '--new', nargs='*',
 metavar='PATH',
 help="Creates a new to-do list at PATH. By default 'to-do.json'")
file_group.add_argument('-o', '--open', nargs='+', metavar='PATH',
 help="Open an existing to-do list at PATH")

#new_item_parent = parser.add_subparsers(title='Add to-do')
#new_item = new_item_parent.add_parser('add', help="Add a to-do")
new_item = parser.add_argument_group('Add to-do')
new_item.add_argument('--add', nargs='+', metavar='DESCRIPTION', action='append',
 help="Add a new to-do with a DESCRIPTION (multiple words)")
""" new_item.add_argument('--also', nargs='+',
 metavar='DESCRIPTION', action='append', dest='add',
 help="Add a new to-do with a DESCRIPTION (multiple words)")
new_item.add_argument('-p', '-priority', dest='priority',
 type=int, action='append',
 help="of to-do being added") """

edit_item = parser.add_argument_group('Edit item position or status')
""" edit_item.add_argument('-u', '--move-up', nargs=2, type=int,
 metavar=('ID', 'PLACES'),
 help="Moves item ID up by a number of PLACES")
edit_item.add_argument('-d', '--move-down', nargs=2, type=int,
 metavar=('ID', 'PLACES'),
 help="Moves item ID down by a number of PLACES")
edit_item.add_argument('-c', '--check', type=int, metavar='ID',
 help="Marks item ID as done. If 0 is entered, marks ALL as done")
edit_item.add_argument('-k', '--uncheck', type=int, metavar='ID',
 help="Marks item ID as not done. If 0 is entered, marks ALL as not done")
 """
edit_item.add_argument('-p', '--change', nargs = 2, type=int,
 metavar=('ID', 'PRIORITY'), action='append',
 help="Changes the priority of ID to PRIORITY")
"""
remove_item = parser.add_argument_group('Remove a to-do')
remove_item.add_argument('-r', '--remove', type=int, metavar='ID',
 help="Remove a to-do using its ID number")
remove_item.add_argument('-confirm', action='store_true',
 help="Confirm removal on command-line")

display_list = parser.add_argument_group('Display the to-do list')
display_list.add_argument('-l', '--list', action='store_true',
 help="List all to-do's")
display_list.add_argument('-t', '--auto', action='store_true',
 help="Toggles if the list is automatically displayed")
 """
args = parser.parse_args()
print(args)