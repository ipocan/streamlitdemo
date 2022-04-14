import numpy as np
import pickle
import pandas as pd
import streamlit as st 


from dropdict import *


# # regression model
file = open("predict_model.pkl", "rb")
prediction_model=pickle.load(file)

# regression model
# file = open("rf_regressor_vehicle_value_predictor.pkl","rb")
# prediction_model=pickle.load(file)




# lookup table
lookup = pd.read_csv("vin_lookup_year.csv")

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

