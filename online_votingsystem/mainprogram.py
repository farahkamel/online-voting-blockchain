# ------------  firstly, add the libraries --------------
# sqlite3: it will be used in our code to use a lightweight disk-based database that doesn't require a separate server process
import sqlite3
# the following line will provide a SQL interface compliant with the DB-API 2.0 specification to make server connection
from sqlite3 import Error
from sqlite3.dbapi2 import Connection
# the below line will provide you with tools that we will use while creating our web pages
from flask import *
# the below line will import the block_chain.py python file as blockbone
import block_chain as blockone
# below line will be used in case of reading the data from the csv file 
import csv
# importing the following line will use pickle to save and restore class instances transparently
import pickle
#the below 2 lines will be used to handle operations regarding time and datetime in our code(time creation)
import time
from datetime import datetime


# using the line below, Flask constructor will take the name of current module (__name__) as argument.
application = Flask(__name__)
# the below line will create the instance of the class Block_chain() from the blockbone (block_chain.py) class
chains = blockone.Block_chain()
# the below line will use the function "create_Genesisblock" defined in the class Block_chain(), through the instance (object) chains 
chains.create_Genesisblock()

# we are defining here the function to establish our connection with the database. this connection will be used for client-server interaction
def establishing_conncetionn():
    connection = None
    movies_database = "votingdb"
    # below is the try-catch statement to connect the database with the server 
    try:
        connection = sqlite3.connect(movies_database)
    # in case the database doesnt get connected, it will generate the error message and will print on screen
    except Error as f:
        print(f)
    #this line will return the established connection to the calling function or the main program
    return connection

# the below function will perform all tasks after creating the connection of the database with the server
def preformingfuntions(connection):
    # these lines of code will execute the lines for the webpage one by one. 
	# A cursor is an object which helps to execute the query and fetch the records from the database.
    currsorobject = connection.cursor()
    # the below line will execute the first query from the database which requires to select all the movies
    currsorobject.execute("select * from movies")
    # the following line will give a list unless the result set is empty, in which case it will give an empty tuple
    db_rowss = currsorobject.fetchall ()
    # defining a new list named movies
    movies = []
    # running over the records one by one with the for loop
    for r in db_rowss:
        # the below line will add the records of the movies or the complete response of the query from the database.
        movies.append({"movieID": r[0], "movie_name":r[1], "movie_star":r[2],"genre":r[3],"age_restricted": False})
    # return complete list of movies / extracted set of movies from the database
    return movies

# the below line wil call the establishing_conncetionn() function to start connecting the database with the server
connection= establishing_conncetionn()
# the following line will provide the established connection to perform all the information extraction tasks
movies= preformingfuntions(connection)
# the following function will get the movie through the indexing operation of using movieID
def get_movie(movieID):
    # it will go through the whole movies set
    for f in movies:
        # if the movieID will match the input movieID of the movie, then it will return that movie data
        if f["movieID"]==movieID:
            return f

# The application route is entered when out app will first boots up. Like other routes, it will load a template with the same name ( application in this case) 
# by default. it has all the header, footer, and any other decorative content here. All other routes will render their templates into the application.
@application.route("/")
# the function below will return the rendered template for the movies set
def functioning():
    context = {"movies": movies}
    return render_template("index.html",movies=movies)

# the below application template will follow the POST method for it. it will be used to send data to the server to create/update a resource.
# the function below will request a movie from the form
@application.route("/homeblock", methods =['POST'])
# the function below will request a movie from the form
def second_functionality():
    prefrence = request.form['movie']
    # the line below will provide the time() function as parameter to the Blocks class and will also pass on the preferences of the movies as input parameter
    blocktwo=blockone.Blocks(time.time(),get_movie(int(prefrence)))
    # it will call the creating_block function from the class and will pass the blockTwo as input parameter
    chains.creating_block(blocktwo)
    # if the redirection will be successful then it will return the True status to the calling place
    return redirect("/Successful")

# the below application rendering template will use all the three methods: the Get, the Post and the Delete method
# the GET method will be used to request data from a specified resource. the Post method will send data to a server to create/update a resource.
# the Delete method will be used to the delete the requested or the specified resource.
@application.route("/Successful", methods =[ "GET","POST","DELETE"])
# the function below is used to return the rendering template defined in the homeblock.html and will work on the showing_chains method of the chains instance
def message():
    return render_template("homeblock.html",chains=chains.showing_chains())
# the below template will only make use of the Get method and will just request data from the server for the movies
@application.route("/showresults", methods = ["GET"])
# the function below will be used to print out the final results 
def finalresults():
    # creating the new dictionary of recording votes
    votes_records={}
    # the following loop will go through the function of showing chains of movies 
    for r in chains.showing_chains():
        if r.block_number!=0:
            if r.information["movieID"] in votes_records:
              votes_records[r.information["movieID"] ] +=1
            else :
                votes_records[r.information["movieID"] ]=1
    # the following list is created to store the information of the movies resource
    information =[]
    # now go through the votes_recorded dictionary using for loop
    for r in votes_records:
        # get movie for each movieID from the voterecords dictionary
        movie_dictionary =get_movie(r)
        movie_dictionary["votes_records"]=votes_records[r]
        # keep on appending the information in the information list
        information.append(movie_dictionary)
    # now this function will return the rendered template showing the showresults.html page through the extracted information in form of list
    return render_template("showresults.html",chains=information )

# lastly, this is the main program.
if __name__=='__main__':
    # now run the application through port 5001 and make the debugging option by keeping it True
    application.run(port = 5001,debug=True)




