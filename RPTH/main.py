import argparse

from .encode import json_to_pth
from .decode import pth_to_json


def arg_parser():
    parser = argparse.ArgumentParser(prog='rpth',
                                     description='Decoding pth to json OR Encode decoded-json to pth',
                                     usage="%(prog)s <cmd> -i <input_path> -o <output_path>")
    parser.add_argument('cmd', type=str, choices=['encode', 'decode'], help="What do you like to do")
    parser.add_argument('-i', '--input', type=str, help='The path to the input file', required=True)
    parser.add_argument('-o', '--output', type=str, help='The path to the output file', required=True)

    return parser


def main():
    args = arg_parser().parse_args()
    if args.cmd == 'encode':
        json_to_pth(args.input, args.output)
    elif args.cmd == 'decode':
        pth_to_json(args.input, args.output)

