# miniproject

Design Decision:<br />
We decided to build this app using the React-Native environment. We tried running the Metro server on both WSL and Windows 11 and running the app on ExpoGo. However, both of these attempts led to networking problems. We decided to, instead, run the React Native Client on the Windows host computer and run our app on an Android Virtual Device (AVD). It took a lot of trouble-shooting, but it finally worked. To make it work, we added more SDK platforms and tools. Then we created a project using:<br />
<br />
``npx react-native init <projectname>``.<br />
<br />
``npm start`` started our project.<br />
<br />
On another Windows Powershell Terminal and navigated to the project folder. With the AVD open, type<br />
<br />
``npm run android``.<br />
<br />
Then it worked. Editing the app JavaScript source file is done on Visual Studio Code.<br />
