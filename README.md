# weatherUpdate_chatbot

I am building this bot to get basic understanding of RASA framework on how different components work.

## Features

If you ask chatbot about location of any place , it should give you the weather details of that place.
Additional to that Bot will be able to respond for proper greeting or chitchat.

## Process to implement( for my ref)

1. Installing rasa
2. creating domain.yml-> which containes everything that exists for bot i.e different intents,entities,slots,responses,actions
3. creating config.yml -> this file basically contains pipeline and policy. I think for my usecase pipeline will be empty
(my understanding is wrong. Basic pipeline is needed atleast for internal models that rasa uses )
4. creating endpoint.yml -> it basically contains the http address where our bot will be running
5. creating stories.yml -> basic flow of my chatbot
6. data.yml is not needed as I don't need any special entity recognition.
7. creating actions.yml -> to perform custom actions in our case to get weather details from external APIs.

## Things to implement
1. Structured happy flow(done)
2. Sad flow(done)
3. When city is not recognised by rasa it should prompt the city and take it.(done)
4. connecting actual api to get relevant details.(needs to be implemented)



