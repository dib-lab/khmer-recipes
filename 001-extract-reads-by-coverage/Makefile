all: reads.fa index.html

clean:
	-rm -f index.sh reads.fa genome.fa repeat.fa

index.sh: index.rst
	~/dev/literate-resting/scan.sh index.rst
	mv index.rst.sh index.sh

reads.fa: index.sh
	bash index.sh

index.html: index.rst
	rst2html.py index.rst index.html