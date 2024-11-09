import React from 'react';
import { StyleSheet, View } from 'react-native';
import { ThemedView } from '@/components/ThemedView'; // Assuming this component respects the color scheme
import { useColorScheme } from '@/hooks/useColorScheme'; // Custom hook to detect color scheme

export default function BlankPage() {
  const colorScheme = useColorScheme(); // Detect light or dark mode

  return (
    <ThemedView
      style={[styles.container, { backgroundColor: colorScheme === 'dark' ? '#353636' : '#D0D0D0' }]}
    >
      {/* You can add content here that respects the current theme */}
      <View style={styles.centeredView}>
        {/* Placeholder text or elements */}

      </View>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
