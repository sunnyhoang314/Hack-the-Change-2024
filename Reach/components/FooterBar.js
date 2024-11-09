// FooterBar.js
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

const FooterBar = () => {
  return (
    <View style={styles.footerContainer}>
      <TouchableOpacity style={styles.button}>
        <Icon name="home" size={24} color="white" />
        <Text style={styles.buttonText}>Home</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}>
        <Icon name="search" size={24} color="white" />
        <Text style={styles.buttonText}>Requests</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}>
        <Icon name="chat" size={24} color="white" />
        <Text style={styles.buttonText}>Ask</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}>
        <Icon name="settings" size={24} color="white" />
        <Text style={styles.buttonText}>Settings</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}>
        <Icon name="people" size={24} color="white" />
        <Text style={styles.buttonText}>Community</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  footerContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    height: 60,
    backgroundColor: '#333',
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    zIndex: 10,
  },
  button: {
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 12,
    marginTop: 4,
  },
});

export default FooterBar;
