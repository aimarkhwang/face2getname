from flask import Flask, render_template, request
import nvapi

app =  Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/kb')
def kb():
    return "kbaseball"

@app.route('/face', methods=['GET', 'POST'])
def face():
    if request.method == 'GET':
        return render_template('face.html')
    else:
        imgurl = request.form['imgurl']
        # 여기에  face(imgurl)함수를 넣으면 결과를 리턴해서 받아서
        name = nvapi.face2getname(imgurl)
        # 결과를 여기에 출력해보기
        print(name)
        return '''
            <h1>{0}</h1>
            <img src='{1}'>
        '''.format(name, imgurl)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# dd = {'a': 1, 'd': '아이유'}
# print(dd['a'])