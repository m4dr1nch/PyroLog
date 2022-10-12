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
__license__ = 'GPLv3'
__version__ = '1.5'

import sys
import os
import shutil
import argparse
from argparse import RawTextHelpFormatter

# This is by no means a comprehensive list.
# Suggestions are encouraged!
finalList = []

fileList = [
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
    '/var/adm',
    '/var/run/utmp',
    '/var/account/pacct',
    '/usr/local/apache/log',
    '/usr/local/apache/logs',
    '/usr/local/www/logs/thttpd_log',
    '/etc/wtmp',
    '/etc/utmp',
    '/etc/mail/access',
    '/etc/httpd/logs/error_log'
]

directoryList = [
    '/var/log/apt/',
    '/var/log/lxd/',
    '/var/log/tomcat9/',
    '/var/log/installer/',
    '/var/log/dist-upgrade/',
    '/var/log/journal/',
    '/var/log/landscape/',
    '/tmp/'
]

homeFileList = [
    '{USER_DIR}/.ksh_history',
    '{USER_DIR}/.bash_history',
    '{USER_DIR}/.sh_history',
    '{USER_DIR}/.zsh_history',
    '{USER_DIR}/.history',
    '{USER_DIR}/.login',
    '{USER_DIR}/.logout',
    '{USER_DIR}/.bash_logut',
    '{USER_DIR}/.Xauthorit'
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


'''
[getArgs, 09/09/2022, 1.2]
A function that parses user arguments, and customizes the help menu.
Returns parsed arguments in a dictionary format.
'''
def getArgs():
    # Help menu text
    help_text_help = 'Show this help message!'
    help_text_method = (
        'Select a method to use. Available methods:\n'
        '1. delete\t| Permanently deletes target/log files;\n'
        '2. clear\t| Fills target/log files with null values. Files themselves remain;'
    )
    help_text_scope = (
        'Select the removal scope. Format: "option,option".\n'
        'Available options:\n'
        '1. all\t| Select all of the options (Dangerous);\n'
        '2. files\t| Use the wordlist with common log files;\n'
        '3. dirs\t| Select a wordlist of directories to recursively remove files in;\n'
        '4. custom\t| Select a custom wordlist, or include/exclude files from the default lists;\n'
        '5. home\t| Remove predefined history/log files in home directories;'
    )
    append_f_text_help = 'Append extra log/target files to the set wordlist.'
    append_d_text_help = 'Append extra log/target directories to the directory list.'
    remove_f_text_help = 'Remove specific log/target files from the wordlist.'
    remove_d_text_help = 'Remove specific log/target directories from the directory list.'
    loglist_text_help = 'Use a custom wordlist of logfiles to clear.'
    dirlist_text_help = 'Use a custom wordlist of directories to clear.'

    usage = 'pyrolog.py [-h] --method METHOD --scope SCOPE [OPTIONS]'

    parse = argparse.ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter, usage=usage)

    required = parse.add_argument_group('Required options')
    required.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=help_text_help)
    required.add_argument('--method', required=True, choices=['delete', 'clear'], metavar='METHOD', help=help_text_method)
    required.add_argument('--scope', required=True, metavar='SCOPE', help=help_text_scope)

    custom = parse.add_argument_group('Custom wordlist options')
    custom.add_argument('-af', required=False, help=append_f_text_help, metavar='PATH', )
    custom.add_argument('-ad', required=False, help=append_d_text_help, metavar='PATH')
    custom.add_argument('-rf', required=False, help=remove_f_text_help, metavar='PATH')
    custom.add_argument('-rd', required=False, help=remove_d_text_help, metavar='PATH')
    custom.add_argument('--loglist', required=False, help=loglist_text_help, metavar='PATH')
    custom.add_argument('--dirlist', required=False, help=dirlist_text_help, metavar='PATH')

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
    if type == 1: print(f'{colors.BOLD}{colors.BG_YELLOW}{colors.BLACK}[WARNING]{colors.RST} {text}')
    elif type == 2: print(f'{colors.BOLD}[{colors.YELLOW}INFO{colors.FG_RST}]{colors.RST} {text}')
    elif type == 3: print(f'{colors.BOLD}[{colors.B_RED}ERROR{colors.FG_RST}]{colors.RST}{colors.B_RED} {text}{colors.RST}')
    elif type == 4: return input(f'{colors.BOLD}{colors.BG_CYAN}[CONFIRM]{colors.RST} {text}')
    elif type == 5: print(f'{colors.BOLD}{colors.BG_RED}[DANGER]{colors.BG_RST}{colors.B_RED} {text}{colors.RST}')
    elif type == 6: print(f'{colors.BOLD}[{colors.B_GREEN}+{colors.FG_RST}]{colors.RST}{colors.B_GREEN} {text}{colors.RST}')
    elif type == 7: print(f'{colors.BOLD}[{colors.B_RED}-{colors.FG_RST}]{colors.RST}{colors.B_RED} {text}{colors.RST}')


'''
[deleteLogs, 08/09/2022, 1.0]
A function used to permamently delete target/log files.
Used when the "delete" method is selected.
'''
def deleteLogs():
    if len(finalList) == 0:
        write('Nothing to do ¯\_(ツ)_/¯!', 2)
        write('Exiting...', 2)
        return
    write('Deleting log files...', 1)
    for log in finalList:
        try:
            os.remove(log)
            write(f'Removed: {log}', 6)
        except PermissionError:
            write(f'Permission denied: {log}', 7)
        except:
            continue


'''
[clearLogs, 13/09/2022, 1.3]
A function used to write null values to target/log files.
Used when the "clear" method is selected.
'''
def clearLogs():
    if len(finalList) == 0:
        write('Nothing to do ¯\_(ツ)_/¯!', 2)
        write('Exiting...', 2)
        return
    write('Clearing log files...', 1)
    for log in finalList:
        try:
            if (os.path.exists(log)):
                f = open(log, 'w')
                f.write('')
                f.close()
                write(f'Cleared: {log}', 6)
        except PermissionError:
            write(f'Permission denied: {log}', 7)
        except:
            continue


'''
[confirm, 08/09/2022, 1.0]
Confirmation request.
Returns a boolean value.
On any input returns True on "n" case-insensitive returns False.
'''
def confirm():
    try:
        ans = write('Are you sure you want to continue? Y/n: ', 4)
        if (str.lower(ans) == 'n'):
            write('Exiting...', 2)
            return False
        return True
    except:
        print()
        write('Exiting...', 2)


'''
[readWordlist, 06/10/2022, 1.4]
This function reads a file and returns an array split by newlines.
The input parameter is a full path.
On success returns an array on failure False.
'''
def readWordlist(input):
    try:
        with open(input, 'r') as wordlist:
            return wordlist.read().strip('\n').split('\n')
    except:
        write(f'Failed to open: {input}', 3)
        write('Exiting...', 2)
        return False


'''
[createList, 11/10/2022, 1.5]
This function creates the final wordlist of files to be removed.
Takes an argument that is a list of input options.
Returns False on error and True on success.
'''
def createList(args):
    scope = args['scope']
    scope = scope.split(',')

    if 'all' in scope:
        write('Scope is set to "all"!', 5)
        scope = ['custom', 'files', 'dirs', 'home']

    if 'custom' in scope:
        # Adds a custom wordlist to the finalList
        # Runs if --loglist option is set
        if args['loglist'] is not None:
            wordlist = readWordlist(args['loglist'])
            if not wordlist: return False
            globals().update(finalList=wordlist)

        # Runs if --dirlist option is set
        if args['dirlist'] is not None:
            wordlist = readWordlist(args['dirlist'])
            if not wordlist: return False
            globals().update(directoryList=wordlist)

        # Append extras to the finalList or the directoryList
        # Runs if -af option is set
        if args['af'] is not None:
            wordlist = readWordlist(args['af'])
            if not wordlist: return False
            globals().update(finalList=finalList+wordlist)

        # Runs if -ad option is set
        if args['ad'] is not None:
            wordlist = readWordlist(args['ad'])
            if not wordlist: return False
            globals().update(directoryList=directoryList+wordlist)

        # Exclude directories from the directoryList
        # Runs if -rd option is set
        if args['rd'] is not None:
            wordlist = readWordlist(args['rd'])
            if not wordlist: return False
            newList = directoryList
            for word in wordlist:
                if word in newList:
                    newList.remove(word)
            globals().update(directoryList=newList)
    if 'files' in scope:
        globals().update(finalList=finalList+fileList)
    if 'dirs' in scope:
        write('Looking for files in common directories...', 2)
        dirFiles = []
        for directory in directoryList:
            enumDir(directory, dirFiles)
        globals().update(finalList=finalList+dirFiles)
    if 'home' in scope:
        write('Looking for files in home directories...', 2)
        passwd = readWordlist('/etc/passwd')
        homes = ['/root']
        files = []
        for user in passwd:
            user = user.split(':')
            if 999 < int(user[2]) < 65534 and user[5] is not None:
                homes.append(user[5])
        for home in homes:
            for file in homeFileList:
                files.append(file.replace('{USER_DIR}', home))
        globals().update(finalList=finalList+files)

    # Exclude entries from the finalList
    # Runs if -rf option is set
    if args['rf'] is not None:
        wordlist = readWordlist(args['rf'])
        if not wordlist: return False
        newList = finalList
        for word in wordlist:
            if word in newList:
                newList.remove(word)
        globals().update(finalList=newList)
    
    return True


'''
[enumDir, 12/10/2022, 1.5]
This function uses recursion to crawl a directory.
Takes to parameters:
1. A starting directory;
2. An array to store values in;
'''
def enumDir(directory, dirFiles):
    try:
        for log in os.listdir(directory):
            file_path = os.path.join(directory, log)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    dirFiles.append(file_path)
                elif os.path.isdir(file_path):
                    enumDir(file_path, dirFiles)
            except:
                continue
    except:
        return

def main():
    banner()
    args = getArgs()
    uid = os.getuid()

    if uid == 0:
        write('Superuser privileges detected!', 5)
    else:
        write('Superuser privileges not found!', 1)

    resp = createList(args)
    if not resp: return

    method = args['method']
    try:
        if method == 'delete':
            if not confirm(): return
            deleteLogs()

        elif method == 'clear':
            if not confirm(): return
            clearLogs()
    except:
        write('Exiting...', 2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        write('Exiting...', 2)
