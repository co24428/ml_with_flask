# febric3을 이용하여 리눅스 서버에 자동 셋업
# 리눅스, git, 페브릭으로 작성된 스크립트
# 상용화시, 최초 셋업 및 업데이트 관리시 사용
#############################################
# 본 파일은 엔트리 파일이다 ( 수행 집입로 )
# apache 서버가 run.py를 바라보고 가동 및 연동
from service.start import app

# 상용화, 배포시에 사용하면됨 -> 개발시에는 start를 실행해도 됨.
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(debug=True)