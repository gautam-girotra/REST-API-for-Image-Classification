# REST-API-for-Image-Classification

This project creates a REST API for Image classification.  
The model is trained using Tensorflow and Keras on the [Intel Image Dataset](https://www.kaggle.com/puneet6060/intel-image-classification) taken from Kaggle.  
The REST API is created using the FLASK framework.  

## Usage
1. Clone the repository and download the dataset in the directory mentioned in the jupyter notebook.
2. Run the Jupyter Notebook for training and saving the model.
3. Create a virtual environment and open the command terminal.
4. Install the required dependencies using ``` pip install -r requirements.txt ```
5. Run ```python application.py```
6. Open your browser and go to this [link](http://127.0.0.1:7777/).
The following website will appear.
![image](https://github.com/gautam-girotra/REST-API-for-Image-Classification/assets/69039186/5eca813d-f783-4115-af27-39cb1bb6dcce)
7. Choose any image that belongs to one of the following classes
``` labels = {0: 'buildings',
 1: 'forest',
 2: 'glacier',
 3: 'mountain',
 4: 'sea',
 5: 'street'}
```

9. Click Upload. The website will automatically redirect to a prediction page.
You will get a JavaScript alert like this one
![image](https://github.com/gautam-girotra/REST-API-for-Image-Classification/assets/69039186/2d59ef5e-c1c1-4e6f-b9e1-7ef3547dff75)

10. Click OK. Now you can see the predicted label and link to return back to the homepage.
![image](https://github.com/gautam-girotra/REST-API-for-Image-Classification/assets/69039186/ec05b113-1186-4dc1-b6b3-c8a4178864c2)



