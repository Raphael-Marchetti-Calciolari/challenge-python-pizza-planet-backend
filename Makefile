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

run:
	@python3 manage.py db init || true
	@python3 manage.py db migrate || true
	@python3 manage.py db upgrade || true
	@echo
	@echo "Starting server..."
	@python3 manage.py run