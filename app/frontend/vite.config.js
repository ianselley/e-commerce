import { defineConfig } from 'vite'
// import vue from '@vitejs/plugin-vue'
// import ViteRestart from 'vite-plugin-restart'
// import { nodeResolve } from '@rollup/plugin-node-resolve'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  // plugins: [
  //   nodeResolve({
  //     moduleDirectories: [path.resolve('./node_modules')],
  //   }),
  //   ViteRestart({
  //     reload: ['./src/**/*'],
  //   }),
  //   vue(),
  // ],
  publicDir: './src/public',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  define: {
    'process.env': {},
  },
  server: {
    fs: {
      strict: false,
    },
    host: '0.0.0.0',
    origin: 'http://0.0.0.0:8080/',
    port: 8080,
    strictPort: true,
  },
})
