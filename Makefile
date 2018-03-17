build: clean
	mkdir -p _build
	pip install -r requirements.txt -t _build
	cp -R .env/lib/python2.7/site-packages/fitparse _build
	cp -R src/* _build

package: 
	aws cloudformation package \
		--template-file cloudformation-template.yaml \
		--s3-bucket thijs-test-runalytics \
		--s3-prefix packages \
		--output-template-file packaged-cloudformation-template.yaml

deploy: 
	aws cloudformation deploy \
		--template-file packaged-cloudformation-template.yaml \
		--stack-name thijs-test-runalytics \
		--capabilities CAPABILITY_IAM

clean:
	find . -name "*.pyc" -exec rm -f {} \;

test:
	py.test tests # --cov=src --cov-report term-missing

testvv:
	py.test tests --cov=src --cov-report term-missing --fulltrace -vv

push-www:
	push-html
	push-css
	push-js

push-html:
	aws s3 cp www/templates/index.html s3://thijs-test-runalytics/

push-css:
	aws s3 cp www/static/style.css s3://thijs-test-runalytics/static/

push-js:
	aws s3 cp www/static/data_loading.js s3://thijs-test-runalytics/static/
