import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 사이드바 설정
st.sidebar.header('사이드바 헤더')  # 사이드바의 헤더 설정
number = st.sidebar.slider("사이드바 슬라이더", 0, 100)  # 슬라이더 위젯 생성
wid = 500  # 너비 설정

# 계절 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(['봄', '여름', '가을', '겨울'])  # 계절별 탭 생성
tab1.info("봄이에요!")  # 봄 탭 정보
tab2.info("여름이에요!")  # 여름 탭 정보
tab3.info("가을이에요!")  # 가을 탭 정보
tab4.info("겨울이에요!")  # 겨울 탭 정보

# 세션 상태에 이름이 없으면 기본값 설정
if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

# 제목 설정
st.title("Interactive widget")  # 앱 제목
st.divider()  # 구분선 추가

# 텍스트 입력 위젯
name = st.text_input(label="이름을 적어주세요!:D")  # 사용자 이름 입력
if name:  # 이름이 입력되면
    st.write(f"{name}님 안녕하세요!")  # 인사 메시지 출력

# 로그인 위젯
my_id = 'zzolab'  # 고정된 ID
my_passwd = '220518'  # 고정된 비밀번호
input_id = st.text_input("ID:(hint:쪼랩은 영어로?)")  # ID 입력
input_passwd = st.text_input("PW:(hint:쪼랩의 생일은? ex. 240815)", type="password")  # 비밀번호 입력
if my_id == input_id and my_passwd == input_passwd:  # ID와 비밀번호가 일치하면
    st.success("로그인에 성공했습니다.")  # 성공 메시지

    # 소수 판별기 기능 구현
    def is_prime(num):
        """주어진 수가 소수인지 판별하는 함수"""
        if num <= 1:  # 1 이하의 수는 소수가 아님
            return False
        for i in range(2, int(num**0.5) + 1):  # 2부터 num의 제곱근까지 반복
            if num % i == 0:  # 나누어 떨어지면 소수가 아님
                return False
        return True  # 소수일 경우 True 반환

    # 소수 판별기 제목 설정
    st.title("소수 판별기")  # 소수 판별기 제목

    # 사용자로부터 자연수 입력 받기
    num = st.number_input("자연수를 입력하세요", min_value=1, value=1, step=1)  # 자연수 입력

    # 버튼을 누르면 소수 판별 결과 출력
    if st.button("소수 판별"):  # 버튼 클릭 시
        if is_prime(num):  # 입력한 수가 소수인지 판별
            st.success(f"{num}은(는) 소수입니다!")  # 소수일 경우 성공 메시지
        else:
            st.warning(f"{num}은(는) 소수가 아닙니다.")  # 소수가 아닐 경우 경고 메시지

    # 요일 확인 미니 프로젝트
    input_date = st.date_input("요일을 찾고 싶은 날짜를 입력해주세요.")  # 날짜 입력 위젯
    if input_date:  # 날짜가 입력되면
        try:
            day_of_week = input_date.strftime("%A")  # %A는 요일을 풀네임으로 표시
            요일_한글 = input_date.strftime("%A")  # 요일을 한글로 변환
            요일_변환 = {
                "Monday": "월요일",
                "Tuesday": "화요일",
                "Wednesday": "수요일",
                "Thursday": "목요일",
                "Friday": "금요일",
                "Saturday": "토요일",
                "Sunday": "일요일"
            }
            st.write(f"{input_date.strftime('%Y%m%d')}의 요일은 {요일_변환[요일_한글]}입니다.")  # 요일 출력
        except ValueError:
            st.error("올바른 날짜 형식을 입력해주세요. (예: 2023-12-12)")  # 오류 메시지

    # 버튼 위젯
    if st.button("버튼을 누르면 뭐가 나올까요??", type='primary'):  # 버튼 클릭 시
        st.write("# 😍")  # 이모지 출력
        random_time = datetime.today().strftime('%s')
        if int(random_time)%2 :
            st.balloons()
        else:
            st.snow()  # 풍선 애니메이션
    else:
        st.write("# 🙄")  # 이모지 출력


    # 체크박스
    if st.checkbox("텍스트를 보여줄까요?"):  # 체크박스 선택 시
        st.write("체크박스가 선택되었습니다!")  # 메시지 출력

    # 라디오 버튼
    radio_option = st.radio("당신의 선택은?", ["A", "B", "C"])  # 라디오 버튼 생성
    st.write(f"당신은 {radio_option}을(를) 선택하셨습니다.")  # 선택한 옵션 출력

    # 멀티선택
    color = st.color_picker("원하는 색상을 선택하세요:", "#00f900")  # 색상 선택기 추가
    st.markdown(f"# <span style='color:{color};'>예쁜 색을 고르셨군요!</span>", unsafe_allow_html=True)  # 선택한 색상 출력

    # 프로그레스 바
    my_bar = st.progress(0)  # 프로그레스 바 초기화
    for percent_complete in range(100):  # 0부터 99까지 반복
        time.sleep(0.01)  # 0.01초 대기
        my_bar.progress(percent_complete + 1)  # 프로그레스 바 업데이트

else:
    st.warning('아이디 또는 비밀번호가 일치하지 않아요.')  # 경고 메시지
