 # Charlotte Durber - She Codes News Project
 
## About This Project
A news website that allows users to read news stories, create their own profile and then post their own news stories.

## How To Run This Code (for MAC users only)

1. Clone repo to your local machine `git clone {{link here}}`

2. Change directory to the cloned repo `cd she_codes_news`

3. Create a virtual environment `python3 -m venv venv`

4. Initialise repo `git init`

5. Activate virtual environment `source venv/bin/activate`

6. Install a library `python3 -m pip install -r requirements.txt`

7. Make initial migrations `python3 manage.py migrate`

8. Run the server `python3 manage.py runserver`

9. Enjoy!


## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )


## Project Features
- [x] Order stories by date

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/main-page.png?raw=true)

- [x] Styled "new story" form

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/form-view.png?raw=true)

- [x] Story images

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/story-image.png?raw=true)

- [x] Log-in/log-out

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/login.png?raw=true)
![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/logout.png?raw=true)

- [x] "Account view" page

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/account-view.png?raw=true)

- [x] "Create Account" page

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/create-account.png?raw=true)

- [x] View stories by author

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/stories-posted.png?raw=true)

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button
        only visible when a user *is* logged in

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/login.png?raw=true)

- [x] "Create Story" functionality only available when user is logged in

![model](https://github.com/cdurber90/she_codes_news/blob/main/she_codes_news/news/static/news/images/logout.png?raw=true)

<!-- ## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories by
        category.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to update and delete stories (consider permissions - who
        should be allowed to update or and/or delete stories).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to “favourite” stories and see a page with your favourite
        stories.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Our form for creating stories requires you to add the publication date,
        update this to automatically save the publication date as the day the
        story was first published (maybe you could then add a field to show
        when the story was updated).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
               
 
- [ ] Gracefully handle the error where someone tries to create a new story when
        they are not logged in.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} ) -->
