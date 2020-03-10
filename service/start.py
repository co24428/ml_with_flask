# flask 기본 구성
# 1. 모듈 가져오기
from flask import Flask, render_template, request
from ml import detect_lang
# 2. flask 객체 생성
app = Flask(__name__)
# 3. 라우팅
@app.route('/')
def home():
    return 'Hello flask'
# 3-1. 언어감지 처리
# 405 error => 기본적으로 GET방식이 됨 > POST도 지원하게끔 바꿔줘라
# 1개 url로 여러 메소드를 지원 => restful
@app.route('/langTypeDetect', methods = ['GET', 'POST'])
def langTypeDetect():
    if request.method == 'POST':
        # 1. 원문 데이터 획득 (get, post 방식으로 전달된 데이터 획득)
        oriTxt = request.form.get('ori') # 500 error, Intenal server error 
        #                                  => 그래서! .get 함수를 통해 잘못되도 None을 리턴하도록..!
        # 위에 대한 방어코드
        if not oriTxt: 
            return {'code':0, 'lang':'', 'desc':'원문데이터 누락'}
        # 2. 언어감지
        lang, desc = detect_lang( oriTxt )
        # 2-1. 디비에 로그처리
        # 3. 응답
        return {'code':1, 'lang':lang, 'desc':desc}
    else: # GET
        return render_template('index.html')

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)