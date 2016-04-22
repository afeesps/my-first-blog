1.in the settings.py add the app name 
static url is  given in the settings 
STATIC_URL = '/static/'

Templates directory can be set in the following configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates').replace('\\','/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

{% load staticfiles %} line in the html page is a must for loading static file s using templates


Now we need to hook up the Git repository on your computer to the one up on GitHub.

Type the following into your console (Replace <your-github-username> with the username you entered when you created your GitHub account, but without the angle-brackets):

$ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
$ git push -u origin master

Username for 'https://github.com': hjwp
Password for 'https://hjwp@github.com':
Counting objects: 6, done.
Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/hjwp/my-first-blog.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.


$ git clone https://github.com/<your-github-username>/my-first-blog.git


One more thing: deploy time!

It'd be good to see if your website will still be working on PythonAnywhere, right? Let's try deploying again.

$ git status
$ git add -A .
$ git status
$ git commit -m "Added view and template for detailed blog post as well as CSS for the site."
$ git push
Then, in a PythonAnywhere Bash console:
$ cd my-first-blog
$ git pull
[...]
