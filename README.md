# WinReg_Search

Search for a registry value over multiple machines. Searching for registry value altered by malcious software.

## Code Example

First the remote registry service must be turned on for the machines to be scanned. This is done by running regscript_on.bat.
Regscript_on iterates through a list of computer names in a text file called complist.txt. 
windows_registry.py pulls from the same list of computer names and then searches for the specific key change
for every user on the machine.

## Motivation

Network hit with malware/virus. This was to help find the origin machine.

[Link 1 to potential virus info](http://www.virusradar.com/en/Win32_Zlader.L/description)

[Link 2 to potential virus info](http://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/worm_zlader.b)

## Installation

Download or fork on github. Running Python 3.5.
