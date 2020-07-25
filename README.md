# discordBotClient
This is a basic Discord client I made with a bot and a webhook. It uses the official Discord.py API and follows the TOS. Currently, you recieve messages from only one guild and can send messages to one channel. To install it:
1. Run `git clone https://github.com/nature174/discordBotClient.git`.

2. Make a text file called token.txt and put your Bot Token in it. Example: `MzNz1EU0NTcxNzM4MzAwNDg3.Xxcvaw.2Q_qrZZrPrKxL95YSuOYw9kdczs'`
+ If you have the `Manage Channel` permissions:

  + To get a bot token, Go to [the Discord Bot maker](https://discord.com/developers/applications) and click on `New Application` on the top. Type any name into the `Name` field and click on `Create`. Click on `Bot` on the left sidebar. Then click on `Add Bot` and `Yes, do it!`. Click on `Copy` below the Token, and paste the token into `token.txt`.

+ Otherwise:

  + Ask a guild moderator with the Manage Channel Permission to get you a bot token (not guaranteed). If the mod gives you the token, put it into `token.txt`

+ If you don't get a token:

  + You will not be able to receive messages, but you may be able to send messages if the next step works.

3. Make a text file called webhook.txt and put the webhook URL into it.
  + If you have the `Manage Webhooks` Permission:
    + Click on the `Edit Channel` (Gear Icon) on the channel you would like to use to send messages. Click on `Integrations` on the sidebar then:
      If you see `View Webhooks`, click on that, then click on `New Webhook`.
      If you just see `Create Webhook`, click on that.
    Change the name of the webhook to your discord username or something similar, then click on `Copy Webhook URL`. Paste the URL into the `webhook.txt` file.
  + If you don't have the `Manage Webhooks` Permission:
    + Ask a guild moderator with the `Manage Webhooks` permission to create a webhook and give you the URL. Put the URL into the `webhook.txt` file.
  + If you can't get a webhook:
    + You will not be able to send messages but you may be able to receive messages if you have a bot token.
