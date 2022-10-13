#!/usr/bin/python3
"""Write a program called Console.py"""


import cmd


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
