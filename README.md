# Crwst project

![Crwst](readme/images/crwstmockup.jpg)

The main goal for this project was to produce a full-stack web-development site based around business logic used to control a centrally-owned dataset, to set up an authentication mechanism and provide paid access to the site's data and/or activities based on the dataset, such as the purchase of a product/service. The site has been built using HTML, CSS, JavaScript, Python, Django, MySQL and Stripe.

A live version of the site can be found [here](https://crwst.herokuapp.com)

The main aim of this site it to provide the user with an online bakery inventory of items of food that they can purchase. The products have been split into 3 categories; Bakes, Bread and Savouries. The site is flexible and further products can be added. The site owner also has the ability to add blog posts and both them and registered users can comment on these blogs to form a discussion.

**For testing purposes, please use the following credit card details:**

Note that Stripe is test stage and not activated.

`Card number:` 4242 4242 4242 4242 

`Exp:` 4242 (MM YY) 
` CSV:`  any 3 numbers, ie. 424 

**For testing purposes, please use the following superuser details:**
 
`Username:` superadmin
`Password:` ms4crwst

---

## **Contents**

* [UX](#ux)
  * [Project Aims](#project-aims)
  * [User and Site owner stories](#user-and-site-owner-stories)
  * [UX Design](#ux-design)
    * [Strategy](#strategy)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [UI](#ui)
  * [Colours](#colours)
  * [Fonts](#fonts)
  * [Wireframes](#wireframes)
* [Technologies Used](#technologies-used)
  * [Languages and Frameworks](#languages-and-frameworks)
  * [Tools](#tools)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features to implement](#features-to-implement)
* [Database Design](#database-design)
* [Testing and Debugging](#testing-and-debugging)
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
  * [User Testing](#user-testing)
* [Deployment](#deployment)
  * [Hosting](#hosting)
  * [AWS](#aws)
  * [Local Hosting](#local-hosting)
* [Credits](#credits)
  * [Code](#code)
  * [Images](#images)

---

## UX

### Project Aims 

This is a full-stack site for fictional company Crwst which is a local bakery that has entered into ecommerce following an online commerce surge with the COVID-19 pandemic. ‘Crwst’ is a Welsh translation of ‘pastry’.

The aim of this site is to offer the inventory of a bakery so that users can browse and securely purchase goods online. Users are able to view all products on one page, sort by 3 different categories; bakes, bread, savouries, as well as sort their search by price, alphabetically and categorically alphabetically. Each product has a link to it’s own product page where a user can see a description, toggle the quantity they want and add the item(s) to their basket. Users can see what is in their shopping cart at anytime in the top right corner and can securely checkout using Stripe. Each interaction has a pop up toast for feedback. Site owners can add, edit and delete products as well as add, edit and delete blog posts. Registered users also have the ability to comment on blogs. Unregistered users will be promoted with a redirect link to sign up. 

Value provided:

Users/Shoppers make use of the site by being able to order products that would be delivered to them. 

Site owners are able to increase their market exposure and customer base by gaining an online presence and offering. This should increase their revenue. 

Research from [Bakery Info](https://bakeryinfo.co.uk/bakery-market-report/bakery-market-report-2021-reveals-impact-of-covid/655314.article) and  [Simply Business]( https://simplybusiness.co.uk/knowledge/articles/2019/09/great-british-bake-off-uk-independent-bakeries-rise/) shows that since 2018, independent bakery businesses have increased in number by 48%. This means it is imperative that local bakery businesses have at least an online presence and where possible an online store to ensure they can compete for their market share. COVID-19 has resulted in the close of many businesses, including hospitality where baked goods are often sold, so an online presence is more important than ever. Food to go was slightly insulated due to its very nature of being low contact and transactional however, it is predicted that following the pandemic there will be a rise in eating out, therefore online shops must optimise their potential to maximise sales. 

### User and Site Owner Stories

![User and Site Owner Stories](readme/images/userstories/userstories.jpg)

[Back to Contents](#contents)

### UX Design

### Strategy 

To start I created a competitive benchmark to compare other bakeries that had an online presence and store to help determine what is this companies USP. What can it do that helps it stand out and increase customers. I have compared multiple bakery websites, including those that do and don’t have an online purchase ability, to determine how their sites are structured, how they separate their products into categories, how they structure their navigation, UI styles and what information they provide to users about products and their profiles and orders. 

* https://www.fabulouswelshcakes.co.uk/ 

Fabulous Welsh Cakes is a Welsh bakery with an online presence and store. They sell different flavoured Welsh-cakes and giftsets and offer bespoke services such as Wedding favours and corporate gifts. They have a clear shop page and include a page in their navigation that shows the different locations where shoppers can purchase in store if they wish. They don’t offer product sorting but have two categories; welsh-cakes and gifts. They have a subtle UI in terms of earthly colours and light delicate font and have gentle interactive actions where on hover the images flip. Their shop link is second in the navigation following the Home which shows its important and clear for the user to find.

* https://www.parsonsbakery.co.uk/  

South West and Wales bakery chain Parsons have a bold and engaging website, with a hero image and lots of visually interesting content. There is no online store however the site is very informative about the brand and includes location information for shoppers. They have a page where you can find locations of their sites. 

* https://hard-lines.co.uk/

Hardlines is a South Wales café that has an online presence and online store. Their UI and graphics are very contemporary and the tone of voice is aimed at young professionals. They have a full products page, individual pages for products with clear pricing, drop down options for quantity and weights. These are coloured and sized appropriately for contrast and hierarchy. However, they do not have a search function on their site which closes off many potential user stories. They have a log in and order history capability too. The sort, search and simplicity of their categories work really well and is something I have taken into this project. 

* https://friends-in-knead.myshopify.com/ 

Friends In Knead are a bakery with a physical store, a online presence and online store. Their site has soft and welcoming UI. When a shopper selects the Shop in navigation they are taken to a page of categories and when selected they are shown the products, I think it would be better UX to be first taken to a full page of products then decide on how to sort. This would assist the site owner in that a user is exposed to more products and may be tempted to purchase more. Each product has its own page with a price and Add to Cart button, however there is no quantity option. Once added to cart, you are immediately taken to your bag, which is not great user experience – a toast with a link would have been a better experience so that the shopper can continue to shop if they wish. They have customer favourites on the homepage, however there are 20 products which is too much choice for a new user.

From this brand comparison and market research key tasks/cases for the site are as below in this strategy trade off: 

|   | Features | Importance | Viability |
| :-: | --------------------------------- |:-------------:| :--------:|
| A | Search function for products by keyword or ingredient | 5 | 5 |
| B | View full product inventory | 5 | 5 |
| C | View individual product details on own page | 5 | 5 |
| D | Information about the brand | 4 | 5 |
| E | Secure user registration and log in and out functionality | 5 | 4 |
| F | User profile with ability to see order history | 5 | 4 |
| G | Securely checkout | 5 | 4 |
| H | Search result product sorting | 4 | 3 |
| I | Find a wholesaler/locations | 2 | 3 |
| J | User ability to save and/or like products in a wishlist | 2 | 3 |
| K | Link to email marketing subscriptions | 2 | 3 |
| L | Contact form | 2 | 3 |
| M | Visible special offers | 5 | 5 |
| N | Provide birthday discounts to registered users | 1 | 2 |
| O | Provide a blog page and view individual blogs | 4 | 5 |
| P | Allow registered users to comment on blogs | 3 | 5 |
|   |  *Total* |  59  | 62  | 

As the importance is higher than the viability this is going to work. The features that are that are the most important and achievable are: 


| A | Search function for products by keyword or ingredient 

| B | View full product inventory 

| C | View individual product details on own page

| D | Information about the brand

| E | Secure user registration and log in and out functionality

| F | User profile with ability to see order history

| G | Securely checkout 

| H | Search result product sorting 

| M | Visible special offers 

| O | Provide a blog page and view individual blogs 

| P | Allow registered users to comment on blogs 

The other features can be released in future updates. 

The user will expect to be able to intuitively find products, update their cart and securely checkout. They may want to read blog posts on recipes, local information and ingredients etc. 

Therefore the navigation should be intuitive and simple. Global navigation will be used for conventionality. Key call to actions will have obvious UI styling with secondary actions have more subtle. For example, ‘Add to Cart’ will be a dark button, whereas ‘Keep Shopping’ will be an outline.  

A special offers banner will appear in the base template and therefore be on every page enticing the user to buy. 

From the menu the user can find products and sort them by category, price, and alphabetically. 

A search bar will be on the base template and as such every page so a user can quickly search for a product at any point. This searches the titles of products and their descriptions to widen the search. 

The blog posts will help the brand appear trustworthy and interest local shoppers. Registered users will be able to comment on blogs. The idea being that users viewing the blog will be able to partake in discussions.  Site owners will be able to add, edit and delete blogs. Users can also search for a blog, by title or description in its own search (separate to products).

Users will be able to securely register and login. The site owner/superuser can add/edit/delete products and blogs.

Stripe is used so users can securely checkout. 

### Scope 

Based on the strategy plane, the key features that are the most important for users and the most achievable are providing information about the brand and the service, a search function that allows a user to find specific products by title or in description. The results are shown on cards that give key information about the product; a clear image, price, category, which the user can then click into to view an individual product page. Users can securely register and log in, they also have a profile page where they can update their default shipping details and view their previous order history. Users can search for and read blogs and registered users can comment on them and form a dialogue. Security has been added so non registered users can add blogs and products and only registered users can checkout. 

The site needs to appear trustworthy and intuitive. It wants to be as helpful and knowledgeable as it can to users by enticing new users, being easy to use for return users so that the number of recipes increases. The company requires a website that expresses its professionality, reliability and trustworthy. 

The website must be a clear showcase of the brand. It should have contemporary features and aesthetic that appeals to potential customers. 

### Structure 

Of the key elements that were determined important, they should be put in this logical order on the site: 

* Search function for products
* Clear link to shop in menu and view all products
* Clear sort and category options in shop menu
* View of shopping cart with ability to update quantities, see total and delivery charge
* Ability to register/log in 
* Profile with default details and order history
* Information about the brand’s service
* Site owner ability to add, edit and delete products and blogs 
* Blog posts and comment ability 

The Home page will be the landing page with search function, menu and a clear call to action to all products. This will include a top navigation (base template) which will have links to an account (the options depending on whether a user is logged in or needs to register), the shopping cart, shop about and blogs. 

The Shop link will have a dropdown sub menu that allows a user to view all products, products by category, by price or alphabetically. 

On the products page, a count will show the number of results, and if the result of a search, the number of search results. Following convention, there will be sort options to the top right of the product cards. 

Each product detail page will have a large image, 50%, and info about the product including name, price, description and a clear add to cart button. If the super user is logged in they will see edit and delete links allowing them to edit the product details or delete it. 

From the Structure plane, the about information will be in text and a brief explanation of the company’s mission with a friendly image. This will also include opening hours and days of delivery. 

Buttons and links change visual style on hover, so that a user knows it is actionable.

External links will open in a new tab so the user does not navigate away from the site.

The blog page has a search function will all blogs underneath, the same visual styling as products page. The site owner/superuser can edit/delete blogs from here via links on each blog card. 

### Skeleton

Figma has been used to design the wireframes, with the designs in the below [wireframes](#wireframes) section. 

Each template with derive from the base template providing visual and navigational consistency. 

The user actions will each have the same visual style for consistency. They will have the same colour theme, the same typography, and a similar percentage of content and whitespace, padding and margins. Components will have enough space around them to breath and remain digestible for users. 

It will be designed responsibly, mobile first, so that these components are visually consistent across devices but suitable for that screen. 

The final design is an iteration from the original wireframes. 

### Surface 

A white background and grey text palette has been deliberately used so the products have sufficient white space around them. Text, links, and navigation have consistent colours, change on hover and the typography is too. 

Design decisions are discussed further below in the [UI](#ui) section. 

Sources of design research came from Dribble, Pinterest and UXPlanet as well as competitor brands. 

[Back to Contents](#contents)

--- 

## UI 

### Colours

A minimal colour scheme has been purposefully chosen against lots of white space so that the product images stand out and that the site has sufficient contrast to be accessible.

Grey text is used for contrast and accessibility against white turning black on hover. This is alternated on primary buttons which are dark grey with white text.

The checkout has its own css file, and form colour scheme with a blue loading overlay. The colour blue is known for its psychological associations with trust so adds feelings of security here. This is also the case for links in the authentication app.

Bootstrap’s danger, warning, info and success colours have been used. 

![Colour scheme](readme/images/colours.png)

### Fonts

I have used Roboto Mono from Google Fonts, with back up Monospace. It is an old-fashioned text that has come to be contemporary and used in small business branding to give it’s design a minimal aesthetic. The font family was imported in to the main base.css file.

### Wireframes

The site is fully responsive as more than 70% of users initial browse and search and purchase goods on the internet via mobile phones. 

Initial wireframes for the site can be found by clicking on the links below:

Desktop
![Desktop Wireframes](readme/images/crwstdesktop.png)

Tablet
![Tablet Wireframes](readme/images/crwsttablet.png)

Mobile
![Phone Wireframes](readme/images/crwstphone.png)

[Back to Contents](#contents)

---

## Technologies used

### Languages and Frameworks

* HTML 
* CSS
* JavaScript
* jQuery
* Python
* Django
* Font-Awesome 
* Google fonts
* Heroku 
* Bootstrap 
* Stripe 
* Code for icon class from Bulma (noted in [credits](#credits))

### Tools

* Git
* Gitpod
* Figma
* Google Fonts
* W3C Validator - used to test my HTML to ensure there were no errors.
* W3C Validator CSS - used to test my CSS to ensure there were no errors.
* JSHint - used to test my JS to ensure there were no errors.
* PEP8 Online - used to check my Python was PEP8 compliant.
* Chrome Dev Tools (including LightHouse)
* AWS and S3 for static files and media storage

[Back to Contents](#contents)

---

## Features

### Existing features 

* Base template / All pages

The base template includes a top navigation that is responsive (main-nav and mobile-top-header templates in includes) for all devices. As the base, this is on every screen. It includes a link to Home, Shop (with a dropdown menu), About and Blog, as well as the users account/login ability and their cart. 

A search function is there to allow the user to easily search for a product on any page, this is good UX and can only help increase sales for the Site owner. 

Under the menu is a banner for special offers. It enlarges when the user hovers over it and links to the products page on click for enhanced UX. 

There is also a footer with contact details. 

* Home 

This has a large image to cover the page for visual interest, with a bold call to action to link to the products page.

* About  

This has a friendly image and a description about the business. It also includes a location link so shoppers can visit as well as opening and collection open hours. 

* All Products

This shows all of the products available with full search and sort functionality. Users can sort by category, price and alphabetically (all both ascending and descending). The page also shows how many search results there are and what the search term was. 

Only SuperUsers can see edit and delete links under product details. 

A JavaScript function makes the image scale up on hover enticing them to click and enhance the UX.

* Product Detail
This page shows the product image, the price, a description, quantity toggle, back to products button and an add to cart button. 

JavaScript restricts the user from adjusting the quantity between 0 and 99, this number can be changed as per the business’s wishes. 

On adding the item to cart, a success message (toast) appears. 

Only SuperUsers can see edit and delete links under product details.

* Bag 

The bag shows the items in the shoppers cart with the ability to adjust the quantities and/or remove the item. They can see the subtotal and delivery. There is a large Secure Checkout button. 

* Checkout

Once clicked secure checkout registered users will be taken to the checkout page. Only registered users will be allowed to get to this, otherwise they will be redirected to signup/log in. 

This includes a form for delivery details, which if signed in and saved in their profile, will appear pre-populated. It also includes an order summary with total and delivery charges. 

There is a clear warning that shows how much their card is about to be charged. 

If the shopper provides invalid card or shipping details they are provided feedback.

* Order confirmation

Providing a successful order completes the shopper will be taken to this page and sent an email confirmation. This shows the full summary of their order. 

The checkout success view is defensively programmed so that only the creator of the order or a superuser can see this. It is so the url cannot be bypassed.

* Profile 

A user can navigate to their profile from the Account link on the main menu. They are shown their default details (if saved) via a form. Alternatively, they can come to this page and add/override their default details. 

The Order history is shown, with links that take them from that order information to their original order confirmation/thank you page.

It has been defensivly built so that only the creator of the order and the superuser can view an order for security reasons.

If a user has not made any orders, a message will be displayed stating the fact so that this portion of the page is not blank. It also enhances the user experience and may entice them to browse products and make a purchase.

* All Blogs
From the main navigation a user can navigate to the business’s blog page. There is a search function that a user can search for keywords which will bring results up if that is in the title or blog text. 

Like the products page, the user can see the total number of blogs and if searched the number of results for that keyword.

Superusers can see edit/delete buttons. 

* Blog detail

A blog detail shows the blog title, blog text and published comments. Only registered users will be able to publish a comment, otherwise they are suggested to sign up. 

Blog posts include a comment section where authorised users can post comments.  This has a maximum character length of 3000. Comments are typcially between 60-5000 so this suits. 

Superusers can see edit/delete buttons. 

* Add product/blog

Only superusers are authorised to add a product or a blog. This is a simple form and can be navigated to from the Account option on the main menu. When added a user is redirected to the blog/product.

* Edit product/blog

Only superusers are authorised to edit a product or a blog. This is a simple form and can be navigated to from the Account option on the main menu. When edited a user is redirected to the blog/product.

* Toasts

Success, information, warning and error messages are built into this project so that users receive relevant feedback to their actions. These appear in the top right. 

* 404/403/500 Error pages

The site has been made with 404/403/500 custom error pages. Currently the site is desinged to redirect an unauthorised user to a sign in page rather than a 403 page, however this functions for other security breaches or can be utilised in a future release. The 404 page is displayed when content is no longer available, for example a product or blog that does not exist. 

These are linked to messages, so an error toast message will show what the issue is. For example 'No Product matches the given query" notifying the user of the problem.

### Features to implement 

There are many features that I would like to implement in future releases: 

* Have the ability to add images on blogs. This would add visual interest and give a better UI to this page.
* Blog result sortability - it would enchange the UX to be able to sort blogs once there are many of them
* A review model on products – it would be great UX if users can review products which that show an accurate total rating on products calculated by real customer reviews
* Email subscription ability (for a real business that wanted to send email notifications)
* Locations page – a page that showed the location of stockists for those that may not want to purchase online, or live near the bakery
* A text input field on cart page so that any dietary requirements could be noted – would need a logically caveat for the business but it’s a potential feature
* Adding further categories such as Vegetarian or Vegan would be important for users
* Allow Super User to add categories (this would require further development to ensure menu links were added to)
* Add more accurate redirects links as they are not always linked for best UX – eg signing in to comment on a blog redirects to homepage 
* Have the number of items in the cart appear in the cart icon as well as the total, as per ecommerce convention 
* Allow shoppers to sign in and register their accounts with their social media accounts

[Back to Contents](#contents)

---

## Database Design

Through the development of the project, SQLite3 was used as this is the default database included with Django. Note, on deployment, you are given the option to utilise PostgreSQL as this is included with Heroku.
Django Allauth, specifically django.contrib.auth.models provided the User model that is used in the Profile App.

There is a Bag App and a Home App however neither currently have the need for models.

* Checkout App; Order Model, Orderline Model
* Products App; Product Model, Category Model
* Profiles App; User Profile Model
* Blog App; Blog Model, Comments Model 

A note on the blog app: Currently there is no maximum length for comments here, but it has been input in the html textarea as a class. Ideally it should be here in the database design and should be included in the future. 

![Data Schema](readme/images/dataschema.png)

[Back to Contents](#contents)

---

## Testing and Debugging  

Testing of the site can be found by clicking [here](https://github.com/sophnagle/crwst/blob/master/README.md#testing-and-debugging))

[Back to Contents](#contents)

---

## Deployment

The site is hosted on [Heroku](www.heroku.com).

The site was deployed using the following steps:

* Create a new repository within GitHub.
* Open repository in gitpod by cloning the repo from GitHub. Developed project
* Create a requirements.txt file by typing pip3 freeze > requirements.txt in the terminal 
* Log in to Heroku and selected "Create New App".
* Select the input field "App Name" and gave app a unique name with hyphens instead of spaces.
* Select the region closest to my location
* Select "Create App".
* Click "Resources" and typed in Postgres in the Add-ons search bar.
* Click "Resources" and typed in Postgres in the Add-ons search bar.
* Select Heroku Postgres and provisioned a free Hobby Dev database.
* Retrieve the Database URL from the hidden Config Vars in "Settings" in Heroku.
* Input the Database URL in the database path in settings.py and removed the local settings.
* Created a Procfile and added web: web: gunicorn crwst.wsgi:application to the file.
* Checked the Procfile to make sure there is no extra line after the first line as this can cause problems in Heroku
* Push the requirements.txt and Procfile to GitHub.
* Run migrations to build the database in Postgres.
* Make sure settings.py file is connected to the mysql database
* In the terminal use the command to backup your current database and load it into a db.json file:./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json 
* Create a superuser with python manage.py createsuperuser and followed the instructions in the terminal.
* Remove the Postgres Database URL so it doesn't end up in version control.
* Type heroku config:set DISABLE_COLLECTSTATIC=1 in the terminal to stop Heroku collecting the static files.
* Then use this command to load your data from the db.json file into postgres:
./manage.py loaddata db.json
* Push all changes to GitHub.
* Typed git push heroku master to push everything to Heroku.
* Select "Deploy" from the Heroku App menu.
* Select "GitHub" from the "Deployment Method" section of the page.
* Ensure my GitHub account is shown in the "Connect to GitHub" section and insert my GitHub repo name in the input field and click "Search".
* Once Heroku had the repo, click "Connect" to complete the link.
* Within ‘Settings’ in the Heroku app, select ‘Reveal Config Vars’ and input the relevant key information in as below: 

| Config Var                  | Key                   |
| ------------------------------ | ----------------------- | 
| AWS_SECRET_KEY_ID |Received when setting up AWS             | 
| AWS_SECRET_ACCESS_KEY |Received when setting up AWS      |
 | DATABASE_URL | This is created when you provisioned Postgres  | 
| EMAIL_HOST_PASS | This is obtained from your email provider    | 
| EMAIL_HOST_USER | Email address                      | 
| SECRET_KEY | This can be randomly generated with a [generator](https://django-secret-key-generator.netlify.app/) | 
| STRIPE_PUBIC_KEY |Found in Stripe dashboard    | 
| STRIPE_SECRET_KEY |Found in Stripe dashboard      |
| STRIPE_WH_SECRET |Obtained from Stripe webhook creation   |
| USW_AWS | True   |

* Select "Deploy" from the Heroku App menu.
* Scroll down the page and selected "Enable Automatic Deployment". This will mean all pushes will automatically update in Heroku
* Select Master Branch under "Branch Selected".
* Click "Deploy Branch"
* Once site was deployed, select ‘Open App’ to launch the site and be able to view and test it within the browser.

### AWS

In order for the static CSS, JS and media files to be stored and useable with Heroku, you need to set up an AWS account like this project.

* Go to [AWS]( https://aws.amazon.com/) and either log in or create an account.
* Search for S3.
* Create a new bucket and ensure that the Block All Public Access tickbox is not checked and click on 'Create Bucket`.
* Click on the Properties tab and enable Static Website Hosting. This will allow AWS to host our static files.
* Input index.html and error.html in the appropriate fields and hit save.
* Click on the Properties tab and click CORS configuration and add the below before hitting save:

        [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
        ]

* Click the Policy Tab and select Policy Generator which creates a security policy for the bucket.
* The policy type is ‘S3 Bucket Policy’ and the Action will be get object.
* Copy the ARN (Amazon Resource Name) from the bucket and paste it in the ARN field. (Make sure to include the starting arn letters)
* Click Add Statement and then Generate Policy and copy and paste the generated policy in to the Bucket Policy Editor.
* Add /* at the end of the resource key as this will allow access to all resources in the bucket.
* Select Save.
* Click the Access Control tab and set the list object permission to everyone under the Public Access section.
* Search for and open ‘IAM’ from the service menu.
* Create a group for your user to belong to.
* Create an access policy for you the group which gives access to the S3 bucket.
* Click the JSON tab and select import managed policy, search for S3 and select S3 Full Access Policy.
* Create a user, give them programmatic access and attach it to the group.
* Download the CSV file that is generated as this contains the keys required to use AWS. It is important that you do this.
* Back in your workspace, install boto3 and django-storages using pip3 install.
* Add the keys to the Config Vars in Django (found in the CSV)
* Create a custom_storage file in your workspace
* Finally, run python manage.py collectstatic and transfers the static info to AWS.

### Local Hosting you wish to clone a copy 

If of my project you will need to:
* Navigate to my GitHub repository.
* Click the ‘code’ button next to the Green Gitpod button.
* Either, download the zip file or clone the repo using ‘gh repo clone’ in the terminal.
* Install the modules listed in the requirements.txt file using python -m pip -r requirements.txt in the terminal.
* Install the JSON files using python manage.py loaddata 
* Create a SuperUser by using python manage.py createsuperuser in the terminal and following the onscreen instructions.
* Run migrations to create your database by using ‘python manage.py migrate’ in the terminal
* Create an env.py file in your application folder and add the following:

        import os

        os.environ["SECRET_KEY"] = "ADD YOUR SECRET KEY HERE"

        os.environ["STRIPE_PUBLIC_KEY"] = "ADD YOUR STRIPE PUBLIC KEY HERE"

        os.environ["STRIPE_SECRET_KEY"] = "ADD YOUR STRIPE SECRET KEY HERE"

        os.environ["STRIPE_WH_SECRET"] = "ADD YOUR STRIPE WEBHOOK SECRET HERE"

        os.environ["EMAIL_HOST_PASS"] = "ADD YOUR EMAIL HOST PASSWORD HERE"

        os.environ["EMAIL_HOST_USER"] = "ADD YOUR EMAIL HOST USERNAME HERE"

* The app can now be run locally by typing python manage.py in the terminal and opening the browser prompt.

[Back to Contents](#contents)

---

## Credits

### Code

[Blog App](https://www.askpython.com/django/django-blog-app)

Much of the base code for the Blog app and Blog and Comment model was taken from this suggestion and adjusted accordingly, the ID removed as Django automatically adds it, and authorisation so only a super user can create a blog and only logged in authorised users can comment. 

[Zoom in Transition](https://stackoverflow.com/questions/33811041/javascript-zoom-in-on-mouseover-without-jquery-or-plugins)

Research on Stackoverflow was used in making the Javascript and CSS code to add animations to the product images when a user hovers over them. This was also used to add a size change animation when the user hovers over the Special offers banner on the base template.    

[Icon Bulma](https://bulma.io/documentation/elements/icon/)

    .icon {
        align-items: center;
        display: inline-flex;
        justify-content: center;
        height: 1.5rem;
        width: 0.75rem;
    }

This code was taken from Bulma to ensure the icons are consistent throughout.

### Images

As this is a fictional site, the images were taken from [Unsplash](https://unsplash.com/), a source of free imagery.

[Chocolate Welshcake](https://www.chocolatier.co.uk/chocolate-fudge-welsh-cakes-recipe/)

[Raspberry and white choc](https://sophiaskitchen.blog/cookies-and-biscuits/welsh-cakes-thermomix-recipe/ )

[Caramel twist](https://unsplash.com/photos/pEh8PyE1UPc)

[Macaroons](https://unsplash.com/photos/q9Vt4pVnGzc)

[Oat cookies](https://unsplash.com/photos/b2AUNwhWryQ)

[Lemon meringue pie](https://unsplash.com/photos/ImhVA1_xOjY )

[Raspberry tart](https://unsplash.com/photos/88sNfcLB_KM)

[Pretzel](https://friends-in-knead.myshopify.com/collections/signature-bakes/products/chocolate-chip-pretzel-cookie)

[Classic welshcake](https://www.peta.org.uk/recipes/gaz-oakleys-welsh-cakes/)

[Olive Bread](https://unsplash.com/photos/ubChh7P4lQo)

[Tomato Foccchia]( https://unsplash.com/photos/ubkpJUe0I5s)

[Wholemeal Bread](https://unsplash.com/photos/rsWZ-P9FbQ4)

[Sausage Roll](https://unsplash.com/photos/wG6qdXkULhI)

[Seeded Bread](https://unsplash.com/photos/qDpKehCEs1Y) 

[Quiche](https://unsplash.com/photos/sOLzB42PKvo)

[Beef Pie](https://pieminister.co.uk/introducing-kevin/)

[Chicken Pie](https://www.tasteandtellblog.com/saturdays-with-rachael-ray-muffin-tin-pot-pies/)

[Pretzel Bread](https://unsplash.com/photos/1GeTpL5FJvY¬)

[Home page cake](https://unsplash.com/photos/D3_u5E6E2Hg)

[Crwst Team About](https://unsplash.com/photos/pMsvOrnIF3Y)

[Back to Contents](#contents)
