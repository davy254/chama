# Django Chama Project

This is an welfare contribution project built with Django. It is built to perform the following:

- Record  New members
- Record  monthly contributions
- Record  all monthly contributions
- Record loans taken

## Roadmap
To build a fully fledged open source welfare record keeping platform.

## Technologies Used

- Django
- Python
- HTML
- CSS
- JavaScript
- Bootstrap



## Installation

1. Clone the repository
2. Create a virtual environment
3. Install the dependencies with `pip install -r requirements.txt`

## Configuration

1. Create a new PostgreSQL database
2. Set up the environment variables by creating a `.env` file in the root directory and adding the following variables:

```
DEBUG=True
SECRET_KEY=<your_secret_key>
DATABASE_URL=postgres://<db_user>:<db_password>@<db_host>/<db_name>

```

3. Run `python manage.py migrate` to apply the database migrations

## Usage

1. Run `python manage.py runserver` to start the development server
2. Access the admin panel at `http://localhost:8000/admin`
3. Add products to the catalog using the admin panel
4. Browse the product catalog, add items to the shopping cart, and checkout

## Testing

1. Run `python manage.py test` to run the included tests

## Deployment

1. Set up a production environment with a web server such as Apache or Nginx
2. Configure the environment variables for the production environment
3. Collect the static files with `python manage.py collectstatic`
4. Set up a process manager such as systemd or supervisor to keep the application running

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
```


