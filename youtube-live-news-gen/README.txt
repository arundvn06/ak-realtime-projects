NEWS APIs:
==========

To create a today's top news headlines vedio and upload it to youtube:
	cd <basepath>\youtube-live-news-gen
	./scrapper.sh

	Newsapi.org:
		https://newsapi.org/register/success
		api key:	ak100akd02b763a61114ceb9ddb24b2e49deb17
		uname: arundvn06@gmail.com
		pwd: ******
		Comments: results are not accurate. giving empty results for basic questions
		
		python examples: https://newsapi.org/docs/client-libraries/python
		
		https://newsapi.org/v2/everything?q=india&from=2024-08-16&to=2024-08-16&sortBy=popularity&apiKey=<REPLACE_ME>
		
		curl --request GET \
		--url 'https://newsapi.org/v2/everything?q=india&from=2024-08-16&to=2024-08-16&sortBy=popularity' \
		--header 'x-api-key: <REPLACE_ME>
'
		
		!wget --header='x-api-key: d02b763a61114ceb9ddb24b2e49deb17' https://newsapi.org/v2/everything?q='rain in hyderabad'&from=2024-08-16&to=2024-08-16&sortBy=popularity -O index.json
	
	mediastack:
		url:	https://mediastack.com/dashboard
		apikey: ak100ak6730b9b71a6082754d24e300cd1ec1a6
		uname: arundvn06@gmail.com
		pwd: ******
		comments: parsing is not good. converting to utf-8 then it's becoming a string,, traversing is difficult.
	
To publish our own APIs:
	https://rapidapi.com/products/api-hub/


Extract news through news APIs:
	SerpAPI:	google's news API
		https://serpapi.com/dashboard
		private api key:	ak100akd1ddc1303a097bb484d60afa6778b5f1fb965ce7f0b78e7037ccce56122c112cak100ak
		
		python library for serpAPI:	https://pypi.org/project/google-search-results/
		examples repo:	https://github.com/serpapi/google-search-results-python/blob/master/serpapi/serp_api_client.py
						
		https://huggingface.co/black-forest-labs/FLUX.1-dev?text=a+crzy+fox+jumps+over+the+lazy+dog - look for quantized model
		
	News API:
		https://newsapi.org/	
			- giving images 
			- 100 requests per day
			- free for development
			- 
		https://newsdata.io/breaking-news-api
		https://open-platform.theguardian.com/explore/
			- local news

Translate text:(English-to-Telegu)
	https://pypi.org/project/translate/
	https://medium.com/@pythonprogrammers/language-translator-in-python-b3362e1ae9c0
	Translator app	- https://www.geeksforgeeks.org/language-translator-using-google-api-in-python/

text-to-speech:
	speecht5_tts - Microsoft's model
		https://huggingface.co/microsoft/speecht5_tts
		https://huggingface.co/blog/speecht5

Create images from news text:
	Stable diffusion
		https://pjoshi15.com/video-inside-text/
		tiny-sD:	https://huggingface.co/segmind/tiny-sd
	
	wordcloud:
		https://medium.com/@m3redithw/wordclouds-with-python-c287887acc8b
		https://colab.research.google.com/drive/12hJVuOrbrr73ABTpUJONdWPM-NBCZuPI#scrollTo=RoF1-Bgp2TXz
		
	
	Image generation APIs:
		https://deepai.org/pricing		- 5$ / month
			apikey: 2d308646-e54b-4eee-a239-03709b1e4e0e
			
			curl \
			-F 'text=A deep blue eyed baffalo flying on the red sky' \
			-H 'api-key:2d308646-e54b-4eee-a239-03709b1e4e0e' \
			https://api.deepai.org/api/text2img 
	
	Banner generator:
		https://apitemplate.io/image-generation-api/
			url:	https://app.apitemplate.io/manage-api/
			apikey:	ak100ak4d40MjEzODM6MTg0OTg6RTgxUTdXZHJSaTdwcXZVTg=
			edit template: https://app.apitemplate.io/manage-templates/
	
	screen shot creater:
		https://pypi.org/project/shot-scraper/0.11/
		https://shot-scraper.datasette.io/_/downloads/en/latest/pdf/
		pip install shot-scraper
		shot-scraper install -b firefox
		shot-scraper https://datasette.io/
		shot-scraper https://datasette.io/ -o datasette.png
		shot-scraper https://datasette.io/ -o - > datasette.png
		shot-scraper https://datasette.io/ -o small.png --width 400 --height 800
		
		
		
		Screenshotting a specific area with CSS selectors
			To take a screenshot of a specific element on the page, use --selector or -s with its CSS selector:
			shot-scraper https://simonwillison.net/ -s '#bighead'
			shot-scraper https://simonwillison.net/ -s '#bighead' -s .overband -o bighead-multi-selector.png
			"api_key": "ak100akd1ddc1303a097bb484d60afa6778b5f1fb965ce7f0b78e7037ccce56122c112c"
			shot-scraper https://serpapi.com/search.xxxxx -a auth.json -o authed.png
			
		https://www.indiatoday.in/news.html
		https://www.hindustantimes.com/
		https://timesofindia.indiatimes.com/india
		https://www.thehindu.com/news/national/
		shot-scraper https://www.indiatoday.in/news.html -s .lhs__section -o indiatoday.jpeg
		shot-scraper multi indiatoday.yml --retina


	resize/color change image:
		cartoonify-image-using-opencv-and-python:	https://www.analyticsvidhya.com/blog/2022/06/cartoonify-image-using-opencv-and-python/
		with PIL:(using this cuurently)	https://www.geeksforgeeks.org/python-pillow-colors-on-an-image/

text to video:
	https://medium.com/@kamaljp/text-to-video-pipeline-python-automation-using-open-ai-models-f4341555c8d9
	
How to upload a video to youtube:
	youtube APIs:
		https://developers.google.com/youtube/v3/docs/
		https://developers.google.com/youtube/v3/getting-started
		https://cloud.google.com/docs/authentication/api-keys#python
		API key / client json generation:
			https://console.cloud.google.com/apis/api/youtube.googleapis.com/metrics?project=neon-equinox-434211-e2&supportedpurview=project

		client id:	818147729494-su0k6289iktrlolh7hcl9nhd28c0j22i.apps.googleusercontent.com
		DrylanD project:
		client id: 878510434818-ed5k77vn4deochqn4n7550qoeqn3lt97.apps.googleusercontent.com
		
	To resolve video publishing to default account: 
		https://stackoverflow.com/questions/41016537/youtube-apis-access-mutiple-youtube-channels-brand-accounts-using-google-adm	
	
	Created youtube thumbnails with canva: https://www.canva.com/design/DAGQRnMRgUM/R_e9971toN4SSCimhLfZRA/edit
		
	Black and white AI:
		drylandenterprises@gmail.com
		client id: 712060138904-5be99fj2pogtseo9bls4tmng37nlp6n2.apps.googleusercontent.com
	
	python libs:
		python-youtube:	https://pypi.org/project/python-youtube/
		simple-youtube-api:	
			How to create youtube developer credentials and run sample app:	
				https://pypi.org/project/simple-youtube-api/
				https://larachamp.com/upload-videos-to-youtube-using-pythonv3-library/
	local files:	F:\certifications\IIITH-AIML\research\youtube
	colab:	https://colab.research.google.com/drive/12hJVuOrbrr73ABTpUJONdWPM-NBCZuPI#scrollTo=3hqjK28nXAcr	



image-to-text:
	tesseract
		https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows
		https://github.com/UB-Mannheim/tesseract/wiki

text-to-speach:
	https://www.geeksforgeeks.org/convert-text-speech-python/
