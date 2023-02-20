import curses


def main(win):
    win.nodelay(True)
    win.addstr("Detected key:")
    while True:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key))
           if key == '\n':
              break           
        except Exception:
           # No input   
           pass

curses.wrapper(main)