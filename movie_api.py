from flask import Flask,jsonify,request
from Business.api_operations.api_manager import ApiManager

app = app = Flask(__name__)
api_manager = ApiManager()

@app.route('/')
def home():
    return "home"

@app.route('/update')
@app.route('/update/<int:page_count>')
def update(page_count=1):
    result = api_manager.update_system(page_count)
    return jsonify(result)

@app.route('/get_all')
def get_all():
    result = api_manager.get_all_movie()
    return jsonify(result)

@app.route('/get_between_indexes',methods=["POST"])
def get_between_indexes():
    begin_index = request.json.get("begin_index",0)
    end_index = request.json.get("end_index",10)
    result = api_manager.get_between_indexes_movie(begin_index,end_index)
    return jsonify(result)

@app.route('/get_by_language')
@app.route('/get_by_language/<int:language_id>')
def get_by_language(language_id=2):
    result = api_manager.get_by_language_movie(language_id)
    return jsonify(result)

@app.route('/get_by_category')
@app.route('/get_by_category/<int:category_id>')
def get_by_category(category_id=1):
    result = api_manager.get_by_category_movie(category_id)
    return jsonify(result)

@app.route('/get_by_imdb')
@app.route('/get_by_imdb/<float:imdb>')
def get_by_imdb(imdb=1):
    result = api_manager.get_by_imdb_movie(imdb)
    return jsonify(result)

@app.route('/get_by_year')
@app.route('/get_by_year/<int:year>')
def get_by_year(year=1000):
    result = api_manager.get_by_year_movie(year)
    return jsonify(result)
        
@app.route('/get_by_name')
@app.route('/get_by_name/<string:name>')
def get_by_name(name=""):
    result = api_manager.get_by_name_movie(name)
    return jsonify(result)

@app.route('/get_by_id')
@app.route('/get_by_id/<int:id>')
def get_by_id(id=1):
    result = api_manager.get_by_id_movie(id)
    return jsonify(result)

#region admin
@app.route('/admin',methods=["POST"])
def admin():
    sql_code = request.json.get("code",None)
    result = api_manager.get_by_custom_code(sql_code)
    return jsonify(result)
#endregion

if __name__ == '__main__':
    #from Business.api_operations.api_helper import ApiHelper
    #ApiHelper.api_configure()
    app.run()
