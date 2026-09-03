# Django Product List Application

## Project Overview

This academic Django project demonstrates the foundational structure of a small database-backed web application. It uses a Django model, ORM query, function-based view, URL routing, and an HTML template to display a list of products stored through an SQLite-backed configuration.

The project focuses on introductory Django development rather than a complete production application.

## Implemented Functionality

- Defines a `Product` data model
- Retrieves product records using the Django ORM
- Displays product names, prices, and descriptions
- Serves the product list from the root application route
- Uses a Django template for server-rendered HTML
- Registers the `Product` model with Django’s built-in admin interface
- Includes an initial database migration for the product model

The public application currently provides a read-only product-list workflow. It does not include custom forms or public create, update, or delete views.

## Technology Stack

- Python
- Django
- Django ORM
- SQLite
- HTML
- Django templates

## Project Structure

```text
.
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── mainapp/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── product_list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── myapp/
├── db.sqlite3
└── .gitignore
```

- `manage.py` provides Django’s command-line entry point.
- `mysite/` contains the project configuration, URL routing, and application server interfaces.
- `mainapp/` contains the implemented product model, view, admin registration, migration, and template workflow.
- `myapp/` contains the default structure of an additional Django app, but it is not registered or integrated into the current application workflow.
- `db.sqlite3` is the configured SQLite database file.

## Data Model

The application defines one model named `Product`.

| Field | Type | Purpose |
|---|---|---|
| `id` | Automatically generated primary key | Identifies each product record |
| `name` | Character field, maximum 100 characters | Stores the product name |
| `price` | Decimal field with six total digits and two decimal places | Stores the product price |
| `description` | Text field | Stores the product description |

The repository includes an initial migration that creates the corresponding product table.

## Application Flow

1. A request is made to the root route, `/`.
2. The `product_list` view retrieves all `Product` records through `Product.objects.all()`.
3. The records are passed to `product_list.html` using the `products` template context.
4. The template renders each product’s name, price, and description in an HTML list.

The project also exposes Django’s built-in administration route at `/admin/` and registers the `Product` model with the admin interface. No custom authentication workflow or custom product-management views are implemented.

## Getting Started

### Prerequisites

- Python 3
- Django
- A graphical web browser

The repository does not currently include a dependency manifest, so Django must be installed manually.

### Installation

Clone the repository:

```bash
git clone https://github.com/asmaayasser1/django-tutorial.git
cd django-tutorial
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install Django:

```bash
python -m pip install Django
```

Apply the included migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

Open the local application in a browser:

```text
http://127.0.0.1:8000/
```

## Storage

The project is configured to use SQLite through Django’s database settings. Product records are accessed through the Django ORM.

`db.sqlite3` is tracked, but its contents were not inspected during this professionalization review.

## Security & Scope

This is an academic, development-oriented Django project and is not prepared for production deployment. Production use would require appropriate configuration, secret management, deployment hardening, and a dedicated security review.

## Testing Status

The repository contains Django’s default test-module scaffolding, but no automated test cases are currently implemented.

## Current Limitations

- The public workflow is limited to displaying product records.
- No custom product forms are implemented.
- No public create, update, or delete views are implemented.
- `myapp` is an unused Django application scaffold.
- No dependency manifest is included.
- No automated tests are implemented.
- The project uses development-oriented configuration.
- No production deployment configuration is provided.
- The tracked database contents have not been verified.

## Academic Context

This project was developed as an introductory Django assignment focused on models, views, templates, URL routing, database integration, and admin configuration.

## Project Status

Academic Django project being refined for professional portfolio presentation.
