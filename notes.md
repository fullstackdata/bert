Find the right configuration for your environment on this page - https://spacy.io/usage
If your environment's python version doesn't match with miniconda or anaconda's python version you cannot proceed.
To make progress, I downgraded my Python version to match miniconda's Python version.
Make sure python -m spacy validate status returns success.
pip install -U pip setuptools wheel
pip install -U spacy[cuda110,transformers,lookups]
python -m spacy download en_core_web_trf



*Jupyter notebook on AWS*
https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5
1. SSH to your aws ec2 instance
2. jupyter notebook --no-browser --port=8888
3. On your local - ssh -i thisIsmyKey.pem -L 8000:localhost:8888 ubuntu@ec2–34–227–222–100.compute-1.amazonaws.com
4. In your browser - localhost:8000/tree   (no need of a token)

Twitter Scraper with Selenium
https://www.youtube.com/watch?v=3KaffTIZ5II
https://github.com/israel-dryer/Twitter-Scraper/blob/main/twitter_scraper.py
Useful to know - xpath
  
