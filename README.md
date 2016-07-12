# Experiment-Page
contain the experiment page for SIlive with listing and discription

Configure the project with the virtualenv environemnt 
and install the corresponding dependencies
-> pip install -r requirement.txt

apply the corresponding migrations

url to hit at the beginning

  -localhost:<port:default=8000>/experiments list of experiments

    you can explore indiviual experiment by the view button or by clicking the title

  -localhost:<port:default=8000>/experiments/<title-of-post>/   --<title> = auto-generated

  -localhost:<port:default=8000>/experiments/add add new experiment ---admin-function

  -localhost:<port:default=8000>/experiments/<title-of-post>/delete ---admin-function
