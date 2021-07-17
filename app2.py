import base64

import streamlit as st
import pandas as pd
import numpy as np
import cv2
import tensorflow as tf
import json

import csv
from itertools import chain
from tensorflow.keras.models import model_from_json
from load_css import local_css
st.set_option("deprecation.showfileUploaderEncoding", False)
@st.cache(allow_output_mutation=True)
def load_model():
  json_file = open('model.json', 'r')
  loaded_model_json = json_file.read()
  json_file.close()
  model = model_from_json(loaded_model_json)
  model.load_weights("model.h5")
  return model
model=load_model()




tab=st.sidebar.radio('Select',['Home','Prediction'])
if tab=='Home':
    main_bg='logo.jpg'
    main_bg_ext='jpg'
    st.markdown(
    f"""
    <style>
    
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
    
    
else:
    title='<h2><p style="font-family:Courier; color:Black; font-size:22px">Know Your Budget now</p></h2>'
    st.markdown(title,unsafe_allow_html=True)
   

    images_output=[]
    inputImages=[]
    textual_detail=[]
    c=0
    outputImage = np.zeros((128, 128, 3), dtype="uint8")


    file1 = st.file_uploader("Please upload bathroom image", type="jpg")
    
    if file1 is not None:
        # Convert the file to an opencv image.
        file_bytes1 = np.asarray(bytearray(file1.read()), dtype=np.uint8)
        opencv_image1 = cv2.imdecode(file_bytes1, 1)
        st.image(opencv_image1)
        image1 = cv2.resize(opencv_image1, (64 , 64))
        c=c+1

        
         
    file2 = st.file_uploader("Please upload bedroom image", type="jpg")

    if file2 is not None:
        # Convert the file to an opencv image.
        file_bytes2 = np.asarray(bytearray(file2.read()), dtype=np.uint8)
        opencv_image2 = cv2.imdecode(file_bytes2, 1)
        st.image(opencv_image2)

        image2 = cv2.resize(opencv_image2, (64 , 64))
        
        c=c+1

         
    file3 = st.file_uploader("Please upload frontal image", type="jpg")

    if file3 is not None:
        # Convert the file to an opencv image.
        file_bytes3 = np.asarray(bytearray(file3.read()), dtype=np.uint8)
        opencv_image3 = cv2.imdecode(file_bytes3, 1)
        st.image(opencv_image3)
        image3 = cv2.resize(opencv_image3, (64 , 64))
        c=c+1
    file4 = st.file_uploader("Please upload kitchen image", type="jpg")

    if file4 is not None:
        # Convert the file to an opencv image.
        file_bytes4 = np.asarray(bytearray(file4.read()), dtype=np.uint8)
        opencv_image4 = cv2.imdecode(file_bytes4, 1)
        st.image(opencv_image4)

        image4 = cv2.resize(opencv_image4, (64 , 64))
        c=c+1
    if c==4:
        inputImages.append(image1)
        inputImages.append(image2)
        inputImages.append(image3)
        inputImages.append(image4)
        outputImage[0:64, 0:64] = inputImages[0]
        outputImage[0:64, 64:128] = inputImages[1]
        outputImage[64:128, 64:128] = inputImages[2]
        outputImage[64:128, 0:64] = inputImages[3]
        images_output.append(outputImage)
        
        
        
    
    
    
        
  
    
    
    
    
    
    
    
    
    
    
    Bedrooms=st.number_input("No of Bedroom",1,10,1)
    c=c+1
    
    
    Bathrooms=st.number_input("No of Bathrooms",1,6,1)
    c=c+1
    zipcode=st.text_input('Zipcode')
    c=c+1
    
    area=st.text_input('Total Area In Square Feet')
    c=c+1
    
    
    
    
    
    textual_detail.append(Bedrooms)
    textual_detail.append(Bathrooms)
    textual_detail.append(area)
    textual_detail.append(zipcode)
    cols=["Bedrooms","Bathrooms","area","zipcode"]
    filename='mini.csv'
    
    
    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(cols) 
        csvwriter.writerow(textual_detail)
        csvfile.close()
        
    
  
    
        
    
    df = pd.read_csv('mini.csv')
    import numpy as np
    import pandas as pd
    d = pd.DataFrame(np.zeros((1, 9)))
    d = d.set_axis(['Bedrooms-1','Bedrooms-2','Bedrooms-3','Bedrooms-4','Bedrooms-5','Bedrooms-6','Bedrooms-7','Bedrooms-8','Bedrooms-10'], axis=1)
    def encode_text_dummy_bedroom(df):
        for x in d.columns:
            dummy_name=x
            df[dummy_name] = d[x]
        df.drop('Bedrooms', axis=1, inplace=True)
   
   
    d1 = pd.DataFrame(np.zeros((1, 11)))
    d1= d1.set_axis(['Bathrooms-1.0','Bathrooms-1.5','Bathrooms-2.0','Bathrooms-2.5','Bathrooms-3.0','Bathrooms-3.25','Bathrooms-3.5','Bathrooms-4.0','Bathrooms-4.5','Bathrooms-5.0','Bathrooms-6.0'], axis=1)
    def encode_text_dummy_bathroom(df):
        for x in d1.columns:
            dummy_name=x
            df[dummy_name]=d1[x]
        df.drop('Bathrooms', axis=1, inplace=True)
   
    d2 = pd.DataFrame(np.zeros((1, 41)))
    d2= d2.set_axis(['zipcode-36372','zipcode-60002','zipcode-60016','zipcode-60046','zipcode-62025','zipcode-62034','zipcode-62088','zipcode-62214','zipcode-62234','zipcode-62249','zipcode-81418','zipcode-81521','zipcode-81524','zipcode-85255','zipcode-85262','zipcode-85266','zipcode-85331','zipcode-91752','zipcode-91901','zipcode-91915','zipcode-92021','zipcode-92253','zipcode-92276','zipcode-92543','zipcode-92677','zipcode-92692','zipcode-92802','zipcode-92880','zipcode-93105','zipcode-93111','zipcode-93314','zipcode-93446','zipcode-93510','zipcode-93720','zipcode-94501','zipcode-94531','zipcode-94565','zipcode-94568','zipcode-95220','zipcode-96019','zipcode-98021'], axis=1)
    def encode_text_dummy_zipcode(df):
        for x in d2.columns:
            dummy_name=x
            df[dummy_name]=d2[x] 
        df.drop("zipcode", axis=1, inplace=True)
           


    
   
 
 
# Encode a numeric column as zscores
    def encode_numeric_zscore(df, name, mean=None, sd=None):
        if mean is None:
            mean = 2364.904672897196
 
        if sd is None:
            sd = 1224.5569818334923
 
        df[name] = (df[name] - mean) / sd
    if(c==8):
        encode_text_dummy_bedroom(df)
        encode_text_dummy_bathroom(df)
        encode_text_dummy_zipcode(df)
        encode_numeric_zscore(df, 'area')
    
        images_output = tf.stack(images_output)
        df = tf.stack(df)
        output=model.predict([df,images_output])
        
        if st.button('PREDICTION'):
          
           
            r1 = list(chain.from_iterable(output))
            for i in r1:
                
                r2=str(i)
                
            local_css("style.css")
 
            t = "<h2><div> <span class='highlight blue'><span class='bold'>Predicted value is ${r4} </span> </span><h2> </div>".format(r4=r2)
            
            st.markdown(t, unsafe_allow_html=True)
            
           
            
            
       