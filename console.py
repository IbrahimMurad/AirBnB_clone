#!/usr/bin/python3
"""This module contains the entry point of the command interpreter
It defines HBNBCommand class that inherites from cmd module
It can work interactively and non-interactively
"""

import cmd
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class works as a console to work as an interpreter
    that uses all the classes defined in AirBnB projects
    """

    def preloop(self):
        """handles the non-interactive mode
        """

        if not sys.stdin.isatty():
            command_with_args = " ".join(sys.argv[1:])
            self.cmdqueue.append(command_with_args)
            self.prompt = ""
        else:
            self.prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when an empty line is exuted"""

        pass

    def do_EOF(self, line):
        """EOF command to exit the program
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def do_create(self, line):
        """Creates a new instance of the named class,
        saves it (to the JSON file) and prints the id

        Usage:
            create [class_name]
        """

        my_args = line.split()
        if len(my_args) == 0:
            print("** class name missing **")
        if len(my_args) == 1:
            if my_args[0] not in storage.all_classes().keys():
                print("** class doesn't exist **")
            else:
                my_obj_class = storage.all_classes()[my_args[0]]
                new_obj = my_obj_class()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance \
    based on the class name and id
    Usage :
        show [class_name] [id]
    """

        my_args = line.split()
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] not in storage.all_classes().keys():
            print("** class doesn't exist **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        else:
            all_objects_list = list(storage.all().values())
            my_obj_list = []
            for obj in all_objects_list:
                if obj.__class__.__name__ == my_args[0]:
                    my_obj_list.append(obj)
            list_of_ids = []
            for obj in my_obj_list:
                list_of_ids.append(obj.id)
            if my_args[1] in list_of_ids:
                print(my_obj_list[list_of_ids.index(my_args[1])])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Usage :
            destroy [class_name] [id]
        """

        my_args = line.split()
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] not in storage.all_classes().keys():
            print("** class doesn't exist **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        else:
            all_objects_list = list(storage.all().values())
            my_obj_list = []
            for obj in all_objects_list:
                if obj.__class__.__name__ == my_args[0]:
                    my_obj_list.append(obj)
            list_of_ids = []
            for obj in my_obj_list:
                list_of_ids.append(obj.id)
            if my_args[1] in list_of_ids:
                obj_key = my_args[0] + '.' + my_args[1]
                storage._FileStorage__objects.pop(obj_key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances/
 based or not on the class name
 Usage:
    all [[class_name]]
 """

        my_args = line.split()
        if len(my_args) == 0:
            all_objects_list = list(storage.all().values())
            to_print_list = [str(obj) for obj in all_objects_list]
            print(to_print_list)
        if len(my_args) == 1:
            if my_args[0] not in storage.all_classes().keys():
                print("** class doesn't exist **")
            else:
                all_objects_list = list(storage.all().values())
                my_obj_list = []
                for obj in all_objects_list:
                    if obj.__class__.__name__ == my_args[0]:
                        my_obj_list.append(obj)
                to_print_list = [str(obj) for obj in my_obj_list]
                print(to_print_list)

    def do_update(self, line):
        """Updates an instance based on the class name \
and id by adding or updating attribute
Usage :
    update [class_name] [id] [attribute_name] [value]
"""

        my_args = line.split()
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] not in storage.all_classes().keys():
            print("** class doesn't exist **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        else:
            all_objects_list = storage.all()
            obj_key = my_args[0] + '.' + my_args[1]
            if obj_key not in all_objects_list.keys():
                print("** no instance found **")
            elif len(my_args) == 2:
                print("** attribute name missing **")
            elif len(my_args) == 3:
                print("** value missing **")
            else:
                my_obj = all_objects_list[obj_key]
                if not hasattr(my_obj, my_args[2]):
                    setattr(my_obj, my_args[2], my_args[3])
                else:
                    attr_type = type(getattr(my_obj, my_args[2]))
                    setattr(my_obj, my_args[2], attr_type(my_args[3]))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
