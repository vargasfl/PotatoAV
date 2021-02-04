<img src ="images/minecraft_potato.png" >

## Welcome to PotatoAV, a student antivirus software!
PotatoAV is an antivirus software that uses VirusTotal's API to scan your system for malicious files.
The program sends a MD5 hash of your file to the API scan, then takes the API's response and cleans it up for you!

#### This is what the API response looks like normally:

<img src ="images/how_the_magic_happens.png" >

#### And this is what it looks like after Potato:

<img src ="images/POTATOFIED.png" >

### What you need beforehand
In order to run Potato, you'll need Python installed on your machine. Other than that you should be good to go! Potato can run on any operating system that can run Python.

### Getting Started
After downloading, first run '__init__' so that the program can initialize itself. Not running '__init__' will lead to an error involving '.vt-config.json'.

`python3 __init__.py`

For everything after that, 'Menu' will be the way to go. Once you run it, the program will tell you everything you need to know!

`python3 Menu.py`

### Outside sources
The '__init__' code came from [4ppsec's VirusTotal API script.](https://github.com/4ppsec/virustotal-api-v2) They were definitely a huge step up from having a text file with all the hashes we want to look for.

### Other Thanks
Thanks to Gavin and Bryan for helping us smooth out the code when it didn't want to work (at all!). 

## Thanks for using PotatoAV
If you want to see more from us check out our Githubs!

[Flavio's Github](https://github.com/vargasfl)

[G's Github](https://github.com/gerardovigil)

Thanks for using PotatoAV! Bye-bye!
