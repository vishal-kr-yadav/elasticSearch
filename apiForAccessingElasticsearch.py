from flask import Flask
from converterFromUnicode import convert
from connection import executeQuery
from connection import createDocument
from converterFromUnicode import convert
app=Flask(__name__)

@app.route('/GET/Review/By/keywords/<keywords>', methods=['GET'])
def getReviewByKeywords(keywords):

    body = {"query": {"match": {'Review15': keywords}}}

    ok=convert(body)
    return executeQuery(ok)

@app.route('/PUT/Review/iphoneX/From/Amazon/<count>', methods=['GET'])
def putReviewforIphoneX(count):
    item=convert(count)
    intItem=int(item)
    print("=======item",item)

    return "Created"



if __name__ == '__main__':
    app.run(debug=True)
