SUBMODULE_NAME = ui
MIGRATIONS_DIR = migrations
SQLITEDB = pizza.sqlite

clear:
	rm -rf $(MIGRATIONS_DIR)
	rm -f $(SQLITEDB)

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

test:
	@python3 manage.py test