import cmd
class Command(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    file = None

    def do_member(self,arg):
        print("in member command! args: {}".format(arg))

    def do_exp(self, arg):
        print("in expenses command! args: {}".format(arg))