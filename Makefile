update:
	git pull -a
	git pull
	git submodule deinit --all -f
	git submodule init
	git submodule update --remote