import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "🏠"
)

st.write('# Battery-Anomaly-Detection Web')

# st.sidebar.sucess("데이터 테스트를 시작하세요")

st.markdown(
    """
    데이터 테스트를 시작하세요!
    
    Test 페이지에서 데이터 업로드 후 분석 시작 버튼을 누르세요!
    
    분석이 완료되면 Result 페이지에서 확인 가능합니다.
    """
)
