from flask import Flask, render_template, request, url_for, redirect
import nvapi
import dbdb

app =  Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('face')) # face로 리다이렉트
    # return "hello world"

@app.route('/kb')
def kb():
    return "kbaseball"

@app.route('/face', methods=['GET', 'POST'])
def face():
    if request.method == 'GET':
        return render_template('face.html')
    else:
        imgurl = request.form['imgurl']

        # pythonanywhere 에서 네이버클라우드 플랫폼이 작동이 안되서 데이터 저장으로 변경
        dbdb.insert_data(imgurl)
        # 데이터 출력
        data = dbdb.select_all()
        return render_template('result.html', data=data)

        # 이 이후에 작업은 matplotlib 를 이용하면 검색어 카운터를 해서 
        # 그래프를 출력해 분석까지 해보면 좋겠습니다.

        # 여기에  face(imgurl)함수를 넣으면 결과를 리턴해서 받아서
        #name = nvapi.face2getname(imgurl)
        # 결과를 여기에 출력해보기
        #print(name)
        # return '''
        #     <h1>{0}</h1>
        #     <img src='{1}'>
        # '''.format(name, imgurl)

# pythonaywhere 사이트에 올리기 위해 변경
if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run(host='0.0.0.0', port=80, debug=True)

# dd = {'a': 1, 'd': '아이유'}
# print(dd['a'])