# Understanding Google Speech 

### Things to look into further
- [Audio Limits](https://cloud.google.com/speech-to-text/quotas) 
- Streaming speech recognition is available [via gRPC](https://cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1) only
- Stop listening after a single word, set the **single_utterance** field to **true** in the ***StreamingRecognitionConfig*** object.

### Initial setup steps
- Install client libraries - Completed
- Set up authentication for a local development environment - Revisit

