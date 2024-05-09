# tiny_rgi
Small tools for the parsing and presentation of CARD RGI data.

[Resistance Gene Identifier](https://card.mcmaster.ca/analyze/rgi) (**RGI*) is a powerful method of identifing antibiotic (and other) resistance genes (ARGs) using contigs generated from assembled short-read data.

To help in the utilization of this tool I've developed some scripts that increase the accesibilty of the results for end users. These tools are under active development and additional tools are forthcoming.

## Tiny RGI combiner
This script combines RGI outputs across samples listed in a mapping file and then bins them into ARO, ARG, Resistance Mechanism, and Drug Class categories and outputs these counts into csv files.  
Example:
```
python tiny_rgi_combiner.py -i mapfile.tab
```

`mapfile.tab` is a two-column, tab-delimited file where the first column is the sample name and second column is the path.
The default output is in the current working directory but this can be modified by setting the desired path using the `-o` argument.
