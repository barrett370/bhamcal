SHELL := zsh
.PHONY calendar:
calendar:
	cd utils && ./full-build.sh
.PHONY diff:
diff: 
	bhamcal sjb786 -o calendar-y3-sjb786_tmp.ical --password ${UNI_PASSWORD}
	if [[ $(diff calendar-y3-sjb786_tmp.ical calendar-y3-sjb768.ical) ]]; then  echo "Calendar has changed"; else  echo "Calendar up to date"; fi
	rm calendar-y3-sjb786_tmp.ical

.PHONY debug:
debug:
	bhamcal sjb786 -o calendar-y3-sjb786.ical --password "${UNI_PASSWORD}"
