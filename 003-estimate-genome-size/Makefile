all: report.txt index.html

clean:
	-rm -f index.sh *.fa *.kh *.kh.info *.dist index.html

distclean: clean
	-rm -f *.png report.txt reads.fa.keep

index.sh: index.rst
	~/dev/literate-resting/scan.sh index.rst
	mv index.rst.sh index.sh

report.txt: index.sh
	BASH_ENV=../env.sh bash index.sh

index.html: index.rst
	rst2html.py index.rst index.html
