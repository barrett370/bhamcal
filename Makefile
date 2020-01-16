
.PHONY calendar:
calendar:
	bhamcal sjb786 -o calendar-y3-sjb786.ical --password "${UNI_PASSWORD}"
	gsutil -h "Cache-Control:no-cache, max-age=0" cp -a public-read calendar-y3-sjb786.ical gs://sjb786-cal-bucket
	cp calendar-y3-sjb786.ical ~/Documents

.PHONY diff:
diff: 
	bhamcal sjb786 -o calendar-y3-sjb786_tmp.ical --password ${UNI_PASSWORD}
	if [[ $(diff calendar-y3-sjb786_tmp.ical calendar-y3-sjb768.ical) ]]; then  echo "Calendar has changed"; else  echo "Calendar up to date"; fi
	rm calendar-y3-sjb786_tmp.ical

.PHONY debug:
debug:
	bhamcal sjb786 -o calendar-y3-sjb786.ical --password ${UNI_PASSWORD}
