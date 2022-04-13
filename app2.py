import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import sys
import os
from PIL import Image
sys.modules['Image'] = Image 
import tensorflow as tf
from tensorflow.keras.preprocessing import image

from dropdict import *
from helperfunctions import *


# # regression model
file = open("predict_model.pkl", "rb")
prediction_model=pickle.load(file)

# regression model
# file = open("rf_regressor_vehicle_value_predictor.pkl","rb")
# prediction_model=pickle.load(file)

# exterior classifier model
exterior_model = tf.keras.models.load_model('./packaged_exterior_classifier/saved_model_ext_class')

# color classifier model
color_model = tf.keras.models.load_model('./packaged_color_classifier/saved_model_color_class_01')

# body type classifier model
bodytype_model = tf.keras.models.load_model('./packaged_body_classifier/saved_model_body_class_01')

# car make classifier model
car_make_clf = tf.keras.models.load_model('./packaged_make_classifier/saved_model_make_class_02')


# lookup table
lookup = pd.read_csv("vin_lookup_year.csv")

def exterior_classification(img_path):
    img = image.load_img(img_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_preprocessed = np.expand_dims(img_array, axis=0)

    predictions = exterior_model(img_preprocessed)

    label = np.argmax(predictions, axis=1)[0]
    decoder = {0: 'Acceptable_image', 1: 'Not_acceptable_image'}
    decoded_label = decoder[label]
    return decoded_label



def color_classification(img_path):

    img = image.load_img(img_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_preprocessed = np.expand_dims(img_array, axis=0)

    predictions = color_model(img_preprocessed)

    label = np.argmax(predictions, axis=1)[0]
    decoder = {0:'Beige', 1:'Black', 2:'Blue', 3:'Brown', 4:'Gold', 5:'Gray', 6:'Green', 7:'Orange', 8:'Pink', 9:'Purple', 10:'Red', 11:'Silver', 12:'White', 13:'Yellow'}
    decoded_label = decoder[label]
    return decoded_label


def body_classification(img_path):

    img = image.load_img(img_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_preprocessed = np.expand_dims(img_array, axis=0)

    predictions = bodytype_model(img_preprocessed)

    label = np.argmax(predictions, axis=1)[0]
    decoder = {0:'Cargo Van', 1:'Convertible', 2:'Coupe', 3:'Crossover', 4:'Hatchback', 5:'Minivan', 26:'Pickup', 7:'Roadster', 8:'SUV', 9:'Sedan', 10:'Wagon'}
    decoded_label = decoder[label]
    return decoded_label


def make_classification(img_path):

    img = image.load_img(img_path, target_size=(220, 220))
    img_array = image.img_to_array(img)
    img_preprocessed = np.expand_dims(img_array, axis=0)

    predictions = car_make_clf(img_preprocessed)

    label = np.argmax(predictions, axis=1)[0]
    decoder = {0: 'Acura', 1: 'Alfa Romeo', 2: 'Aston Martin', 3: 'Audi',4: 'BMW', 5: 'Bentley', 6: 'Buick', 7: 'Cadillac', 8: 'Chevrolet',9: 'Chrysler', 10: 'Dodge', 11: 'FIAT', 12: 'Ferrari', 13: 'Ford',
               14: 'GENESIS', 15: 'GMC', 16: 'Honda', 17: 'Hummer', 18: 'Hyundai',19: 'INFINITI', 20: 'Isuzu', 21: 'Jaguar', 22: 'Jeep', 23: 'KARMA',24: 'Kia', 25: 'Lamborghini', 26: 'Land Rover', 27: 'Lexus', 28: 'Lincoln',
               29: 'Lotus', 30: 'MINI', 31: 'Maserati', 32: 'Maybach', 33: 'Mazda',34: 'McLaren', 35: 'Mercedes-Benz', 36: 'Mercury', 37: 'Mitsubishi',
               38: 'Nissan', 39: 'Oldsmobile', 40: 'Plymouth', 41: 'Pontiac',42: 'Porsche', 43: 'RAM', 44: 'Rolls-Royce', 45: 'Saab',
               46: 'Saturn', 47: 'Scion', 48: 'Subaru', 49: 'Suzuki', 50: 'Toyota',51: 'Volkswagen', 52: 'Volvo', 53: 'smart'}
    decoded_label = decoder[label]
    return decoded_label


## Regression model price prediction function
def car_price_predictor(make, model, trim, vehicle_type, body_type, drivetrain,fuel_type, engine_block, transmission, base_exterior_color, base_interior_color, state, miles, year, engine_size,
       cylinders, is_certified, carfax_1_owner, carfax_clean_title):
    
    
   
    prediction=prediction_model.predict(pd.DataFrame(
        
       columns=['make', 'model', 'trim', 'vehicle_type', 'body_type', 'drivetrain','fuel_type', 'engine_block', 'transmission', 'base_exterior_color', 'base_interior_color', 'state', 'miles', 'year', 'engine_size',
       'cylinders', 'is_certified', 'carfax_1_owner', 'carfax_clean_title'], 
       
       data = np.array([make, model, trim, vehicle_type, body_type, drivetrain,fuel_type, engine_block, transmission, base_exterior_color, base_interior_color, state, miles, year, engine_size,
       cylinders, is_certified, carfax_1_owner, carfax_clean_title]).reshape(1, 19)))
    print(prediction)
    return prediction




def main():
    #st.title("     AUTOMATES")
    html_temp = """
    <h1 style='text-align: center; color: black;'>AUTOMATES</h1>
    <div style="background-color:#FFCB05;padding:10px">
    <h2 style="color:#00274C;text-align:center;">Car Price Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #st.markdown("<h1 style='text-align: center; color: red;'>AUTOMATES</h1>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("Please upload an exterior image of your car")

            # text over upload button "Upload Image"
        if uploaded_file is not None:

            with open(uploaded_file.name,"wb") as f:
                f.write(uploaded_file.getbuffer())

            message = exterior_classification(uploaded_file.name)
            color_msg = color_classification(uploaded_file.name)
            make_msg = make_classification(uploaded_file.name)
            body_msg = body_classification(uploaded_file.name)
            # deleting uploaded saved picture after prediction
            os.remove(uploaded_file.name)
            # display message
            st.text(message)
            st.text(make_msg)
            st.text(body_msg)
            st.text(color_msg)

            if message is 'Not_acceptable_image':
                uploaded_file = st.text("Upload an exterior image of your car")

        make = st.selectbox("Make",car_make)

        # if make == 'No Selection':
        #     # make classifier from Cody will impute this information
        #     make = make_msg


        vehicle_type = st.selectbox("Vehicle Type",car_vehicletype[make])

        # if vehicle_type == 'No Selection':
        # #     # vehicle type classifier from Cody will impute this information
        #     vehicle_type = impute_vehicletype(lookup,make)

        model = st.selectbox("Model",car_model[make][vehicle_type])

        # if model == 'No Selection':
        # #     # function will make this imputation
        #     model = impute_model(lookup,make,vehicle_type)

        trim = st.selectbox("Trim",car_trim[make][vehicle_type][model])
        
        # if trim =='No Selection':
        #     trim = impute_trim(lookup,make,vehicle_type,model)



        body_type = st.selectbox("Body Type",car_bodytype[make][vehicle_type][model][trim])

        # if body_type == 'No Selection':
        #     body_type = body_msg
        #     #body_type = impute_bodytype(lookup,make,vehicle_type,model,trim)

        drivetrain = st.selectbox("Drive Type",car_drivetrain[make][vehicle_type][model][trim])

        # if drivetrain =='No Selection':
        #     drivetrain = impute_drivetrain(dataframe,make,vehicle_type,model,trim,body_type)

        fuel_type = st.selectbox("Fuel Type",car_fueltype[make][vehicle_type][model][trim])

        # if fuel_type =='No Selection':
        #     fuel_type = impute_fueltype(dataframe,make,vehicle_type,model,trim,body_type,drivetrain)

        engine_block = st.selectbox("Engine Type",car_engineblock[make][vehicle_type][model][trim])

        # if engine_block == 'No Selection':
        #     engine_block = impute_engineblock(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type)

        engine_size = st.selectbox("Engine Size",car_enginesize[make][vehicle_type][model][trim])

        # if engine_size == 'No Selection':
        #     engine_size = impute_enginesize(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block)
        
        cylinders = st.selectbox("Cylinders",car_cylinders[make][vehicle_type][model][trim])

        # if cylinders == 'No Selection':
        #     cylinders = impute_cylinders(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size)

    with col2:
        doors = st.selectbox("Doors",car_doors[make][vehicle_type][model][trim])

        # if doors =='No Selection':
        #     doors = impute_doors(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size,cylinders)

        
        transmission = st.selectbox("Transmission",car_transmission[make][vehicle_type][model][trim])

        # if transmission =='No Selection':
        #     impute_transmission(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size,cylinders,doors)
            
        base_exterior_color = st.selectbox("Exterior Color",exterior)

        # if base_exterior_color == 'No Selection':
        #     base_exterior_color = color_msg

        base_interior_color = st.selectbox("Interior Color",interior)

        state = st.selectbox("State",states)


#         miles_str = st.selectbox("Miles",("No selection","I want to enter milage of my car"))

#         if miles_str == "No selection":

#             miles_text = st.text("Please leave milage information 0")
#         else: 
#             miles_text = st.text("Please enter milage information")


        miles = st.number_input('Miles',min_value=0, step=1)

        year = st.selectbox("Year",car_year[make][vehicle_type][model][trim])


        is_certified = st.selectbox("Certified",("Yes","No"))

        if is_certified =="Yes":
            is_certified =1
        else:
            is_certified=0


        carfax_1_owner = st.selectbox("First owner",("Yes", "No"))

        if carfax_1_owner == "Yes":
            carfax_1_owner=1
        else:
            carfax_1_owner=0

        carfax_clean_title = st.selectbox("Clean Title",("Yes","No"))

        if carfax_clean_title =="Yes":
            carfax_clean_title=1
        else:
            carfax_clean_title=0
    
        # city_mpg = impute_city_mpg(lookup,year, make, model, trim, vehicle_type, body_type, drivetrain, fuel_type, engine_block, engine_size, transmission, doors, cylinders)
        #city_mpg = 32
        
        # highway_mpg = impute_highway_mpg(lookup,year, make, model, trim, vehicle_type, body_type, drivetrain, fuel_type, engine_block, engine_size, transmission, doors, cylinders)
        #highway_mpg = 43

        result = 0
        if st.button("Predict"):
            result=car_price_predictor(make, model, trim, vehicle_type, body_type, drivetrain,fuel_type, engine_block, transmission, base_exterior_color, base_interior_color, state, miles, year, engine_size,
       cylinders, is_certified, carfax_1_owner, carfax_clean_title)
        st.success('Estimated value of your car is {} USD'.format(result))


if __name__=='__main__':
    main()

