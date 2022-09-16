from flask import request, Blueprint

import src.word2vec_service as word2vec_service


app = Blueprint('app', __name__, url_prefix='/')


@app.route('/api/keyword/relation/mention')
def get_news_sims():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return "No parameter"

    for key in parameter_dict.keys():
        return word2vec_service.get_news_sims_keyword(request.args[key])


@app.route('/api/keyword/relation/search')
def get_search_log_sims():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return "No parameter"

    for key in parameter_dict.keys():
        return word2vec_service.get_search_log_sims_keyword(request.args[key])
