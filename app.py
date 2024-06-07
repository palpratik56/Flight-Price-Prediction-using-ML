from flask import Flask, url_for, render_template
from form import input
import joblib
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aetege'

model = joblib.load('model.joblib')

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html', title='Home')

@app.route('/Predict', methods=['GET', "POST"])
def pre():
    fo  = input()
    if fo.validate_on_submit():
        x_new = pd.DataFrame(dict(
            airline=[fo.airline.data],
            date_of_journey=[fo.doj.data.strftime("%Y-%m-%d")],
            source=[fo.src.data],
            destination=[fo.des.data],
            dep_time=[fo.dep.data.strftime("%H:%M:%S")],
            arrival_time=[fo.arr.data.strftime("%H:%M:%S")],
            duration=[fo.dur.data],
            total_stops=[fo.tos.data],
            additional_info=[fo.addinfo.data]
        ))
        pred = model.predict(x_new)[0]
        output = f'The predicted fare is INR {pred:,.0f}'
    else:
        output = 'Please Provide details to predict fare'
    return render_template('predict.html', title='Predict', form = fo, out = output)

if __name__ == '__main__':
    app.run(debug=True)