import pandas
import requests
import configparser
import os
import argparse
from io import BytesIO
from command import Command

DEF_CONFIG = "config/config.ini"

config = configparser.ConfigParser()
parser = argparse.ArgumentParser(
    description="Manage group of people expenses, and help equally divide them.")


def load_config(config_filename):
    if os.path.isfile(config_filename):
        config.read(config_filename)
        print("Configuration loaded.")

    else:
        print("Couldn't load config file - {}".format(config_filename))


def load_exp_data():
    req = requests.get(config['remote']['url'])
    data = req.content
    df = pandas.read_csv(BytesIO(data))
    print(df.head())
    print("Data Loaded.")


def parse_args():
    parser.add_argument(
        '-c', type=str,dest='config', metavar='config_file', help="config file")
    # subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # member_parser = subparsers.add_parser('member', help='member operations')
    # member_parser.add_argument('-n',help='add new member')

    # add_parser = subparsers.add_parser('add', help='expenses operaiton')
    # add_parser.add_argument('-m', help='member name')
    args = parser.parse_args()
    print(args)
    return args


def create_def_config():
    config['remote'] = {
        'url': "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ3SK7T0uZq0DotBWk5gFOj8fYa_chLYHlFHcQR-cUwSo2Tt-9DMs-q3clBYk2IBuB5B6abVLy3q0wX/pub?gid=0&single=true&output=csv"}


if __name__ == "__main__":
    print("Welcome in expenses equalizer.")
    create_def_config()

    args = parse_args()
    if args.config:
        load_config(args.config)

    cmd = Command()
    load_exp_data()
    
    cmd.cmdloop()


