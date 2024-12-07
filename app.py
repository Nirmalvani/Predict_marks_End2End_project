from flask import Flask, request, render_template

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import 
from src.pipeline.predict_pipeline import CustomData, predictpipeline

app = Flask(__name__)

# Route for the home page 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datapred',methods=['GET','POST'])
def datapred():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(gender = request.form.get('gender'),
            race_ethnicity= request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))
                  ) # Here we will be getting the data from predict piepline
        
        df = data.get_data_as_dataframe()
        print(df)

        predict = predictpipeline()
        results = predict.predict(df)
        return render_template('home.html',result = results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

    
