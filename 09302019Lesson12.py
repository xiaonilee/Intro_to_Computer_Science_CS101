# Q. finish crawl_web:
def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be 
    # introduced in unit 4.
    try:
        if url == "http://xkcd.com/353":
            return '<?xml version="1.0" encoding="utf-8" ?><?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html xmlns="http://www.w3.org/1999/xhtml"> <head> <title>xkcd: Python</title> <link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /> <!--[if IE]><link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /><![endif]--> <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /> <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /> <link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> <link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> </head> <body> <div id="container"> <div id="topContainer"> <div id="topLeft" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s">\t<ul> <li><a href="http://xkcd.com/554"">Archive</a><br /></li>\t <li><a href="http://blag.xkcd.com/">News/Blag</a><br /></li> <li><a href="http://store.xkcd.com/">Store</a><br /></li> <li><a href="/about/">About</a><br /></li> <li><a href="http://forums.xkcd.com/">Forums</a><br /></li> </ul> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="topRight" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <div id="topRightContainer"> <div id="logo"> <a href="/"><img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/></a> <h2><br />A webcomic of romance,<br/> sarcasm, math, and language.</h2> <div class="clearleft"></div> <br />XKCD updates every Monday, Wednesday, and Friday. </div> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> <div id="contentContainer"> <div id="middleContent" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"><h1>Python</h1><br/><br /><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><br/><br/><img src="http://imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python yesterday. It was wonderful. Perl, Im leaving you." alt="Python" /><br/><br/><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><h3>Permanent link to this comic: http://xkcd.com/353/</h3><h3>Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/python.png</h3><div id="transcript" style="display: none">[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]Guy 1: You39;re flying! How?Guy 2: Python!Guy 2: I learned it last night! Everything is so simple!Guy 2: Hello world is just 39;print &quot;Hello, World!&quot; 39;Guy 1: I dunno... Dynamic typing? Whitespace?Guy 2: Come join us! Programming is fun again! It39;s a whole new world up here!Guy 1: But how are you flying?Guy 2: I just typed 39;import antigravity39;Guy 1: That39;s it?Guy 2: ...I also sampled everything in the medicine cabinet for comparison.Guy 2: But i think this is the python.{{ I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I39;m leaving you. }}</div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="middleFooter" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /> <map name="comicmap"> <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /> <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /> <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /> <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /> <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /> </map><br/><br />Search comic titles and transcripts:<br /><script type="text/javascript" src="//www.google.com/jsapi"></script><script type="text/javascript"> google.load(\"search\", \"1\"); google.setOnLoadCallback(function() { google.search.CustomSearchControl.attachAutoCompletion( \"012652707207066138651:zudjtuwe28q\", document.getElementById(\"q\"), \"cse-search-box\"); });</script><form action="//www.google.com/cse" id="cse-search-box"> <div> <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /> <input type="hidden" name="ie" value="UTF-8" /> <input type="text" name="q" id="q" autocomplete="off" size="31" /> <input type="submit" name="sa" value="Search" /> </div></form><script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&lang=en"></script><a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a><br /> <br/> <div id="comicLinks"> Comics I enjoy:<br/> <a href="http://www.qwantz.com">Dinosaur Comics</a>, <a href="http://www.asofterworld.com">A Softer World</a>, <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>, <a href="http://www.boltcity.com/copper/">Copper</a>, <a href="http://questionablecontent.net/">Questionable Content</a>, <a href="http://achewood.com/">Achewood</a>, <a href="http://wondermark.com/">Wondermark</a>, <a href="http://thisisindexed.com/">Indexed</a>, <a href="http://www.buttercupfestival.com/buttercupfestival.htm">Buttercup Festival</a> </div> <br/> Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).<br/> <br/> <h4>We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. <br />The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.<br />This is not the algorithm. This is close.</h4><br/> <div class="line"></div> <br/> <div id="licenseText"> <!-- <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"><img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /></a><br/> --> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.<!-- <rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "><Work rdf:about=""><dc:creator>Randall Munroe</dc:creator><dcterms:rightsHolder>Randall Munroe</dcterms:rightsHolder><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:source rdf:resource="http://www.xkcd.com/"/><license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /></Work><License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"><permits rdf:resource="http://web.resource.org/cc/Reproduction" /><permits rdf:resource="http://web.resource.org/cc/Distribution" /><requires rdf:resource="http://web.resource.org/cc/Notice" /><requires rdf:resource="http://web.resource.org/cc/Attribution" /><prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /><permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /></License></rdf:RDF> --> <br/> This means you\"re free to copy and share these comics (but not to sell them). <a href="/license.html">More details</a>.<br/> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> </div> </body></html> '
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

def union(p, q):
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
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
        return crawled


# Q. product_list:
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    result = 1
    for e in list_of_numbers:
        result = result * e
    return result

print(product_list([9]))
#>>> 9

print(product_list([1,2,3,4]))
#>>> 24

print(product_list([]))
#>>> 1

# Q. greatest:
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    max = 0
    for e in list_of_numbers:
        if e > max:
            max = e
    return max

print(greatest([4,23,1]))
#>>> 23
print(greatest([]))
#>>> 0

# Q. total_enrollment:
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

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(university):
    students = 0
    total_tuitions = 0
    for e in university:
        students += e[1]
        total_tuitions += e[2] * e[1]
    return students, total_tuitions

print(total_enrollment(udacious_univs))
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

print(total_enrollment(usa_univs))
#>>> (77285,3058581079)

#Q. max_pages:
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
    limit = 0
    while tocrawl and limit < max_pages:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            limit += 1
    return crawled

print(crawl_web("http://www.udacity.com/cs101x/index.html",1))
#>>> ['http://www.udacity.com/cs101x/index.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",3))
#>>> ['http://www.udacity.com/cs101x/index.html', 
#>>> 'http://www.udacity.com/cs101x/flying.html', 
#>>> 'http://www.udacity.com/cs101x/walking.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",500)) 
#>>> ['http://www.udacity.com/cs101x/index.html', 
#>>> 'http://www.udacity.com/cs101x/flying.html', 
#>>> 'http://www.udacity.com/cs101x/walking.html', 
#>>> 'http://www.udacity.com/cs101x/crawling.html', 
#>>> 'http://www.udacity.com/cs101x/kicking.html']


#Q. max_Depth
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
            return  ('<a href="http://top.contributors/elssar.html">'
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
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
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

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    i = 1
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            if i <= max_depth:
                union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        i += 1
    return crawled

print(crawl_web("http://www.udacity.com/cs101x/index.html",0))
#>>> ['http://www.udacity.com/cs101x/index.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",1))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",50))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

print(crawl_web("http://top.contributors/forbiddenvoid.html",2))
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

print(crawl_web("A1",3))
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)

