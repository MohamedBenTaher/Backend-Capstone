
## Django DRF Booking API

This API is designed for managing bookings of a hotel or similar facility. It is built using Django and Django REST Framework (DRF).
Features

   - Token-based authentication
   - User management using Djoser
   - APIs for managing bookings

# Authentication

This API uses token-based authentication. To access the API, users must obtain an authentication token by providing their credentials. The token must be included in the headers of subsequent requests.
User Management

User management is implemented using Djoser. This library provides endpoints for registration, login, and password reset.
APIs

The following APIs are available:

    - /api/restaurant/booking/tables/- This endpoint allows you to view and create,view,edit,delete bookings. Only authenticated users can create,edit,delete bookings.
    - /api/restaurant/menu/ - This endpoint allows you to view  menu items
    - /api/restaurant/menu/<id>/ - This endpoint allows you to view, update, and delete a specific menu item. Only the user who created the menu item can update or delete it.
    - /api/restaurant/api-token-auth/ This edpoint allows you create a Token using your username and password
    - Djoser endpoints for registration and login 

# testing

This API has been thoroughly tested using Django TestCase. All tests are included in the tests.py file.
Installation

To install this API, follow these steps:

   - Clone the repository to your local machine.
   - Create a virtual environment using python pipenv shell,
   - Install the required packages using pipenv install.
   - Run the database migrations using python manage.py migrate.
   - Create a superuser using python manage.py createsuperuser.
   - Start the server using python manage.py runserver.

# Usage

To use the API, follow these steps:

  - Obtain an authentication token by logging in or registering using the Djoser endpoints.
  - Include the authentication token in the headers of subsequent requests.
  - Use the available endpoints to manage bookings.

Credits

This API was created by Mohamed Ben Taher. If you have any questions or concerns, please contact me at mbentaher1998@gmail.com.
