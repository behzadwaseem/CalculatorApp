from website import create_app

app = create_app()

if __name__ == '__main__':
#ensures that this line ONLY executes when this file is run directly
    app.run(debug=True)
    #runs flask application, starts website, debug means that everytime python code is changed, web server is autmatically re-run