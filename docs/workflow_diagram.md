# Video to Text Converter - Workflow Diagram

## System Architecture Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              INPUT FILES                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
            ┌───────▼────────┐                 ┌────────▼────────┐
            │  VIDEO FILES   │                 │  AUDIO FILES    │
            │                │                 │                 │
            │  • MP4         │                 │  • MP3          │
            │  • MOV         │                 │  • WAV          │
            │  • AVI         │                 │  • M4A          │
            │  • MKV         │                 │  • FLAC         │
            │  • FLV         │                 │  • AAC          │
            │  • WMV         │                 │  • OGG          │
            │  • WEBM        │                 │  • WMA          │
            │  • M4V         │                 │  • OPUS         │
            └────────┬───────┘                 └────────┬────────┘
                     │                                  │
                     │                                  │
         ┌───────────▼──────────┐                       │
         │  AUDIO EXTRACTION    │                       │
         │  (FFmpeg)            │                       │
         │  Video → MP3         │                       │
         └───────────┬──────────┘                       │
                     │                                  │
                     └──────────────┬───────────────────┘
                                    │
                     ┌──────────────▼──────────────┐
                     │    AUDIO FILE (MP3/WAV)     │
                     └──────────────┬──────────────┘
                                    │
                     ┌──────────────▼──────────────┐
                     │   WHISPER AI PROCESSING     │
                     │                             │
                     │  1. Load Model              │
                     │  2. Detect Language         │
                     │  3. Transcribe Audio        │
                     │  4. Generate Timestamps     │
                     └──────────────┬──────────────┘
                                    │
┌───────────────────────────────────┴───────────────────────────────────┐
│                           OUTPUT FILES                                │
└───────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
         ┌──────────▼──────┐ ┌──────▼──────┐ ┌─────▼──────────┐
         │  PLAIN TEXT     │ │  DETAILED   │ │  AUDIO FILE    │
         │  transcript.txt │ │  TIMESTAMPS │ │  (video only)  │
         │                 │ │             │ │                │
         │  Full text      │ │  [0.00s -   │ │  Extracted     │
         │  transcript     │ │   7.00s]    │ │  MP3 audio     │
         │  (continuous)   │ │  Text...    │ │  from video    │
         └─────────────────┘ └─────────────┘ └────────────────┘
```

## Processing Time Comparison

| Model Size | Speed         | 10-min Video | 60-min Video |
|------------|---------------|--------------|--------------|
| tiny       | ~32x realtime | ~20 seconds  | ~2 minutes   |
| base       | ~16x realtime | ~40 seconds  | ~4 minutes   |
| small      | ~6x realtime  | ~1.5 minutes | ~10 minutes  |
| medium     | ~2x realtime  | ~5 minutes   | ~30 minutes  |
| large      | ~1x realtime  | ~10 minutes  | ~60 minutes  |

## Model Selection Decision Tree

```
                    START
                      │
                      ▼
         ┌────────────────────────┐
         │  What's your priority? │
         └────────────┬───────────┘
                      │
         ┌────────────┼────────────┐
         │            │            │
    ┌────▼────┐  ┌────▼────┐  ┌───▼────┐
    │  SPEED  │  │ BALANCE │  │ACCURACY│
    └────┬────┘  └────┬────┘  └───┬────┘
         │            │            │
    ┌────▼────┐  ┌────▼────┐  ┌───▼────┐
    │  TINY   │  │  BASE   │  │ LARGE  │
    │  MODEL  │  │  MODEL  │  │ MODEL  │
    └─────────┘  └─────────┘  └────────┘
```

## Data Flow Example

### Input
```
video.mp4 (1.5 GB, 45 minutes)
```

### Processing Steps
```
1. Detect format         → Video file (MP4)
2. Extract audio         → video_audio.mp3 (45 MB)
3. Load Whisper base     → ~150 MB download (first time)
4. Detect language       → English
5. Transcribe            → ~3 minutes processing
```

### Output
```
video_transcript.txt                    (52 KB)
video_transcript_detailed.txt           (68 KB)
video_audio.mp3                         (45 MB)
```

## Language Detection Flow

```
Input Audio
    │
    ▼
┌───────────────────────┐
│ Analyze first 30s     │
│ of audio              │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ Detect language       │
│ (99+ languages)       │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ Confidence score      │
│ > 80%: Auto-detect    │
│ < 80%: Manual specify │
└───────────────────────┘
```

## Error Handling Flow

```
                    Input File
                         │
                         ▼
                  ┌──────────────┐
                  │ File exists? │
                  └──────┬───────┘
                         │
                    YES  │  NO
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
    ┌──────────────────┐    ┌──────────────┐
    │ Valid format?    │    │ Error: File  │
    └────────┬─────────┘    │ not found    │
             │              └──────────────┘
        YES  │  NO
      ┌──────┴──────┐
      │             │
      ▼             ▼
┌──────────┐  ┌──────────────┐
│ Process  │  │ Error: Show  │
│ file     │  │ supported    │
└──────────┘  │ formats      │
              └──────────────┘
```
