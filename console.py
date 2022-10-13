#!/usr/bin/python3
"""Write a program called Console.py"""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """class HBNBcommand"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit func"""
        return True

    def do_EOF(self):
        """end of file func"""
        return True

    def empty_line(self):
        """empty line + Enter should execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
