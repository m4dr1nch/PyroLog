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
__version__ = '1.4'

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

logDirs = [
    '/var/log/apt/',
    '/var/log/lxd/',
    '/var/log/tomcat9/',
    '/var/log/installer/',
    '/var/log/dist-upgrade/',
    '/var/log/journal/',
    '/var/log/landscape/',
    '/tmp/'
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
        'Select the removal scope. Available options:\n'
        '1. all\t| Attempt to delete as many logs as possible;\n'
        '2. files\t| Use only the log file wordlist;\n'
        '3. dirs\t| Use only the directory wordlist;'
    )
    incl_l_text_help = 'Append extra log/target files to the set wordlist.'
    incl_d_text_help = 'Append extra log/target directories to the directory list.'
    excl_l_text_help = 'Remove specific log/target files from the wordlist.'
    excl_d_text_help = 'Remove specific log/target directories from the directory list.'
    loglist_text_help = 'Use a custom wordlist of logfiles to clear.'
    dirlist_text_help = 'Use a custom wordlist of directories to clear.'

    parse = argparse.ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    parse.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=help_text_help)
    parse.add_argument('--method', required=True, choices=['delete', 'clear'], metavar='METHOD', help=help_text_method)
    parse.add_argument('--scope', required=True, choices=['all', 'files', 'dirs'], metavar='SCOPE', help=help_text_scope)
    parse.add_argument('--incl-l', required=False, help=incl_l_text_help, metavar='PATH', )
    parse.add_argument('--incl-d', required=False, help=incl_d_text_help, metavar='PATH')
    parse.add_argument('--excl-l', required=False, help=excl_l_text_help, metavar='PATH')
    parse.add_argument('--excl-d', required=False, help=excl_d_text_help, metavar='PATH')
    parse.add_argument('--loglist', required=False, help=loglist_text_help, metavar='PATH')
    parse.add_argument('--dirlist', required=False, help=dirlist_text_help, metavar='PATH')

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

'''
[deleteLogs, 08/09/2022, 1.0]
A function used to permamently delete target/log files and target log directories.
Used when the "delete" method is selected.
Takes an argument that defines the scope.
'''
def deleteLogs(scope):
    if scope == 'all' or scope == 'files':
        write('Deleting log files...', 1)
        for log in logFiles:
            try:
                os.remove(log)
                write(f'Removed: {log}', 6)
            except:
                write(f'Not found: {log}', 7)
    
    if scope == 'all' or scope == 'dirs':
        write('Looking for files in common directories...', 2)
        for directory in logDirs:
            try:
                for log in os.listdir(directory):
                    file_path = os.path.join(directory, log)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(filepath)
                    except:
                        write(f'Failed to delete: {file_path}', 7)
            except:
                write(f'Directory not found: {directory}', 7)

'''
[clearLogs, 13/09/2022, 1.3]
A function used to write null values to target/log files and files in target log directories.
Used when the "clear" method is selected.
Takes an argument that defines the scope.
'''
def clearLogs(scope):
    if scope == 'all' or scope == 'files':
        write('Clearing log files...', 1)
        for log in logFiles:
            try:
                f = open(log, 'w')
                f.write('')
                f.close()
                write(f'Cleared: {log}', 6)
            except:
                write(f'Not found: {log}', 7)

    if scope == 'all' or scope == 'dirs':
        write('Looking for files in common directories...', 2)
        for directory in logDirs:
            try:
                clearDirRec(directory)
            except:
                write(f'Directory not found: {directory}', 7)

'''
[clearDirRec, 13/09/2022, 1.3]
Function clears all of the files in a directory and if there are subdirectories then those are also cleared via recursion.
Used in conjunction with the "clearLogs" function when the "clear" method is selected.
'''
def clearDirRec(directory):
    for log in os.listdir(directory):
        file_path = os.path.join(directory, log)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                f = open(file_path, 'w')
                f.write('')
                f.close()
                write(f'Cleared: {file_path}', 6)
            elif os.path.isdir(file_path):
                clearDirRec(file_path)
        except:
            write(f'Failed to clear: {file_path}', 7)

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
            return wordlist.read().strip('\n').split('\n');
    except:
        write(f'Failed to open: {input}', 3)
        write('Exiting...', 2)
        return False

def main():
    banner()
    args = getArgs()
    uid = os.getuid()

    # Sets a custom wordlist if specified
    # Runs if --loglist option is set
    if args['loglist'] is not None:
        wordlist = readWordlist(args['loglist'])
        if not wordlist: return;
        globals().update(logFiles=wordlist)

    # Runs if --dirlist option is set
    if args['dirlist'] is not None:
        wordlist = readWordlist(args['dirlist'])
        if not wordlist: return;
        globals().update(logDirs=wordlist)

    # Append extras to logFiles and logDirs
    # Runs if --incl-l option is set
    if args['incl_l'] is not None:
        wordlist = readWordlist(args['incl_l'])
        if not wordlist: return;
        globals().update(logFiles=logFiles+wordlist)
    
    # Runs if --incl-d option is set
    if args['incl_d'] is not None:
        wordlist = readWordlist(args['incl_d'])
        if not wordlist: return;
        globals().update(logDirs=logDirs+wordlist)

    # Exclude entries from logFiles and logDirs
    # Runs if --excl-l option is set
    if args['excl_l'] is not None:
        wordlist = readWordlist(args['excl_l'])
        if not wordlist: return;
        newFiles = logFiles
        for word in wordlist:
            if word in newFiles:
                newFiles.remove(word)
        globals().update(logFiles=newFiles)
    
    # Runs if --excl-d option is set
    if args['excl_d'] is not None:
        wordlist = readWordlist(args['excl_d'])
        if not wordlist: return;
        newDirs = logDirs
        for word in wordlist:
            if word in newDirs:
                newDirs.remove(word)
        globals().update(logDirs=newDirs)

    scope = args['scope']
    method = args['method']

    try:
        if method == 'delete':
            if uid == 0:
                write('Superuser privileges detected!', 5)
            else:
                write('Superuser privileges not found!', 1)
            
            if scope == 'all':
                write('This will delete both the log files and log directories!', 1)
            elif scope == 'files':
                write('This will delete only the log files!', 1)
            elif scope == 'dirs':
                write('This will delete only the log directories!', 1)
            
            if not confirm(): return
            deleteLogs(scope)

        elif method == 'clear':
            if uid == 0:
                write('Superuser privileges detected!', 5)
            else:
                write('Superuser privileges not found!', 1)
            
            if scope == 'all':
                write('This will clear both the log files and log directories!', 1)
            elif scope == 'files':
                write('This will clear only the log files!', 1)
            elif scope == 'dirs':
                write('This will clear only the log directories!', 1)
            
            if not confirm(): return
            clearLogs(scope)
    except:
        write('Exiting...', 2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        write('Exiting...', 2)