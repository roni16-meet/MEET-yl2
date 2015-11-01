from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 
app = Flask(__name__)
@app.route("/")
def home():
	return render_template('home.html')


@app.route("/roni")
def roni():
	return render_template('roni.html')

@app.route("/contact_me",methods=['GET','POST'])
def contact_me():
	return render_template('contact_me.html')
	



if __name__ == "__main__": ## this if statement is telling python when running this file run the following lines
	app.debug = True ## this to let flask show us errors if there is any
	app.run()
	

