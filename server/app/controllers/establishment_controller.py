from app import app

@app.route('/establishments')
def establishments():
    return 'Establishments'