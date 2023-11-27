from flask import render_template

class http_exceptions():
    def page_not_found(e):
        return render_template("404.html"), 404