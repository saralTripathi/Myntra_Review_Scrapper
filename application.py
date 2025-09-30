from flask import Flask, render_template, request
from flask_cors import cross_origin
from src.scrapper.scrape import ScrapeReviews


application = Flask(__name__) # initializing a flask appa
app=application


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route("/review", methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        scrape = ScrapeReviews(
            product_name=request.form['content'],
            no_of_products=int(request.form['prod_no'])
        )
        columns, data = scrape.get_review_data()
        
        
    return render_template("results.html",
                           titles = columns,
                           rows = data)

    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
                                

          
                
