import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Permite acesso externo ao container
    port: 5173,
    watch: {
      usePolling: true, // Força a leitura de arquivos (necessário no Docker)
    }
  }
})