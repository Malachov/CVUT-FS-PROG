#to run the website
#-------------------------------

from website import create_app

app = create_app()


#rerun webserver after every python code change
#for development purpose
if __name__ == '__main__':
    app.run(debug = True)