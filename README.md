# FoodSource

## Submitted to AuburnHacks 2021
## Devpost - https://devpost.com/software/foodsource-4qpjck
## Video - https://youtu.be/J9d-NxqzP0g

## Inspiration
Food insecurity has always been a pernicious social problem in the United States, but it has often been overlooked by legislators. Now, the COVID-19 pandemic and subsequent economic depression have greatly exacerbated food insecurity and hunger in America. Access to soup kitchens and other in-person food dispensaries has been cut off by the threat of infection. We wanted to use remote delivery APIs and web-dev essentials to create a community-minded digital solution to this problem - a solution that anyone could contribute to.

## What it does
FoodSource is a web app that allows lower-income users suffering from food insecurity to sign up and, after verification, broadcast their location along with a list of requested food items to anyone viewing the website. Other users can then respond to any given broadcast by using the site’s integration with Doordash and Lyft to order food for the broadcaster at the specified location. In this way, we have built the framework to crowdsource the problem of hunger during the pandemic: anyone can log onto the site and order food for the hungry, and the remote nature of the delivery removes the risk of COVID transmission. We have also implemented basic cybersecurity measures through mandatory Twilio SMS verification for all those who request food. With FoodSource, we can all do our part to feed the hungry - even from the comfort of our own living rooms.

## How we built it
FoodSource was built using Python 3, Flask, and JavaScript. We also used the Doordash and Lyft APIs to add food delivery options, and we used the Twilio Verify API to implement SMS verification for users requesting food. On the client side, the dynamically updated map was written using the HERE Maps API.

## Challenges we ran into
Implementing the dynamic map that updates with each new food request was a difficult task, and we had to use several workarounds to get each map marker to highlight its corresponding entry in the list of food requests when hovered over.

## Accomplishments that we're proud of
We are proud of having created an intuitive user interface that is easy to navigate for both food donors and food recipients alike.

## What we learned
Through FoodSource, we familiarized ourselves with the HERE Maps API as well as with Twilio. We also improved our knowledge of JavaScript.

## What's next for FoodSource
We plan to make the map more feature-rich and improve the range of authentication options for food recipients who may not have access to cell phones. Additionally, we hope to create some sort of in-app communication system for the donors to directly communicate with those who are food insecure.
