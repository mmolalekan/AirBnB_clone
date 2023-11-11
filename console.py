#!/usr/bin/python3
"""Module Documentation"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class Documentation"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Function Documentation"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_obj = storage.classes()[line]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Function Documentation"""
        args = line.split(" ")
        if len(args) < 2:
            print("** instance is missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_quit(self, arg):
        """Function Documentation"""
        return True

    def help_quit(self):
        """Function Documentation"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Function Documentation"""
        print()
        return True

    def emptyline(self):
        """Function Documentation"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
