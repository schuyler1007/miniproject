# miniproject

Design Decisions:<br />
<br />
We decided to build this app using the React-Native environment. We tried running the Metro server on both WSL and Windows 11 and running the app on ExpoGo. However, both of these attempts led to networking problems. We decided to, instead, run the React Native Client on the Windows host computer and run our app on an Android Virtual Device (AVD). It took a lot of trouble-shooting, but it finally worked. To make it work, we added more SDK platforms and tools. Then we created a project using:<br />
<br />
``npx react-native init <projectname>``.<br />
<br />
``npm start`` started our project.<br />
<br />
On another Windows Powershell Terminal, navigate to the project folder. With the AVD open, type<br />
<br />
``npm run android``.<br />
<br />
Then it worked. Editing the app JavaScript source file is done on Visual Studio Code.<br />
<br />
Next, we decided that we wanted Google Firebase to handle much of the backend of our app. We created a new project and made sure to change the parent resource from "bu.edu" to "to-be-sorted", so that BU would not block us from adding a firebase project. Afterward, we connected our newly made app to our Firebase project by installing the app module into our root directory and adding Firebase config files.
<br />
This video helped us implement Google Sign-In function: https://www.youtube.com/watch?v=gai4aYcNunc&t=382s
<br />
Note: The keystore sometimes comes up missing in the command line. To get the SHA-1 fingerprint, open Adnroid Studio IDE with the `...android/app` as the root directory and run `gradle signingreport` there.

## Installation of Modules for Python files
In order to run python file including the main.py, run the following command in your shell to install all modules needed in your enviornment.
```
cd misc
pip install -r requirement.txt
```

## Run the application
To run this application, go to the following directory and run the following command in your shell
```
cd src
python3 main.py
```

## What each module does
### [get_tweets](../miniproject/src/get_tweets.py): 
this module takes the user name or screen id of Twitter account as an input, and returns the 20 most recent tweets of the specified user (including retweeted tweets) using Twitter API

### [get_content](../miniproject/src/get_content.py):
this module takes sentenses and returns the content of those sentenses using Cloud Natural Language API

## [get_sentiment](../miniproject/src/get_sentiment.py):
this module takes sentenses and returns the sentiment of those sentenses using Cloud Natural Language API

## [main.py](../miniproject/src/main.py)
this is the main file of the application
