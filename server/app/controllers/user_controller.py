from app import app

@app.route('/users')
def users():
    return 'users'