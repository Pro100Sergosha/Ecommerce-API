# Ecommerce-API

Welcome to the Ecommerce API project! This API serves as the backend for an e-commerce platform, designed to manage products, handle user interactions, and simulate purchases. The API offers a range of functionalities including product management, cart operations, and user authentication, leveraging Django and Django REST Framework for a robust and scalable solution.

## Table of Contents

#### [Functionality](#funcionality)

#### [Advantages](#advantages)

#### [Installation](#installation)

#### [API Endpoints](#api-endpoints)

#### [Contact](#contact-1)

## Functionality:

__Product Management:__ Perform CRUD operations on products, including details, prices, and stock.

__Media Handling:__ Upload and manage product images and videos.

__Color Management:__ Define and manage color options for products.

__Cart Management:__ Add products to user carts and view cart contents, with its statuses.

__User Authentication:__ Register and authenticate users with support for Google account integration.


### Advantages:

__Scalable Architecture::__ Built with Django and Django REST Framework, the API is designed to handle growth and adapt to increasing traffic and data loads.

__Comprehensive Product Management:__ Offers detailed management of product attributes, including price, stock, images, and more, ensuring flexibility in product representation.

__Media Handling:__ Supports uploading and managing product-related images and videos, enhancing the visual appeal and information available to users.

__User-Friendly Cart Management:__ Allows users to add products to their cart and view their cart contents easily, improving the shopping experience.

__Efficient Purchase Simulation:__ Simulates the purchase process with real-time stock updates, providing a realistic experience for users.

__Secure Authentication:__ Includes user registration, login, and email confirmation features with support for Google account integration, ensuring secure and seamless user access.

__Interactive API Documentation:__ Integrated with Swagger UI, providing an interactive and user-friendly interface for exploring and testing the API endpoints.

### Technology Stack:

__Django:__ The Django web framework is used for developing the server-side of the application, providing a powerful and secure tool for working with databases and handling requests.

__Python:__ Python programming language is used for writing the business logic of the application, including serial number generation, invoice amount calculations, and payment date setting.

## Installation (!!!Commands may vary for your OS!!!)

__1. Clone the repository:__

```
git clone https://github.com/Pro100Sergosha/Ecommerce-API.git
```
__2. Navigate to the project directory:__

```
cd Ecommerce-API
```

__3. Create your virtual environment:__
```
python -m venv venv
```

__4. Activate your virtual enviroment:__
```
venv\Scripts\activate
```
__5. Install the dependencies:__

```
pip install -r requirements.txt
```

__6. Set up environment variables by creating a .env file in the root directory. Use .env.example as a template:__
```
code .env
```
__7. Apply the database migrations to set up the database schema:__
```
python manage.py migrate
```
__8. Start the application__:
```
python manage.py runserver
```
## API Endpoints

### __Products__

List Products: GET /api/products/

Retrieve Product: GET /api/products/{id}/

Create Product: POST /api/products/

Update Product: PUT /api/products/{id}/

Delete Product: DELETE /api/products/{id}/


### __Images__

List Images: GET /api/images/

Retrieve Image: GET /api/images/{id}/

Upload Image: POST /api/images/

Delete Image: DELETE /api/images/{id}/


### __Colors__

List Colors: GET /api/colors/

Retrieve Color: GET /api/colors/{id}/

Create Color: POST /api/colors/

Update Color: PUT /api/colors/{id}/

Delete Color: DELETE /api/colors/{id}/


### __Videos__
List Videos: GET /api/videos/

Retrieve Video: GET /api/videos/{id}/

Upload Video: POST /api/videos/

Delete Video: DELETE /api/videos/{id}/


### __Cart__

Get Cart: GET /api/products/cart/

Add Product to Cart: POST /api/products/cart/


### _Buy Product__

Simulate Purchase: POST /api/products/buy-product/


### __Authentication__

Register: POST /dj-rest-auth/registration/

Login: POST /dj-rest-auth/login/

Logout: POST /dj-rest-auth/logout/

Confirm Email: GET /dj-rest-auth/registration/account-confirm-email/{key}/


### (!!!Before testing google authentication you need to set up google sign in method [GOOGLE-SIGN-IN TUTORIAL](https://www.youtube.com/watch?v=yO6PP0vEOMc) !!!)

Google Authentication: GET /accounts/login/


### __For detailed documentation of all endpoints, please refer to the API Documentation below.__

Swagger Documentation: Available at http://127.0.0.1:8000/swagger/


## Contact
For any questions or suggestions, please contact prizrakgames21@mail.ru.
