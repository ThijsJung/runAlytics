build: clean
	mkdir -p _build
	pip install -r requirements.txt -t _build
	cp -R src/* _build

package: 
	aws cloudformation package \
		--template-file cloudformation-template.yaml \
		--s3-bucket thijs-test-runalytics \
		--s3-prefix packages \
		--output-template-file _build/packaged-cloudformation-template.yaml

deploy: 
	aws cloudformation deploy \
		--template-file _build/packaged-cloudformation-template.yaml \
		--stack-name thijs-test-runalytics \
		--capabilities CAPABILITY_IAM

clean:
	find . -name "*.pyc" -exec rm -f {} \;

test:
	py.test tests --cov=src --cov-report term-missing

testvv:
	py.test tests --cov=src --cov-report term-missing --fulltrace -vv
