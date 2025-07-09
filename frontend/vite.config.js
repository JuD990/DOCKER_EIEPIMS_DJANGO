import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@assets': path.resolve(__dirname, 'src/assets'),
      '@services': path.resolve(__dirname, 'src/components/services'),
      '@user-info': path.resolve(__dirname, 'src/components/user_info'),
      '@logout': path.resolve(__dirname, 'src/components/Logout'),
      '@profilePics': path.resolve(__dirname, 'src/assets/profile/user_profile_pics'),
      '@profileDept': path.resolve(__dirname, 'src/assets/profile/department_logo'),
    }
  }
})
