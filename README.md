This website models a private equity fund for real estate investors.

To use, please open the link to the testing site, deployed live using Heroku:
https://homely-zr.herokuapp.com/

This website was built using Flask, a Python library for building web apps.
It incorporate Flask PyMongo, another Python library which allows web apps to
store data in MongoDB, a NoSql database.

The HTML pages were made using Jinja2 templates. When you reach the website, the first
page displayed is rendered by the properties_index.html file. This page is a list of the
funds which the private equity fund, Homely Properties, has either previously or is
currently collecting investments for from users. The former listings have been marked
CLOSED, and the latter have been marked as 'OPEN' on the page.

Please select one of the funds marked 'OPEN'. To test making an initial offer to invest,
click on the 'Invest Now!' button. Enter your information, submit, and then click on "View All Offers" to see your offer in the list.

From the 'View All Offers' page (which can also be accessed by clicking one the
'Show Me More' buttons on the home page), please test using the 'Edit' and 'Delete'
buttons to see more functionality of the site.

In an future version of this app, users would be notified via email when their offers
were approved, making them official investors in the fund (with K1 tax benefits as well
as many other benefits for you and your family)! Additional improvements would include
user authentication to allow secure financial processing, information hiding as
needed for privacy, and additional functions such as being able to email staff on the site
to ask questions; and schedule appointments to see the property before the user makes an
offer.
