import os
import Assignment_6_Tools as AT
import argparse as parser


def print_menu_table():

    menu = AT.Menu()
    menu.display_menu()
    menu.menu_selections()


def main():

    print_menu_table()


if __name__ == '__main__':
    main()

