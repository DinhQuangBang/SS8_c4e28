from flask import Flask, render_template
app = Flask(__name__)


@app.route('/c4e')
def c4e():
    return render_template('c4e.html')

if __name__ == '__main__':
  app.run (debug=True)
 