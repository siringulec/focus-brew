# Task Manager Dockerized Django Application

This repository contains a Dockerized Django application for a project named "FocusBrew". The Docker setup ensures that the application runs consistently across different environments without any dependency conflicts. This README provides instructions on how to run the application using Docker.

## Prerequisites

Make sure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To run the Task Manager Django application, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   $ git clone https://github.com/siringulec/focus-brew.git
   $ cd task_manager
   ```

2. Build the Docker images:

   ```bash
   $ docker-compose build
   ```

3. Start the Docker containers:

   ```bash
   $ docker-compose up -d
   ```

   The `-d` flag runs the containers in detached mode.

4. Apply database migrations:

   ```bash
   $ docker-compose exec web python manage.py migrate
   ```

5. Create a superuser (admin):

   ```bash
   $ docker-compose exec web python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

6. Access the Task Manager application:

   Open your web browser and visit [http://localhost:8000](http://localhost:8000). You should see the Task Manager homepage.

7. Login to the admin panel:

   To access the admin panel, visit [http://localhost:8000/admin](http://localhost:8000/admin) and log in using the superuser credentials you created in step 5.

8. Start managing tasks:

   Use the Task Manager application to create, update, and manage tasks according to your project requirements.

## Stopping the Application

To stop the Task Manager application, run the following command in the project directory:

```bash
$ docker-compose down
```

This will stop and remove the Docker containers associated with the application.

## Development and Customization

You can make changes to the Django application as per your project requirements. The source code is located in the `task_manager` directory. Feel free to modify the code and update the Docker setup as needed.

## Troubleshooting

If you encounter any issues or have questions, please refer to the [Django documentation](https://docs.djangoproject.com/) or the [Docker documentation](https://docs.docker.com/). Additionally, you can check the project's issue tracker on GitHub for known issues and solutions.
