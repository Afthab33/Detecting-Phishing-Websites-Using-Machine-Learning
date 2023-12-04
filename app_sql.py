

import numpy as np
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]

from flask import Flask, request, jsonify, render_template
import joblib


import url_features

# Load the model from the file 
model = joblib.load('phishing.pkl')  

# Use the loaded model to make predictions 

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    


    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      

                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      
                      return render_template('register.html',text="This Username is Already in Use ")
    else:

                 


# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                  
                  return render_template('register.html',text="Succesfully Registered")
                
                  return render_template('login.html')


@app.route('/login')
def login(): 
    return render_template('login.html')         


@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
            
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
              
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
             
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                 
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index1.html')
    else:
        return render_template('login.html',text='Use Proper Username and Password')

                                               



                          



@app.route('/production')
def production(): 
    return render_template('index1.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]
    a=int_features

    url_processed = url_features.main(a[0])
      
        


    url_processed =np.array(url_processed ).reshape(1,-1)
    prediction=model.predict(url_processed)
    print(prediction)                                                                                                                                                                                              
    
    if prediction==-1:
        return render_template('index1.html',prediction_text='This is a Phishing Website')
    else:
        return render_template('index1.html',prediction_text='This is not a Phishing Website')





if __name__ == "__main__":
    app.run(debug=False)
