from flask import Flask, render_template, request
from predict import predict_movies


app=Flask(__name__)

@app.route('/', methods=["GET",'POST'])
def home():
    if request.method == 'POST':
        movie_name=request.form.get('movie').strip()
        pred = predict_movies(movie_name)
        print(pred.head())
        print(request.form.get('movie'))

    return render_template('home.html')



if __name__=='__main__':
    app.run(debug=True)