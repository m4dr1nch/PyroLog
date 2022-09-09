----
# PyroLog
## Introduction
**PyroLog** is an effective but also a simple log cleaner. This is a tool that can be used to clear your tracks as a pen-tester or just clean a computer. **PyroLog** is currently only available on Linux and requires python3.

![screenshot](https://i.imgur.com/IGhVAmO.jpeg)

*(No dependencies)*

## Help Menu
```
usage: pyrolog.py [-h] --method METHOD --scope SCOPE

options:
  -h, --help       Show this help message!
  --method METHOD  Select a method to use. Available methods:
                   1. delete    | Permanently deletes log files;
                   2. clear     | Fills log files with null values. Log files themselves remain;
  --scope SCOPE    Select the removal scope. Available options:
                   1. all       | Attempt to delete as many logs as possible;
```