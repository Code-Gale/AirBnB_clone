#!/usr/bin/python3
"""Entry point"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """
    class for the console interpreter.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it, and print its id.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        prints the object's string representation using its class name and ID.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Ddstroys an instance based on a class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        shows string representations of instances.
        """
        obj_dict = storage.all()
        if arg:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            filtered_objs = [str(obj) for key,
                             obj in obj_dict.items() if args[0] in key]
        else:
            filtered_objs = [str(obj) for obj in obj_dict.values()]
        print(filtered_objs)

    def do_update(self, arg):
        """
        Update an instance based on class name, id, attribute, and value.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')

        instance = obj_dict[key]
        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
