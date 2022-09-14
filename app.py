from flask import Flask, request
import word2vec

app = Flask(__name__)


@app.route('/api/keyword/relation/mention')
def get_news_sims():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return "No parameter"


    for key in parameter_dict.keys():
        return word2vec.get_news_sims_keyword(request.args[key])

@app.route('/api/keyword/relation/search')
def get_search_log_sims():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return "No parameter"


    for key in parameter_dict.keys():
        return word2vec.get_search_log_sims_keyword(request.args[key])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
