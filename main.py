from flask import Flask,render_template,request
app = Flask(__name__)
import classifier as cl
import json

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def result():

    if request.method == 'POST':

        image = request.files["pic"]
        image.save("static/uploads/"+image.filename)
        result = cl.classify(image.filename)
        r = result.index(max(result))
        labels = ['Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis-like lesions', 'Dermatofibroma', 'Melanocytic nevi', 'Melanoma', 'Vascular lesions']
        ans = labels[r]
        return render_template('result.html', r = r, imgname = image.filename, labels = labels, result = result, ans = ans)

    else:

        return render_template('result.html', name="shine")

if __name__ == "__main__":
    app.run(debug=True)