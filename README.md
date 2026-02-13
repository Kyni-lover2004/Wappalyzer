Hey everyone. This is a simple python tool I made to check what technologies a website is using. I am learning web pentesting and I wanted to automate the "recon" part where you look for CMS, servers, and versions.

**(Note: I have permission and am authorized to perform this pentest on the targets I scan)**

### What it does:
- Checks the HTTP headers for server info (like Nginx or Apache).
- Uses Wappalyzer to find things like WordPress, jQuery, or PHP versions.
- Uses BuiltWith to see what else is hidden in the site code.
- Prints everything in colors so it's easier to read.

### Getting started
You need to install some libraries first. Run these commands in your terminal:

```bash
pip install requests
pip install python-Wappalyzer
pip install builtwith
pip install colorama
```

### How to use it
It is very easy to run. Just use this command:

```bash
python analyzer.py site.com
```

### Why I made this
I am practicing on TryHackMe and HackTheBox and I got tired of checking headers manually in the browser. This script helps me see quickly if a site has old versions of software that might have bugs/CVEs.

### To-do list (Maybe):
- [ ] Save the results to a .txt file
- [ ] Add more headers to check
- [ ] Make it faster

### Warning
Don't use this on sites you don't own or don't have permission to test. Use it for learning and ethical stuff only!
