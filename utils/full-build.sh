#!/bin/zsh


date=$(date +'%m-%d-%Y')
filename="calendar-y3-sjb786-${date}.ical"
touch ${filename}
bhamcal sjb786 -o ${filename} --password "${UNI_PASSWORD}"
gsutil -h "Cache-Control:no-cache, max-age=0" cp -a public-read ${filename} gs://sjb786-cal-bucket
cp ${filename} ~/Documents
