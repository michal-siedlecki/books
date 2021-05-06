# Querybook - Books REST API


![GitHub repo size](https://img.shields.io/github/license/michal-siedlecki/books)
![GitHub repo size](https://img.shields.io/github/repo-size/michal-siedlecki/books)

Querybook is a web app REST API that allows users to manage the books database.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed `python` >= 3.6.2
* You have a `<Windows/Linux/Mac>` machine.

## Installing Querybook

To install Querybook, follow these steps:

```
git clone https://github.com/michal-siedlecki/books
cd books-app
source venv/bin/activate
```
Now You have to set `SECRET_KEY` environmental variable since it is removed from repo.

```
export SECRET_KEY='my_very_secret_key'
```
You need to create database user `booksadmin` and database `books`. Next You need grant all 
privileges on database `books` to `booksadmin`
```
psql 
CREATE USER booksadmin PASSWORD 'testing321';
CREATE DATABASE books;
GRANT ALL PRIVILEGES ON DATABASE books TO booksadmin;
```

## Using Querybook

To use Querybook, follow these steps:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Contributing to Querybook

To contribute to Querybook, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.
Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@michal-siedlecki](https://github.com/michal-siedlecki) 😎 [author]


## Contact

If you want to contact me you can reach me at <siedlecki.michal@gmail.com>.

## License

This project uses the following license: MIT (<https://github.com/michal-siedlecki/books/blob/main/LICENSE>).
