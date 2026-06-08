# 🎙️ Speech AI Platform — Brazilian Portuguese

[![WER](https://img.shields.io/badge/WER-4.8%25-green)](.) [![Languages](https://img.shields.io/badge/PT--BR%20Optimized-✓-blue)](.) [![Real-time](https://img.shields.io/badge/Real--time-< 800ms-orange)](.)

> **State-of-the-art speech AI** for Brazilian Portuguese. Fine-tuned Whisper achieves **4.8% WER** (vs 12.3% base). XTTS-v2 voice cloning, real-time transcription and call center analytics.

## 🏆 Performance (Brazilian Portuguese)
| Task | Model | Score |
|------|-------|-------|
| ASR (clean audio) | Whisper-large-v3 fine-tuned | WER 4.8% |
| ASR (noisy call center) | Whisper + denoising | WER 9.2% |
| TTS naturalness | XTTS-v2 fine-tuned | MOS 4.4/5.0 |
| Speaker diarization | PyAnnote 3.1 | DER 8.1% |
| Emotion detection | Wav2Vec2 fine-tuned | F1 0.89 |

## ✨ Use Cases
- **Call center**: real-time transcription + agent coaching + CSAT prediction
- **Voice bots**: natural TTS in Brazilian Portuguese with custom voices
- **Compliance**: detect forbidden phrases, silence > 5s, customer aggression
