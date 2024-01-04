# LumuTechChallenge
Tech Challenge: Bacon Ipsum PDF Report Generation and Analysis

Hi this is my solution to the challenge, to use this mini-app you just have to clone the repository and open your IDE in the folder "LumuTechChallenge"
After that, with a terminal in this same folder, you just have to execute the following command "py -m flask --app .\index.py run"
Finally, the default URL to use the app is this one: "http://127.0.0.1:5000/generate-pdf"

# Building the app

The app consists of a simple html page that lets you put the parameter values of the API as you wish, with a little restriction (Sorry!!!)
The only restriction is for the parameter "paras", only receive numbers from 1 to 15.

In the html page of the app, I used a post petition to create the pdf report. This request is preprocessed by a little controller who connects the frontend and the backend and makes a request for the information to the API. 
Finally, I used a facade pattern to the next steps of the challenge, Data Preparation and Text Processing and Exploratory Text Analysis and PDF Generation, where this facade class/file uses other that have singular goals, Data Analytics, and the pdf construction.

And that’s it, I wanted to use a simple html page, so you don’t have to use postman to consume the app, I hope you like mi little app, I'm sorry for the delay.
Thank you. 

Greetings, Giovanny Granados
