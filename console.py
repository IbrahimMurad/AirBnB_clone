#!/usr/bin/python3
"""This module contains the entry point of the command interpreter
It defines HBNBCommand class that inherites from cmd module
It can work interactively and non-interactively
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class works as a console to work as an interpreter
    that uses all the classes defined in AirBnB projects
    """

    prompt = '(hbnb) '
    
    def emptyline(self):
        """do nothing when an empty line is exuted"""

        return None
    
    def do_EOF(self, line):
        """EOF command to exit the program
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()