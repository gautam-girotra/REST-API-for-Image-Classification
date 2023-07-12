from flask import Flask,render_template,redirect,url_for,request
from tensorflow.keras.utils import load_img,img_to_array
from keras.models import load_model
import os
import numpy as np
from PIL import Image
import tensorflow_hub as hub
import werkzeug

global labels 
labels = {0: 'buildings',
 1: 'forest',
 2: 'glacier',
 3: 'mountain',
 4: 'sea',
 5: 'street'}


global img_path

app = Flask(__name__)

@app.route('/predict/<path>',methods=['GET','POST'])
def predict(path):
    model = load_model('model.h5',custom_objects={'KerasLayer':hub.KerasLayer})
    #load the image
    my_image = load_img(path, target_size=(224, 224))

    #preprocess the image
    my_image = img_to_array(my_image)
    my_image = my_image*1./255
    my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2])) 
    # print('This is the result: ',np.argmax(model.predict(my_image)))
    predicted_class = np.argmax(model.predict(my_image))
    prediction = str.capitalize(labels[predicted_class])
    return render_template(template_name_or_list="prediction.html", predicted_class=prediction)

@app.route('/upload/',methods=['GET','POST'])
def upload_image():

    if request.method == "POST":#Checking of the HTTP method initiating the request is POST.
        img_file = request.files["image_file"]#Getting the file name to get uploaded.
        img_path = os.path.join(app.root_path, img_file.filename)#Preparing the full path under which the image will get saved.
        img_file.save(img_path)#Saving the image in the specified path.
        print("Image uploaded successfully.")
        """
        After uploading the image file successfully, next is to predict the class label of it.
        The application will fetch the URL that is tied to the HTML page responsible for prediction and redirects the browser to it.
        The URL is fetched using the endpoint 'predict'.
        """
        return redirect(url_for(endpoint="predict",path=img_path))
    return "Image upload failed."


def index():
    return render_template('upload_image.html')
app.add_url_rule(rule="/", endpoint="homepage", view_func=index)

if __name__ == '__main__':
    # app.run(debug=False)
    
    app.run(host='0.0.0.0', port=7777,debug=True)

