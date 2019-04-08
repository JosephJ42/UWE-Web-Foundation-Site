#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html\n"

formData = cgi.FieldStorage()
title = formData.getvalue("title")
name = formData.getvalue("name")


print """
<!doctype html>

<html>
  <head>
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Clifton Rocks Form Request Accepted</title>
    <link rel="stylesheet" type="text/css" href="Style/main.css">

  </head>

  <body>
         <nav>
          <a href="Index.html"><img id="logoHBM" src="Images/logo-resized.png" alt="Clifton Rocks Logo"></a>
          <label class="menulabel" for="toggle">&#9776;</label>
          <input type="checkbox" id="toggle"/>
          <div class="menu">
  
          <a href="Line-up.html"><button class="navbutton">Line-Up</button></a>
          <a href="Tickets.html"><button class="navbutton">Tickets</button></a>
          <a href="About Us.html"><button class="navbutton">About Us</button></a>
          <a href="Index.html"><img id="logo" src="Images/logo-resized.png" alt="Clifton Rocks Logo"></a>
          <a href="Maps.html"><button class="navbutton">Maps</button></a>
          <a href="Gallery.html"><button class="navbutton">Gallery</button></a>
          <a href="Contact us.html"><button class="navbutton">Contact Us</button></a>
          </div>
      </nav>

    <article class="article">
    <img id="articleimage" src="Images/FormImg.jpg" alt="Clifton Rocks festival">
     <section class="sectiontext">
     <p class="text"><strong>{0} {1}</strong>, thank you for your inquiry. We will be in touch as soon as possible.</p> 
    </section>
         
    </article>

  </body>

</html>
""".format(title,name)