python 32-bit or 64-bit?

<pre><code>import platform
platform.architecture()</code></pre>


Find the right configuration for your environment on this page - https://spacy.io/usage <br/>
<b>If your environment's python version doesn't match with miniconda or anaconda's python version you cannot proceed.</b><br/>
To make progress, I downgraded my Python version to match miniconda's Python version. <br/>
Make sure `python -m spacy validate` returns success. <br/>

<pre><code>pip install -U pip setuptools wheel
pip install -U spacy[cuda110,transformers,lookups]
python -m spacy download en_core_web_trf</pre></code>



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
scroll to load all elements
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

Jupyter Tabnine
pip3 install jupyter-tabnine --user
jupyter nbextension install --py jupyter_tabnine --user
jupyter nbextension enable jupyter_tabnine --user --py
jupyter serverextension enable --py jupyter_tabnine --user


VS Code Useful Extensions 
https://ahmed-nafies.medium.com/my-top-10-visual-studio-code-extensions-for-python-in-2020-9896beb04e89

Evaluate:
Pylance
Python
Remote SSH
GitLens
Bracket Pair Colorizer 2
Dracula Official
Idented Block Highlighting
JSON Pretty Printer
GitLens — Git supercharged
Edit CSV
Git Graph
Markdown All in One
Python Docstring Generator
reStructuredText
