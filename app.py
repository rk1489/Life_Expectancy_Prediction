import streamlit as st
import pickle
import numpy as np

# Loading the Pickel Model
model = pickle.load(open(r"life_expectancy.pkl", "rb"))


def predict_life_expectancy(features):

    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = model.predict(features)

    return prediction


def main():

    html_temp = """
        <div style = "background-color:tomato; padding: 10px;">
            <center><h1>Life Expectancy Predictor ML App</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    development_status = ["Developing", "Developed"]
    country_name = ['Afghanistan', 'Albania', 'Algeria', 'Angola',
       'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
       'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
       'Bolivia (Plurinational State of)', 'Bosnia and Herzegovina',
       'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria',
       'Burkina Faso', 'Burundi', "Côte d'Ivoire", 'Cabo Verde',
       'Cambodia', 'Cameroon', 'Canada', 'Central African Republic',
       'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
       'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
       'Czechia', "Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
       'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
       'Hungary', 'Iceland', 'India', 'Indonesia',
       'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
       'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic",
       'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania',
       'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
       'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
       'Mexico', 'Micronesia (Federated States of)', 'Monaco', 'Mongolia',
       'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
       'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
       'Niger', 'Nigeria', 'Niue', 'Norway', 'Oman', 'Pakistan', 'Palau',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
       'Poland', 'Portugal', 'Qatar', 'Republic of Korea',
       'Republic of Moldova', 'Romania', 'Russian Federation', 'Rwanda',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan',
       'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden',
       'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand',
       'The former Yugoslav republic of Macedonia', 'Timor-Leste', 'Togo',
       'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
       'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
       'United Arab Emirates',
       'United Kingdom of Great Britain and Northern Ireland',
       'United Republic of Tanzania', 'United States of America',
       'Uruguay', 'Uzbekistan', 'Vanuatu',
       'Venezuela (Bolivarian Republic of)', 'Vietnam', 'Yemen',
       'Zambia', 'Zimbabwe']
    

    Country = country_name.index(st.selectbox(
        "Country",
        tuple(country_name)
    )) + 1
    
    Developed = development_status.index(st.selectbox(
        "Development Status",
        tuple(development_status)
    ))
    
    Year = st.text_input("Year")

    Adult_Mortality = st.text_input("Adult Mortality Rate ('Deaths per 1000 b/w 15-60 years')") 
     
    infant_deaths = st.text_input("Infant Death Rate ('Infant deaths per 1000 live births')")
    Alcohol = st.text_input("Alcohol Consumption (in litres/person)")
    percentage_expenditure = st.text_input("Percentage Expenditure (in USD/person on living)")
    Hepatitis_B = st.text_input("Hepatitis B ('Deaths per month')")
    Measles = st.text_input("Measles ('Deaths per month')")
    BMI = st.text_input("Body Mass Index - BMI (in kg/sq.m)")

    under_five_deaths = st.text_input("Under-Five Deaths ('Deaths per 1000')")
    Polio = st.text_input("Polio ('Deaths per month')")
    Total_expenditure = st.text_input("Total Expenditure ('GDP % on health sector')")
    Diphtheria = st.text_input("Diphtheria ('Deaths per month')")
    HIV_AIDS = st.text_input("HIV/AIDS ('Deaths per month')")
    GDP = st.text_input("GDP ( in billion USD )")
    Population = st.text_input("Population (in exact figures for e.g. 33736494)")
    thin_19 = st.text_input("Thinness 1-19 Years ('%age thin out of total 1-19 years')")
    thin_9 = st.text_input("Thinness 5-9 Years ('%age thin out of total 5-9 years')")
    Income_composition = st.text_input("Income Composition of Resources (on scale of 1)")
    Schooling = st.text_input("Schooling (on scale of 100)")

    if st.button("Predict"):
        
        features = [Country, Year, Adult_Mortality, infant_deaths, Alcohol, percentage_expenditure, Hepatitis_B, Measles, BMI, under_five_deaths, Polio, Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population, thin_19, thin_9, Income_composition, Schooling, Developed]
        prediction = predict_life_expectancy(features)
        st.success("The Life Expectancy is predicted to be {} years.".format(round(prediction[0],2)))

    if st.button("About"):
        st.text("Predicts the Life Expectancy on the basis of various health-related factors.")
        st.text("Built by Raushan")
        
if __name__ == '__main__':
    main()
