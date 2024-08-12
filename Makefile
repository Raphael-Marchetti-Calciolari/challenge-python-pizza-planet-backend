SUBMODULE_NAME = ui

update:
	git pull -a
	git pull
	git submodule deinit --all -f
	git submodule init
	git submodule update --remote
	git add $(SUBMODULE_NAME)
	git commit -m "submodule update"
	git push