// ============================================================
// CONFIGURAÇÃO DO FIREBASE — GUNGO AGÊNCIA & MARKETING
// ============================================================
// Substitui os valores abaixo pelos que copiaste da consola do
// Firebase (Definições do projeto > Os teus apps > SDK config).
// NÃO precisas de mexer em mais nenhum ficheiro além deste.
// ============================================================

const firebaseConfig = {
  apiKey: "AIzaSyCxUFKRC4g21jyDSkyFOQnTw7jda9iIzxU",
  authDomain: "gungo-agencia.firebaseapp.com",
  projectId: "gungo-agencia",
  storageBucket: "gungo-agencia.firebasestorage.app",
  messagingSenderId: "1069724155335",
  appId: "1:1069724155335:web:c8438ff3bd7a35d737ade2"
};

// ============================================================
// CLOUDINARY — usado só para guardar as fotos (gratuito, sem cartão)
// ============================================================
// cloudName: encontras no topo do teu Dashboard do Cloudinary
// uploadPreset: crias em Settings > Upload > Upload presets > Add upload preset
//               (define "Signing Mode" como "Unsigned")
const cloudinaryConfig = {
  cloudName: "lghrqzf4",
  uploadPreset: "gungo_portfolio"
};
