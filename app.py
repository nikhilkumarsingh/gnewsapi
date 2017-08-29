import json
from flask import Flask, request
from gnewsclient import gnewsclient
from fuzzywuzzy import process

app = Flask(__name__)

gnews = gnewsclient()


@app.route('/', methods=['GET'])
def get_news():
	print(request.args)
	if request.args.get('news'):
		gnews.topic = process.extractOne(request.args['news'], gnews.topics)[0]

	if request.args.get('geo-country'):
		gnews.edition = process.extractOne(request.args['geo-country'], gnews.editions)[0]

	if request.args.get('language'):
		gnews.language = process.extractOne(request.args['language'], gnews.languages)[0]

	news = gnews.get_news()

	return json.dumps(news), 200



if __name__ == "__main__":
	app.run(debug=True, port=8000)