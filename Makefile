
.PHONY calendar:
calendar:
	bhamcal sjb786 -o calendar.ical --password ${UNI_PASSWORD}
	gsutil -h "Cache-Control:no-cache, max-age=0" cp -a public-read calendar.ical gs://sjb786-cal-bucket
	cp calendar.ical ~/Documents
