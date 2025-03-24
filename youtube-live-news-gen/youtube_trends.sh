
#!/bin/bash

time_stamp=$(date +%Y-%m-%d)
BASE_DIR="F:/certifications/IIITH-AIML/research/imagen/banner/"
DIR="${BASE_DIR}${time_stamp}"

if [ ! -d "$DIR" ]; then
  mkdir -p "${DIR}"
fi

#if [ -d "$DIR" ]; then
	mkdir -p "${DIR}/youtube_trends"
	mkdir -p "${DIR}/youtube_trends/original"
	mkdir -p "${DIR}/youtube_trends/croped"

	cd "${DIR}/youtube_trends/original"
	
	shot-scraper multi ${BASE_DIR}youtube_trends.yml --retina

	python ${BASE_DIR}youtube_trends.py
#fi
