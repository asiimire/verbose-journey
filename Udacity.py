#Udacity
# 1)
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
"""def stamps(i):
    five = 0
    two = 0
    one = 0
    while i > 0:
        if i == 0:
            break
        if i >= 5:
            five = five + 1
            i = i - 5
        if i == 0:
            break
        if i < 5 or i == 2:
            two = two + 1
            i = i - 2
        if i == 0:
            break
        if i < 2 or i == 1:
            one = one + 1
            i = i - 1
    return five, two, one

print(stamps(8))
# >>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print(stamps(5))
# >>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print(stamps(29))
# >>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print(stamps(0))
# >>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
#2)
#Superhero nuisance
# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.
# Write a Python procedure, fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).
# NOTE: # If you are experiencing difficulties taking
# this problem seriously, please refer back to
# "Superhero flyby", the prequel, in Problem Set 11.
# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #
def fix_machine(debris, product):
    x = 0
    while x < len(product):
        if debris.find(product[x]) == -1:
            return "Give me something that's not useless next time."
        x += 1
    return product
print(fix_machine('UdaciousUdacitee', 'Udacity'))
print(fix_machine('buy me dat Unicorn', 'Udacity'))
print(fix_machine('AEIOU and sometimes y... c', 'Udacity'))
print(fix_machine('wsx0-=mttrhix', 't-shirt'))"""
#3)
# By Websten from forums
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
# Assume that the birthday and current date are correct dates (and no
# time travel).
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ans = 0
    mid_year = year1 + 1
    first_month = month1 + 1
    last_month = 1

    while mid_year < year2:
        if mid_year % 4 == 0:
            ans += 366
        else:
            ans += 365
        mid_year += 1

    if year1 < year2:
        while first_month <= 12:
            if first_month == 1 or first_month == 3 or first_month == 5 or first_month == 7 or first_month == 8 or first_month == 10 or first_month == 12:
                ans += 31
            elif first_month == 4 or first_month == 6 or first_month == 9 or first_month == 11:
                ans += 30
            else:
                if year1 % 400 == 0:
                    ans += 29
                elif year1 % 100 == 0:
                    ans += 28
                elif year1 % 4 == 0:
                    ans += 29
                else:
                    ans += 28
            first_month += 1

        while last_month < month2:
            if last_month == 1 or last_month == 3 or last_month == 5 or last_month == 7 or last_month == 8 or last_month == 10 or last_month == 12:
                ans += 31
            elif last_month == 4 or last_month == 6 or last_month == 9 or last_month == 11:
                ans += 30
            else:
                if year2 % 400 == 0:
                    ans += 29
                elif year2 % 100 == 0:
                    ans += 28
                elif year2 % 4 == 0:
                    ans += 29
                else:
                    ans += 28
            last_month += 1
    else:  # year1 == year2
        while first_month < month2:
            if first_month == 1 or first_month == 3 or first_month == 5 or first_month == 7 or first_month == 8 or first_month == 10 or first_month == 12:
                ans += 31
            elif first_month == 4 or first_month == 6 or first_month == 9 or first_month == 11:
                ans += 30
            else:
                if year1 % 400 == 0:
                    ans += 29
                elif year1 % 100 == 0:
                    ans += 28
                elif year1 % 4 == 0:
                    ans += 29
                else:
                    ans += 28
            first_month += 1

    if year1 == year2 and month1 == month2:
        ans += day2 - day1
    else:
        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
            ans += (31 - day1)
        elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
            ans += (30 - day1)
        else:
            if year1 % 400 == 0:
                ans += (29 - day1)
            elif year1 % 100 == 0:
                ans += (28 - day1)
            elif year1 % 4 == 0:
                ans += (29 - day1)
            else:
                ans += (28 - day1)

        ans += day2

    return ans


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()

#4)
#                 10-row School abacus
#                         by
#                      Michael H
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

"""def print_abacus(value):
       #
       ### Add you code here
       #
        x = 0
        first = True
        ans = ""
        sample = "|00000*****|"
        while x < 10:
           if first:
               ans = sample[:11 - value % 10] + '   ' + sample[11 - value % 10:] + ans
               first = False
           else: ans = sample[:11 - value % 10] + '   ' + sample[11 - value % 10:] + '\n' + ans
           value /= 10
           x += 1
        print ans

       #
       ### Add you code here
       #

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|


# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.

def jungle_animal(animal, my_speed):
    if animal == 'zebra': print "Try to ride a zebra!"
    elif animal == 'cheetah' and my_speed > 115: print "Run!"
    elif animal == 'cheetah': print "Stay calm and wait!"
    else: print "Introduce yourself!"

jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

#jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"s

# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).

def is_leap_baby(day,month,year):
    # Write your code after this line.
    if month != 2 or day != 29: return False
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False


# The function 'output' prints one of two statements based on whether
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!


# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
def find_element(s, t):
    i = 0
    for e in s:
        if e == t:
            return i
        i = i + 1
    return -1
#OR WE COULD USE A WHILE LOOP
def find_element(s, t):
    i = 0
    while e < len(s):
        if s[i] == t:
            return i
        i = i + 1
    return -1
#OR WE COULD USE INDEX
def find_element(s, t):
    i = 0
    while i < len(s):
        if s[i]==t:
            return s.index(t)
        i = i + 1
    return -1
#OR
def find_element(s, t):
    i = 0
    if t in s:
        return s.index(t)
    return -1

print
find_element([1, 2, 3], 3)
# >>> 2

# print find_element(['alpha','beta'],'gamma')
# >>> -1


# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


# To test, uncomment all lines
# below except those beginning with >>>.

a = [1, 2, 3]
b = [2, 4, 6]
union(a, b)
print(a)
# >>> [1,2,3,4,6]
print(b)
# >>> [2,4,6]
#FINISH CRAWL WEB
#Finish crawl web

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be
    # introduced in unit 4.
    try:
        if url == "http://xkcd.com/353":
            return  '<?xml version="1.0" encoding="utf-8" ?><?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html xmlns="http://www.w3.org/1999/xhtml"> <head> <title>xkcd: Python</title> <link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /> <!--[if IE]><link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /><![endif]--> <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /> <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /> <link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> <link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> </head> <body> <div id="container"> <div id="topContainer"> <div id="topLeft" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s">\t<ul> <li><a href="http://xkcd.com/554"">Archive</a><br /></li>\t <li><a href="http://blag.xkcd.com/">News/Blag</a><br /></li> <li><a href="http://store.xkcd.com/">Store</a><br /></li> <li><a href="/about/">About</a><br /></li> <li><a href="http://forums.xkcd.com/">Forums</a><br /></li> </ul> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="topRight" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <div id="topRightContainer"> <div id="logo"> <a href="/"><img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/></a> <h2><br />A webcomic of romance,<br/> sarcasm, math, and language.</h2> <div class="clearleft"></div> <br />XKCD updates every Monday, Wednesday, and Friday. </div> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> <div id="contentContainer"> <div id="middleContent" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"><h1>Python</h1><br/><br /><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><br/><br/><img src="http://imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python yesterday. It was wonderful. Perl, Im leaving you." alt="Python" /><br/><br/><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><h3>Permanent link to this comic: http://xkcd.com/353/</h3><h3>Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/python.png</h3><div id="transcript" style="display: none">[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]Guy 1: You39;re flying! How?Guy 2: Python!Guy 2: I learned it last night! Everything is so simple!Guy 2: Hello world is just 39;print &quot;Hello, World!&quot; 39;Guy 1: I dunno... Dynamic typing? Whitespace?Guy 2: Come join us! Programming is fun again! It39;s a whole new world up here!Guy 1: But how are you flying?Guy 2: I just typed 39;import antigravity39;Guy 1: That39;s it?Guy 2: ...I also sampled everything in the medicine cabinet for comparison.Guy 2: But i think this is the python.{{ I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I39;m leaving you. }}</div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="middleFooter" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /> <map name="comicmap"> <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /> <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /> <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /> <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /> <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /> </map><br/><br />Search comic titles and transcripts:<br /><script type="text/javascript" src="//www.google.com/jsapi"></script><script type="text/javascript"> google.load(\"search\", \"1\"); google.setOnLoadCallback(function() { google.search.CustomSearchControl.attachAutoCompletion( \"012652707207066138651:zudjtuwe28q\", document.getElementById(\"q\"), \"cse-search-box\"); });</script><form action="//www.google.com/cse" id="cse-search-box"> <div> <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /> <input type="hidden" name="ie" value="UTF-8" /> <input type="text" name="q" id="q" autocomplete="off" size="31" /> <input type="submit" name="sa" value="Search" /> </div></form><script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&lang=en"></script><a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a><br /> <br/> <div id="comicLinks"> Comics I enjoy:<br/> <a href="http://www.qwantz.com">Dinosaur Comics</a>, <a href="http://www.asofterworld.com">A Softer World</a>, <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>, <a href="http://www.boltcity.com/copper/">Copper</a>, <a href="http://questionablecontent.net/">Questionable Content</a>, <a href="http://achewood.com/">Achewood</a>, <a href="http://wondermark.com/">Wondermark</a>, <a href="http://thisisindexed.com/">Indexed</a>, <a href="http://www.buttercupfestival.com/buttercupfestival.htm">Buttercup Festival</a> </div> <br/> Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).<br/> <br/> <h4>We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. <br />The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.<br />This is not the algorithm. This is close.</h4><br/> <div class="line"></div> <br/> <div id="licenseText"> <!-- <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"><img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /></a><br/> --> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.<!-- <rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "><Work rdf:about=""><dc:creator>Randall Munroe</dc:creator><dcterms:rightsHolder>Randall Munroe</dcterms:rightsHolder><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:source rdf:resource="http://www.xkcd.com/"/><license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /></Work><License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"><permits rdf:resource="http://web.resource.org/cc/Reproduction" /><permits rdf:resource="http://web.resource.org/cc/Distribution" /><requires rdf:resource="http://web.resource.org/cc/Notice" /><requires rdf:resource="http://web.resource.org/cc/Attribution" /><prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /><permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /></License></rdf:RDF> --> <br/> This means you\"re free to copy and share these comics (but not to sell them). <a href="/license.html">More details</a>.<br/> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> </div> </body></html> '
        elif url == "http://xkcd.com/554":
            return  '<?xml version="1.0" encoding="utf-8" ?> <?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?> <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <title>xkcd: Not Enough Work</title> <link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /> <!--[if IE]><link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /><![endif]--> <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /> <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /> <link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> <link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> </head> <body> <div id="container"> <div id="topContainer"> <div id="topLeft" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <ul> <li><a href="/archive/">Archive</a><br /></li> <li><a href="http://blag.xkcd.com/">News/Blag</a><br /></li> <li><a href="http://store.xkcd.com/">Store</a><br /></li> <li><a href="/about/">About</a><br /></li> <li><a href="http://forums.xkcd.com/">Forums</a><br /></li> </ul> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="topRight" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <div id="topRightContainer"> <div id="logo"> <a href="/"><img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/></a> <h2><br />A webcomic of romance,<br/> sarcasm, math, and language.</h2> <div class="clearleft"></div> XKCD updates every Monday, Wednesday, and Friday. <br /> Blag: Remember geohashing? <a href="http://blog.xkcd.com/2012/02/27/geohashing-2/">Something pretty cool</a> happened Sunday. </div> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> <div id="contentContainer"> <div id="middleContent" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <h1>Not Enough Work</h1><br/> <br /> <div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/553/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t">Random</a></li> <li><a href="/555/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul> </div> <br/> <br/> <img src="http://imgs.xkcd.com/comics/not_enough_work.png" title="It39;s even harder if you39;re an asshole who pronounces &lt;&gt; brackets." alt="Not Enough Work" /><br/> <br/> <div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/553/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b">Random</a></li> <li><a href="/555/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul> </div> <h3>Permanent link to this comic: http://xkcd.com/554/</h3> <h3>Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/not_enough_work.png</h3> <div id="transcript" style="display: none">Narration: Signs your coders don39;t have enough work to do: [[A man sitting at his workstation; a female co-worker behind him]] Man: I39;m almost up to my old typing speed in dvorak [[Two men standing by a server rack]] Man  1: Our servers now support gopher. Man  1: Just in case. [[A woman standing near her workstation speaking to a male co-worker]] Woman: Our pages are now HTML, XHTML-STRICT, and haiku-compliant Man: Haiku? Woman: &lt;div class=&quot;main&quot;&gt; Woman: &lt;span id=&quot;marquee&quot;&gt; Woman: Blog!&lt; span&gt;&lt; div&gt; [[A woman sitting at her workstation]] Woman: Hey! Have you guys seen this webcomic? {{title text: It39;s even harder if you39;re an asshole who pronounces &lt;&gt; brackets.}}</div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="middleFooter" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /> <map name="comicmap"> <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /> <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /> <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /> <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /> <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /> </map><br/><br /> Search comic titles and transcripts:<br /> <script type="text/javascript" src="//www.google.com/jsapi"></script> <script type="text/javascript"> google.load("search", "1"); google.search.CustomSearchControl.attachAutoCompletion( "012652707207066138651:zudjtuwe28q", document.getElementById("q"), "cse-search-box"); }); </script> <form action="//www.google.com/cse" id="cse-search-box"> <div> <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /> <input type="hidden" name="ie" value="UTF-8" /> <input type="text" name="q" id="q" autocomplete="off" size="31" /> <input type="submit" name="sa" value="Search" /> </div> </form> <script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&lang=en"></script> <a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a> <br /> <br/> <div id="comicLinks"> Comics I enjoy:<br/> <a href="http://threewordphrase.com/">Three Word Phrase</a>, <a href="http://oglaf.com/">Oglaf</a> (nsfw), <a href="http://www.smbc-comics.com/">SMBC</a>, <a href="http://www.qwantz.com">Dinosaur Comics</a>, <a href="http://www.asofterworld.com">A Softer World</a>, <a href="http://buttersafe.com/">Buttersafe</a>, <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>, <a href="http://questionablecontent.net/">Questionable Content</a>, <a href="http://www.buttercupfestival.com/buttercupfestival.htm">Buttercup Festival</a> </div> <br/> Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).<br/> <br/> <h4>We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. <br />The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.<br />This is not the algorithm. This is close.</h4><br/> <div class="line"></div> <br/> <div id="licenseText"> <!-- <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"><img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /></a><br/> --> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>. <!-- <rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "><Work rdf:about=""><dc:creator>Randall Munroe</dc:creator><dcterms:rightsHolder>Randall Munroe</dcterms:rightsHolder><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:source rdf:resource="http://www.xkcd.com/"/><license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /></Work><License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"><permits rdf:resource="http://web.resource.org/cc/Reproduction" /><permits rdf:resource="http://web.resource.org/cc/Distribution" /><requires rdf:resource="http://web.resource.org/cc/Notice" /><requires rdf:resource="http://web.resource.org/cc/Attribution" /><prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /><permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /></License></rdf:RDF> --> <br/> This means you"re free to copy and share these comics (but not to sell them). <a href="/license.html">More details</a>.<br/> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> </div> </body> </html> '
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    greatest = 0
    for i in list_of_numbers:
        if greatest < i:
            greatest = i
    return greatest


print
greatest([4, 23, 1])
# >>> 23
print
greatest([])
# >>> 0


# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string,
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [['California Institute of Technology', 2175, 37704],
             ['Harvard', 19627, 39849],
             ['Massachusetts Institute of Technology', 10566, 40732],
             ['Princeton', 7802, 37000],
             ['Rice', 5879, 35551],
             ['Stanford', 19535, 40569],
             ['Yale', 11701, 40500]]


def total_enrollment(p):
    total_students = 0
    total_tuition = 0
    for name, students, tuition in p:
        total_students = total_students + students
        total_tuition = total_tuition + tuition * students
    return total_students, total_tuition

# print total_enrollment(udacious_univs)
# >>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside
# interpreter you might not see it.

# print total_enrollment(usa_univs)
# >>> (77285,3058581079)


# The web crawler we built at the end of Unit 3 has some serious
# flaws if we were going to use it in a real crawler. One
# problem is if we start with a good seed page, it might
# run for an extremely long time (even forever, since the
# number of URLS on the web is not actually finite). This
# question and the following one explore two different ways
# to limit the pages that it can crawl.

# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.

# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html']

print crawl_web("http://www.udacity.com/cs101x/index.html",3)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",500)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']


#
# This question explores a different way (from the previous question)
# to limit the pages that it can crawl.
#
#######

# THREE GOLD STARS #
# Yes, we really mean it!  This is really tough (but doable) unless
# you have some previous experience before this course.


# Modify the crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.
#
# For example, if max_depth is 0, the only page that should
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that
# it links to directly. If max_depth is 2, the crawl should
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
                    '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return ('<a href="http://top.contributors/elssar.html">'
                    '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
                    '<a href="http://top.contributors/johang.html">'
                    '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
                    '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
                    '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

# print crawl_web("http://www.udacity.com/cs101x/index.html",0)
# >>> ['http://www.udacity.com/cs101x/index.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",1)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html',
# >>> 'http://www.udacity.com/cs101x/crawling.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",50)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html',
# >>> 'http://www.udacity.com/cs101x/crawling.html',
# >>> 'http://www.udacity.com/cs101x/kicking.html']

# print crawl_web("http://top.contributors/forbiddenvoid.html",2)
# >>> ['http://top.contributors/forbiddenvoid.html',
# >>> 'http://top.contributors/graemeblake.html',
# >>> 'http://top.contributors/angel.html',
# >>> 'http://top.contributors/dreyescat.html',
# >>> 'http://top.contributors/johang.html',
# >>> 'http://top.contributors/charlzz.html']

# print crawl_web("A1",3)
# >>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)


# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


def check_sudoku(p):
    n = len(p) # Extract the size of grid
    digit = 1 # start with 1
    while digit <= n: # Go through each digit
        i = 0
        while i < n: # go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n: # for each entry in thr row / column
                if p[i][j] == digit: # check row count
                    row_count = row_count + 1
                if p[j][i] == digit: # check column count
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 # next row/column
        digit = digit + 1
    return True # nothing was wrong

#HOME WORK
#1#
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric():
    # Your code here

#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False

#2#
# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean():


print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
#print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])"""
#>>> 2.0

# print check_sudoku(incorrect)
# >>> False

# print check_sudoku(correct)
# >>> True

# print check_sudoku(incorrect2)
# >>> False

# print check_sudoku(incorrect3)
# >>> False

# print check_sudoku(incorrect4)
# >>> False

# print check_sudoku(incorrect5)
# >>> False


# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(number):
    hour = int(number / 3600)
    minute = int((number - hour * 3600) / 60)
    result = str(hour)
    if hour == 1:
        result += ' hour, '
    else:
        result += ' hours, '
    result += str(minute)
    if minute == 1:
        result += ' minute, '
    else:
        result += ' minutes, '
    result += str(number - hour * 3600 - minute * 60)
    if number - hour * 3600 - minute * 60 == 1:
        result += ' second'
    else:
        result += ' seconds'
    return result


print
convert_seconds(3661)
# >>> 1 hour, 1 minute, 1 second

print
convert_seconds(7325)
# >>> 2 hours, 2 minutes, 5 seconds

print
convert_seconds(7261.7)


# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(number):
    hour = int(number / 3600)
    minute = int((number - hour * 3600) / 60)
    result = str(hour)
    if hour == 1:
        result += ' hour, '
    else:
        result += ' hours, '
    result += str(minute)
    if minute == 1:
        result += ' minute, '
    else:
        result += ' minutes, '
    result += str(number - hour * 3600 - minute * 60)
    if number - hour * 3600 - minute * 60 == 1:
        result += ' second'
    else:
        result += ' seconds'
    return result


def download_time(file, f_unit, bandwidth, b_unit):
    if f_unit == 'kb':
        file *= 2 ** 10
    elif f_unit == 'kB':
        file *= 2 ** 10 * 8
    elif f_unit == 'Mb':
        file *= 2 ** 20
    elif f_unit == 'MB':
        file *= 2 ** 20 * 8
    elif f_unit == 'Gb':
        file *= 2 ** 30
    elif f_unit == 'GB':
        file *= 2 ** 30 * 8
    elif f_unit == 'Tb':
        file *= 2 ** 40
    elif f_unit == 'TB':
        file *= 2 ** 40 * 8

    if b_unit == 'kb':
        bandwidth *= 2 ** 10
    elif b_unit == 'kB':
        bandwidth *= 2 ** 10 * 8
    elif b_unit == 'Mb':
        bandwidth *= 2 ** 20
    elif b_unit == 'MB':
        bandwidth *= 2 ** 20 * 8
    elif b_unit == 'Gb':
        bandwidth *= 2 ** 30
    elif b_unit == 'GB':
        bandwidth *= 2 ** 30 * 8
    elif b_unit == 'Tb':
        bandwidth *= 2 ** 40
    elif b_unit == 'TB':
        bandwidth *= 2 ** 40 * 8

    return convert_seconds((file + 0.0) / (bandwidth + 0.0))


print
download_time(1024, 'kB', 1, 'MB')
# >>> 0 hours, 0 minutes, 1 second

print
download_time(1024, 'kB', 1, 'Mb')
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print
download_time(13, 'GB', 5.6, 'MB')
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print
download_time(13, 'GB', 5.6, 'Mb')
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print
download_time(10, 'MB', 2, 'kB')
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print
download_time(10, 'MB', 2, 'kb')
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable




