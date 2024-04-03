# RAG-TECH-STACK

## Step-by-Step Instructions : 
1. git clone repo and cd into it 
2. `pip install -r requirements.txt`
3.`mkdir models`
4. copy your `m3e-base` model to `models/`
5. `cd src/stremlit-web` 
6. fill `<OPENAI-API-KEY>` with your own key in the `.env` file
7. run `streamlit run demo.py` in your cli






## Deploy using Docker
1. git clone repo and cd into it 
2. `mkdir models`
3. copy your `m3e-base` model to `models/`
4. fill `<OPENAI-API-KEY>` with your own key in the `.env` file under `/src/streamlit-web`
5. `docker build -t my-image-name .`
6. `docker run -p 8501:8501 my-image-name`
7. visit localhost:8501
