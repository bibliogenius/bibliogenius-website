# BiblioGenius — Static site build
# Usage:
#   make build          Generate all pages + blog
#   make site           Generate site pages only (Python)
#   make blog           Generate blog only (Zola)
#   make new LANG=pt    Create a new translation file from the French reference
#   make serve          Start a local dev server (PORT=8000 by default)
#   make clean          Remove generated language subdirectories
#   make deploy         Build + rsync to VPS (vitrine + blog)

PORT ?= 8000
DEPLOY_HOST ?= hub-vps
DEPLOY_PATH ?= /var/www/bibliogenius.org/

.PHONY: build site blog clean serve new deploy

build: site blog

site:
	python3 _build/build.py

blog:
	cd _blog && zola build
	@rm -rf blog
	@cp -r _blog/public blog
	@rm -f blog/robots.txt blog/sitemap.xml
	@# Zola emits a paginator alias at page/1/ that JS-redirects to the blog
	@# index, and a bare 68-byte 404. Neither should be indexed, and the alias
	@# needs a canonical or it reads as a thin duplicate of /blog/.
	@python3 -c "import pathlib; \
		p = pathlib.Path('blog/page/1/index.html'); \
		p.write_text(p.read_text(encoding='utf-8').replace('<meta charset=\"utf-8\">', \
			'<meta charset=\"utf-8\">\n<meta name=\"robots\" content=\"noindex, follow\">\n<link rel=\"canonical\" href=\"https://bibliogenius.org/blog/\">', 1), encoding='utf-8') \
		if p.exists() and 'noindex' not in p.read_text(encoding='utf-8') else None"
	@python3 -c "import pathlib; \
		p = pathlib.Path('blog/404.html'); \
		p.write_text('<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<meta name=\"robots\" content=\"noindex, follow\">\n<title>Page introuvable - BiblioGenius</title>\n</head>\n<body>\n<h1>Page introuvable</h1>\n<p><a href=\"/blog/\">Retour au blog</a> &middot; <a href=\"/\">bibliogenius.org</a></p>\n</body>\n</html>\n', encoding='utf-8') if p.exists() else None"
	@echo "Blog built → blog/"

new:
	@test -n "$(LANG)" || { echo "Usage: make new LANG=pt"; exit 1; }
	@test ! -f _i18n/story/$(LANG).yml || { echo "_i18n/story/$(LANG).yml already exists"; exit 1; }
	@cp _i18n/story/fr.yml _i18n/story/$(LANG).yml
	@echo "Created _i18n/story/$(LANG).yml"
	@echo "→ Translate it, then run: make build"

clean:
	@for f in _i18n/story/*.yml; do \
		lang=$$(basename "$$f" .yml); \
		if [ "$$lang" != "fr" ] && [ -d "$$lang" ]; then \
			rm -rf "$$lang"; \
			echo "Removed $$lang/"; \
		fi; \
	done

# Port 8000 is regularly taken by something else on this machine: a Docker
# container, or the BiblioGenius desktop build, whose own HTTP server answers
# peers there. Binding then fails and the browser hits that other service,
# which 404s on every page of this site. Check first and say so.
serve:
	@python3 -c "import socket,sys; s=socket.socket(); 		sys.exit(0) if s.connect_ex(('127.0.0.1', $(PORT))) else sys.exit(1)" 		|| { echo "Port $(PORT) is already in use (Docker, or the BiblioGenius desktop app)."; 		     echo "Free it, or run: make serve PORT=8001"; exit 1; }
	@echo "http://localhost:$(PORT)/story.html"
	python3 -m http.server $(PORT)

deploy: build
	@echo "Deploying to $(DEPLOY_HOST):$(DEPLOY_PATH)"
	rsync -avz --delete \
		--exclude-from=.deployignore \
		./ $(DEPLOY_HOST):$(DEPLOY_PATH)
	@echo "Done → https://bibliogenius.org"
