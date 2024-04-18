class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Doesn't do anything on ENTER
        """
        pass

    def do_quit(self, line):
        """Exits the program
        """
        return True

    def do_EOF(self, line):
        """Handles the end of file
        """
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in [cls.__name__ for cls in globals().values()
                              if isinstance(cls, type)]:
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if args[0] not in [cls.__name__ for cls in globals().values()
                           if isinstance(cls, type)]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        save the change into the JSON file
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in [cls.__name__ for cls in globals().values()
                              if isinstance(cls, type)]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances or
        based on class name"""
        args = arg.split()

        if not args:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in [cls.__name__ for cls in globals().values()
                              if isinstance(cls, type)]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in storage.all().items()
               if key.startswith(class_name + ".")])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save changes into the JSON file)
        """
        args = arg.split()
        objects = storage.all()

        if not arg:
            print("** class name missing **")
        elif args[0] not in [cls.__name__ for cls in globals().values()
                             if isinstance(cls, type)]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                obj = objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")

    def default(self, arg):
        """Default command that handles class cmds: <class name>.func()

        <class name>.all(): retrieve all instances of a class
        <class name>.count(): retrieve the number of instances of a class
        <class name>.show(<id>): retrieve an instance based on its ID
        <class name>.destroy(<id>): destroy an instance based on its ID
        <class name>.update(<id>, <attribute name>, <attribute value>):
            updates an instance based on its ID
        <class name>.update(<id>, <dictionary representation>):
            updates an instance based on its ID
        Note: d = ast.literal_eval(re.search('({.+})', update_dict).group(0))
        """
        args = arg.split('.', 1)

        class_name = args[0]
        if class_name in [cls.__name__ for cls in globals().values()
                          if isinstance(cls, type)]:
            command = args[1].strip('()')
            commands = {'all': self.do_all, 'count': self.obj_count}

            if command in commands:
                commands[command](class_name)
            elif command.startswith('show'):
                obj_id = command.split('("', 1)[1].rstrip('")')
                self.do_show(args[0] + ' ' + obj_id)

            elif command.startswith('destroy'):
                obj_id = command.split('("', 1)[1].rstrip('")')
                self.do_destroy(args[0] + ' ' + obj_id)

    @staticmethod
    def obj_count(arg):
        """This prints the number of instances of a class

        Usage: <class name>.count(), retrieve the number of instances
        of a class
        """
        if not arg:
            print("** class name missing**")
        elif arg not in [cls.__name__ for cls in globals().values()
                         if isinstance(cls, type)]:
            print("** class doesn't exist **")
        else:
            counter = 0
            for key in storage.all():
                if arg == key.split('.')[0]:
                    counter += 1
            print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
