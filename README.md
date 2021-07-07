# whatsapp-autoforward-message

We have seen that a lot many people have demanded auto forward message in whatsapp, but there is no feature available in WhatsApp application (Android/IOS). Here I have created an application which automatically forward message comes from the one group/individual contact to another group or individual contact.

# Technology Used

- Python
- Selenium

# How does it work?

1. Download **/dist/** folder from the repository.
2. Open _run-me.bat_ file in notepad.
3. You will see below command in the file.
4. WhatsAppAutoForward.exe --source "{{Source Group/Contact name}}" --sourceIsGroup True --target "{{Target Group/Contact Name}}" --prefix "{{Prefix for forwarding message}}.
5. Replace {{Source Group/Contact name}} with your group name from which you would like to forward the message.
6. Replace {{Target Group/Contact Name}} with your group name to which you would like to forward the message.
7. --SourceIsGroup must be True if the source is group else no need to pass the parameter.
8. Save the file _run-me.bat_ .
9. Open Command Prompt and run the above batch file.

# Limitations

This application has some limitations to forward the message as below.

1. It can forward normal message
2. It can forward emoji
3. It can forward message with emoji
4. It can forward message with reply
5. It doesn't work for image, video, gif messages
