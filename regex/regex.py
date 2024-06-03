"""regular expression helps to find paatter inside a string 
Regular expression module:- re"""
import re 
mystr = "You can learn any programming language, whether it is Python2, Python3, Pearl, Java, javascript or PHP."

# match() method, finds matching at the begining of the scene
#sysntax
"""
var = re.match(pattern, string, optional flags"""
var1 = re.match("You",mystr)
print(var1)

#ignore cases in the string
var1 = re.match("you",mystr,re.I)
print(var1)


# search() :- used to match in entire string 
"""
var = re.search(pattern, string, optional flags"""

arp = "Internet  192.168.1.1             4   0011.2233.4455  ARPA   Vlan1"
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*",arp) # r is raw string 
# . :- any charecter except new line 
# + :- previos expression can repeat multiple time, + one or more exoressions, * zero or more repetations 
# ?
print(a.group(1))

"""
Breaking Down the Regular Expression
Let's dissect the regular expression pattern r"(.+?) +(\d) +(.+?)\s{2,}(\w)*":

(.+?):

. matches any character except newline.
+ matches one or more of the preceding token.
? makes the + non-greedy, meaning it will match as few characters as possible.
(.+?) captures this match in a group.
+:

matches a space.
+ matches one or more spaces.
(\d):

\d matches any digit (0-9).
(\d) captures this match in a group.
+:

matches a space.
+ matches one or more spaces.
(.+?):

. matches any character except newline.
+ matches one or more of the preceding token.
? makes the + non-greedy, meaning it will match as few characters as possible.
(.+?) captures this match in a group.
\s{2,}:

\s matches any whitespace character (space, tab, newline).
{2,} matches 2 or more of the preceding whitespace characters.
(\w)*:

\w matches any word character (alphanumeric or underscore).
* matches 0 or more of the preceding token.
(\w)* captures this match in a group.
Explanation of Captured Groups
Given the ARP entry string, let's see what each part of the regex captures:

(.+?): Matches and captures Internet.
+: Matches the spaces following Internet.
(\d): Matches and captures 4.
+: Matches the spaces following 4.
(.+?): Matches and captures 192.168.1.1.
\s{2,}: Matches the two or more spaces following 192.168.1.1.
(\w)*: Matches and captures word characters after the spaces (e.g., ARPA, Vlan1).
Adjusted Regular Expression
The given regular expression pattern does not correctly match the provided ARP entry string. Here's an improved version of the regex pattern to capture all relevant parts of the ARP entry:

python
Copy code
import re

arp = "Internet  192.168.1.1             4   0011.2233.4455  ARPA   Vlan1"
pattern = r"(\S+)\s+(\S+)\s+(\d+)\s+([\da-fA-F\.]+)\s+(\S+)\s+(\S+)"
match = re.search(pattern, arp)

if match:
    protocol = match.group(1)
    ip_address = match.group(2)
    age = match.group(3)
    mac_address = match.group(4)
    arp_type = match.group(5)
    interface = match.group(6)
    
    print(f"Protocol: {protocol}")
    print(f"IP Address: {ip_address}")
    print(f"Age: {age}")
    print(f"MAC Address: {mac_address}")
    print(f"ARP Type: {arp_type}")
    print(f"Interface: {interface}")
    
Explanation of the Improved Regex
(\S+): Matches and captures non-whitespace characters for Protocol.
\s+: Matches one or more whitespace characters.
(\S+): Matches and captures non-whitespace characters for IP Address.
\s+: Matches one or more whitespace characters.
(\d+): Matches and captures one or more digits for Age.
\s+: Matches one or more whitespace characters.
([\da-fA-F\.]+): Matches and captures MAC address characters (digits, a-f, A-F, and dots).
\s+: Matches one or more whitespace characters.
(\S+): Matches and captures non-whitespace characters for ARP Type.
\s+: Matches one or more whitespace characters.
(\S+): Matches and captures non-whitespace characters for Interface.

"""