Building all the recipes
========================

Start with a blank Ubuntu 14.04 LTS system.

Install::

   apt-get update
   apt-get -y install screen git curl gcc make g++ python-dev unzip \
           default-jre pkg-config libncurses5-dev r-base-core \
           r-cran-gplots python-matplotlib sysstat samtools python-pip \
           ipython-notebook

   pip install virtualenv

As a user, check out::

   cd ~/
   mkdir dev
   cd dev
   git clone https://github.com/ged-lab/khmer.git
   git clone https://github.com/ged-lab/nullgraph.git
   git clone https://github.com/ged-lab/khmer-recipes.git
   git clone https://github.com/ged-lab/literate-resting.git

   python -m virtualenv ipy7 --system-site-packages
   . ipy7/bin/activate
   
   cd khmer
   git checkout feature/collect_reads
   python setup.py install

And now grab recipes & build::

   pip install sphinx

   cd ~/dev/
   git clone https://github.com/ged-lab/khmer-recipes.git recipes
   cd recipes
   make all

Writing recipes - guidelines
============================

Use the recipe in 001 as a guideline.

A few points --

* make sure that there is a target for the last thing produced by the
  script, and that this target depends on the ReST file.

* small output files (figures, etc.) that are necessary to render the ReST
  files on github should be included in the repository.

* put 'set -e' at the top of your literate resting shell commands so that
  the script exits with an error message when a command fails.  I believe
  '|| 1' can be used in situations where you want an error to be OK.
