# Django Recipe App

This repository contains the source code for the Django Recipe App, a web application developed using the Django framework. The app allows users to create, save, and rate recipes, offering a robust platform for cooking enthusiasts to share and discover new dishes.

## Key Features

- **User Registration and Login**: Users can register and log in to the app to create, save, and rate recipes.
- **Recipe Creation**: Users can create new recipes by providing a title, description, ingredients list, and instructions. An image of the finished dish can also be uploaded.
- **Recipe Search and Browse**: Users can search for recipes by keyword or browse by category or cuisine type.
- **Recipe Rating and Review**: Users can rate and review recipes created by other users.
- **User Profile**: Each user has a profile page displaying their created recipes, saved recipes, and activity such as comments and ratings.
- **Admin Interface**: A superuser (admin) can manage recipes and users through the Django admin interface.
- **Responsive Design**: The app is designed to be responsive, ensuring a good user experience on both desktop and mobile devices.
- **Recipe Tags**: Add tags to recipes, allowing multiple tags per recipe, similar to hashtags. Users can view all recipes associated with a tag and pagination will be added for better navigation.
- **Category Selection**: Categories will be selectable from a pre-defined list created by the admin.
- **Multiple Comments**: Enable multiple comments per recipe with pagination.
- **Django Bootstrap**: Use Django Bootstrap to design a more user-friendly interface.

## Additional Features

- **Social Sharing**: Enable users to share their favorite recipes on social media platforms like Facebook and Twitter.
- **Shopping List**: Allow users to create a shopping list from the ingredients list of a recipe, with options to print or email it.
- **Advanced Search**: Provide advanced search options, allowing users to search for recipes based on criteria like dietary restrictions or cooking time.
- **Video Tutorials**: Allow users to upload and share video tutorials of their recipes.

## Demo Video

You can view a demo of the app below:

[![Django Recipe App Demo] (https://github.com/HafsaSultana/Django_Recipe_App/blob/main/Django_Recipe%20App_23_05_2023.mp4)]


## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- PostgreSQL (optional for production)

### Installation

## 1. Clone the repository:
   git clone https://github.com/your-username/django-recipe-app.git
   cd django-recipe

## 2. Create a virtual environment and activate it:
  venv venv
  source venv/bin/activate

## 3. Install the required dependencies:
  pip install -r requirements.txt

## 4. Configure the PostgreSQL database (optional for production):
  Create a PostgreSQL database and user.
  Update the DATABASES setting in settings.py with your database credentials.

## 5. Apply migrations:
  python manage.py migrate
  
## 6. Create a superuser:
  python manage.py createsuperuser

## 7. Start the development server:
  python manage.py runserver

**8.** Open your browser and visit http://127.0.0.1:8000 to access the application.

## Project Structure
- **recipes:** Contains models, views, and templates for recipe management.
- **users:** Manages user registration, login, and profiles.
- **templates:** Shared templates for rendering HTML pages.
- **static:** Static files such as CSS, JavaScript, and images.
