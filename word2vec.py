from gensim.models.word2vec import Word2Vec


def get_news_sims_keyword(keyword):
    model = Word2Vec.load('word2vec.model')

    sims_dict = []

    try:
        sims = model.wv.most_similar(keyword, topn=15)  # get other similar words
    except KeyError:
        sims_dict.append({
            'code': "400",
            'msg': "검색 결과가 없습니다."
        })
        return sims_dict

    for sims_keyword in sims:
        related_keyword = sims_keyword[0]
        similarity = sims_keyword[1]
        sims_dict.append({
            'related_keyword':related_keyword,
            'similarity':similarity
        })

    return sims_dict


def get_search_log_sims_keyword(keyword):
    model = Word2Vec.load('word2vec_2.model')

    sims_dict = []

    try:
        sims = model.wv.most_similar(keyword, topn=15)  # get other similar words
    except KeyError:
        sims_dict.append({
            'code':"400",
            'msg':"검색 결과가 없습니다."
        })
        return sims_dict

    for sims_keyword in sims:
        related_keyword = sims_keyword[0]
        similarity = sims_keyword[1]
        sims_dict.append({
            'related_keyword': related_keyword,
            'similarity': similarity
        })

    return sims_dict
