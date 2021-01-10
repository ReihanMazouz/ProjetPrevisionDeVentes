from flask import Flask, request, render_template,request
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from joblib import dump, load

Images = os.path.join('static', 'images')



X_train=pd.read_csv('/Users/reihan/Documents/DossierPython/ProjetDataAnalysisPython/Flask_Docs/app/X_train.csv')  
y_train=pd.read_csv('/Users/reihan/Documents/DossierPython/ProjetDataAnalysisPython/Flask_Docs/app/y_train.csv')  


random_forest= RandomForestRegressor()
model=random_forest.fit(X_train,y_train)
#dump(model, 'monpremiermodele.modele')
#Model=load('monpremiermodele.modele')


def FitrandomForest():
	random_forest= RandomForestRegressor()
	model=random_forest.fit(X_train,y_train)
	dump(model, 'monpremiermodele.modele')  #Enregistrement du model 

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = Images
    #FitrandomForest()

    @app.route('/')
    def homepage():
        return render_template('home.html')

    @app.route('/visu')
    def visu():
    	data = os.path.join(app.config['UPLOAD_FOLDER'], 'data.jpg')
    	quantity = os.path.join(app.config['UPLOAD_FOLDER'], 'quantity.jpg')
    	temp = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.jpg')
    	unitprice = os.path.join(app.config['UPLOAD_FOLDER'], 'unitprice.jpg')
    	marge = os.path.join(app.config['UPLOAD_FOLDER'], 'marge.jpg')
        return render_template('visu.html',data = data,quantity = quantity,temp = temp,unitprice = unitprice,marge = marge)

    @app.route('/pred')
    def pred():
        return render_template('pred.html')


    @app.route('/result',methods = ['POST', 'GET'])
    def result():
	    if request.method == 'POST':
	        form_data = request.form
	       	tab=[]
    		tab.append(form_data['Prix'])
    		tab.append(form_data['Marge'])
    		tab.append(form_data['CA'])
    		tab.append(form_data['Temperature'])
    		tab.append(form_data['Humidite'])
    		Predict=model.predict([tab])
	        return render_template('result.html',form_data = form_data, prix=Predict)

    return app

