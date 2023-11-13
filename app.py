import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('./model/best_xgboost_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the column names
columns = pd.read_csv('columns.csv')

def predict_house_price(data):
    # Preprocess the input data as needed for your regression model
    # Make sure the order of features matches the order used during training

    # Assuming 'District', 'Style', 'Extwall', 'Nr_of_rms', 'Bdrms', 'Fbath' are categorical features
    data['District'] = pd.Categorical(data['District'], categories=list(range(1, 15)))
    data['Style'] = pd.Categorical(data['Style'], categories=['AP 1', 'Rm or Rooming House', 'Mansion', 'Duplex O/S', 'Cape Cod',
       'Ranch', 'Cottage', 'Colonial', 'Duplex N/S', 'Residence O/S',
       'Milwaukee Bungalow', 'Dplx Bungalow', 'Townhouse', 'Triplex',
       'Tudor', 'Bi-Level', 'Split Level', 'Duplex-Cottage',
       'Multiple Residential Bldgs', 'Contemporary',
       'Residence O/S 2sty+', 'Tavern', 'Res O/S A & 1/2',
       'Store Bldg - Multi Story (Store & Apt, Store & Ofc',
       'Res O/S 1 Story', 'Office Building - Multi Story ( Ofc & Apt)',
       'Residence With Commercial Usage', 'Service Building',
       'Medical Clinic', 'Multi Story Warehouse', 'Condo Ranch',
       'Pole Building', 'Bowling Alley', 'Res O/S 2sty +',
       'AP1 (Conventional Apt with 4-6 Units)', 'Funeral Home',
       'Sit Down Restaurant'])
    data['Extwall'] = pd.Categorical(data['Extwall'], categories=['Frame', 'Stone', 'Brick', 'Aluminum / Vinyl', 'Stucco', 'Block',
       'Masonry / Frame', 'Prem Wood', 'Fiber-Cement',
       'Fiber Cement/Hardiplank', 'Aluminum/Vinyl', 'Asphalt/Other',
       'Masonry/Frame', 'Wood', 'Alum/Vynyl Siding', 'Concrete Block',
       'Other', 'Masonary Frame', 'Metal Siding', 'Precast Masonary'])
    data['Nr_of_rms'] = pd.Categorical(data['Nr_of_rms'], categories=list(range(0, 64)))
    data['Bdrms'] = pd.Categorical(data['Bdrms'], categories=list(range(0, 33)))
    data['Fbath'] = pd.Categorical(data['Fbath'], categories=list(range(0, 11)))

    # One-hot encode categorical columns for the test data
    data = pd.get_dummies(data, columns=['District', 'Style', 'Extwall', 'Nr_of_rms', 'Bdrms', 'Fbath'])

    # Ensure that the test data has the same columns as your training data
    data = data.reindex(columns=columns.columns, fill_value=False)

    # Make predictions
    prediction = model.predict(data)

    return prediction


st.title('Real Estate Price Prediction App')

# Load image from a file path or URL
image_path = "./image.png"  # Replace with the path to your image file or URL
st.image(image_path, use_column_width=True)

# Get user input
st.sidebar.header('Input Features')
district = st.sidebar.selectbox('District number of the property', range(1, 16))
style = st.sidebar.selectbox('Architectural Style', ['AP 1', 'Rm or Rooming House', 'Mansion', 'Duplex O/S', 'Cape Cod',
       'Ranch', 'Cottage', 'Colonial', 'Duplex N/S', 'Residence O/S',
       'Milwaukee Bungalow', 'Dplx Bungalow', 'Townhouse', 'Triplex',
       'Tudor', 'Bi-Level', 'Split Level', 'Duplex-Cottage',
       'Multiple Residential Bldgs', 'Contemporary',
       'Residence O/S 2sty+', 'Tavern', 'Res O/S A & 1/2',
       'Store Bldg - Multi Story (Store & Apt, Store & Ofc',
       'Res O/S 1 Story', 'Office Building - Multi Story ( Ofc & Apt)',
       'Residence With Commercial Usage', 'Service Building',
       'Medical Clinic', 'Multi Story Warehouse', 'Condo Ranch',
       'Pole Building', 'Bowling Alley', 'Res O/S 2sty +',
       'AP1 (Conventional Apt with 4-6 Units)', 'Funeral Home',
       'Sit Down Restaurant'])
extwall = st.sidebar.selectbox('Exterior wall material used', ['Frame', 'Stone', 'Brick', 'Aluminum / Vinyl', 'Stucco', 'Block',
       'Masonry / Frame', 'Prem Wood', 'Fiber-Cement',
       'Fiber Cement/Hardiplank', 'Aluminum/Vinyl', 'Asphalt/Other',
       'Masonry/Frame', 'Wood', 'Alum/Vynyl Siding', 'Concrete Block',
       'Other', 'Masonary Frame', 'Metal Siding', 'Precast Masonary'])
stories = st.sidebar.number_input('Number of Stories', min_value=1.0, max_value=4.0, value=1.0, step=0.5)
year_built = st.sidebar.number_input('Year Built', min_value=1835, max_value=2022, value=2000)
nr_of_rms = st.sidebar.selectbox('Number of Rooms', range(0,64))
fin_sqft = st.sidebar.number_input('Square Footage of Finished Space (ft²)', min_value=256, max_value=26930, value=2000)
bdrms = st.sidebar.selectbox('Bedrooms', range(0,33))
fbath = st.sidebar.selectbox('Full Bathrooms', range(0,11))
lotsize = st.sidebar.number_input('Size of the land (ft²)', min_value=0, max_value=219978, value=3500)
year_sold = st.sidebar.number_input('Year Sold', min_value=2002, max_value=2022, value=2002)

# Create a DataFrame from the user input
user_data = pd.DataFrame({
    'District': [district],
    'Style': [style],
    'Extwall': [extwall],
    'Stories': [stories],
    'Year_Built': [year_built],
    'Nr_of_rms': [nr_of_rms],
    'Fin_sqft': [fin_sqft],
    'Bdrms': [bdrms],
    'Fbath': [fbath],
    'Lotsize': [lotsize],
    'year_sold': [year_sold],
})

# Initialize prediction variable
prediction = None

# Add a "Predict" button
if st.button('Predict'):
    prediction = predict_house_price(user_data)

# Display the prediction
if prediction is not None:
    st.markdown(f"Predicted Real Estate Price")
    st.write(f"${prediction[0]:,.2f}")

