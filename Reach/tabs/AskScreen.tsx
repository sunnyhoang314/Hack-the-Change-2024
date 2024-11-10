// AskScreen.tsx
import React, { useState, useEffect } from 'react';
import { View, Text, Button, Image, StyleSheet, Alert } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import * as Location from 'expo-location';
import axios from 'axios';
import { calculateDistance } from './utils/calculateDistance';  // Import the helper function

export default function AskScreen() {
  const [profileImage, setProfileImage] = useState<string | null>(null);
  const [taskImage, setTaskImage] = useState<string | null>(null);
  const [userName, setUserName] = useState('');
  const [peopleNeeded, setPeopleNeeded] = useState(1);
  const [distance, setDistance] = useState(0);
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState<{ latitude: number; longitude: number } | null>(null);

  // Request permission and get location
  useEffect(() => {
    const getLocation = async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status === 'granted') {
        let loc = await Location.getCurrentPositionAsync({});
        setLocation({
          latitude: loc.coords.latitude,
          longitude: loc.coords.longitude,
        });
      } else {
        Alert.alert('Permission Denied', 'Location permission is required');
      }
    };
    getLocation();
  }, []);

  const pickImage = async (type: 'profile' | 'task') => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [1, 1],
      quality: 1,
    });

    if (!result.canceled) {
      if (type === 'profile') {
        setProfileImage(result.uri);
      } else if (type === 'task') {
        setTaskImage(result.uri);
      }
    }
  };

  const submitAskForHelp = async () => {
    if (!location) {
      Alert.alert('Error', 'Location is required');
      return;
    }

    // Example data for the task (from your backend)
    const taskLatitude = 51.0447; // Example latitude from backend
    const taskLongitude = -114.0719; // Example longitude from backend

    // Calculate the distance using the helper function
    const calculatedDistance = calculateDistance(location.latitude, location.longitude, taskLatitude, taskLongitude);
    setDistance(calculatedDistance);

    const formData = new FormData();
    formData.append('user_name', userName);
    formData.append('people_needed', peopleNeeded.toString());
    formData.append('distance', calculatedDistance.toString());
    formData.append('description', description);
    formData.append('latitude', location.latitude.toString());
    formData.append('longitude', location.longitude.toString());

    if (profileImage) {
      const profileUri = {
        uri: profileImage,
        type: 'image/jpeg',
        name: 'profile.jpg',
      };
      formData.append('profile_picture', profileUri);
    }

    if (taskImage) {
      const taskUri = {
        uri: taskImage,
        type: 'image/jpeg',
        name: 'task.jpg',
      };
      formData.append('task_picture', taskUri);
    }

    try {
      const response = await axios.post('http://192.168.1.x:8000/api/ask_for_help/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      Alert.alert('Success', 'Your request has been submitted!');
      setProfileImage(null);
      setTaskImage(null);
      setUserName('');
      setPeopleNeeded(1);
      setDistance(0);
      setDescription('');
    } catch (error) {
      console.error('Error uploading images:', error);
      Alert.alert('Error', 'There was an issue submitting your request.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Ask for Help</Text>

      {/* Profile Image Picker */}
      <Button title="Pick Profile Image" onPress={() => pickImage('profile')} />
      {profileImage && <Image source={{ uri: profileImage }} style={styles.imagePreview} />}

      {/* Task Image Picker */}
      <Button title="Pick Task Image" onPress={() => pickImage('task')} />
      {taskImage && <Image source={{ uri: taskImage }} style={styles.imagePreview} />}

      {/* Form Inputs */}
      <TextInput
        style={styles.input}
        placeholder="Your Name"
        value={userName}
        onChangeText={setUserName}
      />
      <TextInput
        style={styles.input}
        placeholder="People Needed"
        value={peopleNeeded.toString()}
        onChangeText={(text) => setPeopleNeeded(Number(text))}
      />
      <TextInput
        style={styles.input}
        placeholder="Description"
        value={description}
        onChangeText={setDescription}
      />

      <Button title="Submit" onPress={submitAskForHelp} />
      <Text>Distance: {distance} km</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  input: {
    height: 40,
    borderColor: '#ddd',
    borderWidth: 1,
    marginVertical: 8,
    paddingHorizontal: 10,
    width: '80%',
  },
  imagePreview: {
