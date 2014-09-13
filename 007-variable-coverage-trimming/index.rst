Recipe 7: Variable abundance trimming
#####################################

This is a recipe for trimming your reads at low-abundance k-mers, as
described in `These are not the k-mers you are looking for: efficient
online k-mer counting using a probabilistic data structure
<http://www.ncbi.nlm.nih.gov/pubmed/25062443>`__. Unlike the
``filter-abund`` script used in that paper, this approach does the
trimming in a streaming few-pass approach, in which most of the data
is only looked at once.

Low-abundance k-mer trimming is primarily useful for removing errors
from short reads prior to assembly or mapping.  This can significantly
reduce memory requirements for assembly, in particular. However, note
that you should only do this kind of error trimming in cases where
your downstream analysis approaches won't correct the errors for you;
see `On the optimal trimming of high-throughput mRNA sequence data,
MacManes, 2014 <http://www.ncbi.nlm.nih.gov/pubmed/24567737>`__ for
more information.

Note: at the moment, the khmer script ``trim-low-abund.py`` is in the
khmer repository under branch ``update/streaming``.  Once we've merged
it into the master branch and cut a release, we'll remove this note
and simply specify the khmer release required.

.. @@branch fix

.. shell start

.. ::

   . ~/dev/ipy7/bin/activate
   set -e
   
   # build a read set
   python ~/dev/nullgraph/make-biased-reads.py -C 10 metagenome.fa > reads.fa

Suppose you have a metagenome, with several different coverage peaks;
here, in this simulated data set, there are three: one at 10, one at
100, and one at about 300.
::

   load-into-counting.py -x 1e8 -k 20 reads.kh reads.fa
   ~/dev/khmer/sandbox/calc-median-distribution.py reads.kh reads.fa reads-cov.dist
   ./plot-coverage-dist.py reads-cov.dist reads-cov.png --xmax=350

.. image:: reads-cov.png
   :width: 500px

Suppose you wanted to remove errors with k-mer abundance trimming (as
in :doc:`../006-streaming-error-trimming/index`) - the problem is that
you can't just use a hard cutoff, because some of the low-abundance k-mers
are real, while some are not.  For example, the k-mer spectrum of this
data set is much broader at 1 than it would be for a high-coverage
genome:
::

   abundance-dist.py -s reads.kh reads.fa reads.dist
   ./plot-abundance-dist.py reads.dist reads-dist.png --xmax=20 --ymax=18000

.. image:: reads-dist.png
   :width: 500px

You can use the -V argument to the sandbox script
``trim-low-abund.py`` to efficiently trim sequences at these k-mers:
::

   ~/dev/khmer/sandbox/trim-low-abund.py -x 1e8 -k 20 -V reads.fa

(By default, trim-low-abund trims k-mers that are unique in reads that
have 20 or higher coverage.  You can change the multiplicity of trimming
with ``-C`` and the trusted coverage with ``-Z``.)

After running trim-low-abund, you'll note that some but not all of the
unique k-mers are now gone:
::
   
   load-into-counting.py -x 1e8 -k 20 reads-trim.kh reads.fa.abundtrim
   abundance-dist.py -s reads-trim.kh reads.fa.abundtrim reads-trim.dist
   ./plot-abundance-dist.py reads-trim.dist reads-trim-dist.png --xmax=20 --ymax=18000

.. image:: reads-trim-dist.png
   :width: 500px

Voila!

As mentioned briefly above, here we are using a more memory- and time-
efficient approach than the ``filter-abund`` script that we published
as part of khmer.  Note that you can use this script on metagenomes
and transcriptomes as well by passing in the ``-V`` parameter for
variable coverage trimming; we'll talk about that more in another recipe,
perhaps.

Resources and Links
~~~~~~~~~~~~~~~~~~~

`This recipe
<https://github.com/ged-lab/khmer-recipes/tree/master/006-streaming-sequence-trimming>`__
is hosted in the khmer-recipes repository,
https://github.com/ged-lab/khmer-recipes/.

It requires the `khmer software <http://khmer.readthedocs.org>`__.
