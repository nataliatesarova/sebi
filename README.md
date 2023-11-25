# Recipe

## Description

HomeChef, a web platform crafted with Django using Python, JavaScript, CSS/Bootstrap, and HTML, is a celebration of heart warming home-cooked meals.
Tailored for home cooks around the globe, this website provides a virtual haven for users passionate about sharing their culinary creations. Whether you're a seasoned home chef or an enthusiastic cook, HomeChef empowers you to create and share your favorite home-cooked recipes.
HomeChef  was created as the fourth project for the Code Institute Diploma in Software Development. The site features include user authentication and full CRUD functionality.
Users are given the ability to elevate their dishes with appealing photos, share their cooking through visual elements, and gives the option to like and comment on the recipes.
Link to the live site - [HomeChef](https://recipeblog-e0d016298fa8.herokuapp.com/)

## Design

### Wireframe mock-ups

[Balsamiq](https://balsamiq.com/) was used to design the wireframes for my website.
![Home Page Wireframe](assets/balsamiq/balsamiq1.png)
![Recipe Page when login Wireframe](assets/balsamiq/balsamiqlogin.png)
![Recipe Page Wireframe not login](assets/balsamiq/balsamiqnotlogin.png)
![Register Wireframe](assets/balsamiq/balsamiqregister.png)
![Login Wireframe](assets/balsamiq/loginbalsamiq.png)
![Add new recipe Wireframe](assets/balsamiq/addnewrecipebalsamiq.png)
![MyProfile Wireframe](assets/balsamiq/myprofilebalsamiq.png)

### Database Schema
![Database Schema Diagram](assets/databaseschema.png)
The database schemas were designed using [Lucid App](https://lucid.app/) These schemas were pivotal in planning the database models and defining their respective fields. They also facilitated visualizing the relationships between the models and their interactions. Recipe comprises four models: Recipe, Profile, User and Comment.

## Agile Development

The project applied Agile Methodology on GitHub for planning and execution. User Stories were established as GitHub issues, outlining their purposes distinctly. Each story contained specific acceptance criteria and tasks, categorized using colored labels such as 'must-have', 'should-have', 'could-have', or 'won't-have' to manage tasks during iterations.

Additionally, 4 Epics were initiated and expanded into 20 User Stories. Each of these stories was also assigned story points based on their complexity.

## Epics and user stories

The following user stories (by epic) were completed. The MoSCoW prioritization was used to categorize the EPIC and user story tasks into Must Have, Should Have, Could Have, and Won't Have. Must Haves are critical, Should Haves are important, Could Haves are desirable, and Won't Haves are excluded for now. It helps focus on crucial tasks first, ensuring project success while allowing flexibility for less critical items.

### User Authentication and Profiles [#1] (https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39537085)

### Recipe management [#2] (https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39569106)

### Interaction with recipes [#3] (https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39571127)

### Admin panel and content management [#4] (https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39536019)

### User Authentication and Profiles
As a new user I can complete a registration form with fields for username, name, email and password so that I can access the site to post recipes, comments and likes.`(MUST HAVE)`

As a registered user I can securely log in using my email and password so that I can access and use the site. `(MUST HAVE)`

As a registered user I can access my profile page for viewing and editing so that I can personalize my profile information.`(COULD HAVE)`

### Recipe management
As a registered user I can create new recipes by providing a title, a list of ingredients, description, detailed method, and images so that I can actively participate in a cooking and recipe-sharing community, access a convenient personal recipe archive, express my culinary creativity and receive feedback and engagement from others.`(MUST HAVE)`

As a logged-in user I can edit any recipe that I've created including modifying the title, ingredients, description, method, and associated images so that I can maintain and improve the recipes, resulting in better cooking outcomes and increased engagement with the platform.`(MUST HAVE)`

As a logged-in user I can delete recipes I've created when necessary so that I can manage the recipe content effectively, ensuring that my profile reflects my best and most relevant culinary creations.`(MUST HAVE)`

As any user I can browse recipes available on the site whether logged in or not so that all can explore, discover, and engage with a variety of recipes, providing inspiration and a sense of community around cooking.`(MUST HAVE)`

As any user I can click on a recipe to access its complete details, which encompass information about ingredients, description, cooking instructions, images, comments, and likes so that i can access detailed recipe information. `(MUST HAVE)`

As a user I can view a maximum of 9 recipes per page and have the ability to navigate between pages so that I can conveniently browse recipes.`(SHOULD HAVE)`

### Interaction with recipes
As a logged-in user I can like a recipe and see number of likes so that I can personalize my recipe collection, engage with others, discover popular dishes, and enhance the overall experience on the platform by expressing preferences and interests in cooking.`(SHOULD HAVE)`

As a registered user I can post comments on recipes so that i can actively participate in the culinary community, share expertise and improve recipes.`(SHOULD HAVE)`

### Admin panel and content management
As a superuser (admin) I can securely log in to the admin panel using my admin credentials so that site administration can be performed. `(MUST HAVE)`

As a superuser I can access a list of all users so that it is possible to manage users. `(MUST HAVE)`

As a superuser I can edit and delete user accounts as needed so that I can prevent misuse and inappropriate content on the site. `(MUST HAVE)`

As a superuser I can edit or delete any recipe on the site, regardless of the user who posted it so that the site can be appropriately managed.`(MUST HAVE)`

As a superuser I can review, approve and moderate comments across the entire site so that i can block, edit and delete inappropriate comments so that I can properly moderate the site. `(SHOULD HAVE)`

As a superuser I can view the likes for recipes so that I can track trends and most popular recipes. `(SHOULD HAVE)` 

























## Future features
Allow the user to save a draft version of a recipe to edit and complete at a later time.
Bio to be available for all registered users to view
Recipe Search and Filters: Allow users to search for recipes using keywords, ingredients, cuisine, and dietary preferences (e.g. gluten free, vegan)
Recipe Categories: Categorize recipes into sections such as breakfast, lunch, dinner, desserts.
Add difficulty level, serving size, nutritional and calorific information.
Newsletter Subscription: Provide a subscription option for users to receive regular updates on new recipes, cooking tips, and the latest blog updates.
Enable sharing of recipes directly via social media.

## Features
### Navigation bar
The Navigation Bar is prominently positioned at the top of the page, with the navigation links aligned to the left side. When a user is logged in, certain links undergo changes; for instance, the Login transforms into Logout, "Register" link changes to "Add New Recipe," and a "MyProfile" link is added. For smaller screen sizes, a hamburger menu is utilized to display the navigation links.

### Homepage
The homepage is accessible to all users, even without registration or logging in. It features recipe cards displaying a featured image, recipe title, author, and creation date. A "View More Details" button, allows all users to explore the recipes. The home and subsequent pages have the capacity to display a maximum of 9 cards.

### Recipe details
Registered and logged in users are able to view, edit, comment and like recipes. Users not registered or logged in will only be able to view recipe details, without the ability to edit, comment or like.

### Registered login
During registration the user must complete all the required fields: username, first name, last name, email, password, and password confirmation. Login requires the entering of both the email and password fields. After logging in the user will be redirected to the main page with recipes.

### Add new recipe
The registered and logged in user will have the option to add a recipe by clicking on the ‘Add new recipe’ option on the navigation bar. The user must enter the fields for Title, Description, Ingredients and Method. If the user does not enter all off these fields and click the submission ‘Create Recipe’ button a ‘Please fill in this field’ prompt will appear. Submitting an image is optional. If no image is submitted a default tomato image will be displayed. The user can designate the recipe post as draft or published and the click the ‘Create Recipe’ button, which will return the user to the homepage with the appearance of a ‘Recipe created successfully’ notice. Draft posts allows the admin to plan publication date and help with editing before publication. If the user designates the recipe as published, admin must first approve it before the recipe appears to the public. The user can delete or edit their own recipe. If the delete button is clicked the user is prompted with the conirmation message 'Are you sure you want to delete this recipe?' and given option to proceed with deletion or cancel. If 'cancel' is selected the user is returned to the recipe edit page. If deletion is selected the user is returned to the homepage and presented with mesage 'Recipe name of recipe was deleted successfully'.

### User profile
When the user logs in the 'My Profile' tab appears in the Navbar. On clicking 'My Profile' the profile detail page opens where the profile pic, name, username,user bio and user history can be viewed. User history shows when the profile was created and last edited.

The profile can be edited with clicking of the action edit icon. It is not mandatory to fill in any fields on the profile, and if no profile pic is uploaded a default smiley face is displayed. The profile pic is displayed when a user published a comment.

### Log out
On clicking 'Log Out' the user is redirected to the homepage where the recipes can be viewed, and with option to register and login.

### Log in
On logging in the user is given the message 'Welcome, you are now logged in'


### Comment on recipes
On posting a comment the logged in user is presented with the message 'Your comment has been created successfully. It will be visible once the admin approves.'

Once the comment has been checked and approved by the admin it will be visible.




