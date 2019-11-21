from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html',name = name)

@app.route('/user/<username>')
def show_user_name(username):
    return 'Username %s' % username

@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'post %d' % post_id



''' for_url 测试  '''
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('show_user_name',username = 'sadf'))


if __name__ == '__main__':
    app.run()
