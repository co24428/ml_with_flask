from sklearn.externals import joblib
import json
import re
# 언어감지 예측 모델 기능으로 학습된 알고리즘을 로드
# 요청이 들어올 때마다 예측하고 결과를 던져준다
# 경로 (entry + 프로젝트 위치까지 고려 기준으로 경로 설정) 
model_path = './service/ml/clf_model_202003101113.model'
label_path = './service/ml/clf_labels.json'
# 분류기(알고리즘)
clf = joblib.load( model_path )
# 레이블(정답)
with open(label_path, 'r') as f:
    clf_label = json.load(f)

# 실제 필요한 부분
def detect_lang( oriTxt ):
    # 1. 데이터 가공
    p = re.compile('[^a-zA-Z]*')
    text = p.sub('', oriTxt.strip().lower() )

    counts = [ 0 for i in range(26) ]
    ASCII_a = ord('a')
    for i in text:
        counts[ord(i) - ASCII_a] += 1

    frequence = list(map(lambda x: x/len(text), counts))
    frequences = [frequence]
    # 2. 예측
    predict = clf.predict( frequences )

    # 3. 출력결과 구성
    return predict[0], clf_label[predict[0]]