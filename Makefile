
.PHONY calendar:
calendar:
	bhamcal sjb786 -o calendar-y3-sjb786.ical --password ${UNI_PASSWORD}
	gsutil -h "Cache-Control:no-cache, max-age=0" cp -a public-read calendar-y3-sjb786.ical gs://sjb786-cal-bucket
	cp calendar-y3-sjb786.ical ~/Documents
