# Travel-guide-website-with-chatbot-and-virtual-tour
A complete travel guide website that has a chatbot made in python(using chatterbot framework) and virtual tour embedded

The chatbot can be trained to say different responces and the chatterbot framework automatically saves them into a database(sql) and divides them grammatically so that
whenever a person gives input, it need not be the same one we trained the bot for.

Flask is used for backend, and flask does not provide us with an database automatically, so phpmyadmin is used to store user information.

You might need to install chatterbot inorder for code to work(I did it in virtual environment, but sometimes.... you know) 

installation for chatterbot:

:-in your terminal, put these commands:
-pip install chatterbot
//you can also do this from github
-pip install git+git://github.com/gunthercox/ChatterBot.git@master

//you might need to downgrade your spacy version inorder to run chatterbot as it uses a previous version...
-pip install spacy --2.2.4

Hope this helps:)
