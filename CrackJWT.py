#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

import sys
import jwt
import termcolor
from colorama import init
import argparse


init(autoreset=True)
def check_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--str', dest='jwt_str', type=str, help='input jwt code')
    parser.add_argument('-p', dest='keys', type=str, help='input key\'s dir')
    parser.add_argument('-a', dest='algorithm', type=str, help='input encryption algorithm')
    return parser.parse_args().jwt_str, parser.parse_args().keys, parser.parse_args().algorithm

def print_sign():
    BANNER = r"""   
                              _        ___  _    _  _____ 
                             | |      |_  || |  | ||_   _|
      ___  _ __   __ _   ___ | | __     | || |  | |  | |  
     / __|| '__| / _` | / __|| |/ /     | || |/\| |  | |  
    | (__ | |   | (_| || (__ |   <  /\__/ /\  /\  /  | |  
     \___||_|    \__,_| \___||_|\_\ \____/  \/  \/   \_/  
                                                          (v 1.0)                                               
    """
    print(BANNER)


def crack_key():
    """爆破jwt秘钥"""
    jwt_str = check_input()[0]
    passwd = check_input()[1]
    with open(passwd) as f:
        for line in f:
            key = line.strip()
            try:
                jwt.decode(jwt_str,verify=True,key=key, algorithms=check_input()[2])
                print(termcolor.colored(r"[+]","green"),"found key successfully-->",termcolor.colored(key,"green"))
                break
            except (
                    jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError,
                    jwt.exceptions.InvalidIssuedAtError,
                    jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError
            ):
                print(r"[+] found key successfully!!!  -->",termcolor.colored(key,"green"))
                break
            except jwt.exceptions.InvalidSignatureError:
                print(r"[+] try key:", key, r'-->', termcolor.colored("error", "red"))
                continue
        else:
            print(r"[+] Done! no key was found\n")



if __name__ == '__main__':
    check_input()
    print_sign()
    crack_key()
