## Instagram-Chat-ML

A simple ml model that can find which user typed what just by training it using a simple json file (with a chat).

### Story

I think that you all know what NGL is. For those who don't know is an app that you can do anonymous QnA with your friends. This thing has
a premium version that allows you to *"find who sent the message"*, but it is a complete lie as the only thing that it tells you is just some 
phone info, ip location etc. that don't help you at all. So I created an ml model (with the help of chatgpt :)) that can be trained with data from
all your chats with friends and predict who sent the message.

### Installation

You will firstly need to request your data from Instagram using this [form](https://www.instagram.com/download/request/) make sure to use **Json** as
format and not html. (It may take up to 48 hours for instagram to send your data)

Now clone the repository and install requirements using these commands:
```shellscript
git clone https://github.com/steveiliop56/Instagram-Chat-ML.git
cd Instagram-Chat-ML/
pip3 install -r requirements.txt
```

After this you will need to unzip the downloaded data from instagram **(you will be amazed from how many data they have collected)**
and find the messages folder and then go to inbox, there you will find a file like ``message_1.json`` or something simillar to that. 
So grab this file and drop it in the ``data_raw`` folder.

Last but not least you will need to go to the ``convert.py`` file and change the line 43 and add the path for the json file. For example 
you probably would add something like this: ``path = "data_raw/message_1.json"``. Now it's time to convert the data to a usable format and
train the model with these 2 commands.

```shellscript
python3 convert.py
python3 train.py
```

It may take some time depending on the ammount of data. (The more data the more time training but better accuracy)

### Running

To run the ml model just run this command:

```shellscript
python3 run.py
```

Now whatever you type the model will preditct who of the users was and output their instagram
username.


