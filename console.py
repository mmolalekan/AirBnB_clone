#!/usr/bin/python3
"""
Module defining the console"""
from cmd import Cmd
from models import storage
from models.engine.error import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = storage.models


class HBNBCommand(Cmd):
    """
    Class defining the Console of the AirBnb Clone.
    Operations with the system is done via
    this class."""

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Exit the Console in non interactive mode"""
        return True

    def do_quit(self, args):
        """Exit the console"""
        return True

    def do_create(self, args):
        """Creates an instance and Throws an Error if ModelName is missing or doesn't exist"""
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Display an Instance.
        Display error message if either
        MyModel or instance_id is missing"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

    def do_destroy(self, arg):
        """Destroys an Instance. Displays error message if
        either MyModel or instance_id is missing"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

    def do_all(self, args):
        """Retrieve all instances"""
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """Updates an instance Throws errors for missing arguments"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")

    def do_models(self, arg):
        """Displays all registered Models"""
        print(*classes)

    def handle_class_methods(self, arg):
        """defines Handle class method"""

        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for x in printable:
                if x in arg:
                    print(val)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass

    def default(self, arg):
        """Handle class methods overrides default method"""
        if '.' in arg and arg.split('.')[0] in classes and arg[-1] == ')':
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """defines empty line to do nothing"""
        return


def parse(line: str):
    """Seperate a line by spaces"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
