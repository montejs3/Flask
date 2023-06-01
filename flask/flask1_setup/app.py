from flask import Flask, render_template , url_for , request , redirect
app = Flask(__name__)




@app.route('/')
def nurse():
    
    return render_template('login.html')

@app.route('/report', methods=['POST', 'GET'])
def report():
    if request.method == 'POST':
        report = request.form
        print("report add to DB")
        
        return render_template('report.html', report= report)
    


if __name__ == '__main__':
    app.run()