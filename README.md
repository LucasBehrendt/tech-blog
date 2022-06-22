# Tech Blog

Tech Blog is an open community-driven site for everyone, whether you're a tech geek that can't get enough of the newest and hottest gadgets on the market, or just looking for some tips on your next purchase. By signin up, users can share their thoughts and interact with other members by commenting on and liking posts.

The main objective of this project is to demonstrate a robust Full Stack application with strong competency in both front-end and back-end development, using the Django framework.

[Find the live website here!](https://tech-blog-pp4.herokuapp.com/)

![Responsive Image](static/images/readme-images/responsive-img.png)

# Table of Contents

## User Experience (UX)
### User Stories

The following user stories were used in an agile approach when creating the application, implemented in order of importance. 

- #### Site Admin

  - As a Site Admin I can manage the post content on the blog so that I can make sure no objectionable posts are present.

  - As a Site Admin I can manage the comments on the blog posts so that I can make sure no objectionable comments are present.

- #### User Registration

  - As a Site User I can register an account so that I can make posts and comments.

  - As a Site User I can update my information so that I can personalize my profile.

  - As a Site User I can delete my profile so that there is no stored info on me.

- #### User Navigation

  - As a Site User I can view a paginated list of posts so that I can easily select a post to view.

  - As a Site User I can click on a post so that I can read the full text.

  - As a Site User I can view how many likes a post have so that I can see which posts are popular.

  - As a Site User I can view comments on a post so that I can read what other users think.

  - As a Site User I can view a list of my own posts so that I can see my content and have easy access to it.

- #### User Interaction

  - As a Site User I can like / unlike a post so that I can interact with the content and show appreciation.

  - As a Site User I can create posts so that I can provide content to the community.

  - As a Site User I can edit or delete my own posts so that I can control my own content.

  - As a Site User I can leave comments on a post so that I can join in the conversation.

  - As a Site User I can delete my own comments so that I can control my own content.

### Structure

The site is structured with simplicity and accessibility in mind, to help users intuitively navigate the site. The landing page gives the user relevant information about each post without cluttering the feed. A simple, fully responsive navigation helps keep the flow of the site balanced when navigating and interacting with the application. All pages are carefully structured to be consistent and pleasing to browse. All user interactions, such as registering an account or creating a post have logical responses and provide relevant feedback.

To help facilitate a logical flow of the application during the development process, a simple flowchart was created using [Lucidchart](https://www.lucidchart.com/pages/).

<details>

<summary>Flowchart</summary>

![Flowchart](static/images/readme-images/flowchart.png)

</details>

### Data Model

The database used for the application requires a Post and Comment model. The user authentication system is included in the Django framework and a User model was therefore already provided. To get an idea of the relationships and fields required in the models, an ERD (Entity Relationship Diagram) was created using [Lucidchart](https://www.lucidchart.com/pages/).

<details>

<summary>Entity Relationship Diagram</summary>

![Entity relationship diagram](static/images/readme-images/erd.png)

</details>

- #### User Model

  - Provided by the Django framework, each new user is given a unique ID which will serve as FK (Foreign Key) in Post & Comment model.

  - Username, Email and Password is chosen by the user and can be updated from the Profile page.

- #### Post Model

  - ID and time of creation is given automatically. 

  - Users can choose a title, excerpt, content and image, while author is automatically set to the signed in users ID.

  - Likes will be 0 when created, and has a Many to Many relationship with the User model, meaning that many users can like the same post, and the same user can like many posts.

- #### Comment Model

  - ID and time of creation is given automatically.

  - Users can choose a body, while author is automatically set to the signed in users ID.

  - The post field has a FK to the Post model, to make sure the comment is assigned to the correct blog post.

### Wireframes

Wireframes were created using Balsamiq to help the planning process and get an idea of how the site was to be built. The finished site came very close to these mockups, with some minor adjustments.

<details>

<summary>Desktop wireframes</summary>

Home page
![Desktop wireframe home](static/images/readme-images/wireframes/Desktop-home.png)

About page
![Desktop wireframe about](static/images/readme-images/wireframes/Desktop-about.png)

Register page
![Desktop wireframe register](static/images/readme-images/wireframes/Desktop-register.png)

Sign in page
![Desktop wireframe sign in](static/images/readme-images/wireframes/Desktop-signin.png)

Profile page
![Desktop wireframe profile](static/images/readme-images/wireframes/Desktop-profile.png)

Sign out page
![Desktop wireframe sign out](static/images/readme-images/wireframes/Desktop-signout.png)

Delete account page
![Desktop wireframe delete account](static/images/readme-images/wireframes/Desktop-delete_account.png)

Create post page
![Desktop wireframe create post](static/images/readme-images/wireframes/Desktop-create_post.png)

Post detail page
![Desktop wireframe post detail](static/images/readme-images/wireframes/Desktop-post.png)

Update post page
![Desktop wireframe update post](static/images/readme-images/wireframes/Desktop-update_post.png)

Delete post page
![Desktop wireframe delete post](static/images/readme-images/wireframes/Desktop-delete_post.png)

</details>

<details>

<summary>Mobile wireframes</summary>

Home page<br>
![Mobile wireframe home](static/images/readme-images/wireframes/Mobile-home.png)

About page<br>
![Mobile wireframe about](static/images/readme-images/wireframes/Mobile-about.png)

Register page<br>
![Mobile wireframe register](static/images/readme-images/wireframes/Mobile-register.png)

Sign in page<br>
![Mobile wireframe sign in](static/images/readme-images/wireframes/Mobile-signin.png)

Profile page<br>
![Mobile wireframe profile](static/images/readme-images/wireframes/Mobile-profile.png)

Sign out page<br>
![Mobile wireframe sign out](static/images/readme-images/wireframes/Mobile-signout.png)

Delete account page<br>
![Mobile wireframe delete account](static/images/readme-images/wireframes/Mobile-delete_account.png)

Create post page<br>
![Mobile wireframe create post](static/images/readme-images/wireframes/Mobile-create_post.png)

Post detail page<br>
![Mobile wireframe post detail](static/images/readme-images/wireframes/Mobile-post.png)

Update post page<br>
![Mobile wireframe update post](static/images/readme-images/wireframes/Mobile-update_post.png)

Delete post page<br>
![Mobile wireframe delete post](static/images/readme-images/wireframes/Mobile-delete_post.png)

</details>

### Design
- #### Colours

  The colours used on the site are discreet and chosen to put emphasis on the content of blog posts, and not be distracting to the user. The background color is a near white Bootstrap colour (bg-light) that gives contrast to the content on the page, which is wrapped in card-like modules with a clear white background. 
  The navigation bar at the top of the page has a gray Bootstrap colour (bg-secondary) that is also consistently used throughout the application on links and buttons.

  User interactions, such as posting and commenting, or registering and deleting an account all have relevant user feedback. The buttons are coloured in an appropriate way, such as delete buttons being red. Messages giving users feedback are also coloured appropriately to clarify user actions taken.

- #### Typography

  The font used for the site is Poppins, an aesthetically and geometrically pleasing font that suits the content and clean feel of the site. If the font isn't imported correctly, Sans-serif will serve as fallback.

- #### Imagery

  The images on the site are mainly user uploaded post images, with a few exceptions. An image depicting a person overwhelmed with technology is used on the About page, and a generic image of tech gadgets is used as placeholder if a user fails to provide one when creating a post. The main focus should always fall on the content written by the members of the site, therefore no other images were necessary.

## Agile Methodology

To better plan and understand the development process, an agile approach was taken when implementing features. GitHub Projects provides a great way of keeping track of progress made and user stories to develop. By creating a project board on a basic kanban template, the development process can be overviewed and tackled in a proficient and time-effective way. Each user story was first created and added to the project board, then moved to In Progress as the feature was being developed, and finally to Done. With this approach it's easy to make sure the most important features gets implemented first.

This approach is especially powerful when working in teams, but still made the development process more enjoyable and easier to keep track of when developing alone.

<details>

<summary>GitHub Project Board</summary>

![GitHub Project Board](static/images/readme-images/project-board.png)

</details>

As evident by the above image, not all user stories were finished in the time frame of this project. These will be implemented and possibly added to in the future.

## Features

The following section will provide an overview of the features included in Tech Blog. The site consists of several pages, all with a consistent layout and logical paths to take. Some pages can only be accessed by members, while others are accessible to all. All features are fully responsive across all devices.

- ### Navigation Bar

  - Featured at the top of all pages is a nav bar, which holds the logo for the site to the left, as well as navigation links on the right side. 

  - When a new user visits the site, the nav bar will hold an 'Account' option that, when clicked, shows two additional links to either sign in or register.

  - A signed in user will see their username instead which, when clicked, shown links to either create a post, the users profile, or to sign out.

  - When viewed on smaller devices, the navigation links will collapse into a so-called burger icon to help keep the nav bar clean.

  <details>

  <summary>Navigation Bar</summary>

  ![Navigation Bar](static/images/readme-images/navbar-desk.png)

  </details>

  <details>

  <summary>Navigation Bar - Signed In</summary>

  ![Navigation Bar - signed in](static/images/readme-images/navbar-desk-auth.png)

  </details>

  <details>

  <summary>Navigation Bar - Mobile</summary>

  ![Navigation Bar - mobile](static/images/readme-images/navbar-collapsed.png)

  </details>

  <details>

  <summary>Navigation Bar - Mobile Dropdown</summary>

  ![Navigation Bar - mobile dropdown](static/images/readme-images/navbar-clicked.png)

  </details>

- ### Home Page

  - The home page is the main blog feed where users can browse posts and get an idea of what the posts are about.

  - Each post entry is listed with newest at the top, with a pagination of five posts per page.

  - Information about author, date posted and number of comments and likes is also visible from here.

  <details>

  <summary>Home Page - Desktop</summary>

  ![Home Page - Desktop](static/images/readme-images/home-desk.png)

  </details>

  <details>

  <summary>Home Page - Mobile</summary>

  ![Home Page - Mobile](static/images/readme-images/home-mobile.png)

  </details>

- ### Footer

  - The footer is a simple bar in clear white that breaks off from the near white background to create a subtle and pleasing element at the bottom of the page.

  - To the left is a short copyright text, and on the right side users can find links to different social media plattforms. Since Tech Blog is for educational purposes the links directs the user to the homepage of each plattform respectively.

  <details>

  <summary>Footer - Desktop</summary>

  ![Footer - Desktop](static/images/readme-images/footer-desk.png)

  </details>

  <details>

  <summary>Footer - Mobile</summary>

  ![Footer - Mobile](static/images/readme-images/footer-mobile.png)

  </details>

- ### About Page

  - The about page serves as a short introduction to the blog and what users can expect to find. The text emphasize that everyone is welcome to become members and start sharing their thought with other members, regardless of whether a user is looking for tips, or want to write reviews etc.

  - A fitting image of a guy overwhelmed with tech gadgets helps relate to users.

  <details>

  <summary>About Page - Desktop</summary>

  ![About Page - Desktop](static/images/readme-images/about-desk.png)

  </details>

  <details>

  <summary>About Page - Mobile</summary>

  ![About Page - Mobile](static/images/readme-images/about-mobile.png)

  </details>

- ### Register Page

  - To be able to interact with the site and post content users must register for an account. This page simply lets users choose a username, email and password and saves it to the database.

  - The built in authentication system in Django worked very well for this and if for instance a username is already in use, a message is shown to the user to inform of this.

  - If a user clicks on Register by misstake and already have an account, a link at the bottom takes the user to the sign in page instead.

  <details>

  <summary>Register Page - Desktop</summary>

  ![Register Page - Desktop](static/images/readme-images/register-desk.png)

  </details>

  <details>

  <summary>Register Page - Mobile</summary>

  ![Register Page - Mobile](static/images/readme-images/register-mobile.png)

  </details>

- ### Sign In Page

  - When a user already has an account, they go to the sign in page. Just like on the register page there is a link at the bottom if the user meant to go there.

  <details>

  <summary>Sign In Page - Desktop</summary>

  ![Sign In Page - Desktop](static/images/readme-images/signin-desk.png)

  </details>

  <details>

  <summary>Sign In Page - Mobile</summary>

  ![Sign In Page - Mobile](static/images/readme-images/signin-mobile.png)

  </details>

- ### Profile Page

  - The profile page is accessible for signed in users, and features the users info with a form to update it if desirable.

  - Users can also delete their account from the link at the bottom if they wish, to make sure no info is stored on them. If clicked, the user is taken to a confirmation screen to make sure an account is not deleted by accident.

  <details>

  <summary>Profile Page - Desktop</summary>

  ![Profile Page - Desktop](static/images/readme-images/profile-desk.png)

  </details>

  <details>

  <summary>Profile Page - Mobile</summary>

  ![Profile Page - Mobile](static/images/readme-images/profile-mobile.png)

  </details>

  <details>

  <summary>Profile Page - Delete Account</summary>

  ![Profile Page - Delete Account](static/images/readme-images/delete-account.png)

  </details>

- ### Sign Out Page

  - When a user clicks the sign out link a page with a message stating they have been signed out is shown. Two links to the home page and back to the sign in page can also be found.

  <details>

  <summary>Sign Out Page - Desktop</summary>

  ![Sign Out Page - Desktop](static/images/readme-images/signout-desk.png)

  </details>

  <details>

  <summary>Sign Out Page - Mobile</summary>

  ![Sign Out Page - Mobile](static/images/readme-images/signout-mobile.png)

  </details>

- ### Create Post Page

  - Signed in users can access this page from the nav bar, and from here they can create post entries by filling out a form.

  - Users choose a title, excerpt, content and an image for their post, while ID, author and time of creation is given automatically.

  - If the user don't upload an image for their post, a generic placeholder image is provided for them.

  <details>

  <summary>Create Post Page - Desktop</summary>

  ![Create Post Page - Desktop](static/images/readme-images/create-post-desk.png)

  </details>

  <details>

  <summary>Create Post Page - Mobile</summary>

  ![Create Post Page - Mobile](static/images/readme-images/create-post-mobile.png)

  </details>

- ### Post Detail Page

  - When user creates or clicks on a post from the home page, the post detail page is shown, with the full content of the post, along with any comments that has been left by users on the post.

  - There is a like button that users can toggle to like / unlike posts and show appreciation to fellow members. 

  - If the author of the post visits the page, there are buttons for updating the post, as well as deleting it.

  - If a user leaves a comment and later wants to delete it, there is a small button on the comments written by the signed in user to delete their own comments. This will trigger a modal to ask for confirmation to prevent accidental deletion.

  <details>

  <summary>Post Detail Page - Desktop</summary>

  ![Post Detail Page - Desktop](static/images/readme-images/post-desk.png)

  </details>

  <details>

  <summary>Liked & Authors Post - Desktop</summary>

  ![Liked & Authors Post - Desktop](static/images/readme-images/post-liked-auth-desk.png)

  </details>

  <details>

  <summary>Authors Post - Mobile</summary>

  ![Authors Post - Mobile](static/images/readme-images/post-auth-mobile.png)

  </details>

  <details>

  <summary>Liked Post - Mobile</summary>

  ![Liked Post - Mobile](static/images/readme-images/post-liked-mobile.png)

  </details>

  <details>

  <summary>Delete Comment</summary>

  ![Delete Comment](static/images/readme-images/delete-comment.png)

  </details>

- ### Update Post

  - If the author of a post wishes to edit or update their post, they click the button on the detail page and a form for updating it is shown.

  - All fields are prepopulated with the existing data to simplify the process for the user.

  - If the user wishes to go back without saving any changes, they can simply click the 'Go back' link at the bottom.

  <details>

  <summary>Update Post Page - Desktop</summary>

  ![Update Post Page - Desktop](static/images/readme-images/update-post-desk.png)

  </details>

  <details>

  <summary>Update Post Page - Mobile</summary>

  ![Update Post Page - Mobile](static/images/readme-images/update-post-mobile.png)

  </details>

- ### Delete Post Page

  - If the author of a post wishes to delete it, they click the button on the detail page and a confirmation page is shown.

  - If the user wishes to go back without deleting the post, they can simply click the 'Keep the post' link at the bottom.

  <details>

  <summary>Delete Post Page - Desktop</summary>

  ![Delete Post Page - Desktop](static/images/readme-images/delete-post-desk.png)

  </details>

  <details>

  <summary>Delete Post Page - Mobile</summary>

  ![Delete Post Page - Mobile](static/images/readme-images/delete-post-mobile.png)

  </details>

- ### Messages

  - To keep users informed, simple message flashes will be displayed on various user interactions, such as creating a post, registering an account etc. These will only be visible a few seconds before dissapearing by themself, to not interfere with the UX.

  <details>

  <summary>Create Account Message</summary>

  ![Create Account Message](static/images/readme-images/msg-account-create.png)

  </details>

  <details>

  <summary>Create Post Message</summary>

  ![Create Post Message](static/images/readme-images/msg-post-create.png)

  </details>

  <details>

  <summary>Delete Post Message</summary>

  ![Delete Post Message](static/images/readme-images/msg-post-delete.png)

  </details>

### Features Left to Implement

- Password reset through the registered e-mail, if the user forgets their password.

- See a list of the users own post, to easier manage their own content.

- A nicer format for writing the body of post entries, like a rich text editor.

- Search function to find a certain post or posts about a certain topic.

- Automatically resize images uploaded by users to improve site performance.

## Testing
### Code Validation

To ensure all code for Tech Blog is correct, validation through various validators was performed. The results are listed below.

- ### HTML Validation

  All HTML code was checked with the [W3C Markup Validator](https://validator.w3.org/). One error was found on the Register page, which was attributed to code provided by the built in authentication system of Django, and could therefore not be addressed. No other error or warnings were found.

  <details>

  <summary>Home Page</summary>

  ![Home Page](static/images/readme-images/testing/html-home.png)

  </details>

  <details>

  <summary>About Page</summary>

  ![About Page](static/images/readme-images/testing/html-about.png)

  </details>

  <details>

  <summary>Register Page</summary>

  ![Register Page](static/images/readme-images/testing/html-register.png)

  </details>

  <details>

  <summary>Sign In Page</summary>

  ![Sign In Page](static/images/readme-images/testing/html-signin.png)

  </details>

  <details>

  <summary>Profile Page</summary>

  ![Profile Page](static/images/readme-images/testing/html-profile.png)

  </details>

  <details>

  <summary>Sign Out Page</summary>

  ![Sign Out Page](static/images/readme-images/testing/html-signout.png)

  </details>

  <details>

  <summary>Delete Account Page</summary>

  ![Delete Account Page](static/images/readme-images/testing/html-account-delete.png)

  </details>

  <details>

  <summary>Create Post Page</summary>

  ![Create Post Page](static/images/readme-images/testing/html-post-create.png)

  </details>

  <details>

  <summary>Post Detail Page</summary>

  ![Post Detail Page](static/images/readme-images/testing/html-post-detail.png)

  </details>

  <details>

  <summary>Post Update Page</summary>

  ![Post Update Page](static/images/readme-images/testing/html-post-update.png)

  </details>

  <details>

  <summary>Post Delete Page</summary>

  ![Post Update Page](static/images/readme-images/testing/html-post-delete.png)

  </details>

- ### CSS Validation

  All CSS code was checked with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). No errors or warnings were found.

  <details>

  <summary>CSS code Results</summary>

  ![CSS code Results](static/images/readme-images/testing/css-validation.png)

  </details>

- ### JavaScript Validation

  All JavaScript code was checked with the [JSHint Code Quality Tool](https://jshint.com/). No errors or warnings were found.

  <details>

  <summary>JavaScript code Results</summary>

  ![JavaScript code Results](static/images/readme-images/testing/jshint.png)

  </details>

- ### Python Validation

  All Python code was checked with the [PEP8 Online Validator](http://pep8online.com/). No errors or warnings were found.

  <details>

  <summary>Blog App admin.py</summary>

  ![Blog App admin.py](static/images/readme-images/testing/pep8-blog-admin.png)

  </details>

  <details>

  <summary>Blog App apps.py</summary>

  ![Blog App apps.py](static/images/readme-images/testing/pep8-blog-apps.png)

  </details>

  <details>

  <summary>Blog App forms.py</summary>

  ![Blog App forms.py](static/images/readme-images/testing/pep8-blog-forms.png)

  </details>

  <details>

  <summary>Blog App models.py</summary>

  ![Blog App models.py](static/images/readme-images/testing/pep8-blog-models.png)

  </details>

  <details>

  <summary>Blog App urls.py</summary>

  ![Blog App urls.py](static/images/readme-images/testing/pep8-blog-urls.png)

  </details>

  <details>

  <summary>Blog App views.py</summary>

  ![Blog App views.py](static/images/readme-images/testing/pep8-blog-views.png)

  </details>

  <details>

  <summary>Blog App test_forms.py</summary>

  ![Blog App test_forms.py](static/images/readme-images/testing/pep8-blog-test_forms.png)

  </details>

  <details>

  <summary>Blog App test_models.py</summary>

  ![Blog App test_models.py](static/images/readme-images/testing/pep8-blog-test_models.png)

  </details>

  <details>

  <summary>Blog App test_urls.py</summary>

  ![Blog App test_urls.py](static/images/readme-images/testing/pep8-blog-test_urls.png)

  </details>

  <details>

  <summary>Blog App test_views.py</summary>

  ![Blog App test_views.py](static/images/readme-images/testing/pep8-blog-test_views.png)

  </details>

  <details>

  <summary>Users App apps.py</summary>

  ![Users App apps.py](static/images/readme-images/testing/pep8-users-apps.png)

  </details>

  <details>

  <summary>Users App backends.py</summary>

  ![Users App backends.py](static/images/readme-images/testing/pep8-users-backends.png)

  </details>

  <details>

  <summary>Users App forms.py</summary>

  ![Users App forms.py](static/images/readme-images/testing/pep8-users-forms.png)

  </details>

  <details>

  <summary>Users App urls.py</summary>

  ![Users App urls.py](static/images/readme-images/testing/pep8-users-urls.png)

  </details>

  <details>

  <summary>Users App views.py</summary>

  ![Users App views.py](static/images/readme-images/testing/pep8-users-views.png)

  </details>

  <details>

  <summary>Users App test_forms.py</summary>

  ![Users App test_forms.py](static/images/readme-images/testing/pep8-users-test_forms.png)

  </details>

  <details>

  <summary>Users App test_urls.py</summary>

  ![Users App test_urls.py](static/images/readme-images/testing/pep8-users-test_urls.png)

  </details>

  <details>

  <summary>Users App test_views.py</summary>

  ![Users App test_views.py](static/images/readme-images/testing/pep8-users-test_views.png)

  </details>

### Responsive Testing
### Lighthouse Testing
### Links and Form Testing
### Fixed Bugs
### Known/Unfixed Bugs

## Technologies Used
### Languages
### Programs & Libraries

## Deployment

## Credits
### Code
### Content
### Media
### Acknowledgements
