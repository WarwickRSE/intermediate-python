# template

A template to create new lessons

We include the following in the .git/config

[filter "strip-notebook-output"]
    clean = "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR"

and use .gitattribute

*.ipynb filter=strip-notebook-output

To hook notebooks and remove output before letting code outputs get saved to the git directory.
