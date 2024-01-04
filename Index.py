from flask import Flask, request, render_template
import pandas
import IndexController
import IndexFacade
from flask import Flask, send_from_directory
#py -m flask --app .\index.py run
app = Flask(__name__)

@app.route('/generate-pdf')
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    data = request.json
    lorem = data.get('lorem', [])
    initialData = IndexController.submitController(data)
    finalDataFrame = IndexFacade.dataPreparation(IndexController.submitController(data))
    IndexFacade.createPlots(finalDataFrame)
    IndexFacade.createPdf(initialData, finalDataFrame)
    return "Your download will complete in a few seconds, please click OK"

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    directory = 'reports'  
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)