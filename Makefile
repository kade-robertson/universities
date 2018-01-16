default:
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal

prod: default
	twine upload dist/*

test: default
	twine upload -r testpypi dist/*
