# Speech Recognition Study

## Overview

This project focuses on exploring and developing a speech recognition system. The study involves various aspects of speech recognition, including audio preprocessing, model training, and real-time speech-to-text conversion. The project aims to build a robust and efficient speech recognition system that can be applied to various use cases, such as language education and healthcare.

## Features

- **Real-time Speech-to-Text Conversion**: Converts spoken words into text in real-time.
- **Audio Preprocessing**: Includes noise reduction, normalization, and feature extraction.
- **Model Training**: Utilizes machine learning techniques to train models on speech datasets.
- **Sentiment Analysis**: Analyzes the sentiment of the recognized text as positive or negative.
- **Multi-Speaker Diarization**: Identifies and separates speech segments from multiple speakers.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/speech-recognition-study.git
    cd speech-recognition-study
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Rename the `.env.example` file to `.env`.
    - Update the environment variables as needed.

5. **Download datasets**:
    - Place your raw audio files in the `data/raw/` directory.

## Usage

### Training the Model

1. **Preprocess the data**:
    ```bash
    python scripts/preprocess_data.py
    ```

2. **Train the model**:
    ```bash
    python scripts/train_model.py
    ```

3. **Evaluate the model**:
    ```bash
    python scripts/evaluate_model.py
    ```

### Running the Application

1. **Start the web application**:
    ```bash
    python app/app.py
    ```

2. **Access the application**:
    - Open your web browser and navigate to `http://localhost:5000`.

3. **Use the Speech-to-Text service**:
    - Click on the microphone icon to start recording your voice.
    - The recognized text will be displayed in real-time.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear descriptions.
4. Push to your branch and create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Python library for performing speech recognition.
- [TensorFlow](https://www.tensorflow.org/) - Machine learning framework used for model training.
- [Librosa](https://librosa.org/) - Python package for music and audio analysis.
