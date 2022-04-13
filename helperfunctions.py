def impute_vehicletype(dataframe,make):
    vehicletype = dataframe[dataframe['make']==make]['vehicle_type'].value_counts().index.tolist()[0]
    return vehicletype

def impute_model(dataframe,make,vehicle_type):
    model = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)]['model'].value_counts().index.tolist()[0]
    return model

def impute_trim(dataframe,make,vehicle_type,model):
    trim = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)]['trim'].value_counts().index.tolist()[0]
    return trim

def impute_bodytype(dataframe,make,vehicle_type,model,trim):
    bodytype = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&(dataframe['trim']==trim)]['body_type'].value_counts().index.tolist()[0]
    return bodytype

def impute_drivetrain(dataframe,make,vehicle_type,model,trim,body_type):
    drive_train = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&(dataframe['trim']==trim)&(dataframe['body_type']==body_type)]['drivetrain'].value_counts().index.tolist()[0]
    return drive_train

def impute_fueltype(dataframe,make,vehicle_type,model,trim,body_type,drivetrain):
    fueltype = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)]['fuel_type'].value_counts().index.tolist()[0]
    return fueltype

def impute_engineblock(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type):
    engineblock = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)&(dataframe['fuel_type']==fuel_type)]['engine_block'].value_counts().index.tolist()[0]
    return engineblock

def impute_enginesize(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block):
    enginesize = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)&(dataframe['fuel_type']==fuel_type)&(dataframe['engine_block']==engine_block)]['enginesize'].value_counts().index.tolist()[0]
    return enginesize

def impute_cylinders(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size):
    cylinders_n = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)&(dataframe['fuel_type']==fuel_type)&\
    (dataframe['engine_block']==engine_block) &(dataframe['engine_size']==engine_size)]['cylinders'].value_counts().index.tolist()[0]
    return cylinders_n

def impute_doors(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size,cylinders):
    doors_n = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)&(dataframe['fuel_type']==fuel_type)&\
    (dataframe['engine_block']==engine_block) &(dataframe['engine_size']==engine_size)&(dataframe['cylinders']==cylinders)]['doors'].value_counts().index.tolist()[0]
    return doors_n

def impute_transmission(dataframe,make,vehicle_type,model,trim,body_type,drivetrain,fuel_type,engine_block,engine_size,cylinders,doors):
    transmission_n = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type)&(dataframe['model']==model)&\
    (dataframe['trim']==trim)&(dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain)&(dataframe['fuel_type']==fuel_type)&\
    (dataframe['engine_block']==engine_block) &(dataframe['engine_size']==engine_size)&(dataframe['cylinders']==cylinders)&(dataframe['doors']==doors)]['transmission'].value_counts().index.tolist()[0]
    return transmission_n














def impute_city_mpg(dataframe,year, make, model, trim, vehicle_type, body_type, drivetrain, fuel_type, engine_block, engine_size, transmission, doors, cylinders):

    if make !='No Selection' and year !='No Selection' and model != 'No Selection' and trim != 'No Selection' and vehicle_type != 'No Selection' and body_type != 'No Selection' and drivetrain != 'No Selection' and fuel_type != 'No Selection' and engine_block != 'No Selection' and engine_size != 'No Selection' and transmission != 'No Selection' and doors != 'No Selection' and cylinders != 'No Selection':

      citympg = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type) &(dataframe['model']==model) & (dataframe['trim']==trim) & \
                    (dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain) & (dataframe['fuel_type']==fuel_type)&(dataframe['engine_block']==engine_block)&\
                    (dataframe['engine_size']==engine_size)&(dataframe['transmission']==transmission)&(dataframe['doors']==doors)&(dataframe['cylinders']==cylinders)&\
                    (dataframe['year']==year)]['city_mpg'].value_counts().index.tolist()[0]

      return citympg


def impute_highway_mpg(dataframe,year, make, model, trim, vehicle_type, body_type, drivetrain, fuel_type, engine_block, engine_size, transmission, doors, cylinders):
    if make !='No Selection' and year !='No Selection' and model != 'No Selection' and trim != 'No Selection' and vehicle_type != 'No Selection' and body_type != 'No Selection' and drivetrain != 'No Selection' and fuel_type != 'No Selection' and engine_block != 'No Selection' and engine_size != 'No Selection' and transmission != 'No Selection' and doors != 'No Selection' and cylinders != 'No Selection':

      highwaympg = dataframe[(dataframe['make']==make)&(dataframe['vehicle_type']==vehicle_type) &(dataframe['model']==model) & (dataframe['trim']==trim) & \
                    (dataframe['body_type']==body_type)&(dataframe['drivetrain']==drivetrain) & (dataframe['fuel_type']==fuel_type)&(dataframe['engine_block']==engine_block)&\
                    (dataframe['engine_size']==engine_size)&(dataframe['transmission']==transmission)&(dataframe['doors']==doors)&(dataframe['cylinders']==cylinders)&\
                    (dataframe['year']==year)]['highway_mpg'].value_counts().index.tolist()[0]

      return highwaympg




