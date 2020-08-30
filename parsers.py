import argparse

class ConsoleParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'{message}')

################ -member- command parser ################
member_parser = ConsoleParser("member")
mem_subparsers = member_parser.add_subparsers(dest='cmd')

add_parser = mem_subparsers.add_parser('add', help='add new member')
add_parser.add_argument("new_member",type=str, help='member name')


################ -exp- command parser ################
exp_parser = ConsoleParser("expenses")
exp_subparsers = exp_parser.add_subparsers(dest='cmd')

load_parser = exp_subparsers.add_parser('load',help='load expenses data')
load_parser.add_argument('-u',help="load from url", type=str)
load_parser.add_argument('-f', help='load from file', type=str)

add_exp_parser = exp_subparsers.add_parser('add', help='add expense')
add_exp_parser.add_argument('member',type=str, help=' member who pay the expense')
add_exp_parser.add_argument('expenses', type=float,nargs='+',help='list of float number expenses')
add_exp_parser.add_argument('-b', type=str,metavar='borrower_name', help='specity who should pay for those expenses')

print_exp_parser = exp_subparsers.add_parser('print',help='printing stored expenses')
print_exp_parser.add_argument('-m',type=str,nargs='+', metavar='member_names', help='print expenses of specific members')
print_exp_parser.add_argument('--owed',action='store_true',help='print other member expenses which given member owe')





