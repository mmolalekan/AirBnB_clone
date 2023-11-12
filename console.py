#!/usr/bin/python3
"""Module Documentation"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State
    }


class HBNBCommand(cmd.Cmd):
    """Class Documentation"""
    prompt = '(hbnb) '

    def precmd(self, line: str) -> str:
        """Function Documentation"""
        keys = line.split(".")
        if keys[1] == "all()":
            return super().precmd(f"all {keys[0]}")
        if keys[1] == "count()":
            count = 0
            for k in storage.all().keys():
                if k.split(".")[0] == "User":
                    count += 1
            print(count)
            return super().precmd("")

    def do_create(self, line):
        """Function Documentation"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in classes.keys():
            print("** class doesn't exist **")
        else:
            for k, v in classes.items():
                if line == k:
                    new_obj = v()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Function Documentation"""
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Function Documentation"""
        args = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Function Documentation"""
        if line not in classes.keys():
            print("** class doesn't exist **")
        else:
            my_list = []
            for key, value in storage.all().items():
                my_list.append(str(value))
            print(my_list)

    def do_update(self, line):
        """Function Documentation"""
        args = line.split(" ")
        objects = storage.all()
        keys = objects.keys()
        if args[0] and args[1]:
            key = f"{args[0]}.{args[1]}"
            if key in keys:
                if args[2] == "" or args[2] is None:
                    print("** attribute name missing **")
                if args[3] == "" or args[3] is None:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()

            elif line == "" or line is None:
                print("** class name missing **")
            elif args[0] not in classes.keys():
                print("** class doesn't exist **")
            elif args[1] == "" or args[1] is None:
                print("** instance id missing **")
            else:
                print("** no instance found **")

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
