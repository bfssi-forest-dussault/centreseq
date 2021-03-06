Examples
~~~~~~~~

The following examples uses a small example dataset sourced from this (BioProject)[https://www.ncbi.nlm.nih.gov/bioproject/PRJNA327743].
You can follow along by retrieving the `.fna` files, available in the following (archive)[https://ndownloader.figshare.com/files/18519863].

Getting started
^^^^^^^^^^^^^^^

Given a directory called `assemblies` that we unzipped our sample archive into:

::

   /home/user/assemblies/
    ├── GCA_001691885.1.fna
    ├── GCA_001691915.1.fna
    ├── GCA_001691965.1.fna
    ├── GCA_001691975.1.fna
    ├── GCA_001691985.1.fna
    ├── GCA_001692005.1.fna
    ├── GCA_001692045.1.fna
    ├── GCA_001692065.1.fna
    ├── GCA_001692085.1.fna
    ├── GCA_001692105.1.fna
    └── GCA_001692145.1.fna

We can run the following command to run centreseq against our 10 input genomes with 16 cores, with all output being
routed to `/home/user/centreseq`:

::

    centreseq core -f /home/user/assemblies/ -o /home/user/centreseq -n 16 --pairwise

Once the program has finished, the following structure can be found in your output directory:

::

    /home/user/centreseq_output
    ├── core_genome
    ├── logs
    ├── mmseqs2
    ├── network_graph_coding.tsv
    ├── network_graph.html
    ├── prokka
    ├── static
    └── reports

An overview of the results can be found in the reports directory. Raw data from the core pipeline can be found in the
*/core_genome*, */mmseqs2*, and */prokka* directories. Please refer to the `Reports` section of the documentation for further details.


Launching the network chart
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view the network chart, open a bash terminal, `cd` to your output directory generated by the `centreseq core` script, and run the following command:

::

    python -m http.server 8080

This will start a simple server at port 8080 that you can navigate to via a web browser (e.g. `http://0.0.0.0:8080`). Navigate to the server in your browser
of choice (Chrome, Chromium or Firefox) and open network_graph.html. From here, you can interrogate the relationships
among your input genomes according to pairwise similarity values. Note that the `--pairwise` flag must have been
activated in order for these files to be generated.
