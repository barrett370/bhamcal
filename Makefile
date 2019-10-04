
.PHONY calendar:
calendar:
	bhamcal sjb786 -o calendar.ical --password ${UNI_PASSWORD} && gsutil cp calendar.ical gs://sjb786-cal-bucket && rm calendar.ical
