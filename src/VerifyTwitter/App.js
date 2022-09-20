/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import type {Node} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Button
} from 'react-native';
import auth from '@react-native-firebase/auth';
import { GoogleSignin } from '@react-native-google-signin/google-signin';

const App: () => Node = () => {

  GoogleSignin.configure({
    webClientId: '766770531670-te2aft1gkplc6fcscvicqt8gru8u9796.apps.googleusercontent.com',
  });

  const signInWithGoogleAsynch = async () => {
    // Get the users ID token
    const { idToken } = await GoogleSignin.signIn();

    // Create a Google credential with the token
    const googleCredential = auth.GoogleAuthProvider.credential(idToken);

    // Sign-in the user with the credential
    const user_sign_in = auth().signInWithCredential(googleCredential);

    user_sign_in.then((user)=> {
      console.log(user);
    })
    .catch((error)=>{
      console.log(error);
    })
  }

  return(
    <View style={{flex:1, justifyContent:'center', alignItems:'center'}}>
        <Button
          title='Sign in with Google'
          onPress={signInWithGoogleAsynch}
        />

    </View>
  );
};


export default App;
