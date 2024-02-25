from app import app

@app.route('/categories')
def categories():
    return 'Categories'