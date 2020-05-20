
#Stack 

***Front-end***
HTML5 (Used HTML5 up template as base, I included their readme below)
CSS3
JavaScript

***Back-end***
Django 3.0.6
Python 3.8
SQLite


#Notes

This project was created by integrating an HTML5up template with a Django back-end.  It was also created with an
Anaconda environment.  To duplicate the project:

1.  create environment with Anaconda3.0
2.  Install the following packages into the created environment:
	1) Django 3.0.6
	2) python-decouple 3.3
	3) django-crispy-forms 1.9.1
	4) django-floppyforms 1.9.0
3. add appropriate information into the .env file located in the main directory
**do not host your personal information located in the .env file in production**
4.  create a superuser
5.  remember to makemigrations and migrate


If you are looking to run other HTML templates on Django, checkout the Django template tags I used in the HTML pages.
I also replaced the original form with a Django form which connects directly to the Django DB.  The form is designed to be added to
the database and send you an email when someone fills out the form.

Please note the routing in the python files
and the template tags for the form in the HTML.

As noted earlier, I included the readme for the HTML5up template below. 

-Erik


#HTML5 Up readme

Prologue by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)



This is Prologue, a simple, single page responsive site template. It features a
clean, minimalistic design and a sticky sidebar with navigation-linked scrolling.

Demo content images* are courtesy of the ridiculously talented Felicia Simion. Check out
more of her amazing work over at deviantART:

http://ineedchemicalx.deviantart.com/

(* = Not included! Only meant for use with my own on-site demo, so please do NOT download
and/or use any of Felicia's work without her explicit permission!)

Demo banner images* courtesy of Unsplash, a radtastic collection of CC0 (public domain)
images you can use for pretty much whatever.

(* = Not included)

AJ
aj@lkn.io | @ajlkn

PS: Not sure how to get that contact form working? Give formspree.io a try (it's awesome).


Credits:

	Demo Images:
		Felicia Simion (ineedchemicalx.deviantart.com)
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)