# Heroku-Streamlit-Setup (hss)

This is a simple cli (command line interface) library to help you put your streamlit webapp in production.

I'll soon write a article on Medium explaining it (:

If you have any problem with it, please open an issue and I'll get back to you.

## Install with pip

This lib is hosted on pypi.org 
<pre>
pip install hss
</pre>

## Why is this package important and what do I need to use it?
From what I've seen there's not lots of documentation about putting streamlit webapps into production, trust me I've suffered. And if this is your first experience with Heroku, this will be very very helpfull.

You just need a Free [Heroku](https://www.heroku.com/) Account, a Github account and a [Streamlit](https://www.streamlit.io/) webapp you want to share with the world.

## The simplest way to use it

1. After the requirements.txt, Procfile and the setup.sh file are created, upload them into your project's repository
2. Create a new app using Heroku and select <b>connect to Github</b> and select your desired repo and click Deploy

## Documentation
<pre>
$ hss --help


Usage:
    hss [options] [&lt;appname&gt;] [&lt;path&gt;] [&lt;email&gt;]

Arguments:
    &lt;appname&gt;             The app filename (with or without .py).
    &lt;path&gt;                The path to the directory containing the application
                          files for which a requirements file should be
                          generated (defaults to the current working
                          directory).
    &lt;email&gt;               The email associated with your Heroku account.

Options:
    --no-reqs             Don't make a requirements file
    --no-setup            Don't make a setup.sh file
    --no-proc             Don't make a Procfile
    --force               Substitute the current requirements.txt.
</pre>
