#!/usr/bin/env python3
'''
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
'''
__author__ = 'm4dr1nch'
__date__ = '2022/09/05'
__deprecated__ = False
__license__ = 'GPLv3'
__version__ = '1.2'

import sys
import os
import shutil
import argparse
from argparse import RawTextHelpFormatter

# This is by no means a comprehensive list.
# Suggestions are encouraged!
logFiles = [
    '/var/log/lastlog',
    '/var/log/messages',
    '/var/log/warn',
    '/var/log/wtmp',
    '/var/log/poplog',
    '/var/log/qmail',
    '/var/log/smtpd',
    '/var/log/telnetd',
    '/var/log/secure',
    '/var/log/auth',
    '/var/log/auth.log',
    '/var/log/cups/access_log',
    '/var/log/cups/error_log',
    '/var/log/thttpd_log',
    '/var/log/spooler',
    '/var/log/nctfpd.errs',
    '/var/log/acct',
    '/var/log/snort',
    '/var/log/bandwidth',
    '/var/log/explanations',
    '/var/log/syslog',
    '/var/log/user.log',
    '/var/log/daemons/info.log',
    '/var/log/daemons/warnings.log',
    '/var/log/daemons/errors.log',
    '/var/log/news',
    '/var/log/news/news',
    '/var/log/news.all',
    '/var/log/news/news.all',
    '/var/log/news/news.crit',
    '/var/log/news/news.err',
    '/var/log/news/news.notice',
    '/var/log/news/suck.err',
    '/var/log/news/suck.notice',
    '/var/log/xferlog',
    '/var/log/proftpd/xferlog.legacy',
    '/var/log/proftpd.xferlog',
    '/var/log/proftpd.access_log',
    '/var/log/httpd/error_log',
    '/var/log/httpsd/ssl_log',
    '/var/log/httpsd/ssl.access_log',
    '/var/log/mail/info.log',
    '/var/log/mail/errors.log',
    '/var/log/ncftpd/misclog.txt',
    '/var/log/dpkg.log',
    '/var/log/cloud-init.log',
    '/var/log/cloud-init-output.log',
    '/var/log/kern.log',
    '/var/log/alternatives.log',
    '/var/log/bootstrap.log',
    '/var/log/auth.sys',
    '/var/log/btmp',
    '/var/log/mysqld/mysqld.log',
    '/var/spool/tmp',
    '/var/spool/errors',
    '/var/spool/locks',
    '/var/apache/log',
    '/var/apache/logs',
    '/usr/local/apache/log',
    '/usr/local/apache/logs',
    '/root/.ksh_history',
    '/root/.bash_history',
    '/root/.sh_history',
    '/root/.zsh_history',
    '/root/.history',
    '/root/.login',
    '/root/.logout',
    '/root/.bash_logut',
    '/root/.Xauthorit',
    '/usr/local/www/logs/thttpd_log',
    '/var/adm',
    '/var/run/utmp',
    '/etc/wtmp',
    '/etc/utmp',
    '/etc/mail/access',
    '/var/account/pacct',
    '/etc/httpd/logs/error_log'
]

logFileDirs = [
    '/var/log/apt/',
    '/var/log/lxd/',
    '/var/log/tomcat9/',
    '/var/log/installer/',
    '/var/log/dist-upgrade/',
    '/var/log/journal/',
    '/var/log/landscape/'
]

# Terminal colors
class colors:
    # Text effects
    RST = '\033[0m'
    FG_RST = '\033[39m'
    BG_RST = '\033[49m'
    BOLD = '\033[1m'

    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    BROWN = '\033[38;2;220;120;50m'

    # Backgrounds
    BG_RED = '\033[41m'
    BG_YELLOW = '\033[43m'
    BG_CYAN = '\033[46m'

    # Bright colors
    B_RED = '\033[91m'
    B_GREEN = '\033[92m'
    B_YELLOW = '\033[93m'
    B_CYAN = '\033[96m'

def banner():
    print(f'{colors.BOLD}{colors.B_RED}')
    print(f'               (&&      @&(')
    print(f'              %% &     &. /&')
    print(f'              &.  @#& %#    @&')
    print(f'              \&     %&*      %&')
    print(f'          .__   &      $/       &%')
    print(f'         %&  (&@%..              @*    .%')
    print(f'           &                     &(    .&&*')
    print(f'           #&\  {colors.B_YELLOW}▄▄▄· ▄· ▄▌▄▄▄{colors.B_RED}     @,   %%  %%')
    print(f'  &#\       &  {colors.B_YELLOW}▐█ ▄█▐█▪██▌▀▄ █·▪{colors.B_RED}   \(*/&     &,')
    print(f'./&  &    %/*   {colors.B_YELLOW}██▀·▐█▌▐█▪▐▀▀▄  ▄█▀▄{colors.B_RED}        %&')
    print(f' %&   \$$      {colors.B_YELLOW}▐█▪·• ▐█▀·.▐█•█▌▐█▌.▐▌{colors.B_RED}       &')
    print(f'  *@#          {colors.B_YELLOW}.▀     ▀ • .▀  ▀ ▀█▄▀▪{colors.B_RED}     ,&')
    print(f'    @&                                  &@')
    print(f'  {colors.BROWN}.<!%#$%#$$$%#$#@$#%#@#$#%#$%#$@#$@%@###$%^&>.')
    print(f'/@(        ====            ========    &(     &\\')
    print(f'@/                 {colors.B_YELLOW}╦  ╔═╗╔═╗{colors.BROWN}          &,  {colors.B_YELLOW}\\\\\\{colors.BROWN}  &\\')
    print(f'&%            ───  {colors.B_YELLOW}║  ║ ║║ ╦{colors.BROWN}  ───     &  {colors.B_YELLOW}\\\\\\\\\\{colors.BROWN} #&')
    print(f'\&.   =====        {colors.B_YELLOW}╩═╝╚═╝╚═╝{colors.BROWN}          #%  {colors.B_YELLOW}\\\\\\{colors.BROWN}  &/')
    print(f' \&..      ====          =========     *&,   %&/')
    print(f'   *<%#$%#$$&^%*%$#$$%#$^$^&$#$$@#%$%&%^%$^&>*')
    print(f'      {colors.FG_RST}Created by: {colors.B_CYAN}{__author__}')
    print(f'      {colors.FG_RST}Version: {colors.B_CYAN}{__version__}')
    print(f'{colors.RST}')

def getArgs():
    # Help menu text
    help_text_help = 'Show this help message!'
    help_text_method = (
        'Select a method to use. Available methods:\n'
        '1. delete\t| Permanently deletes log files;\n'
        '2. clear\t| Fills log files with null values. Log files themselves remain;'
    )
    help_text_scope = (
        'Select the removal scope. Available options:\n'
        '1. all\t| Attempt to delete as many logs as possible;'
    )

    parse = argparse.ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    parse.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=help_text_help)
    parse.add_argument('--method', required=True, choices=['delete', 'clear'], metavar='METHOD', help=help_text_method)
    parse.add_argument('--scope', required=True, choices=['all'], metavar='SCOPE', help=help_text_scope)

    return vars(parse.parse_args())

'''
Print colored output to the screen.
Available types (Int):
1. WARNING
2. INFO
3. ERROR
4. CONFIRM
5. DANGER
6. SUCCESS  (Small)
7. FAILED   (Small)
'''
def write(text, type):
    if type == 1:
        print(f'{colors.BOLD}{colors.BG_YELLOW}{colors.BLACK}[WARNING]{colors.RST} {text}')
    elif type == 2:
        print(f'{colors.BOLD}[{colors.YELLOW}INFO{colors.FG_RST}]{colors.RST} {text}')
    elif type == 3:
        print(f'{colors.BOLD}[{colors.B_RED}ERROR{colors.FG_RST}]{colors.RST}{colors.B_RED} {text}{colors.RST}')
    elif type == 4:
        ans = input(f'{colors.BOLD}{colors.BG_CYAN}[CONFIRM]{colors.RST} {text}')
        return ans
    elif type == 5:
        print(f'{colors.BOLD}{colors.BG_RED}[DANGER]{colors.BG_RST}{colors.B_RED} {text}{colors.RST}')
    elif type == 6:
        print(f'{colors.BOLD}[{colors.B_GREEN}+{colors.FG_RST}]{colors.RST}{colors.B_GREEN} {text}{colors.RST}')
    elif type == 7:
        print(f'{colors.BOLD}[{colors.B_RED}-{colors.FG_RST}]{colors.RST}{colors.B_RED} {text}{colors.RST}')

def deleteFiles():
    write('Deleting log files...', 1)
    for log in logFiles:
        try:
            os.remove(log)
            write(f'Removed: {log}', 6)
        except:
            write(f'Not found: {log}', 7)

def deleteLogDirs():
    write('Looking for files in common directories...', 2)
    for directory in logFileDirs:
        try:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(filepath)
                except:
                    write(f'Failed to delete: {file_path}', 7)
        except:
            write(f'Directory not found: {directory}', 7)

def clearFiles():
    write('Clearing log files...', 1)
    for log in logFiles:
        try:
            f = open(log, 'w')
            f.write('')
            f.close()
            write(f'Cleared: {log}', 6)
        except:
            write(f'Not found: {log}', 7)

def clearLogDirs():
    write('Looking for files in common directories...', 2)
    for directory in logFileDirs:
        try:
            clearLogDir(directory)
        except:
            write(f'Directory not found: {directory}', 7)

def clearLogDir(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                f = open(file, 'w')
                f.write('')
                f.close()
            elif os.path.isdir(file_path):
                clearLogDir(directory)
        except:
            write(f'Failed to delete: {file_path}', 7)

def confirm():
    ans = write('Are you sure you want to delete the files? Y/n: ', 4)
    if (str.lower(ans) == 'n'):
        write('Exiting...', 2)
        return False
    return True

def main():
    banner()
    args = getArgs()
    uid = os.getuid()

    try:
        if (args['scope'] == 'all'):
            if (args['method'] == 'delete'):
                if (uid == 0):
                    write('Superuser privileges detected!', 5)
                    write('This will delete all of the log and history files!', 1)
                    if (not confirm()): return
                else:
                    write('Superuser privileges not found!', 1)
                    write('This will attempt to delete all of the log files and history files!', 1)
                    if (not confirm()): return
                deleteFiles()
                deleteLogDirs()
            elif (args['method'] == 'clear'):
                if (uid == 0):
                    write('Superuser privileges detected!', 5)
                    write('This will clear all of the log files and history files!', 1)
                    if (not confirm()): return
                else:
                    write('Superuser privileges not found!', 1)
                    write('This will attempt to clear all of the log files and history files!', 1)
                    if (not confirm()): return
                clearFiles()
                clearLogDirs()

    except:
        write('Exiting...', 2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        write('Exiting...', 2)