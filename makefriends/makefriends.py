#!/usr/bin/env/python 

# multiline comment with the html code for the page 

try: 
	USERS=open("users.txt", "r")

except IOerror: 
	print "Error opening user database!"

# now initialize the html code 
html_code=""" 
<html>
<head>
    <link rel="stylesheet" href="./makefriends.css">
    <title>PluggedIn - make friends</title>
</head>
    
<body> 

    <div class="topmenu">
        <a href="dashboard">Dashboard</a> &emsp;&emsp;&emsp;&emsp;
        <a href="makefriend">Make a friend</a> &emsp;&emsp;&emsp;&emsp;
        <a href="seefriend">See a friend</a>  &emsp;&emsp;&emsp;&emsp; 
        <div class="logout">
        <a href="http://www.cs.mcgill.ca/~ycukra/PluggedIn/home/">Logout</a></div>
    </div>

    <div class="content">
    	<div class="header"><h1>Connect.</h1> </div>
    	<div class="userlist">
    		<form name="checkusers" method="post"> <!-- action, method--> 
"""

currentuser=USERS.readline() # get username 

while currentuser!="":

	USERS.readline() # next line will be password, which we don't need 
	currentfullname=USERS.readline()
	USERS.readline() # next line will be job desc, which we don't need 

	# create checkbox 
	html_code += ("""
		<div class="check"><input type="checkbox" name="makefriend" value="%s"></div>
		""" % currentuser) 
	html_code += ("""
		<div class="username"><h3>%s</h3></div> 
		""" % currentuser)
	# append full name 
	html_code += ("""<div class="fullname"><h3>%s</h3></div>
		""" % currentfullname) 
	# line break 
	html_code += (""" </br>

		""")
	currentuser=USERS.readline() # now, get next username 

USERS.close() # close the file 

# finish HTML code 
html_code += """
		</div> 
	</div>
</body>

</html>"""

INDEX=open("index.html", "w")
except IOerror:
	print "Error writing to HTML doc!"	