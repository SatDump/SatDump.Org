(cd _tabs && python3 ../sat-list/generate_sat_list_md.py)
bundle exec jekyll build --source . --destination $1
