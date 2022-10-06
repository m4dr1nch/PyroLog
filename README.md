----
# PyroLog
## Introduction
**PyroLog** is an effective but also a simple log cleaner. This is a tool that can be used to clear your tracks as a pen-tester or just clean a computer. **PyroLog** is currently only available on Linux and requires python3.

![screenshot](https://i.imgur.com/6HwBSP6.jpg)

*(No dependencies)*

## Help Menu
```
usage: pyrolog.py [-h] --method METHOD --scope SCOPE [--incl-l PATH] [--incl-d PATH] [--excl-l PATH] [--excl-d PATH] [--loglist PATH] [--dirlist PATH]

options:
  -h, --help       Show this help message!
  --method METHOD  Select a method to use. Available methods:
                   1. delete    | Permanently deletes target/log files;
                   2. clear     | Fills target/log files with null values. Files themselves remain;
  --scope SCOPE    Select the removal scope. Available options:
                   1. all       | Attempt to delete as many logs as possible;
                   2. files     | Use only the log file wordlist;
                   3. dirs      | Use only the directory wordlist;
  --incl-l PATH    Append extra log/target files to the set wordlist.
  --incl-d PATH    Append extra log/target directories to the directory list.
  --excl-l PATH    Remove specific log/target files from the wordlist.
  --excl-d PATH    Remove specific log/target directories from the directory list.
  --loglist PATH   Use a custom wordlist of logfiles to clear.
  --dirlist PATH   Use a custom wordlist of directories to clear.
```

Basic usage:
```bash
sudo pyrolog.py --method clear --scope all
```