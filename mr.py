import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep

#os.system("xdg-open https://www.facebook.com/mr.be0001")
time.sleep(1)
os.system('clear')

# ARYAN escape codes for colors
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"

logo = f'''{Colors.YELLOW}
                                     



  ______          __      __                   
 
  /$$$$$$                                         
 /$$__  $$                                        
| $$  \ $$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$__  $$| $$  | $$ |____  $$| $$__  $$
| $$__  $$| $$  \__/| $$  | $$  /$$$$$$$| $$  \ $$
| $$  | $$| $$      | $$  | $$ /$$__  $$| $$  | $$
| $$  | $$| $$      |  $$$$$$$|  $$$$$$$| $$  | $$
|__/  |__/|__/       \____  $$ \_______/|__/  |__/
                     /$$  | $$                    
                    |  $$$$$$/                    
                     \______/                     

                                               
                                               
                                               
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  𑁍•𓆩⃝⃝━꯭꯭̽̽𝐓𝐡꯭𝗘 𝐅𝐚꯭̽𝐌𝐎𝐮꯭̽𝐒  ⃪ᷟ 𝐄𝐝𝐢𝐢𝐭๏꯭̽𝐑꯬꯭ ̶ͬ 𒄬•- ๛⃝₍𓆤『٭❲ 𝐀𝐫̽͜ɣ𝐚͢͡ŋ — ː › 🩶 🪽₎̚ꪹ •⃛ꭗ. ฝ'꯭Ꮗ ꜛ'𝗘𝘅'𝗼̬̬̬̬̬̬̬̬̬̬ ː »ﮩﮩﮩᰔᩚ͢ː ›🩷.꯭꯬•𝐗.꯭꯬☘️🌎^||
    乛✰  𝐎𝐨𝐏𝛅 V4RUN BOY BABY 🩷.꯭꯬•𝐗.꯭꯬☘️🌎^||
   
    𝗫𝗛𝗔𝗟𝗢 𝗠𝗔𝗝𝗘 𝗞𝗥𝗢 𝗧𝗢𝗢𝗟 𝗦𝗘  𝗕𝗔𝗖𝗛𝗔 𝗟𝗢𝗚 :)
   𝗠𝗔𝗗𝗘 𝗕𝗬 => 𝗔𝗿𝗬𝗮𝗻 𝗱𝗼𝗻 𝗯𝗮𝗯𝗬 [×]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ➜𝗠𝗨𝗟𝗧𝗬 𝗖𝗢𝗢𝗞𝗜𝗘𝗦 𝗣𝗢𝗦𝗧 𝗧𝗢𝗢𝗟 𝗘𝗡𝗝𝗢𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘
 ➜𝗠𝗨𝗟𝗧𝗬 𝗣𝗢𝗦𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗧𝗦 𝗧𝗢𝗢𝗟 𝗙𝗨𝗟𝗟 𝗪𝗢𝗥𝗞𝗜𝗡𝗚
                                               
                                               
==>  ArYan.x3  Multi Cookie PosT Tool 


{Colors.RESET}'''

def logx():
    print(logo)
    print(40 * '=')
    print(f"\t{Colors.BLUE}Author : Dakku Gang{Colors.RESET}")
    print(40 * '=')

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
      
def login_with_cookies(cookie_file_path):
    try:
        with open(cookie_file_path, 'r') as file:
            cookies = file.readlines()
    except FileNotFoundError:
        exit(f'{Colors.RED}File not found at path: {cookie_file_path}{Colors.RESET}')

    return [Start(cookie=cookie.strip()) for cookie in cookies]

def bot_comment(fb_instances, comment_file_path, post_id, delay_time):
    with open(comment_file_path, 'r') as file:
        lines = file.readlines()

    while True:
        for FB in fb_instances:
            if lines:
                random_line = random.choice(lines)
                comment_text = random_line.strip()

                Comment = FB.CommentToPost(post=post_id, text=comment_text)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if 'status' in Comment and Comment['status'] == 'success':
                    print(f'{Colors.GREEN}Comment "{comment_text}" Sent at {current_time}{Colors.RESET}')
                else:
                    print(f'{Colors.RED}Comment "{comment_text}" Not Sent at {current_time}{Colors.RESET}')
                print(40 * '=')
                time.sleep(delay_time)
            else:
                print(f'{Colors.RED}No comments found in file: {comment_file_path}{Colors.RESET}')
                break

def main():
    logx()
    cookie_file_path = input('Enter the path to your cookies text file: ')
    comment_file_path = input('Enter the path to your comments text file: ')
    post_id = input('Input ID Post: ')
    delay_time = int(input('Input delay time in seconds: '))
    fb_instances = login_with_cookies(cookie_file_path)
    bot_comment(fb_instances, comment_file_path, post_id, delay_time)
    
main()
