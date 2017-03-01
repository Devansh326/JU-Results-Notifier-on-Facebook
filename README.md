# JU-Results-Notifier-on-Facebook

### bot that posts on facebook page everytime a result is published in the official website of Jadavpur University

1. [JU Results Notifier FB Page](https://www.facebook.com/Jadavpur-University-Results-Notifier-1792892714369394/)

2. [JU results portal](http://www.juexam.org/newexam/)

*Here is a bit of a background*. The current system of the Jadavpur University website has no student account system. Hence, the results doesn't get sent to the students via emails. We don't even get to know when our result comes out. Usually it happens that one extra eager bright student of a class checks the result portal everyday and the rest of the people get to know from her/him.

So the aim is to at least notify the students when a result comes out and facebook being the more common place, a facebook page is suited as ideal solution.


### For the eager fellow who wants to go through the code

This is a plain python app. The heart of the project is the library [selenium](http://selenium-python.readthedocs.io/), a python webdriver which basically replicates a browser in code. (for those of you who know stuff already, I found it a better choice over scrapy for this task as it has forms to fill).

You'll also need facebook-sdk for python. Check the requirements.txt in the code.

The app is deployed on Heroku.

Note: You'll find flask elements in the code. As of know the flask part has NO role in the app. I kept it for future features.


### Coming up..

Messenger support where a student can send a message and subscribe to a specific result, say the 2nd Year 1st Sem of EE, 2017. When the result comes out, the student will get a ping on messenger.


### Issues and Contribution

Contribute whatever new cool feature you can make :)

The app does not have checks to report malfunction. So raise issues when it does.
