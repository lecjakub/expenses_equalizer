import cmd
import parsers
from equalizer import Equalizer


class Command(cmd.Cmd):
    intro = 'Welcome to the expenses equalizer shell. Type help or ? to list commands.\n'
    prompt = '[exp_eq] '
    file = None
    eq = Equalizer()

    def do_member(self, arg):
        try:
            args = parsers.member_parser.parse_args(arg.split())
        except Exception as exc :
            print(exc)
            return
        print(f"in member command! args: {arg}")
        if args.cmd == 'add':
            print(f"Creating new member: {args.new_member}")
            self.eq.add_member(args.new_member)

    def do_exp(self, arg):
        try:
            args = parsers.exp_parser.parse_args(arg.split())
        except Exception as exc :
            print(exc)
            return
        print(f"in expenses command! args: {arg}")
        if args.cmd == 'load':
            print('in load command')
            if args.f:
                print('load from file')
            if args.u:
                print('load from url')

    def do_exit(self, arg):
        print('Thank you for using Expenses Equalizer.')
        return True

    def precmd(self, line:str):
        if not (line.startswith('exp load') or len(line) == 0):
            if not self.check_spreadsheet():
                return ""
        return line

    def check_spreadsheet(self):
        if self.eq.spreadsheet is None:
            ans = input(
                "No spreadsheet loaded. Do you want to initialize new one? [y/n]")
            if ans.lower() == 'y':
                self.eq.init_spreadsheet()
                return True
            else: return False
        else: return True
