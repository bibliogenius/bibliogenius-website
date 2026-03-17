# BiblioGenius — Static site build
# Usage:
#   make build          Generate all pages + blog
#   make site           Generate site pages only (Python)
#   make blog           Generate blog only (Zola)
#   make new LANG=pt    Create a new translation file from the French reference
#   make serve          Start a local dev server on port 8000
#   make clean          Remove generated language subdirectories

.PHONY: build site blog clean serve new

build: site blog

site:
	python3 _build/build.py

blog:
	cd _blog && zola build
	@rm -rf blog
	@cp -r _blog/public blog
	@rm -f blog/robots.txt blog/sitemap.xml
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

serve:
	@echo "http://localhost:8000/story.html"
	python3 -m http.server 8000
