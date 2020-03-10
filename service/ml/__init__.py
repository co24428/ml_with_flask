from sklearn.externals import joblib
import json
# 언어감지 예측 모델 기능으로 학습된 알고리즘을 로드
# 요청이 들어올 때마다 예측하고 결과를 던져준다
# 경로 (entry + 프로젝트 위치까지 고려 기준으로 경로 설정) 
model_path = './service/ml/clf_model_202003101113.model'
label_path = './service/ml/clf_labels.json'
# 분류기(알고리즘)
clf = joblib.load( model_path )
with open(label_path, 'r') as f:
    clf_label = json.load(f)

def detect_lang( oriTxt ):
    return 'en', '영어'