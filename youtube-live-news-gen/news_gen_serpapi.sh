
#!/bin/bash

time_stamp=$(date +%Y-%m-%d)
BASE_DIR="F:/certifications/IIITH-AIML/research/imagen/banner/"
DIR="${BASE_DIR}${time_stamp}"

if [ ! -d "$DIR" ]; then
  mkdir -p "${DIR}"
fi

if [ -d "$DIR" ]; then
	#mkdir -p "${DIR}/wtrends"
	mkdir -p "${DIR}/wheadlines"
	mkdir -p "${DIR}/wheadlines/img"

	cd "${DIR}"

	python ../news_gen.py
fi
