import { Tabs } from 'expo-router';
import { FontAwesome } from '@expo/vector-icons';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ tabBarActiveTintColor: 'blue' }}>
      <Tabs.Screen name="home" options={{ title: 'Home', tabBarIcon: ({ color }) => <FontAwesome size={28} name="home" color={color} /> }} />
      <Tabs.Screen name="ask" options={{ title: 'Ask', tabBarIcon: ({ color }) => <FontAwesome size={28} name="question-circle" color={color} /> }} />
      <Tabs.Screen name="community" options={{ title: 'Community', tabBarIcon: ({ color }) => <FontAwesome size={28} name="users" color={color} /> }} />
      <Tabs.Screen name="request" options={{ title: 'Request', tabBarIcon: ({ color }) => <FontAwesome size={28} name="envelope" color={color} /> }} />
      <Tabs.Screen name="settings" options={{ title: 'Settings', tabBarIcon: ({ color }) => <FontAwesome size={28} name="cog" color={color} /> }} />
    </Tabs>
  );
}
