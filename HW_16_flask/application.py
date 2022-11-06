# ------------------------------------------------
# Program by Anton Praljuk
#
#
# Version      Date           Info
# 1.0          05-Nov-2022    Initial Version
#
# ----------------------------------------------

from flask import Flask


application = Flask(__name__)


@application.route("/")
def index():
    return f'Hello my friend, u want some magic?'


@application.route("/help")
def helppage():
    return f'<b><font color=blue>This is Help Page</font></b>'


@application.route("/user")
def usermain_page():
    return f'User Main Page'


@application.route("/user/<username>")
def show_user_page(username):
    return f'Hello {username.upper()}'


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return f'SubPath is: {subpath}'


@application.route("/square/<int:x>")
def calc_kvadrat(x):
    return f'Square from {str(x)}: {str(x)}^2 = {str(x*x)}'


@application.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page


#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.env   = "Anton working hard"
    application.run()
#------------------------------