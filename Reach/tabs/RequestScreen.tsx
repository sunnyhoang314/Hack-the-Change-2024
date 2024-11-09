// tabs/request.tsx
import { View, Text, StyleSheet } from 'react-native';

export default function RequestScreen() {
  return (
    <View style={styles.container}>
      <Text>Request Screen Content</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
