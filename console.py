#!/usr/bin/python3
"""create a program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """console for the project"""
    prompt = '(hbnb) '
    file = None

    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        exit()

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, class_name):
        """ Creates a new instance of a class saves it
        (to the JSON file) and prints the id\n"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            cls = self.classes[class_name]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arguments):
        """Prints the string representation of an instance
            based on the class name and id\n"""
        args = arguments.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + "." + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            else:
                print(storage.all()[obj].__str__())

    def do_destroy(self, arguments):
        """Deletes an instance based on the class name and id\n"""
        if not arguments:
            print("** class name missing **")
            return
        args = arguments.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + "." + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[obj]
                storage.save()

    def do_all(self, arguments):
        """Prints all string representation of all instances
            based or not on the class name\n"""
        args = arguments.split()
        list_of_str = []
        if not args:
            for key in storage.all():
                list_of_str.append(str(storage.all()[key].__str__()))
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for key in storage.all():
                if isinstance(storage.all()[key], self.classes[args[0]]):
                    list_of_str.append(str(storage.all()[key].__str__()))
        print(list_of_str)

    def do_update(self, arguments):
        """ Updates an instance based on the class name and id\n"""
        args = arguments.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = args[0] + "." + args[1]
        if obj not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[obj]
        if hasattr(instance, args[2]):
            attribute_type = type(getattr(instance, args[2]))
            setattr(instance, args[2], attribute_type(args[3]))
        else:
            setattr(instance, args[2], args[3])
        storage.save()

    def default(self, command):
        """advances tasks method"""
        args = command.split('.')
        instance_list = []
        if args[1] == "all()":
            if args[0] not in self.classes:
                print("* class doesn't exist *")
                return
            for key in storage.all():
                if isinstance(storage.all()[key], self.classes[args[0]]):
                    instance_list.append(str(storage.all()[key].__str__()))
            print(instance_list)
            return
        if args[1] == "count()":
            count = 0
            if args[0] not in self.classes:
                print("* class doesn't exist *")
                return
            for key in storage.all():
                if isinstance(storage.all()[key], self.classes[args[0]]):
                    count += 1
            print(count)
            return
        arguments = args[1].split('(')
        if arguments[0] == "show":
            if args[0] not in self.classes:
                print("* class doesn't exist *")
                return
            if arguments[1] == ")":
                print("* instance id missing *")
                return
            obj = args[0] + "." + arguments[1].split('"')[1]
            if obj not in storage.all():
                print("* no instance found *")
                return
            print(storage.all()[obj].__str__())
            return
        if arguments[0] == "destroy":
            if args[0] not in self.classes:
                print("* class doesn't exist *")
                return
            if arguments[1] == ")":
                print("* instance id missing *")
                return
            obj = args[0] + "." + arguments[1].split('"')[1]
            if obj not in storage.all():
                print("* no instance found *")
                return
            del storage.all()[obj]
            storage.save()
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
