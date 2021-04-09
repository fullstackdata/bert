!pip install -U pip setuptools wheel
!pip install -U spacy[transformers,lookups]
!pip install -U spacy[cuda110,transformers,lookups]   - cuda 11 GPU
!python -m spacy download en_core_web_trf

import spacy
spacy.load('en_core_web_trf')
