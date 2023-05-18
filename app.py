# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:36:43 2022
@author: Student
""" 
import pickle   
import streamlit as st 
from streamlit_option_menu import option_menu
incomeprediction_model = pickle.load(open('IncomePrediction/saved_model/incomeprediction_model.sav','rb'))
with st.sidebar:
    selected = option_menu('HOME',
                           ['ABOUT PROJECT', 'INCOME PREDICTOR'],
                           icons = ['person-lines-fill','activity'],
                           default_index = 0)
if (selected == 'INCOME PREDICTOR'):
    st.title('INCOME PREDICTION USING MACHINE LEARNING')
    age = st.text_input('Enter Age: ')
    fnlwgt = st.text_input('Enter final weight: ')
    workclass = st.text_input('Enter working class [0-8]: ')
    education = st.text_input('Enter Education [0-16]: ')
    education_num = st.text_input("Enter number of years spent on Education: ")
    marital_status = st.text_input('Enter Marital status [0-6]: ')
    occupation = st.text_input('Enter Occupation [0-14]: ')
    relationship = st.text_input('Enter Relationship [0-5]: ')
    race = st.text_input('Enter Race [0-4]: ')
    sex = st.text_input('Enter Sex[0/1]: ')
    capital_gain = st.text_input('Enter Capital gain: ')
    capital_loss = st.text_input('Enter Capital loss: ')
    hours_per_week = st.text_input('Enter the number of hours of work per week: ')
    native_country = st.text_input('Enter the native country: ')
    income = ''
    if st.button('GET RESULT'):

        incomeprediction = incomeprediction_model.predict([[age, fnlwgt, workclass, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country]])
        if (incomeprediction[0] == 1):
            income = ('The Person earns >50K$ per year')
        else:
            income = ('The Person earns <=50K$ per year')
    st.success(income)
if (selected == 'ABOUT PROJECT'):
    st.title('DETAILS OF THE ATTRIBUTES')
    st.text('The attributes of the dataset are Age, Work Class, Final weight, Education, ')
    st.text('Education years, Marital status, Occupation, Relationship, Race, Sex,')
    st.text('Capital Gain, Capital Loss,Work hours per week, Native Country.')
    st.text('Age, final weight, education years, capital gain, capital loss, work hours per')
    st.text('week are numerical and others are categorical.')
    st.title('RANGE OF INPUT VALUES')
    st.text('Age: 10 - 90')
    st.text('Work Class [0 – 8]: 0-Unknown, 1-Federal-gov, 2-Local-gov, 3-Never-worked,')
    st.text('4–Private, 5-Self-emp-inc, 6-Self-emp-not-inc, 7-State-gov, 8-Without-pay')
    st.text('Final Weight: 12000 - 150000')
    st.text('Education [0 – 15]: 0-10th, 1-11th, 2-12th, 3-1st-4th, 4-5th-6th,')
    st.text('5-7th-8th, 6-9th, 7-Assoc-acdm, 8-Assoc-voc, 9–Bachelors, 10–Doctorate,')
    st.text('11-HS-grad, 12–Masters, 13–Preschool, 14-Prof-school, 15-Some-college')
    st.text('Marital_status [0 – 6]: 0–Divorced, 1-Married-AF-spouse, 2-Married-civ-spouse,')
    st.text('3-Married-spouse-absent, 4-Never-married, 5–Separated, 6-Widowed')
    st.text('Occupation [0 – 14]: 0–Unknown, 1-Adm-clerical, 2-Armed-Forces, 3-Craft-repair,')
    st.text('4-Exec-managerial, 5-Farming-fishing, 6-Handlers-cleaners, 7-Machine-op-inspct,')
    st.text('8-Other-service, 9-Priv-house-serv, 10-Prof-specialty, 11-Protective-serv,')
    st.text('12–Sales, 13-Tech-support, 14-Transport-moving')
    st.text('Relationship [0 – 5]: 0–Husband, 1-Not-in-family, 2-Other-relative, 3-Own-child,')
    st.text('4–Unmarried, 5 – Wife')
    st.text('Race [0 -4]: 0-Amer-Indian-Eskimo, 1-Asian-Pac-Islande, 2–Black, 3–Other, 4-White')
    st.text('Sex [0/1]: 0–Female, 1-Male')
    st.text('Capital gain: 0 - 100000 ')
    st.text('Capital loss: 0 - 4000')
    st.text('Work hours per week: 1 - 99')
    st.text('Native_country [0-41]: 0-Unknown, 1–Cambodia, 2–Canada, 3–China, 4–Columbia, 5–Cuba,')
    st.text('6–Dominican Republic, 7–Ecuador, 8-El-Salvador, 9–England, 10–France,  11–Germany,')
    st.text('12–Greece, 13–Guatemala, 14–Haiti, 15-Holand-Netherlands, 16–Honduras, 17-Hong Kong,')
    st.text('18–Hungary, 19–India, 20–Iran, 21–Ireland, 22–Italy, 23–Jamaica, 24–Japan, 25 – Laos,')
    st.text('26–Mexico, 27–Nicaragua, 28-Outlying-US(Guam-USVI-etc),  29–Peru, 30–Philippines,')
    st.text('31–Poland, 32–Portugal, 33-Puerto-Rico, 34–Scotland, 35-South Korea, 36–Taiwan,')
    st.text('37–Thailand, 38–Trinidad & Tobago, 39 - United-States, 40–Vietnam, 41-Yugoslavia')
