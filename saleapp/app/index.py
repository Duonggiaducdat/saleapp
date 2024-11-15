from flask import render_template
import dao

from app import app


@app.route("/")
def index():
    cates = dao.load_categories()
    prods= dao.load_products()
    return render_template("index.html", categories=cates, products=prods)

@app.route("/register")
def register():
    return render_template("register.html")
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)