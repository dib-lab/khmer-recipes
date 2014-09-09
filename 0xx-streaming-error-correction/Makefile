all: reads.fa.corr index.html

clean:
	-rm -f index.sh *.fa *.kh *.kh.info *.dist index.html mutation_details.txt\
		reads.fa.corr reads.fa.details.txt reads.fa.keep reads.keep.ht

distclean: clean

index.sh: index.rst
	~/dev/literate-resting/scan.sh index.rst
	mv index.rst.sh index.sh

reads.fa.corr: index.sh
	bash index.sh

index.html: index.rst
	rst2html.py index.rst index.html