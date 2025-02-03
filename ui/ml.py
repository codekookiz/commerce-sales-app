import streamlit as st, joblib, numpy as np


def run_ml() :
    st.subheader('')

    st.header('ML (머신러닝)')
    st.text('')

    st.info('기본 정보를 바탕으로 상품의 예상 판매량을 알려드립니다.')
    st.text('')

    st.subheader('판매량 예측을 위해 하단 정보를 입력해주세요.')
    st.text('')

    day = st.selectbox('요일을 선택하세요.', ['월', '화', '수', '목', '금', '토', '일'])
    holiday = st.selectbox('공휴일 여부를 알려주세요.', ['공휴일', '평일'])
    expense = st.number_input('마케팅 비용을 입력하세요. (만원)', min_value=0, value=50)
    competitor = st.number_input('경쟁 상품의 가격을 입력하세요.', min_value=0, value=20000)
    price = st.number_input('상품 가격을 입력하세요.', min_value=10, value=20000)
    month = st.number_input('현재 월을 입력하세요.', min_value=1, max_value=12)
    st.subheader('')

    new_day = 0
    if day == '월' :
        new_day = 0
    elif day == '화' :
        new_day = 1
    elif day == '수' :
        new_day = 2
    elif day == '목' :
        new_day = 3
    elif day == '금' :
        new_day = 4
    elif day == '토' :
        new_day = 5
    else :
        new_day = 6

    new_holiday = 0
    if holiday == '공휴일' :
        new_holiday = 1
    elif holiday == '평일' :
        new_holiday = 0

    new_data = np.array([new_day, new_holiday, expense, competitor, price, month]).reshape(1, 6)
    regressor = joblib.load('model/regressor.pkl')
    pred = int(regressor.predict(new_data)[0].round())

    if st.button('예측 판매량 확인') :
        if pred >= 0 :
            st.text('')
            pred = format(pred, ',')
            st.subheader(f'해당 상품의 예상 판매량은 {pred}개입니다.')
        else :
            st.subheader('예측이 불가능한 데이터입니다.')