#!/usr/bin/python3
"""Write a program called Console.py"""


import cmd
import sys

from requests import delete

from models.base_model import BaseModel
import models

def get_instance(args):
    if len(args) == 0:
        print("** class name missing **")
        return None
    elif globals().get(args[0]) is None:
        print("** class doesn't exist **")
        return None
    elif len(args) == 1:
        print("** instance id missing **")
        return None

    try:
        selected_object = models.storage.all()[f"{args[0]}.{args[1]}"]
        return selected_object
    except:
        print("** no instance found **")
        return None

class HBNBCommand(cmd.Cmd):
    """class HBNBcommand"""
    prompt = "(hbnb)"

    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif globals().get(arg) is None:
            print("** class doesn't exist **")
            return
        
        new_base = BaseModel()
        new_base.save()
        print(new_base.id)

    def do_show(self, arg):
        args = arg.split()
        selected_object = get_instance(args)
        if selected_object is not None:
            print(selected_object)
        
    def do_destroy(self, arg):
        args = arg.split()
        selected_object = get_instance(args)
        if selected_object is not None:
            models.storage.destroy(f"{args[0]}.{args[1]}")

    def do_all(self, arg):
        objs = models.storage.all()
        if len(arg):
            if globals().get(arg) is None:
                print("** class doesn't exist **")
                return
        objs_filtered = []
        for key, value in objs.items():
            if value.__class__.__name__ == arg or len(arg) == 0:
                objs_filtered.append(value.__str__())
        print(objs_filtered)

    def do_update(self, arg):
        args = arg.split()
        selected_object = get_instance(args)
        if selected_object is not None:
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            
            selected_object.__dict__[args[2]] = args[3]
            models.storage.save()
        
    def do_quit(self, arg):
        """quit func"""
        return True

    def do_EOF(self):
        """end of file func"""
        return True

    def emptyline(self):
        """empty line + Enter should execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
