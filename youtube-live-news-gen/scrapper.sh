
#!/bin/bash

time_stamp=$(date +%Y-%m-%d)
BASE_DIR="F:/certifications/IIITH-AIML/research/imagen/banner/"
DIR="${BASE_DIR}${time_stamp}"

if [ ! -d "$DIR" ]; then
	mkdir -p "${DIR}"
	mkdir -p "${DIR}/dup"

	cd "${DIR}"

	shot-scraper multi ${BASE_DIR}indiatoday.yml --retina

	#shot-scraper multi ${BASE_DIR}test.yml --retina
	#shot-scraper https://www.indiatoday.in/news.html -o indiatoday.jpeg

	python ../color-change.py
	python ../img-to-text-to-speach.py
	python ../convert-imgs2video.py
	python ../youtube/upload_video2youtube.py
fi
