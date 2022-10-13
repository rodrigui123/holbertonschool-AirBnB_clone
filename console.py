#!/usr/bin/python3
"""Write a program called Console.py"""


import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNBcommand"""
    prompt = "(hbnb)"

    def quit(self):
        """quit func"""
        return True

    def EOF(self):
        """end of file func"""
        return True

    def empty_line(self, args):
        """empty line + Enter should execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
