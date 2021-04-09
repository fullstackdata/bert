!pip install -U pip setuptools wheel
!pip install -U spacy[transformers,lookups]
!python -m spacy download en_core_web_trf

import spacy
spacy.load('en_core_web_trf')
