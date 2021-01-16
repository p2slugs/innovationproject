# P2 Slugs - Recipe Website
Welcome to our Trimester 2 Portfolio! This is where you can find and access our code and important pieces throughout the course.

### [Scrum Board](https://github.com/orgs/p2slugs/projects/1) (tracking sheet + schedule) | includes ticket items/cards

### Link to Running Code: http://99.88.196.26/ | [Git Repository](https://github.com/p2slugs/recipebox/)

## Big Tickets/Goals Completed Week 1/11-1/15
###  1. HTML, Project Overview Page 
- __description:__ Changing the look of the website included updating the color palette, the fonts, font size, and formatting of the text. The CSS was updated to make the website more interactive and user-friendly. Although there are some pages that are not up to date, the recipes page is working well with the new format.
- __link to code:__ [base.html](https://github.com/p2slugs/recipebox/blob/main/templates/base.html) and [overview.html](https://github.com/p2slugs/recipebox/blob/main/templates/overview.html)
- __instructions to evaluate:__ review [here](http://99.88.196.26/) to see updates on the filtering system and overall appearance.
### 2. Sign Up Form 
- __description:__
- __link to code:__
- __instructions to evaluate:__
### 3. Deploy with Raspberry Pi 
- __description:__ getting the website deployed this week was a big ticket which is a card in the Scrum Board called *deploy with raspberry pi*. First, Eva had to get the site running well through Intellij, as there was a problem after transfering from repl. She edited the base.html to make room for other pages' content and allow the pages to be seen when navigated from the navabar. She edited the views.py file, made a wsgi.py file, made an init.py file, and a requirements1.txt file in prep of deployment. Following Mr. Mortensen's steps for deploying, she was able to get a virtual environment finally created but ran into more problems later on. By the running the website through her raspberry pi, she got the website up for everyone to see on her personal ip address (port forwarded).
- __link to code:__ [wsgi.py](https://github.com/p2slugs/recipebox/blob/main/wsgi.py), [init.py](https://github.com/p2slugs/recipebox/blob/main/__init__.py), [views.py](https://github.com/p2slugs/recipebox/blob/main/views.py), [base.html](https://github.com/p2slugs/recipebox/blob/main/templates/base.html); Check Github Contributions above for specific changes
- __instructions to evaluate:__ the website can been viewed from this link http://99.88.196.26/ 
### 4. User Request Form Output/Storing Inputted Data 
- __description:__ after building a user input form, Ali's goal was to try and store a user's inputted name and comment on a seperate page or index by making a index template page to intake information from the input form. He was successful in getting the index page to work for the user's name, but it still working on finding a solution for the comment. This ticket is in the Scrum Board called *User Request Form Output/Storing Inputted Data*
- __link to code:__ http://99.88.196.26/ ; Check Github Contributions above for specific changes
- __instructions to evaluate:__ the website can been viewed from this link http://99.88.196.26/.  Click on the recipe request page and you will see a fill-in section. After clicking submit, a page redirect should occur where the name typed in should be stored.

## Scrum Master Grading Based on Above and Individual Support
__Individual Support__

Ali 19/20
1. tickets/cards: User Request Form Output/Storing Inputted Data; Ali would lose a point this week because the ticket didn't perfectly match up with his code. Though he was ale to store user inputted names on a seperate page through the index template, he wasn't able to store user comments on that same page, which he needs to try and fix next week. Everything else went well with Ali, regarding his code and success with the templates he worked on.
2. evidence of code: [views.py](https://github.com/p2slugs/recipebox/blob/main/views.py), [sign.html](https://github.com/p2slugs/recipebox/blob/main/templates/sign.html), [index.html](https://github.com/p2slugs/recipebox/blob/main/templates/index.html)
3. guidance for running and reviewing code: the website can been viewed from this link http://99.88.196.26/. Click on the recipe request page and you will see a fill-in section. After clicking submit, a page redirect should occur where the name typed in should be stored.

Linda
1. tickets/cards: I completed the sign up form, and helped a little on solving issues with deployment. I learned from Ms. Trish Ladd's lectures and her templates to create a sign up page with html/css/js with our project's theme. Together with Eva, we found out specific files that needed to be added and Eva did the deployment.
2. evidence of code:
3. guidance for running and reviewing code:

Sophie 19/20
1. tickets/cards: 1) Find out how to filter recipes with tags - successful; can check progress on recipes.html or the recipes page, 2) Clean up appearance of site and make main pages look similar - definitely made the website more aesthetically pleasing on the main pages, but some other pages (such as sign up and about us) did not match the css, thus -1pt.
2. evidence of code: Check out [base.html](https://github.com/p2slugs/recipebox/blob/main/templates/base.html), [recipes.html](https://github.com/p2slugs/recipebox/blob/main/templates/recipes.html), and [overview.html](https://github.com/p2slugs/recipebox/blob/main/templates/overview.html) for my updates on the code.
3. guidance for running and reviewing code: the website can be viewed at http://99.88.196.26/. The "recipes" page should feature a filtering system where you can select what you want to see based on meal types and dietary preferences.

Eva
1. tickets/cards: I completed the the raspberry pi big ticket item, also helped with minor changes like adding in the about us pictures. I did a lot for getting the website able to run and it worked out in the end! I had to fix our Intellij problem, make an init.py, wsgi.py file, and edit the views.py file as well. I plan to get it running solely with the new way later on.
2. evidence of code: code can be seen in links above in description of big ticket #3 as well as commits in repo. also here: [wsgi.py](https://github.com/p2slugs/recipebox/blob/main/wsgi.py), [init.py](https://github.com/p2slugs/recipebox/blob/main/__init__.py), [views.py](https://github.com/p2slugs/recipebox/blob/main/views.py), [base.html](https://github.com/p2slugs/recipebox/blob/main/templates/base.html); Check Github Contributions above for specific changes 
3. guidance for running and reviewing code: to run and review code, you can view the running website at http://99.88.196.26/ and see the files in github


__Grades From Scrum Master__
| Team Member | Grade  | Reasoning |
| ----------- | ------ | --------- |
| Eva (SM)    |   18/20   |      I focused most of my attention on getting our website to run with the raspberry pi this week. I setup our project with the following files: wsgi.py, init.py, requirements1.txt, and edited files like about.py, views.py, and imported images. I would have liked to get the website running with the new way that Mr. M provided directions for, but after getting the virtual environment to work I ran into more problems. I still fufilled my task of getting it running but plan to do it the new way in the following week(s) by going to tutorial again. For this reason, I'm taking off 2 points.        |
| Ali         |   19/20   |     Ali got the recipe request form to store user's inputs and display what they entered. There is also a link that takes you back to the main page. It was much needed in our website. I agree with his score and give him 19/20.      |
| Sophie      |        |           |
| Linda       |   19/20   |           |

## Project Overview
A cooking website that has a database for recipes. We will use web scraping to find recipes. They will be organized into different categories, all using data. There will also be forms to add recipes, which we will use GET, POST, and SQLalchemy for. Our project purpose is to create a website using more advanced techniques than Trimester 1 and present it to the community at Night At The Museum, our teacher, and College Board. We will learn how to do more with data, Python, Flask, SQLalchemy, HTML, and CSS. In addition, we will deploy our website on Raspberry Pi so people from wide area network can all access. 

## Project Components
- home page
- recipes & ingredients page
- about us page
  - describes project overview in further detail (like a README)
  - introduce team members (goals, skills, etc.)
- navigation bar will be implemented
- recipe box / cooking tips / “like” a recipe feature?
- categories of food (16 types of food total)
  - breakfast
  - lunch
  - dinner
  - dessert
- Random Recipe Generator (API Webscraping)

## Delivery Plans & Milestones
- Fridays: asynchronous days / end of every school week
- Midterm: Jan 19-22
- N@tM: March 8-12
- College Board: May 13 (AP exam)

## Weekly Log
- Jan 6: tech talk about deployment and DevOps; 7 layers of the OSI model
- Jan 5: test prep on data and the Internet; took a quiz on the student lecture we had; missed one question about IP addresses/how the binary sysytem is related to it
- Jan 4: class discussion of 2 minute review for Thur/Fri, new year routine, and project reflections
- Dec 16: tech talks and scrum master presented an overview of project 
- Dec 14: reflected on project plan in class and started working on codes
- Dec 11: asynchronous day; each worked on individual assignment including ui mock-up, looking into CRUD, start of code, and gathering more data
- Dec 10: finalizing project plan desriptions and overviews; final updates to journals
- Dec 8/9: tech talks and practice exam corrections; no new updates on project plan
- Dec 7: updated repo name, moved Google Doc project plan to readme, organized responsibilities on scrum board
- Dec 4: filmed video, planned goals on scrum board, and created a table of collaborators
- Dec 3: created [project plan](https://docs.google.com/document/d/1j8Poc5Uar2J0xh_4jdK0nkSDv1neLWqGaCXjXDnQRRg/edit?usp=sharing) and wrote in new recipes for data collection, individual tasks were to find a breakfast recipe and put it on the [recipe doc](https://docs.google.com/document/d/14oFXFl3pcBhb3CPn6F3FZB0GHa1upJOBGRTt-Ql9KWw/edit?usp=sharing)
- Dec 2: created new organization and repo

## Goals
- get website deployed
- do more with data and allow multiple ingredients and steps to be added to one recipe
- solve intellij problems with running and commit more with intellij instead of repl to track progress
- work on ui/html
- solve webscrpaing/api

## Collaborators

| Team Member | Github Contributions  |
| ------------- |:---------------------:|
| Eva         | [Github](https://github.com/evagravin)|
| Ali         | [Github](https://github.com/Ali-Saad)|
| Sophie      | [Github](https://github.com/sophieleeajh)|
| Linda       | [Github](https://github.com/lindalonglong)|

## College Board / Teacher Requirements (Track to Meeting Them)

| Big Idea Number / Requirement           | Big Idea Summary  | Project Goal To Meet Each Requirement |
| -------------------------- |---------------------| ----------------------------------|
| Big Idea #1                | Creative Development: Collaboration, Design, Development, Function, Purpose, Resolving Errors | Working together as a team of 4 to come up with ideas and implement them. Collaboration between group and pair shares. Journals to keep track of progress. |
| Big Idea #2 and #3:        | Data, Algorithms and Programming: Using data, algorithms, and programming to create code. | Using SQLalchamey to create a database for our recipes and have the ability to add more recipes. Going beyond the Python fundamentals with logic and data. Using GET and POST, Python backend, and creating a data related UI. Having the ability to create, read, update, and delete recipes.|
| Big Idea #3:               | Algorithms and Programming: Using algos and programming to design and present to the user. | Creating a great UI desgin for our data filled website. Using HTML, CSS, and Javascript. Making a visual storyboard before putting it into our website. We will have options to go to different recipe pages and add in your own recipes. |
| Big Idea #4:               | Computing Systems and Networks: How computing systems and networks function on the internet.| Deploying our website on a Raspberry Pi server, using HTTP protocol for communication, using GET to request data, and POST to update the data. We will use an internet router. |
| Big Idea #5:               | Impact of Computing: The effects that computing can have and with our project. | Deploying our website onto the internet with a Raspberry Pi, sharing it to the community through Night At the Museum, and sharing it with College Board (AP Test). |
